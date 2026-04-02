# RecruitAI | Semantic Resume Parser & Ranker

An AI-powered recruitment tool designed to automate the screening of thousands of resumes using **Natural Language Processing (NLP)**. Unlike traditional keyword-based filters, RecruitAI understands the **context** and **meaning** of a candidate's experience.

## Key Features

- **Semantic Matching:** Utilizes **BERT (Sentence-Transformers)** to calculate the mathematical similarity between CVs and Job Descriptions.
- **Batch & ZIP Processing:** High-speed extraction for multiple PDFs or compressed ZIP folders using **PyMuPDF**.
- **Skills Gap Analysis:** Automatically identifies missing technical requirements (e.g., React, Docker) and highlights them in real-time.
- **Ranked Leaderboard:** A dynamic, Bootstrap-based dashboard that sorts candidates from highest to lowest match score.

## How it Works

The system converts text into high-dimensional vector embeddings using the `all-MiniLM-L6-v2` model. It then calculates the **Cosine Similarity** between the Job Description vector and each Candidate vector.

## 🛠 Tech Stack

- **Language:** Python 3.10+
- **Framework:** Flask (Backend), Bootstrap 5 (Frontend)
- **AI/ML:** Sentence-Transformers, PyTorch
- **PDF Engine:** PyMuPDF (fitz)
- **Data Handling:** Zipfile, Shutil

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/your-username/RecruitAI.git](https://github.com/your-username/RecruitAI.git)
   cd RecruitAI
   ```
2. **Setup Virtual Environment:**
   ```bash
    python -m venv venv
    venv\Scripts\activate
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the App:**
   ```bash
   python app.py
   ```

Visit http://127.0.0.1:5000 in your browser.

```

```
