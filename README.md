# 🎤 Speech to Text Analysis 🎤

This repository contains the code for a speech to text analysis tool. It is written in Python and uses the [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library to handle audio stream. Capture audio is transcribed by Google Cloud Speech-to-Text API and then the transcription is sent to the OpenAI API for text analysis.

## Requirements

- Python 3.10 or later
- [OpenAI API Key](https://platform.openai.com/account/api-keys)
- [Google Cloud API Key](https://console.cloud.google.com/apis/credentials)

## Installation

To install the required libraries, run the following command:

```bash
pip install -r requirements.txt
```

## Setup
1. Create a new bucket in Google Cloud Storage.
2. Set the bucket name in the `.env` file.
3. Set the Google Cloud API Key in the `.env` file.
4. Set the OpenAI API Key in the `.env` file.

## Usage

To use the speech to text analysis tool, run the following command:

```bash
python speech_to_text.py
```