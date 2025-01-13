from fpdf import FPDF
import PyPDF2

def extract_text_from_pdf(pdf_path):
    """Extract text from a PDF file."""
    with open(pdf_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
    return text

def save_corrected_pdf(original_pdf_path, corrected_text):
    """Save the corrected text to a new PDF file."""
    output_pdf_path = "outputFiles/corrected_" + original_pdf_path.split('/')[-1]

    # Create an FPDF object and set up basic document settings
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()

    # Set font for the PDF
    pdf.set_font("Arial", size=12)

    # Add the corrected text (split into lines for better formatting)
    lines = corrected_text.split('\n')
    for line in lines:
        pdf.cell(200, 10, txt=line, ln=True)

    # Save the PDF
    pdf.output(output_pdf_path)
    print(f"Corrected PDF saved as {output_pdf_path}")