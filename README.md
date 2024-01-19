# ScriptQuin



# <p align="center">ScriptQuin: Generate Your Code</p>

<p align="center">
    <img src="./images/script.png" width=300 height=300 />
</p>


[ScriptQuin](https://github.com/SauravKumarMahato/ScriptQuin)  This project combines Streamlit, the ChatGPT API, and Selenium(in python)  to create a user-friendly platform. Users input HTML code, and gets Selenium test scripts in Python, streamlining the process of automated testing for web applications.

## Table of Contents

- [Features](#features)
- [Demo](#demo)
- [Installation](#installation)
- [Runnig Application](#running-application)
- [Dependencies](#dependencies)
- [Contributing](#contributing)
- [License](#license)

## Features

**Code Generator**: Put you html code inside text box given and then click `Generate Script` button to get the script on right half portion of streamlit app.

## Demo
<!-- demo link -->
https://github.com/SauravKumarMahato/ScriptQuin/assets/83631265/9f46b718-bbef-424b-aad5-5185c440e34d

## Installation

### Prerequisites

Ensure you have Python installed on your system. You can download it from python.org.

Before running ScriptQuin, you will need an OpenAI API key if the project utilizes OpenAI's services. You can obtain an API key by registering on the OpenAI platform.

### Setup

1. Clone the repository:

```bash
git clone https://github.com/SauravKumarMahato/ScriptQuin.git
```

2. Navigate to the cloned directory:

```bash
cd ScriptQuin
```

3. Install the required dependencies:

```bash
pip install -r requirements.txt
```

4. Add your OpenAI API key at the top [api_call.py](./api_call.py) files having section something like below: 

```python
openai.api_key = "YOUR_API_KEY"
```

## Running Application

For running the Projet write below code in your terminal.

```bash
streamlit run app.py
```

It will now open a web interface of streamlit and now you can test the application.

## Dependencies

Main dependencies which are required for this project to run are given below:

- openai 
- streamlit

You can find all dependencies required in  `requirements.txt`

## Contributing

We encourage contributions to enhance and elevate [ScriptQuin](https://github.com/SauravKumarMahato/ScriptQuin.git). Don't hesistate to submit issues, suggest new features, or initiate pull requests. Kindly follow our Code of Conduct for a respectful and collaborative environment.

## License

This project is licensed under the [MIT License](/LICENSE).
