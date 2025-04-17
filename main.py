from mcp.server.fastmcp import FastMCP


mcp = FastMCP("AI Sticky Notes")

NOTES_FILE = os.path.join(os.path.dirname(__file__),"notes.txt")

def ensure_file():
    if not os.path.exists(NOTES_FILE):
        with open(NOTES_FILE, "w") as f:
            f.write("")

@mcp.tool()


def add_note(message: str) -> str:
    """
    Append a new note to the sticky note file.

    Args:
        message (str): The note content to be added.

    returns:
        str: Confirmation message indicating the note was saved.

    
    
    """
    ensure_file()
    with open(NOTES_FILE, "a") as f:
        f.write(message + "\n")
        return "Note Saved!"
    


@mcp.tool()


def read_notes() ->str:
    """
    Read and retur all notes from the sticky note file.

    Return:
    str: All notes as a single string separated by line breaks.
    if no notes exists, a default message is returned.

    
    """