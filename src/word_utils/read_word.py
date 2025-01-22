from docx import Document

def extract_text_from_word(file_path):
    """
    Extract all text from a Word (.docx) file.

    Args:
        file_path (str): Path to the Word file.

    Returns:
        str: Extracted text.
    """
    document = Document(file_path)
    text = "\n".join([p.text for p in document.paragraphs if p.text.strip()])
    return text
