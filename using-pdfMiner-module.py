from pdfminer.converter import HTMLConverter
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from io import BytesIO

def convert_pdf_to_html(pdf_path, output_path):
    rsrcmgr = PDFResourceManager()
    codec = 'utf-8'
    laparams = None
    with BytesIO() as output_buffer:
        device = HTMLConverter(rsrcmgr, output_buffer, codec=codec, laparams=laparams)
        with open(pdf_path, 'rb') as pdf_file:
            interpreter = PDFPageInterpreter(rsrcmgr, device)
            for page in PDFPage.get_pages(pdf_file):
                interpreter.process_page(page)
        html_data = output_buffer.getvalue()
    
    with open(output_path, 'wb') as output_file:
        output_file.write(html_data)

# Example usage
pdf_path = './input.pdf'
output_path = './output.html'

convert_pdf_to_html(pdf_path, output_path)
