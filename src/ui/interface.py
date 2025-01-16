import os
import tkinter as tk
from tkinter import filedialog, messagebox
import threading

class LoadingWindow:
    def __init__(self, parent):
        """Create a window that shows a loading message while the process is running."""
        self.window = tk.Toplevel(parent)
        self.window.title("Processing...")
        self.window.geometry("300x150")
        self.label = tk.Label(self.window, text="Processing your PDF...\nPlease wait...", font=("Helvetica", 12))
        self.label.pack(pady=20)

        self.close_button = None  # Will be created later when processing is complete

    def show_result(self, message):
        """Update the window with the result of the process."""
        self.label.config(text=message)
        self.label.pack(pady=20)

        if not self.close_button:  # Ensure the button is only created once
            # Add a button to close the window after the process
            self.close_button = tk.Button(self.window, text="Close", command=self.window.destroy)
            self.close_button.pack(pady=10)

    def close(self):
        """Close the loading window."""
        self.window.destroy()

def start_gui(process_pdf_callback):
    """Start the GUI to handle file selection and processing."""
    # Create the main window
    root = tk.Tk()
    root.title("LexFix")

    # Set the initial size of the window (width x height)
    root.geometry("600x400")

    # Create and place widgets (buttons, labels, etc.)
    label = tk.Label(root, text="Choose a PDF file to correct")
    label.pack(pady=10)

    def open_file():
        """Open file dialog to choose a PDF."""
        pdf_path = filedialog.askopenfilename(filetypes=[("PDF Files", "*.pdf")])
        if pdf_path:
            # Create the loading window
            loading_window = LoadingWindow(root)

            # Run PDF processing in a separate thread to keep the GUI responsive
            threading.Thread(target=process_pdf_callback, args=(pdf_path, loading_window), daemon=True).start()

    open_button = tk.Button(root, text="Open PDF", command=open_file)
    open_button.pack(pady=20)

    # Start the GUI loop
    root.mainloop()
