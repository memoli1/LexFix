import tkinter as tk
from tkinter import filedialog, messagebox
from word_utils.process_word import WordProcessor

def start_gui():
    """Start the GUI for user interaction."""
    processor = WordProcessor(language='en-US')  # Initialize the WordProcessor

    def preview_errors(file_path):
        """Preview and allow selective correction of errors."""
        errors = processor.check_errors_in_word(file_path)  # Fetch errors
        if not errors:
            messagebox.showinfo("No Errors Found", "No errors were found in the document!")
            return

        # Store user selections for corrections
        selected_errors = [tk.BooleanVar(value=True) for _ in errors]

        # Open a new window for the error preview
        preview_window = tk.Toplevel()
        preview_window.title("Error Preview")
        preview_window.geometry("600x400")

        canvas = tk.Canvas(preview_window)
        scrollbar = tk.Scrollbar(preview_window, command=canvas.yview)
        frame = tk.Frame(canvas)

        # Configure the canvas and scrollbar
        canvas.create_window((0, 0), window=frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        # Populate the error preview with selection options
        for i, error in enumerate(errors):
            error_frame = tk.Frame(frame, padx=10, pady=5)
            error_frame.pack(fill="x")

            error_label = tk.Label(
                error_frame,
                text=f"Error {i + 1}: {error['context']}",
                fg="red",
                wraplength=550,
                justify="left"
            )
            error_label.pack(anchor="w")

            suggestion_label = tk.Label(
                error_frame,
                text=f"Suggestion: {', '.join(error['suggestions'])}",
                fg="green",
                wraplength=550,
                justify="left"
            )
            suggestion_label.pack(anchor="w")

            select_checkbox = tk.Checkbutton(
                error_frame,
                text="Apply this correction",
                variable=selected_errors[i]
            )
            select_checkbox.pack(anchor="w")

        # Add "Confirm Corrections" button
        def confirm_corrections():
            # Collect selected errors
            selected = [errors[i] for i, var in enumerate(selected_errors) if var.get()]
            if not selected:
                messagebox.showinfo("No Corrections", "No corrections were selected!")
                preview_window.destroy()
                return

            # Save the corrected file
            output_path = filedialog.asksaveasfilename(
                defaultextension=".docx",
                filetypes=[("Word Documents", "*.docx")],
                title="Save Corrected File As"
            )
            if not output_path:
                messagebox.showinfo("No Output File", "Please specify where to save the corrected file.")
                return

            try:
                processor.correct_text_in_word(file_path, output_path, selected)
                messagebox.showinfo("Success", f"Corrected file saved to {output_path}")
                preview_window.destroy()
            except Exception as e:
                messagebox.showerror("Error", f"An error occurred: {e}")

        confirm_button = tk.Button(preview_window, text="Confirm Corrections", command=confirm_corrections)
        confirm_button.pack(pady=10)

        frame.update_idletasks()
        canvas.configure(scrollregion=canvas.bbox("all"))
        canvas.pack(side="left", fill="both", expand=True)
        scrollbar.pack(side="right", fill="y")

        preview_window.mainloop()

    def process_file():
        """Handle file selection, error preview, and correction."""
        file_path = filedialog.askopenfilename(filetypes=[("Word Documents", "*.docx")])
        if not file_path:
            messagebox.showinfo("No File Selected", "Please select a Word file to process.")
            return

        # Preview errors
        preview_errors(file_path)

    # Set up the main GUI window
    root = tk.Tk()
    root.title("LexFix: Word Document Processor")
    root.geometry("400x200")

    label = tk.Label(root, text="Select a Word document to process", padx=10, pady=10)
    label.pack()

    select_button = tk.Button(root, text="Select File", command=process_file)
    select_button.pack(pady=20)

    root.mainloop()
