# app.py - Flask application for biodata collection and PDF generation

from flask import Flask, render_template, request, send_file
from fpdf import FPDF
import os
import tempfile

app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/generate_pdf', methods=['POST'])
def generate_pdf():
    # Extract biodata from form
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    phone = request.form.get('phone', '')
    address = request.form.get('address', '')
    education = request.form.get('education', '')
    experience = request.form.get('experience', '')
    skills = request.form.get('skills', '')
    
    # Create PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Set title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(190, 10, 'Personal Bio Data', 0, 1, 'C')
    pdf.ln(10)
    
    # Content formatting function
    def add_field(label, value):
        pdf.set_font('Arial', 'B', 12)
        pdf.cell(40, 10, label, 0, 0)
        pdf.set_font('Arial', '', 12)
        pdf.multi_cell(150, 10, value)
    
    # Add fields
    add_field('Name:', name)
    add_field('Email:', email)
    add_field('Phone:', phone)
    add_field('Address:', address)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(190, 10, 'Education', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(190, 10, education)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(190, 10, 'Experience', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(190, 10, experience)
    pdf.ln(5)
    
    pdf.set_font('Arial', 'B', 14)
    pdf.cell(190, 10, 'Skills', 0, 1)
    pdf.set_font('Arial', '', 12)
    pdf.multi_cell(190, 10, skills)
    
    # Save PDF to a temporary file
    temp_file = tempfile.NamedTemporaryFile(delete=False, suffix='.pdf')
    pdf_path = temp_file.name
    temp_file.close()
    pdf.output(pdf_path)
    
    # Return the PDF as a download
    return send_file(pdf_path, as_attachment=True, download_name=f"{name.replace(' ', '_')}_biodata.pdf", mimetype='application/pdf')

if __name__ == '__main__':
    app.run(debug=True)