![Interpreter](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/movie.gif?raw=true)

### **Hosting and Spaces:**
[![Colab](https://img.shields.io/badge/Google-Colab-blue)](https://colab.research.google.com/drive/1jGg-NavH8t4W2UVs8MyVMv8bs49qggfA?usp=sharing)
[![Replit](https://img.shields.io/badge/Replit-IDE-blue)](https://replit.com/@HaseebMir/open-code-interpreter)
[![PyPi](https://img.shields.io/badge/PyPi-Package-blue)](https://pypi.org/project/open-code-interpreter/)
[![Building](https://github.com/haseeb-heaven/Open-Code-Interpreter/actions/workflows/python-app.yml/badge.svg)](https://github.com/haseeb-heaven/Open-Code-Interpreter/actions/workflows/python-app.yml)

### **Support Project:**
<a href="https://www.buymeacoffee.com/haseebheaven">
    <img src="https://img.buymeacoffee.com/button-api/?text=Buy%20me%20a%20coffee&emoji=&slug=haseebheaven&button_colour=40DCA5&font_colour=ffffff&font_family=Cookie&outline_colour=000000&coffee_colour=FFDD00" width="200" height="50" />
</a>
<a href="https://ko-fi.com/heavenhm">
    <img src="https://img.shields.io/badge/KoFi-ffdd00?style=for-the-badge&logo=Ko-fi&logoColor=orange" width="200" height="50" />
</a>

**Welcome to Open-Code-Interpreter 🎉,** an innovative open-source and free alternative to traditional Code Interpreters. This is powerful tool and it also leverages the power of **GPT 3.5 Turbo**,**PALM 2**, **HuggingFace models** like **Code-llama**, **Mistral 7b**, **Wizard Coder**, and many more to transform your instructions into executable code for **free** and **safe** to use environments and even has **Vision Models** for Image Processing available.

**Open-Code-Interpreter** is more than just a code generator. It's a versatile tool that can execute a wide range of tasks. Whether you need to find files in your system 📂, save images from a website and convert them into a different format 🖼️, create a GIF 🎞️, edit videos 🎥, or even analyze files for data analysis and creating graphs 📊, Open-Code-Interpreter can handle it all.

After processing your instructions, **Open-Code-Interpreter** executes the generated code and provides you with the result. This makes it an invaluable tool for developers 💻, data scientists 🧪, and anyone who needs to quickly turn ideas into working code and now with **Vision Models** it can also process images and videos.

Designed with versatility in mind, **Open-Code-Interpreter** works seamlessly on every operating system, including _Windows, MacOS, and Linux_. So, no matter what platform you're on, you can take advantage of this powerful tool 💪.

**Experience the future of code interpretation with Open-Code-Interpreter today! 🚀**

## **Why this is Unique Interpreter?**

The distinguishing feature of this interpreter, as compared to others, is its **commitment to remain free 🆓**. It does not require any model to download or follow to **tedious processes** or methods for execution. It is designed to be **simple** and **free** for all users and works on all major OS **_Windows,Linux,MacOS_**

## **Future Plans:**
- ~~🎯 We plan to integrate **GPT 3.5** models.~~ *🎯 We have added support for **GPT 3.5** models*.
- 🌐 .~~We plan to provide **Vertex AI (PALM 2)** models..~~ We have added support for **PALM-2** model using [**LiteLLM**](https://litellm.ai/)
- 🔗 ~~We plan to provide API Base change using [**LiteLLM**](https://litellm.ai/)~~. Added Support for [**LiteLLM**](https://litellm.ai/)
- 🤖 More **Hugging Face** models with free-tier.
- 💻 Support for more **Operating Systems**.
- 📝 Support for **Multi-Modal** for _Text_ and _Vision_.
- 📊 Support for **Google** and **OpenAI** Vision Models.
- Support for **Local** models via **LLM Studio**.

## **Table of Contents**
- [Features](#🌟-features)
- [Installation](#📥-installation)
- [Usage](#️🛠️-usage)
- [Examples](#📖-examples)
- [Settings](#️⚙️-settings)
- [Contributing](#🤝-contributing)
- [Versioning](#📌-versioning)
- [License](#📜-license)
- [Acknowledgments](#🙏-acknowledgments)

## 📥 **Installation**

## Installtion with Python package manager.
To install Open-Code-Interpreter, run the following command:</br>

```bash
pip install open-code-interpreter
```
- To run the interpreter with Python:</br>
```bash
interpreter -m 'gemini-pro' -md 'code' -dc
```
- Make sure you install required packages before running the interpreter.</br>
- And you have API keys setup in the `.env` file.</br>

## Installtion with Git
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
3. Setup the Keys required.

## HUGGING FACE API Key setup.

*Step 1:* **Obtain the HuggingFace API key.**

*Step 2:* Visit the following URL: *https://huggingface.co/settings/tokens* and get your Access Token.

*Step 3:* Save the token in a `.env` file as:</br>
```bash
echo "HUGGINGFACE_API_KEY=Your Access Token" > .env
```

## Google GEMINI and PALM-2 API Key setup.

*Step 1:* **Obtain the Google Palm API key.**

*Step 2:* Visit the following URL: *https://makersuite.google.com/app/apikey*

*Step 3:* Click on the **Create API Key** button.

*Step 4:* The generated key is your API key. Please make sure to **copy** it and **paste** it in the required field below.
```bash
echo "PALM_API_KEY=Your API Key" > .env
echo "GEMINI_API_KEY=Your API Key" > .env
```

## OpenAI API Key setup.

*Step 1:* **Obtain the OpenAI API key.**

*Step 2:* Visit the following URL: *https://platform.openai.com/account/api-keys*

*Step 3:* Sign up for an account or log in if you already have one.

*Step 4:* Navigate to the API section in your account dashboard.

*Step 5:* Click on the **Create New Key** button.

*Step 6:* The generated key is your API key. Please make sure to **copy** it and **paste** it in the required field below.
```bash
echo "OPENAI_API_KEY=Your API Key" > .env
```

# Offline models setup.</br>
This Interpreter supports offline models via **LLM Studio** so to download it from [here](https://lmstudio.ai/) and follow the steps below.
- Download any model from **LLM Studio** like _Phi-2,Code-Llama,Mistral_.
- Then in the app go to **Local Server** option and select the model.
- Start the server and copy the **URL**.
- Open config file `configs/offline-model.config` and paste the **URL** in the `api_base` field.
- Now you can use the model with the interpreter set the model name to `offline-model` and run the interpreter.</br>

4. Run the interpreter with Python:</br>
### Running with Python.
```bash
python interpreter.py -md 'code' -m 'gpt-3.5-turbo' -dc 
```

5. Run the interpreter directly:</br>
### Running Interpreter without Python (Executable MacOs/Linux only).
```bash
./interpreter -md 'code' -m 'gpt-3.5-turbo' -dc 
```

## 🌟 **Features**

- 🚀 Code Execution: Open-Code-Interpreter can execute the code generated from your instructions.

- 💾 Code Save/Update: It has the ability to save the generated code for future use and 
 edit the code if needed on the fly using **advanced editor**.

- 📡 Offline models: It has the ability to use **offline models** for code generation using **LLM Studio**.

- 📜 Command History: It has the ability to save all the commands as history.

- 📜 Command Mode: Commands entered with '/' are executed as commands like `/execute` or `/edit`.

- 🔄 Mode Selection: It allows you to select the mode of operation. You can choose from `code` for generating code, `script` for generating shell scripts, or `command` for generating single line commands.

- 🧠 Model Selection: You can set the model for code generation. By default, it uses the `code-llama` model.

- 🌐 Language Selection: You can set the interpreter language to Python or `JavaScript`. By default, it uses `Python`.

- 👀 Code Display: It can display the generated code in the output, allowing you to review the code before execution.

- 💻 Cross-Platform: Open-Code-Interpreter works seamlessly on every operating system, including Windows, MacOS, and Linux.

- 🤝 Integration with HuggingFace: It leverages the power of HuggingFace models like Code-llama, Mistral 7b, Wizard Coder, and many more to transform your instructions into executable code.

- 🎯 Versatility: Whether you need to find files in your system, save images from a website and convert them into a different format, create a GIF, edit videos, or even analyze files for data analysis and creating graphs, Open-Code-Interpreter can handle it all.

## 🛠️ **Usage**

To use Open-Code-Interpreter, use the following command options:

- List of all **modes** are: </br>
    - `code` - Generates code from your instructions.
    - `script` - Generates shell scripts from your instructions.
    - `command` - Generates single line commands from your instructions.
    -  `vision` - Generates description of image or video.

- List of all **models** are (**Contribute - MORE**): </br>
    - `gpt-3.5-turbo` - Generates code using the GPT 3.5 Turbo model.
    - `gpt-4` - Generates code using the GPT 4 model.
    - `gemini-pro` - Generates code using the Gemini Pro model.
    - `palm-2` - Generates code using the PALM 2 model.
    - `code-llama` - Generates code using the Code-llama model.
    - `code-llama-phind` - Generates code using the Code-llama Phind model.
    - `mistral-7b` - Generates code using the Mistral 7b model.
    - `wizard-coder` - Generates code using the Wizard Coder model.
    - `star-chat` - Generates code using the Star Chat model.
    - `offline-model` - Generates code using the Offline model.

- Basic usage (with least options)</br>
```python
python interpreter.py -dc
```

- Using different models (replace 'model-name' with your chosen model) </br>
```python
python interpreter.py -md 'code' -m 'model-name' -dc
```

- Using different modes (replace 'mode-name' with your chosen mode) </br>
```python
python interpreter.py -m 'model-name' -md 'mode-name'
```

- Using auto execution </br>
```python
python interpreter.py -m 'wizard-coder' -md 'code' -dc -e
```

- Saving the code </br>
```python
python interpreter.py -m 'code-llama' -md 'code' -s
```

- Selecting a language (replace 'language-name' with your chosen language) </br>
```python
python interpreter.py -m 'gemini-pro' -md 'code' -s -l 'language-name'
```


# Interpreter Commands 🖥️

Here are the available commands:

- 📝 `/save` - Save the last code generated.
- ✏️ `/edit` - Edit the last code generated.
- ▶️ `/execute` - Execute the last code generated.
- 🔄 `/mode` - Change the mode of interpreter.
- 🔄 `/model` - Change the model for interpreter.
- 📦 `/install` - Install a package from npm or pip.
- 🌐 `/language` - Change the language of the interpreter.
- 🧹 `/clear` - Clear the screen.
- 🆘 `/help` - Display this help message.
- 📝 `/version` - Display the version of the interpreter.
- 🚪 `/exit` - Exit the interpreter.
- 📜 `/log` - Toggle different modes of logging.
- ⏫ `/upgrade` - Upgrade the interpreter.
- 💻 `/shell` - Access the shell.


## 📖 **Examples**
Code Interpreter Demo
[![code_interpreter_demo](https://img.youtube.com/vi/GGLNBfbN0oY/0.jpg)](https://youtube.com/shorts/GGLNBfbN0oY)

Example of GPT 3.5 Turbo.
![chatgpt_command](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/chat-gpt-command.png?raw=true "GPT 3.5 Turbo Code")</br>

Example of PALM-2 based on **Google Vertex AI**.
![chatgpt_command](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/palm-2-command.png?raw=true "GPT 3.5 Turbo Code")</br>

Example of Code llama with code mode:
![code_llama_code](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/code-llama-code.png?raw=true "Code Llama Code Mode")</br>

Example of Code llama with command mode:
![code_llama_command](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/code-llama-command.png?raw=true "Code Llama Command Mode")</br>

Example of Mistral with code mode:
![mistral_code](https://github.com/haseeb-heaven/open-code-interpreter/blob/main/resources/mistral-code.png?raw=true "Mistral Code Mode")</br>


## ⚙️ **Settings**
You can customize the settings of the current model from the `.config` file. It contains all the necessary parameters such as `temperature`, `max_tokens`, and more.

### **Steps to add your own custom API Server**
To integrate your own API server for OpenAI instead of the default server, follow these steps:
1. Navigate to the `Configs` directory.
2. Open the configuration file for the model you want to modify. This could be either `gpt-3.5-turbo.config` or `gpt-4.config`.
3. Add the following line at the end of the file:
   ```
   api_base = https://my-custom-base.com
   ```
   Replace `https://my-custom-base.com` with the URL of your custom API server.
4. Save and close the file.
Now, whenever you select the `gpt-3.5-turbo` or `gpt-4` model, the system will automatically use your custom server.

### **Steps to add new Hugging Face model**

1. 📋 Copy the `.config` file and rename it to `configs/hf-model-new.config`.
2. 🛠️ Modify the parameters of the model like `start_sep`, `end_sep`, `skip_first_line`.
3. 📝 Set the model name from Hugging Face to `HF_MODEL = 'Model name here'`.
4. 🚀 Now, you can use it like this: `python interpreter.py -m 'hf-model-new' -md 'code' -e`.
5. 📁 Make sure the `-m 'hf-model-new'` matches the config file inside the `configs` folder.

## 🤝 **Contributing**

If you're interested in contributing to **Open-Code-Interpreter**, we'd love to have you! Please fork the repository and submit a pull request. We welcome all contributions and are always eager to hear your feedback and suggestions for improvements.

## 📌 **Versioning**

🚀 **v1.0** - Initial release.</br>
📊 **v1.1** - Added **Graphs** and **Charts** support.</br>
🔥 **v1.2** - Added **LiteLLM** Support.</br>
🌟 **v1.3** - Added **GPT 3.5** Support.</br>
🌴 **v1.4** - Added **PALM 2** Support.</br>
🎉 **v1.5** - Added **GPT 3.5/4** models official Support.</br>
📝 **v1.6** - Updated Code Interpreter for Documents files (**JSON**, **CSV**,**XML**).</br>
🌴 **v1.7** - Added **Gemini Pro Vision** Support for Image Processing.</br>
🌴 **v1.8** - Added **Interpreter Commands Support**.</br>
- **1.8.1** - Added **Interpreter Commands** _Debugging Support_.</br>
- **1.8.2** - Fixed **Interpreter Commands** </br>
- **1.8.3** - Added **Interpreter Commands** _Upgrade and Shell Support_.</br>
- **1.8.4** - Fixed **Interpreter Model switcher** _Bug_.</br></br>
🗨️ **v1.9** - Added new **Chat mode** 🗨️ for Chatting with your **Files**, **Data** and more.</br>
- **v1.9.1** - Fixed **Unit Tests** and **History Args** <br>
- **v1.9.2** - Updated **Google Vision** to adapt LiteLLM instead of **Google GenAI** *.<br>
- **v1.9.3** - Added **Local Models** Support via **LLM Studio**.<br>

## 📜 **License**

This project is licensed under the **MIT License**. For more details, please refer to the LICENSE file.

Please note the following additional licensing details:

- The **GPT 3.5/4 models** are provided by **OpenAI** and are governed by their own licensing terms. Please ensure you have read and agreed to their terms before using these models. More information can be found at [OpenAI's Terms of Use](https://openai.com/policies/terms-of-use).

- The **PALM models** are officially supported by the **Google PALM 2 API**. These models have their own licensing terms and support. Please ensure you have read and agreed to their terms before using these models. More information can be found at [Google Generative AI's Terms of Service](https://developers.generativeai.google/terms).

- The **Hugging Face models** are provided by **Hugging Face Inc.** and are governed by their own licensing terms. Please ensure you have read and agreed to their terms before using these models. More information can be found at [Hugging Face's Terms of Service](https://huggingface.co/terms-of-service).

## 🙏 **Acknowledgments**

- We would like to express our gratitude to **HuggingFace**,**Google**,**META**,**OpenAI** for providing the models.
- A special shout-out to the open-source community. Your continuous support and contributions are invaluable to us.

## **📝 Author**
This project is created and maintained by [Haseeb-Heaven](www.github.com/haseeb-heaven).