#! python3
from PyPDF2 import PdfFileMerger
import os

pdfs_location = (
    r'D:\path\path1\path path\this is a multiline long'
    r'\path\pathpath\path\PDF FOLDER')

os.chdir(pdfs_location)

# Specific PDFs in directory in order listed
# pdfs = ['pdf1.pdf', 'pdf2.pdf']

# All PDFs in directory
pdfs = [a for a in os.listdir() if a.endswith(".pdf")]

merger = PdfFileMerger()

for pdf in pdfs:
    merger.append(pdf)

merger.write("result.pdf")
merger.close()
