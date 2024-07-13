# Robochat 🤖

![License](https://img.shields.io/badge/license-MIT-blue.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue)

Robochat is an interactive chatbot application built using Streamlit and Google's Gemini models. This project demonstrates the use of generative AI models, `gemini-pro` and `gemini-pro-vision`, to create a chatbot capable of answering questions and providing responses based on user input.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Technologies](#technologies)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Introduction
Robochat is designed to provide quick and accurate responses to user queries. It leverages the powerful generative capabilities of `gemini-pro` for text responses and `gemini-pro-vision` for vision-based interactions.

## Features
- **Interactive Chat Interface**: Engaging UI built with Streamlit.
- **Generative AI**: Utilizes `gemini-pro` for generating text responses.
- **Vision AI**: Integrates `gemini-pro-vision` for handling vision-based inputs (e.g., images).

## Installation
To run Robochat locally, follow these steps:

1. **Clone the repository**:
    ```sh
    git clone https://github.com/yourusername/robochat.git
    cd robochat
    ```

2. **Create a virtual environment**:
    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment**:
    - On Windows:
        ```sh
        venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```sh
        source venv/bin/activate
        ```

4. **Install dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

5. **Set up environment variables**:
    Create a `.env` file in the project root and add your Google API key:
    ```env
    GOOGLE_API_KEY=your_google_api_key
    ```

## Usage
To start the Streamlit application, run:
```sh
streamlit run app.py
