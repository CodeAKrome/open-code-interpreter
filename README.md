![Interpreter](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/movie.gif?raw=true)

### **Hosting and Spaces:**
[![Plugin](https://img.shields.io/badge/Google-Colab-blue)](https://colab.research.google.com/drive/1lzhLsGQicM5Dr4ixLDYNwzTT2d_YJgCg?usp=sharing)
[![Plugin](https://img.shields.io/badge/Replit-Replit-blue)](https://replit.com/@HaseebMir/open-code-interpreter)

<a href="https://www.buymeacoffee.com/haseebheaven"><img src="https://img.buymeacoffee.com/button-api/?text=Buy me a coffee&emoji=&slug=haseebheaven&button_colour=40DCA5&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" /></a>

**Welcome to Open-Code-Interpreter 🎉,** an innovative open-source and free alternative to traditional Code Interpreters. This powerful tool is not just free, but it also leverages the power of HuggingFace models like **Code-llama**, **Mistral 7b**, **Wizard Coder**, **GPT 3**, **PALM 2** and many more to transform your instructions into executable code.

**Open-Code-Interpreter** is more than just a code generator. It's a versatile tool that can execute a wide range of tasks. Whether you need to find files in your system 📂, save images from a website and convert them into a different format 🖼️, create a GIF 🎞️, edit videos 🎥, or even analyze files for data analysis and creating graphs 📊, Open-Code-Interpreter can handle it all.

After processing your instructions, **Open-Code-Interpreter** executes the generated code and provides you with the result. This makes it an invaluable tool for developers 💻, data scientists 🧪, and anyone who needs to quickly turn ideas into working code.

Designed with versatility in mind, **Open-Code-Interpreter** works seamlessly on every operating system, including _Windows, MacOS, and Linux_. So, no matter what platform you're on, you can take advantage of this powerful tool 💪.

**Experience the future of code interpretation with Open-Code-Interpreter today! 🚀**

## **Unique Interpreter:**

The distinguishing feature of this interpreter, as compared to others, is its **commitment to remain free 🆓**. It does not require any model downloads or follow to **tedious processes** or methods for execution. It is designed to be **simple** and **free** for all users. 🏃‍♂️

## **Future Plans:**
- ~~🎯 We plan to provide **GPT 3.5** models for free.~~ 🎯 We have added support for **GPT 3.5** models.
- 🌐 We plan to provide **Vertex AI (PALM 2)** models for free.
- 🔗 We plan to provide API Base change using [**LiteLLM**](https://litellm.ai/)
- 🤖 More **Hugging Face** models with free-tier.
- 💻 Support for more **Operating Systems**.


## **Table of Contents**
- [Features](#🌟-features)
- [Installation](#📥-installation)
- [Usage](#️🛠️-usage)
- [Examples](#📖-examples)
- [Settings](#️⚙️-settings)
- [Structure](#🏗️-structure)
- [Contributing](#🤝-contributing)
- [Versioning](#📌-versioning)
- [License](#📜-license)
- [Acknowledgments](#🙏-acknowledgments)

## 📥 **Installation**

To get started with Open-Code-Interpreter, follow these steps:</br>

1. Clone the repository:</br>
```git
git clone https://github.com/haseeb-heaven/open-code-interpreter.git
cd open-code-interpreter
```
2. Install the required packages:</br>
```bash
pip install -r requirements.txt
```
3. **(ONLY FOR HUGGING FACE)**:</br>
If you plan to use HuggingFace models, you will need a HuggingFace token. Go to [HuggingFace Tokens](https://huggingface.co/settings/tokens) and get your Access Token.</br>

4. **(ONLY FOR HUGGING FACE)**:</br>
If you obtained a HuggingFace token, save the token in a `.env` file as:</br>
```bash
echo "HUGGINGFACE_API_KEY=Your Access Token" > .env
```
5. **(ONLY FOR HUGGING FACE)**:</br>
Run the interpreter. If you are using HuggingFace models, use the following command:</br>
```bash
python interpreter.py -m 'code-llama' -md 'code' -dc
```
6. If you are using GPT 3.5 or PALM models directly,just use the following command:</br>
```bash
python interpreter.py -md 'code' -m 'gpt-3.5-turbo' -dc 
```

## 🌟 **Features**

- 🚀 Code Execution: Open-Code-Interpreter can execute the code generated from your instructions.

- 💾 Code Saving: It has the ability to save the generated code for future use or reference.

- 📜 Command History: It has the ability to save all the commands as history.

- 🔄 Mode Selection: It allows you to select the mode of operation. You can choose from `code` for generating code, `script` for generating shell scripts, or `command` for generating single line commands.

- 🧠 Model Selection: You can set the model for code generation. By default, it uses the `code-llama` model.

- 🌐 Language Selection: You can set the interpreter language to Python or `JavaScript`. By default, it uses `Python`.

- 👀 Code Display: It can display the generated code in the output, allowing you to review the code before execution.

- 💻 Cross-Platform: Open-Code-Interpreter works seamlessly on every operating system, including Windows, MacOS, and Linux.

- 🤝 Integration with HuggingFace: It leverages the power of HuggingFace models like Code-llama, Mistral 7b, Wizard Coder, and many more to transform your instructions into executable code.

- 🎯 Versatility: Whether you need to find files in your system, save images from a website and convert them into a different format, create a GIF, edit videos, or even analyze files for data analysis and creating graphs, Open-Code-Interpreter can handle it all.

## 🛠️ **Usage**

To use Open-Code-Interpreter, use the following command options:

- Code interpreter with least options.
```python
python interpreter.py -dc
```
- Code interpreter with GPT 3.5.
```python
python interpreter.py -md 'code' -m 'gpt-3.5-turbo' -dc 
```
- Code Llama with code mode selected.
```python
python interpreter.py -m 'code-llama' -md 'code'
```
- Code Llama with command mode selected.
```python
python interpreter.py -m 'code-llama' -md 'command'
```
- Mistral with script selected
```python
python interpreter.py -m 'mistral-7b' -md 'script'
```
- Wizard Coder with code selected and display code.
```python
python interpreter.py -m 'wizard-coder' -md 'code' -dc
```
- Wizard Coder with code selected and display code and auto execution.
```python
python interpreter.py -m 'wizard-coder' -md 'code' -dc -e
```
- Code Llama with code mode selected and save code
```python
python interpreter.py -m 'code-llama' -md 'code' -s
```
- Code Llama with code mode selected and javascript selected langauge.
```python
python interpreter.py -m 'code-llama' -md 'code' -s -l 'javascript'
```

## 📖 **Examples**

Example of Code llama with code mode:
![code_llama_code](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/code-llama-code.png?raw=true "Code Llama Code Mode")</br>

Example of Code llama with command mode:
![code_llama_command](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/code-llama-command.png?raw=true "Code Llama Command Mode")</br>

Example of Mistral with code mode:
![mistral_code](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/mistral-code.png?raw=true "Mistral Code Mode")</br>


## ⚙️ **Settings**
You can customize the settings of the current model from the `.config` file. It contains all the necessary parameters such as `temperature`, `max_tokens`, and more.

If you want to add a new model from Hugging Face, follow these steps:

1. 📋 Copy the `.config` file and rename it to `configs/hf-model-new.config`.
2. 🛠️ Modify the parameters of the model like `start_sep`, `end_sep`, `skip_first_line`.
3. 📝 Set the model name from Hugging Face to `HF_MODEL = 'Model name here'`.
4. 🚀 Now, you can use it like this: `python interpreter.py -m 'hf-model-new' -md 'code' -e`.
5. 📁 Make sure the `-m 'hf-model-new'` matches the config file inside the `configs` folder.

# 🏗️ **Structure**
```markdown
This is the directory strcuture of this repo.
.
|____.config: Configuration file for the project.
|____resources: Directory containing various resource files used in the project.
|____libs: Directory containing various Python modules used in the project.
| |____package_installer.py: Module for installing necessary packages.
| |____code_interpreter.py: Module for code execution and management.
| |____markdown_code.py: Handles markdown messages and code snippets.
| |____logger.py: Logs interpreter activities.
| |____utility_manager.py: Provides utility functions like reading configs and getting OS platform.
|____README.md: Project's main documentation.
|____interpreter.py: Handles command-line arguments, manages code generation, and executes code.
|____logs: Directory containing log files.
| |____interpreter.log: Log file for the interpreter activities.
| |____code-interpreter.log: Log file for the code interpreter activities.
|____.gitignore: Specifies intentionally untracked files that Git should ignore.
|____.env: Environment variables for the project.
|____configs: Directory containing configuration files for different models.
| |____mistral-7b.config: Configuration file for the Mistral-7b model.
| |____wizard-coder.config: Configuration file for the Wizard Coder model.
| |____star-chat.config: Configuration file for the Star Chat model.
| |____code-llama.config: Configuration file for the Code Llama model.
| |____code-llama-phind.config: Configuration file for the Code Llama Phind model.
|____history: Directory containing history files.
| |____history.json: JSON file storing the history of commands.
|____LICENSE.txt: Text file containing the license details for the project.
```

## 🤝 **Contributing**

If you're interested in contributing to **Open-Code-Interpreter**, we'd love to have you! Please fork the repository and submit a pull request. We welcome all contributions and are always eager to hear your feedback and suggestions for improvements.

## 📌 **Versioning**

**v1.0** - Initial release.</br>
**v1.1** - Added Graphs and Charts support.</br>
**v1.2** - Added LiteLLM Support.</br>
**v1.3** - Added Gpt 3.5 Support.</br>


## 📜 **License**

This project is licensed under the **MIT License**. For more details, please refer to the LICENSE file.
Although this project is licensed under the MIT License, the GPT 3.5 model is provided by Heaven-GPT and is subject to its own permissive license. You can read more about it [here](https://heaven-gpt.haseebmir.repl.co/privacy). Please note that this license is inclusive to this interpreter only.


## 🙏 **Acknowledgments**

- We would like to express our gratitude to **HuggingFace** for providing the models.
- A special shout-out to the open-source community. Your continuous support and contributions are invaluable to us.
