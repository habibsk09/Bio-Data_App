# 🧬 Biodata Generator App

This is a web-based **Biodata Generator** built with **Flask (Python)** and **HTML/CSS**. The app lets users fill in a simple form with personal, educational, and professional details — and then **generates a downloadable PDF** formatted as a clean and structured biodata sheet.

---

## 🚀 Features

- 📋 Easy-to-use biodata form  
- 🧾 PDF generation using Python `fpdf`  
- 🎯 Centered and clean layout with titles and sections  
- 📥 One-click download of your biodata in PDF format  
- 🔒 All data processed locally; nothing is stored  

---

## 🖼️ Example Output

Here is a sample of the generated biodata PDF:

![PDF Preview](XYZ_biodata.pdf)



---

## 💻 Tech Stack

- **Backend**: Python 3, Flask  
- **Frontend**: HTML, CSS (can be enhanced with Bootstrap)  
- **PDF Engine**: FPDF (Python library)  

---

## 📦 Installation

1. **Clone the repository:**

```bash
git clone https://github.com/your-username/biodata-generator.git
cd biodata-generator
2. Create a virtual environment (optional but recommended):
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.Install required libraries:
pip install -r requirements.txt
▶️ Run the App
python app.py
Then open your browser and go to:
👉 http://localhost:5000
📂 Project Structure
biodata-generator/
├── templates/
│   └── index.html         # HTML form page
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── static/ (optional)     # CSS or assets
└── Biodata Generator.pdf  # Sample PDF output (optional)
🛠️ To-Do / Improvements
• Add profile picture upload

• Support multi-page PDFs for long content

• Add date of birth, gender, and other biodata fields

• Use Bootstrap for responsive UI

• Host online (e.g., Render, Vercel, Heroku)
📃 License
This project is open-sourced under the MIT License.
👤 Author
Made with ❤️ Habibur Saikh

---




