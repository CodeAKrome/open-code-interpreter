"""
This file contains the `Interpreter` class which is responsible for:

- Initializing the interpreter with the necessary configurations and arguments.
- Handling different modes of operation: Code, Script, and Command.
- Generating code based on the user's input and the selected mode.
- Executing the generated code if the user chooses to do so.
- Handling errors during code execution and attempting to resolve them by installing missing packages.
- Cleaning up response files after each iteration.
- Opening resource files such as graphs, charts, and tables generated by the code.
- Logging all important actions and errors for debugging and traceability.
"""

import os
import platform
import subprocess
import time
import webbrowser
from libs.code_interpreter import CodeInterpreter
from litellm import completion
from libs.logger import initialize_logger
from libs.markdown_code import display_code, display_markdown_message
from libs.package_installer import PackageInstaller
from libs.utility_manager import UtilityManager
from dotenv import load_dotenv
        
class Interpreter:
    logger = None
    client = None
    interpreter_version = "1.7"
    
    def __init__(self, args):
        self.args = args
        self.history = []
        self.utility_manager = UtilityManager()
        self.code_interpreter = CodeInterpreter()
        self.package_installer = PackageInstaller()
        self.logger = initialize_logger("logs/interpreter.log")
        self.client = None
        self.config_values = None
        self.system_message = ""
        self.gemini_vision = None
        self.initialize()

    def _open_resource_file(self,filename):
        try:
            if os.path.isfile(filename):
                if platform.system() == "Windows":
                    subprocess.call(['start', filename], shell=True)
                elif platform.system() == "Darwin":
                    subprocess.call(['open', filename])
                elif platform.system() == "Linux":
                    subprocess.call(['xdg-open', filename])
                self.logger.info(f"{filename} exists and opened successfully")
        except Exception as exception:
            display_markdown_message(f"Error in opening files: {str(exception)}")

    def _clean_responses(self):
        files_to_remove = ['graph.png', 'chart.png', 'table.md']
        for file in files_to_remove:
            try:
                if os.path.isfile(file):
                    os.remove(file)
                    self.logger.info(f"{file} removed successfully")
            except Exception as e:
                print(f"Error in removing {file}: {str(e)}")
    
    def _extract_content(self,output):
        try:
            return output['choices'][0]['message']['content']
        except (KeyError, TypeError) as e:
            self.logger.error(f"Error extracting content: {str(e)}")
            raise
    
    def initialize(self):
        self.INTERPRETER_LANGUAGE = self.args.lang if self.args.lang else 'python'
        self.SAVE_CODE = self.args.save_code
        self.EXECUTE_CODE = self.args.exec
        self.DISPLAY_CODE = self.args.display_code
        self.INTERPRRETER_MODEL = self.args.model if self.args.model else None
        self.logger.info(f"Interpreter args model selected is '{self.args.model}")
        self.logger.info(f"Interpreter model selected is '{self.INTERPRRETER_MODEL}")
        self.system_message = ""
        self.INTERPRETER_MODE = 'code'

        if self.INTERPRETER_MODE == 'Vision':
            self.system_message = "You are top tier image captioner and image analyzer. Please generate a well-written description of the image that is precise, easy to understand"
        else:
            # Open file system_message.txt to a variable system_message
            try:
                with open('system/system_message.txt', 'r') as file:
                    self.system_message = file.read()
                    if self.system_message != "":
                        self.logger.info(f"System message read successfully")
            except Exception as exception:
                self.logger.error(f"Error occurred while reading system_message.txt: {str(exception)}")
                raise
        
        # Initialize client and mode.
        self.initialize_client()
        self.initialize_mode()
        
        try: # Make this as optional step to have readline history.
            self.utility_manager.initialize_readline_history()
        except:
            self.logger.error(f"Exception on initializing readline history")

    def initialize_client(self):
        load_dotenv()
        hf_model_name = ""
        self.logger.info("Initializing Client")
        
        self.logger.info(f"Interpreter model selected is '{self.INTERPRRETER_MODEL}")
        if self.INTERPRRETER_MODEL is None or self.INTERPRRETER_MODEL == "":
            self.logger.info("HF_MODEL is not provided, using default model.")
            self.INTERPRRETER_MODEL = self.INTERPRRETER_MODEL
            hf_model_name = self.INTERPRRETER_MODEL.strip().split("/")[-1]
            config_file_name = f"configs/gpt-3.5-turbo.config" # Setting default model to GPT 3.5 Turbo.
        else:
            config_file_name = f"configs/{self.INTERPRRETER_MODEL}.config"
        
        self.logger.info(f"Reading config file {config_file_name}")    
        self.config_values = self.utility_manager.read_config_file(config_file_name)
        self.INTERPRRETER_MODEL = str(self.config_values.get('HF_MODEL', self.INTERPRRETER_MODEL))       
        hf_model_name = self.INTERPRRETER_MODEL.strip().split("/")[-1]
        
        self.logger.info(f"Using model {hf_model_name}")
        
        if "gpt" in self.INTERPRRETER_MODEL:
            if os.getenv("OPENAI_API_KEY") is None:
                load_dotenv()
            if os.getenv("OPENAI_API_KEY") is None:
                # if there is no .env file, try to load from the current working directory
                load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
                
            # Read the token from the .env file
            hf_key = os.getenv('OPENAI_API_KEY')
            if not hf_key:
                raise Exception("OpenAI Key not found in .env file.")
            elif not hf_key.startswith('sk-'):
                raise Exception("OpenAI token should start with 'sk-'. Please check your .env file.")
        
        model_api_keys = {
            "palm": "PALM_API_KEY",
            "gemini-pro": "GEMINI_API_KEY"
        }

        for model, api_key_name in model_api_keys.items():
            if model in self.INTERPRRETER_MODEL:
                self.logger.info(f"User has agreed to terms and conditions of {model}")

                if os.getenv(api_key_name) is None:
                    load_dotenv()
                if os.getenv(api_key_name) is None:
                    # if there is no .env file, try to load from the current working directory
                    load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))

                api_key = os.getenv(api_key_name)
                # Validate the token
                if not api_key:
                    raise Exception(f"{api_key_name} not found in .env file.")
                elif " " in api_key or len(api_key) <= 15:
                    raise Exception(f"{api_key_name} should have no spaces, length greater than 15. Please check your .env file.")
        else:
            if os.getenv("HUGGINGFACE_API_KEY") is None:
                load_dotenv()
            if os.getenv("HUGGINGFACE_API_KEY") is None:
                # if there is no .env file, try to load from the current working directory
                load_dotenv(dotenv_path=os.path.join(os.getcwd(), ".env"))
                
            # Read the token from the .env file
            hf_key = os.getenv('HUGGINGFACE_API_KEY')
            if not hf_key:
                raise Exception("HuggingFace token not found in .env file.")
            elif not hf_key.startswith('hf_'):
                raise Exception("HuggingFace token should start with 'hf_'. Please check your .env file.")

    def initialize_mode(self):
        self.CODE_MODE = True if self.args.mode == 'code' else False
        self.SCRIPT_MODE = True if self.args.mode == 'script' else False
        self.COMMAND_MODE = True if self.args.mode == 'command' else False
        self.VISION_MODE = True if self.args.mode == 'vision' else False
        if not self.SCRIPT_MODE and not self.COMMAND_MODE and not self.VISION_MODE:
            self.CODE_MODE = True
    
    def get_prompt(self,message: str, chat_history: list[tuple[str, str]]) -> str:
        system_message = None
        
        if self.CODE_MODE:
            system_message = self.system_message
        elif self.SCRIPT_MODE:
            system_message = "Please generate a well-written script that is precise, easy to understand, and compatible with the current operating system."
        elif self.COMMAND_MODE:
            system_message = "Please generate a single line command that is precise, easy to understand, and compatible with the current operating system."
        elif self.VISION_MODE:
            system_message = "Please generate a well-written description of the image that is precise, easy to understand"
            return system_message
        
        messages = [
            {"role": "system", "content":system_message},
            {"role": "assistant", "content": "Please generate code wrapped inside triple backticks known as codeblock."},
            {"role": "user", "content": message}
        ]
        return messages
    
    def generate_text(self,message, chat_history: list[tuple[str, str]], temperature=0.1, max_tokens=1024,config_values=None,image_file=None):
        self.logger.debug("Generating code.")
        
        # Use the values from the config file if they are provided
        if config_values:
            temperature = float(config_values.get('temperature', temperature))
            max_tokens = int(config_values.get('max_tokens', max_tokens))
            api_base = str(config_values.get('api_base', None)) # Only for OpenAI.

        # Get the system prompt
        messages = self.get_prompt(message, chat_history)
        
        # Check if the model is GPT 3.5/4
        if 'gpt' in self.INTERPRRETER_MODEL:
            self.logger.info("Model is GPT 3.5/4.")
            if api_base != 'None':
                # Set the custom language model provider
                custom_llm_provider = "openai"
                self.logger.info(f"Custom API mode selected for OpenAI, api_base={api_base}")
                response = completion(self.INTERPRRETER_MODEL, messages=messages, temperature=temperature, max_tokens=max_tokens, api_base=api_base, custom_llm_provider=custom_llm_provider)
            else:
                self.logger.info(f"Default API mode selected for OpenAI.")
                response = completion(self.INTERPRRETER_MODEL, messages=messages, temperature=temperature, max_tokens=max_tokens)
            self.logger.info("Response received from completion function.")
                
        # Check if the model is PALM-2
        elif 'palm' in self.INTERPRRETER_MODEL:
            self.logger.info("Model is PALM-2.")
            self.INTERPRRETER_MODEL = "palm/chat-bison"
            response = completion(self.INTERPRRETER_MODEL, messages=messages,temperature=temperature,max_tokens=max_tokens)
            self.logger.info("Response received from completion function.")
        
        # Check if the model is Gemini Pro
        elif 'gemini' in self.INTERPRRETER_MODEL:

            if self.INTERPRETER_MODE == 'Vision':
                # Import Gemini Vision only if the model is Gemini Pro Vision.
                try:
                    from libs.gemini_vision import GeminiVision
                    self.gemini_vision = GeminiVision()
                except Exception as exception:
                    self.logger.error(f"Error importing Gemini Vision: {exception}")
                    raise

                self.logger.info("Model is Gemini Pro Vision.")
                response = None

                # Check if image_file is valid.
                if not image_file:
                    self.logger.error("Image file is not valid or Corrupted.")
                    raise ValueError("Image file is not valid or Corrupted.")
                
                # Check if image contains URL.
                if 'http' in image_file or 'https' in image_file or 'www.' in image_file:
                    self.logger.info("Image contains URL.")
                    response = self.gemini_vision.gemini_vision_url(prompt=messages,image_url=image_file)
                else:
                    self.logger.info("Image contains file.")
                    response = self.gemini_vision.gemini_vision_path(prompt=messages,image_path=image_file)
                
                self.logger.info("Response received from completion function.")
                return response # Return the response from Gemini Vision because its not coding model.
            else:
                self.logger.info("Model is Gemini Pro.")
                self.INTERPRRETER_MODEL = "gemini/gemini-pro"
                response = completion(self.INTERPRRETER_MODEL, messages=messages,temperature=temperature)
                self.logger.info("Response received from completion function.")
            

        # Check if model are from Hugging Face.
        else:
            # Add huggingface/ if not present in the model name.
            if 'huggingface/' not in self.INTERPRRETER_MODEL:
                self.INTERPRRETER_MODEL = 'huggingface/' + self.INTERPRRETER_MODEL
            
            self.logger.info(f"Model is from Hugging Face. {self.INTERPRRETER_MODEL}")
            response = completion(self.INTERPRRETER_MODEL, messages=messages,temperature=temperature,max_tokens=max_tokens)
            self.logger.info("Response received from completion function.")
        
        self.logger.info(f"Generated text {response}")
        generated_text = self._extract_content(response)
        self.logger.info(f"Generated content {generated_text}")
        return generated_text

    def get_code_prompt(self, task, os_name):
        prompt = f"Generate the code in {self.INTERPRETER_LANGUAGE} language for this task '{task} for Operating System: {os_name}'."
        self.history.append((task, prompt))
        return prompt

    def get_script_prompt(self, task, os_name):
        language_map = {'macos': 'applescript', 'linux': 'bash', 'windows': 'powershell'}
        self.INTERPRETER_LANGUAGE = language_map.get(os_name.lower(), 'python')
        
        script_type = 'Apple script' if os_name.lower() == 'macos' else 'Bash Shell script' if os_name.lower() == 'linux' else 'Powershell script' if os_name.lower() == 'windows' else 'script'
        prompt = f"\nGenerate {script_type} for this prompt and make this script easy to read and understand for this task '{task} for Operating System is {os_name}'."
        return prompt

    def get_command_prompt(self, task, os_name):
        prompt = f"Generate the single terminal command for this task '{task} for Operating System is {os_name}'."
        return prompt
    
    def handle_vision_mode(self, task):
        prompt = f"Give accurate and detailed information about the image provided and be very detailed about the image '{task}'."
        return prompt

    def get_mode_prompt(self, task, os_name):
        if self.CODE_MODE:
            return self.get_code_prompt(task, os_name)
        elif self.SCRIPT_MODE:
            return self.get_script_prompt(task, os_name)
        elif self.COMMAND_MODE:
            return self.get_command_prompt(task, os_name)
        elif self.VISION_MODE:
            return self.handle_vision_mode(task)

    def execute_code(self, extracted_code, os_name):
        # If the interpreter mode is Vision, do not execute the code.
        if self.INTERPRETER_MODE == 'Vision':
            return None, None
        
        execute = 'y' if self.EXECUTE_CODE else input("Execute the code? (Y/N): ")
        if execute.lower() == 'y':
            try:
                code_output, code_error = "", ""
                if self.SCRIPT_MODE:
                    code_output, code_error = self.code_interpreter.execute_script(extracted_code, os_type=os_name)
                elif self.COMMAND_MODE:
                    code_output, code_error = self.code_interpreter.execute_command(extracted_code)
                elif self.CODE_MODE:
                    code_output, code_error = self.code_interpreter.execute_code(extracted_code, language=self.INTERPRETER_LANGUAGE)
                return code_output, code_error
            except Exception as exception:
                self.logger.error(f"Error occurred while executing code: {str(exception)}")
                return None, str(exception)  # Return error message as second element of tuple
        else:
            return None, None  # Return None, None if user chooses not to execute the code

    def interpreter_main(self):
        
        self.logger.info(f"Code Interpreter - v{self.interpreter_version}")
        os_platform = self.utility_manager.get_os_platform()
        os_name = os_platform[0]

        # Seting the mode.
        if self.SCRIPT_MODE:
            self.INTERPRETER_MODE = 'Script'
        elif self.COMMAND_MODE:
            self.INTERPRETER_MODE = 'Command'
        elif self.VISION_MODE:
            self.INTERPRETER_MODE = 'Vision'

        start_sep = str(self.config_values.get('start_sep', '```'))
        end_sep = str(self.config_values.get('end_sep', '```'))
        skip_first_line = self.config_values.get('skip_first_line', 'False') == 'True'
        
        self.logger.info(f"Mode: {self.INTERPRETER_MODE} Start separator: {start_sep}, End separator: {end_sep}, Skip first line: {skip_first_line}")

        # Display system and Assistant information.
        display_code(f"OS: '{os_name}', Language: '{self.INTERPRETER_LANGUAGE}', Mode: '{self.INTERPRETER_MODE}' Model: '{self.INTERPRRETER_MODEL}'")
        display_markdown_message("Welcome to the **Interpreter**. I'm here to **assist** you with your everyday tasks. "
                                  "\nPlease enter your task and I'll do my best to help you out.")
        
        while True:
            try:
                task = input("> ")
                if task.lower() in ['exit', 'quit']:
                    break
                prompt = self.get_mode_prompt(task, os_name)
                
                # Clean the responses
                self._clean_responses()
                
                # Check if prompt contains any file uploaded by user.
                extracted_file_name = self.utility_manager.extract_file_name(prompt)
                self.logger.info(f"Input prompt extracted_name: '{extracted_file_name}'")

                if extracted_file_name is not None:
                    full_path = self.utility_manager.get_full_file_path(extracted_file_name)
                    self.logger.info(f"Input prompt full_path: '{full_path}'")
                    
                    # Check if image contains URL.
                    if 'http' in extracted_file_name or 'https' in extracted_file_name or 'www.' in extracted_file_name:
                        self.logger.info("Image contains URL Skipping the file processing.")
                    
                    else:
                        # Check if the file exists and is a file
                        if os.path.isfile(full_path):
                            # Check if file size is less than 50 KB
                            file_size_max = 50000
                            file_size = os.path.getsize(full_path)
                            self.logger.info(f"Input prompt file_size: '{file_size}'")
                            if file_size < file_size_max:
                                try:
                                    with open(full_path, 'r', encoding='utf-8') as file:
                                        # Check if file extension is .json, .csv, or .xml
                                        file_extension = os.path.splitext(full_path)[1].lower()
                                        
                                        if file_extension in ['.json','.xml']:
                                            # Split by new line and read only 20 lines
                                            file_data = '\n'.join(file.readline() for _ in range(20))
                                            self.logger.info(f"Input prompt JSON/XML file_data: '{str(file_data)}'")
                                            
                                        elif file_extension == '.csv':
                                            # Read only headers of the csv file
                                            file_data = self.utility_manager.read_csv_headers(full_path)
                                            self.logger.info(f"Input prompt CSV file_data: '{str(file_data)}'")
                                            
                                        else:
                                            file_data = file.read()
                                            self.logger.info(f"Input prompt file_data: '{str(file_data)}'")
                                            
                                        if any(word in prompt.lower() for word in ['graph', 'graphs', 'chart', 'charts']):
                                            prompt += "\n" + "This is file data from user input: " + str(file_data) + " use this to analyze the data."
                                            self.logger.info(f"Input Prompt: '{prompt}'")
                                        else:
                                            self.logger.info("The prompt does not contain both 'graph' and 'chart'.")
                                except Exception as exception:
                                    self.logger.error(f"Error reading file: {exception}")
                            else:
                                self.logger.error("File size is greater.")
                        else:
                            self.logger.error("File does not exist or is not a file.")                         
                else:
                    self.logger.info("No file name found in the prompt.")
            
                # If graph were requested.
                if any(word in prompt.lower() for word in ['graph', 'graphs']):
                    if self.INTERPRETER_LANGUAGE == 'python':
                        prompt += "\n" + "using Python use Matplotlib save the graph in file called 'graph.png'"
                    elif self.INTERPRETER_LANGUAGE == 'javascript':
                        prompt += "\n" + "using JavaScript use Chart.js save the graph in file called 'graph.png'"

                # if Chart were requested
                if any(word in prompt.lower() for word in ['chart', 'charts', 'plot', 'plots']):    
                    if self.INTERPRETER_LANGUAGE == 'python':
                        prompt += "\n" + "using Python use Plotly save the chart in file called 'chart.png'"
                    elif self.INTERPRETER_LANGUAGE == 'javascript':
                        prompt += "\n" + "using JavaScript use Chart.js save the chart in file called 'chart.png'"

                # if Table were requested
                if 'table' in prompt.lower():
                    if self.INTERPRETER_LANGUAGE == 'python':
                        prompt += "\n" + "using Python use Pandas save the table in file called 'table.md'"
                    elif self.INTERPRETER_LANGUAGE == 'javascript':
                        prompt += "\n" + "using JavaScript use DataTables save the table in file called 'table.html'"
                 
                # Start the LLM Request.     
                self.logger.info(f"Prompt: {prompt}")
                generated_output = self.generate_text(prompt, self.history, config_values=self.config_values,image_file=extracted_file_name)
                
                # No extra processing for Vision mode.
                if self.INTERPRETER_MODE == 'Vision':
                    display_markdown_message(f"{generated_output}")
                    continue

                # Extract the code from the generated output.
                self.logger.info(f"Generated output type {type(generated_output)}")
                extracted_code = self.code_interpreter.extract_code(generated_output, start_sep, end_sep, skip_first_line,self.CODE_MODE)
                
                # Display the extracted code.
                self.logger.info(f"Extracted code: {extracted_code[:50]}")
                
                if self.DISPLAY_CODE:
                    display_code(extracted_code)
                    self.logger.info("Code extracted successfully.")
                
                if extracted_code:
                    current_time = time.strftime("%Y_%m_%d-%H_%M_%S", time.localtime())
                    
                    if self.INTERPRETER_LANGUAGE == 'javascript' and self.SAVE_CODE and self.CODE_MODE:
                        self.code_interpreter.save_code(f"output/code_{current_time}.js", extracted_code)
                        self.logger.info(f"JavaScript code saved successfully.")
                    
                    elif self.INTERPRETER_LANGUAGE == 'python' and self.SAVE_CODE and self.CODE_MODE:
                        self.code_interpreter.save_code(f"output/code_{current_time}.py", extracted_code)
                        self.logger.info(f"Python code saved successfully.")
                    
                    elif self.SAVE_CODE and self.COMMAND_MODE:
                        self.code_interpreter.save_code(f"output/command_{current_time}.txt", extracted_code)
                        self.logger.info(f"Command saved successfully.")
  
                    elif self.SAVE_CODE and self.SCRIPT_MODE:
                        self.code_interpreter.save_code(f"output/script_{current_time}.txt", extracted_code)
                        self.logger.info(f"Script saved successfully.")
                  
                    # Execute the code if the user has selected.
                    code_output, code_error = self.execute_code(extracted_code, os_name)
                    
                    if code_output:
                        self.logger.info(f"{self.INTERPRETER_LANGUAGE} code executed successfully.")
                        display_code(code_output)
                        self.logger.info(f"Output: {code_output[:100]}")
                    elif code_error:
                        self.logger.info(f"Python code executed with error.")
                        display_markdown_message(f"Error: {code_error}")
                        
                    # install Package on error.
                    error_messages = ["ModuleNotFound", "ImportError", "No module named", "Cannot find module"]
                    if code_error is not None and any(error_message in code_error for error_message in error_messages):
                        package_name = self.package_installer.extract_package_name(code_error, self.INTERPRETER_LANGUAGE)
                        if package_name:
                            self.logger.info(f"Installing package {package_name} on interpreter {self.INTERPRETER_LANGUAGE}")
                            self.package_installer.install_package(package_name, self.INTERPRETER_LANGUAGE)

                            # Wait and Execute the code again.
                            time.sleep(10)
                            code_output, code_error = self.execute_code(extracted_code, os_name)
                            if code_output:
                                self.logger.info(f"{self.INTERPRETER_LANGUAGE} code executed successfully.")
                                display_code(code_output)
                                self.logger.info(f"Output: {code_output[:100]}")
                            elif code_error:
                                self.logger.info(f"Python code executed with error.")
                                display_markdown_message(f"Error: {code_error}")
                            
                    try:
                        # Check if graph.png exists and open it.
                        self._open_resource_file('graph.png')
                        
                        # Check if chart.png exists and open it.
                        self._open_resource_file('chart.png')
                        
                        # Check if table.md exists and open it.
                        self._open_resource_file('table.md')
                    except Exception as exception:
                        display_markdown_message(f"Error in opening resource files: {str(exception)}")
                
                self.utility_manager.save_history_json(task, self.INTERPRETER_MODE, os_name, self.INTERPRETER_LANGUAGE, prompt, extracted_code, self.INTERPRRETER_MODEL)
                
            except Exception as exception:
                self.logger.error(f"An error occurred: {str(exception)}")
                raise