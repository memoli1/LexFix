import os
from ui.interface import start_gui

from utils.pdf_utils import extract_text_from_pdf, save_corrected_pdf
from utils.text_utils import correct_spelling

def main():
    # Prompt user for the input PDF file path
    input_pdf_path = input("Enter the path to the input PDF file: ")

    # Ensure the output directory exists
    output_directory = "output_files"
    os.makedirs(output_directory, exist_ok=True)

    # Generate the output file name dynamically
    input_filename = os.path.basename(input_pdf_path)
    output_pdf_path = os.path.join(output_directory, f"corrected_{input_filename}")

    try:
        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(input_pdf_path)

        # Correct spelling
        corrected_text = correct_spelling(extracted_text)

        # Save corrected text to a new PDF
        save_corrected_pdf(output_pdf_path, corrected_text)

        print(f"Corrected PDF saved to {output_pdf_path}")
    except FileNotFoundError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    start_gui()