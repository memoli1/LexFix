import tkinter as tk
from tkinter import filedialog
from utils.pdf_utils import extract_text_from_pdf, save_corrected_pdf
from utils.text_utils import correct_spelling

def start_gui():
    # Create the main window
    root = tk.Tk()
    root.title("LexFix")

    # Set the initial size of the window (width x height)
    root.geometry("600x400")  # You can adjust the size as needed


    # Create and place widgets (buttons, labels, etc.)
    label = tk.Label(root, text="Choose a PDF file to correct")
    label.pack(pady=10)

    def open_file():
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            # Extract text, correct it, and save a corrected PDF
            extracted_text = extract_text_from_pdf(pdf_path)
            corrected_text = correct_spelling(extracted_text)
            save_corrected_pdf(pdf_path, corrected_text)
            tk.messagebox.showinfo("Success", "PDF corrected successfully!")

    open_button = tk.Button(root, text="Open PDF", command=open_file)
    open_button.pack(pady=20)

    # Start the GUI loop
    root.mainloop()
