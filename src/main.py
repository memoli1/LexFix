import os
from pdf_utils.extract_text_from_pdf import extract_text_from_pdf
from pdf_utils.save_corrected_pdf import save_corrected_pdf
from text_utils.correct_spelling import correct_spelling_advanced, correct_spelling_simple

def process_pdf(input_pdf_path, loading_window):
    """Process the PDF file: extract text, correct, and save as a new PDF."""
    try:
        # Get the directory of the input file
        input_directory = os.path.dirname(input_pdf_path)

        # Generate the output file name dynamically
        input_filename = os.path.basename(input_pdf_path)
        output_pdf_path = os.path.join(input_directory, f"corrected_{input_filename}")

        # Extract text from the PDF
        extracted_text = extract_text_from_pdf(input_pdf_path)

        # Correct text (spelling and punctuation)
        corrected_text = correct_spelling_simple(extracted_text)
        #corrected_text = restore_punctuation(corrected_text)  # Optionally restore punctuation

        # Save corrected text to a new PDF in the same directory as the input file
        save_corrected_pdf(output_pdf_path, corrected_text)

        success_message = f"Corrected PDF saved to: {output_pdf_path}"
        print(success_message)  # Print to terminal
        loading_window.show_result(f"Corrected PDF saved")
    except FileNotFoundError as e:
        error_message = f"Error: {e}"
        print(error_message)  # Print error to terminal
        loading_window.show_result(error_message)  # Show error in GUI
    except Exception as e:
        error_message = f"An unexpected error occurred: {e}"
        print(error_message)  # Print error to terminal
        loading_window.show_result(error_message)  # Show error in GUI

def main():
    """Launch the GUI or process files directly."""
    from ui.interface import start_gui
    # Pass the process_pdf function to the GUI
    start_gui(process_pdf)

if __name__ == "__main__":
    main()