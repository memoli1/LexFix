# pdfUtils/save_corrected_pdf.py

import os
from fpdf import FPDF


def save_corrected_pdf(original_pdf_path, corrected_text):
    """Save the corrected text to a new PDF file."""

    # Extract the file name and directory from the original PDF path
    directory, filename = os.path.split(original_pdf_path)
    filename_without_extension = os.path.splitext(filename)[0]

    # Create a new file name with 'correct_' prefix
    new_filename = f"correct_{filename_without_extension}.pdf"

    # Create the full path for the new file
    output_pdf_path = os.path.join(directory, new_filename)

    # Create a PDF document
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add corrected text to the PDF, handling multi-line text
    for line in corrected_text.split('\n'):
        pdf.multi_cell(0, 10, line)

    # Ensure the output directory exists
    output_dir = os.path.dirname(output_pdf_path)
    os.makedirs(output_dir, exist_ok=True)

    # Save the PDF
    pdf.output(output_pdf_path)