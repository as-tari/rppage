import docx
import re

def parse_word_document(file):
    """
    Parse a Word document and return the text content.

    Args:
        file (file-like object): The uploaded Word document file.

    Returns:
        str: Text content of the Word document.
    """
    doc = docx.Document(file)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)

def identify_chapters(text):
    """
    Identify chapters in the text content.

    Args:
        text (str): Text content of the Word document.

    Returns:
        list: List of chapter titles.
    """
    chapters = []
    for line in text.split('\n'):
        if re.match(r'^Chapter \d+:.*$', line):
            chapters.append(line)
    return chapters
