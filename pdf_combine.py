#! python3
from PyPDF2 import PdfFileMerger
import os

pdfs_location = (
    r'D:\plhnk\Documents\Global Riser\178 - PAC_BORA 5 YR'
    r'\1 Planning\Tools\Equipment Certs\FOR REPORTS')

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
