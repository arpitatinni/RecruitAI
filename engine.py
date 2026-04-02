import fitz
import re
from sentence_transformers import SentenceTransformer, util


model = SentenceTransformer('all-MiniLM-L6-v2')

# A dictionary of common tech skills to look for
SKILLS_DB = [
    'Python', 'Flask', 'Django', 'SQL', 'MySQL', 'SQLite', 'PostgreSQL',
    'Machine Learning', 'Deep Learning', 'NLP', 'BERT', 'Transformers',
    'HTML', 'CSS', 'Bootstrap', 'JavaScript', 'React', 'Node.js',
    'Git', 'GitHub', 'Docker', 'AWS', 'Azure', 'Java', 'C++', 'PHP'
]

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

def get_missing_skills(resume_text, job_desc):
    # Normalize text to lowercase for matching
    resume_text = resume_text.lower()
    job_desc = job_desc.lower()
    
    missing = []
    for skill in SKILLS_DB:
        # Check if the skill is mentioned in the Job Description
        if skill.lower() in job_desc:
            # If it's in the JD but NOT in the Resume, it's a "Missing Skill"
            if skill.lower() not in resume_text:
                missing.append(skill)
    return missing

def calculate_match(resume_text, job_description):
    embedding1 = model.encode(resume_text, convert_to_tensor=True)
    embedding2 = model.encode(job_description, convert_to_tensor=True)
    cosine_score = util.pytorch_cos_sim(embedding1, embedding2)
    return round(float(cosine_score[0][0]) * 100, 2)