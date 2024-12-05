import docx

def parse_word_document(file_path):
    """
    Parse a Word document and extract text.

    Args:
        file_path (str): Path to the Word document file

    Returns:
        str: Extracted text from the Word document
    """
    doc = docx.Document(file_path)
    text = []
    for para in doc.paragraphs:
        text.append(para.text)
    return '\n'.join(text)

def identify_chapters(text):
    """
    Identify and extract text for Chapter 1, Chapter 2, and Chapter 3.

    Args:
        text (str): Extracted text from the Word document

    Returns:
        dict: Dictionary containing text for each chapter
    """
    chapters = {}
    chapter_headers = ['Chapter 1', 'Chapter 2', 'Chapter 3']
    for header in chapter_headers:
        start_index = text.find(header)
        if start_index != -1:
            end_index = text.find(next((h for h in chapter_headers if h != header), None), start_index)
            if end_index == -1:
                end_index = len(text)
            chapters[header] = text[start_index:end_index]
    return chapters
