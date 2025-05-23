# AI Sticky Notes

AI Sticky Notes is a lightweight, AI-powered note-taking application built using the MCP framework. It allows you to add, read, and summarize notes through a simple interface, making it ideal for quick thoughts, to-do lists, or daily journaling.

## ✨ Features

- **Add Notes**: Append new notes to a persistent file.
- **Read Notes**: Retrieve all saved notes.
- **Latest Note**: Access the most recently added note.
- **Summarize Notes**: Generate a summary of all current notes using AI.


## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- MCP framework
- Claude AI model integration
- uv package manager (optional but recommended)

### Installation

#### Clone the Repository

```bash
git clone https://github.com/yourusername/AI-Sticky-Notes.git
cd AI-Sticky-Notes

```
Install Dependencies

Using uv:

```bash
uv pip install -r requirements.txt
```

or using pip:
```bash
pip install -r requirements.txt
```

Run the Application
```bash
python main.py
```

## Usage
The application provides several tools and resources:

### Add a Note
adds a new note to notes.txt.
```bash
@mcp.tool()
def add_note(message: str) -> str:
    ...

```

## Reads All Notes
Retrivers all saved notes.

```bash
@mcp.tool()
def read_notes() -> str:
    ...

```

### Get Latest Note
fetches the most recently added note

```bash
@mcp.resource("notes://latest")
def get_latest_note() -> str:
    ...

```

## Summarize Notes
Generates a summary of all current notes using AI
```bash
@mcp.prompt()
def note_summary_prompt() -> str:
    ...

```
## AI Integration
The application integrates with the Claude AI model to provide intelligent summaries of your notes. Ensure that your environment is configured correctly to interact with Claude.

