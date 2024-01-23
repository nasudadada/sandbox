# Streamlit OpenAI Text-to-Speech App in Docker

This project is a web application that uses OpenAI's text-to-speech model (tts-1) to convert text into speech through Streamlit. It can be easily set up and run using Docker.

## Prerequisites

- Docker installed on your machine
- An OpenAI API key is required (can be obtained from [OpenAI's website](https://openai.com/))

## Setup

1. Create a .env File:
   Create a .env file in the root directory of the project and add the following content:

   ```makefile
   OPENAI_API_KEY=your_api_key_here
   ```
   *Note: Replace your_api_key_here with your actual OpenAI API key.*

2. Build the Docker Image:
   ```bash
   docker build -t streamlit-text2speech-app .

3. Run the Docker Container:
    ```bash
    docker run -p 8501:8501 streamlit-text2speech-app
    ```
## Usage
After running the Docker container, open a web browser and navigate to http://localhost:8501. The application's UI will be displayed, where you can input text and convert it into speech.