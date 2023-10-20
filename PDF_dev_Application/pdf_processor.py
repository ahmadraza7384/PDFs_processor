# PDFs Processor

import requests
import tkinter as tk
from tkinter import filedialog

class PDFProcessor:
    def __init__(self, public_key, secret_key):
        self.base_url = "https://developer.ilovepdf.com/tools"
        self.public_key = public_key
        self.secret_key = secret_key

    def _get_headers(self):
        return {
            "Authorization": f"Bearer {self.secret_key}"
        }

    # Merge pdfs Logic
    def merge_pdfs(self, file_paths, output_path):
        url = f"{self.base_url}/merge"
        payload = {"tasks": []}
        for path in file_paths:
            payload["tasks"].append({"filename": path})
        response = requests.post(url, headers=self._get_headers(), json=payload)
        download_url = response.json()["output"]
        download_response = requests.get(download_url, stream=True)
        with open(output_path, 'wb') as output_file:
            for chunk in download_response.iter_content(chunk_size=8192):
                output_file.write(chunk)
    
    # splits pdfs logic           
    def split_pdfs(self, file_paths, output_path):
        url = f"{self.base_url}/split"
        payload = {"tasks": []}
        for path in file_paths:
            payload["tasks"].append({"filename": path})
        response = requests.post(url, headers=self._get_headers(), json=payload)
        download_url = response.json()["output"]
        download_response = requests.get(download_url, stream=True)
        with open(output_path, 'wb') as output_file:
            for chunk in download_response.iter_content(chunk_size=8192):
                output_file.write(chunk)

    # remove pdfs logic
    def remove_pass_pdfs(self, file_paths, output_path):
        url = f"{self.base_url}/remove_password"
        payload = {"tasks": []}
        for path in file_paths:
            payload["tasks"].append({"filename": path})
        response = requests.post(url, headers=self._get_headers(), json=payload)
        download_url = response.json()["output"]
        download_response = requests.get(download_url, stream=True)
        with open(output_path, 'wb') as output_file:
            for chunk in download_response.iter_content(chunk_size=8192):
                output_file.write(chunk)
    
    # Extract Text logic            
    def extract_text(self, file_paths, output_path):
        url = f"{self.base_url}/extract"
        payload = {"tasks": []}
        for path in file_paths:
            payload["tasks"].append({"filename": path})
        response = requests.post(url, headers=self._get_headers(), json=payload)
        download_url = response.json()["output"]
        download_response = requests.get(download_url, stream=True)
        with open(output_path, 'wb') as output_file:
            for chunk in download_response.iter_content(chunk_size=8192):
                output_file.write(chunk)
    
    # Convert Images Logic            
    def convert_image(self, file_paths, output_path):
        url = f"{self.base_url}/image_convert"
        payload = {"tasks": []}
        for path in file_paths:
            payload["tasks"].append({"filename": path})
        response = requests.post(url, headers=self._get_headers(), json=payload)
        download_url = response.json()["output"]
        download_response = requests.get(download_url, stream=True)
        with open(output_path, 'wb') as output_file:
            for chunk in download_response.iter_content(chunk_size=8192):
                output_file.write(chunk)            

class PDFProcessorGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("PDF Processor for Ahmad Raza")
        self.geometry("400x200")
        self.processor = PDFProcessor(public_key="https://api.ilovepdf.com/v1/auth", secret_key="https://api.ilovepdf.com/v1/auth")

        self.file_paths = []

        # GUI elements
        self.upload_button = tk.Button(self, text="Upload PDFs", command=self.upload_pdfs)
        self.upload_button.pack(pady=20)

        self.process_button = tk.Button(self, text="Merge PDFs", command=self.merge_pdfs)
        self.process_button.pack()
        
        self.process_button = tk.Button(self, text="Split PDFs", command=self.split_pdfs)
        self.process_button.pack(pady=20)

        self.process_button = tk.Button(self, text="Remove Password of PDFs", command=self.remove_pass_pdfs)
        self.process_button.pack(pady=10)
        
        self.process_button = tk.Button(self, text="Extract texts", command=self.extract_text)
        self.process_button.pack(pady=10)
        
        self.process_button = tk.Button(self, text="Convert Images", command=self.convert_image)
        self.process_button.pack(pady=10)
        
    def upload_pdfs(self):
        file_paths = filedialog.askopenfilenames(title="Select PDF files", filetypes=[("PDF files", "*.pdf")])
        self.file_paths = list(file_paths)


    # Merge Pdfs
    def merge_pdfs(self):
        if len(self.file_paths) >= 2:
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_path:
                self.processor.merge_pdfs(self.file_paths, output_path)
                tk.messagebox.showinfo("Success", "PDFs merged successfully!")
        else:
            tk.messagebox.showerror("Error", "Select at least 2 PDF files to merge.")

    #Splits pdf
    def split_pdfs(self):
        if len(self.file_paths) >= 1:
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_path:
                self.processor.split_pdfs(self.file_paths, output_path)
                tk.messagebox.showinfo("Success", "PDFs split successfully!")
        else:
            tk.messagebox.showerror("Error", "Select at least 1 PDF files to split.")
    
    # Removed password of pdf        
    def remove_pass_pdfs(self):
        if len(self.file_paths) >= 1:
            output_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF files", "*.pdf")])
            if output_path:
                self.processor.remove_pass_pdfs(self.file_paths, output_path)
                tk.messagebox.showinfo("Success", "PDFs Removed password successfully!")
        else:
            tk.messagebox.showerror("Error", "Select at least 1 PDF files to merge.")
    
    # Extract Text        
    def extract_text(self):
        if len(self.file_paths) >= 1:
            output_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
            if output_path:
                self.processor.extract_text(self.file_paths, output_path)
                tk.messagebox.showinfo("Success", "text extract text successfully!")
        else:
            tk.messagebox.showerror("Error", "Select at least 1 Text files to extract.") 
    # Convert to image        
    def convert_image(self):
        if len(self.file_paths) >= 1:
            output_path = filedialog.asksaveasfilename(defaultextension=".img", filetypes=[("IMG files", "*.img")])
            if output_path:
                self.processor.convert_image(self.file_paths, output_path)
                tk.messagebox.showinfo("Success", "Image merged successfully!")
        else:
            tk.messagebox.showerror("Error", "Select at least 1 text files to merge.") 
            
            
if __name__ == "__main__":
    app = PDFProcessorGUI()
    app.mainloop()
