# Bale AI Bot

A simple bot for the Bale messenger that receives user messages, sends them to a language model (LLM), and returns the AI response.

## Features

- Receives text messages from users in Bale
- Sends messages to an AI service and returns the response
- Error handling (the bot does not crash if the AI service is unavailable)
- No API key required (uses the `llmf` library)

## Requirements

- Python 3.8 or higher
- pip

## Installation

```bash
pip install balebale llmf