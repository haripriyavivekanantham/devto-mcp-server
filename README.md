# Personalized Letter Writing MCP

A Python-based Model Context Protocol (MCP) server that helps compatible AI applications create personalized letters from user-provided thoughts, situations, and preferences.

The project supports English, Tamil, and Tanglish, with customizable writing tones and visual letter formats.

## Features

* Turn rough thoughts or situations into structured letter-writing requests.
* Choose the output language: English, Tamil, or Tanglish.
* Customize the writing tone, including warm, emotional, funny, formal, and friendly.
* Choose from plain-text and HTML letter formats.
* Specify up to three visual themes.
* Include optional portrait guidance.
* Access resources containing writing guidelines, tones, formats, languages, and themes.

**Note:** This MCP server prepares instructions for a compatible AI client. It does not call an AI model directly; the connected AI application uses those instructions to produce the final letter.

## Tech Stack

* Python 3.11+
* Model Context Protocol (MCP) Python SDK
* `uv` for dependency management

## Project Structure

```text
personalized-letter-writing-mcp/
├── main.py
├── server.py
├── pyproject.toml
├── uv.lock
├── .python-version
├── .gitignore
└── README.md
```

## Prerequisites

* Python 3.11 or newer
* `uv` installed
* An MCP-compatible AI client

## Setup

Open a terminal in the project directory and install the dependencies:

```bash
uv sync
```

## Run the Server

Start the MCP server using:

```bash
uv run main.py
```

The server uses standard input/output (stdio) transport. Configure it in your MCP-compatible client using that client's MCP configuration instructions.

## MCP Components

**Tool**

* `create_letter_request` — prepares a personalized letter-writing request.

**Prompt**

* `personalized_letter_writer` — provides a reusable letter-writing prompt.

**Resources**

* `letter://guidelines`
* `letter://tones`
* `letter://formats`
* `letter://languages`
* `letter://themes`

## Author

Haripriya Vivekanantham

## License

No license file is currently included. Add an appropriate license if you intend to distribute the project publicly.
