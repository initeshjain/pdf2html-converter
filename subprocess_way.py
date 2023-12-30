import os
import subprocess

def convert_pdf_to_html(pdf_path, output_dir):
    # Create the output directory if it doesn't exist
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Get the absolute paths of the PDF file and output directory
    abs_pdf_path = os.path.abspath(pdf_path)
    abs_output_dir = os.path.abspath(output_dir)

    # Run pdf2htmlEX Docker command with volume mount
    subprocess.call(['docker', 'run', '-ti', '--rm',
                     '-v', f'{abs_pdf_path}:/pdf/input.pdf',
                     '-v', f'{abs_output_dir}:/pdf/output',
                     'bwits/pdf2htmlex', 'pdf2htmlEX', '/pdf/input.pdf', '/pdf/output/output.html'])

    print(f"PDF conversion complete. HTML file saved to: {os.path.join(output_dir, 'output.html')}")

# Example usage
pdf_path = r'F:\PROJECTS\PYTHON\PDF2HTML\input.pdf'
output_dir = r'F:\PROJECTS\PYTHON\PDF2HTML'

convert_pdf_to_html(pdf_path, output_dir)
