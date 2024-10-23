import tkinter as tk
from tkinter import filedialog, messagebox
import PyPDF2

# Function to merge PDFs
def merge_pdfs(pdf_list, output_path):
    pdf_writer = PyPDF2.PdfWriter()

    for pdf in pdf_list:
        pdf_reader = PyPDF2.PdfReader(pdf)
        for page_num in range(len(pdf_reader.pages)):
            page = pdf_reader.pages[page_num]
            pdf_writer.add_page(page)

    with open(output_path, 'wb') as output_pdf:
        pdf_writer.write(output_pdf)

# Function to browse and select multiple PDF files
def browse_files():
    files = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF Files", "*.pdf")])
    pdf_list.extend(files)  # Add selected files to the list
    update_file_list()

# Function to display the selected PDF files in the listbox
def update_file_list():
    listbox.delete(0, tk.END)
    for pdf in pdf_list:
        listbox.insert(tk.END, pdf)

# Function to select the location to save the merged PDF
def save_file():
    if not pdf_list:
        messagebox.showerror("Error", "No PDF files selected!")
        return
    output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
    if output_path:
        merge_pdfs(pdf_list, output_path)
        messagebox.showinfo("Success", "PDFs merged successfully!")

# Function to clear the selected PDF files
def clear_list():
    pdf_list.clear()
    update_file_list()

# Set up the GUI
root = tk.Tk()
root.title("PDF Merger")
root.geometry("500x400")

pdf_list = []  # List to store selected PDF file paths

# Title Label
title_label = tk.Label(root, text="PDF Merger Application", font=("Helvetica", 16))
title_label.pack(pady=10)

# Listbox to display selected PDFs
listbox = tk.Listbox(root, width=60, height=10)
listbox.pack(pady=10)

# Browse Button to select PDFs
browse_button = tk.Button(root, text="Browse PDFs", command=browse_files)
browse_button.pack(pady=5)

# Save Button to merge and save the merged PDF
save_button = tk.Button(root, text="Merge & Save PDF", command=save_file)
save_button.pack(pady=5)

# Clear Button to clear the selected PDFs
clear_button = tk.Button(root, text="Clear List", command=clear_list)
clear_button.pack(pady=5)

# Start the Tkinter event loop
root.mainloop()