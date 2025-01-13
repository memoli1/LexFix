from pdfUtils import extract_text_from_pdf, save_corrected_pdf
from textUtils import correct_spelling
import os

def main():
    pdf_path = "/Users/alessandro/IdeaProjects/LexFix/src/inputFiles/inputTest.pdf"
    output_dir = "outputFiles"

    # Ensure the output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Extract text from the PDF
    extracted_text = extract_text_from_pdf(pdf_path)

    # Correct spelling
    corrected_text = correct_spelling(extracted_text)

    # Save corrected text to a new PDF
    save_corrected_pdf(pdf_path, corrected_text)

if __name__ == "__main__":
    main()