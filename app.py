import os
import zipfile
import shutil
from flask import Flask, render_template, request
from engine import calculate_match, extract_text_from_pdf, get_missing_skills

app = Flask(__name__)

# Folder to store uploaded CVs temporarily
UPLOAD_FOLDER = 'uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Helper function to process individual files
def process_file(path, jd, results_list, display_name=None):
    text = extract_text_from_pdf(path)
    score = calculate_match(text, jd)
    missing = get_missing_skills(text, jd)
    results_list.append({
        'filename': display_name if display_name else os.path.basename(path),
        'score': score,
        'missing': missing
    })

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/analyze', methods=['POST'])
def analyze():
    if request.method == 'POST':
        job_desc = request.form.get('job_description')
        uploaded_files = request.files.getlist('resume_files')
        
        if not job_desc or not uploaded_files:
            return render_template('index.html', error="Please provide both a JD and files.")

        all_results = []
        
        for file in uploaded_files:
            # OPTION 1: IT'S A PDF
            if file.filename.endswith('.pdf'):
                file_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(file_path)
                process_file(file_path, job_desc, all_results)
                os.remove(file_path)

            # OPTION 2: IT'S A ZIP
            elif file.filename.endswith('.zip'):
                zip_path = os.path.join(UPLOAD_FOLDER, file.filename)
                file.save(zip_path)
                
                temp_extract = os.path.join(UPLOAD_FOLDER, "temp_zip")
                with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                    zip_ref.extractall(temp_extract)
                    
                for root, dirs, files in os.walk(temp_extract):
                    for filename in files:
                        if filename.endswith('.pdf'):
                            f_path = os.path.join(root, filename)
                            process_file(f_path, job_desc, all_results, filename)
                
                # Cleanup
                os.remove(zip_path)
                shutil.rmtree(temp_extract)

        # SORT: Highest score first
        ranked_results = sorted(all_results, key=lambda x: x['score'], reverse=True)
        return render_template('index.html', results=ranked_results, jd=job_desc)
    
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)