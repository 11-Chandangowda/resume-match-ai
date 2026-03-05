import pdfplumber
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text


def calculate_match_score(resume, jd):
    texts = [resume, jd]
    tfidf = TfidfVectorizer().fit_transform(texts)
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0]
    return round(score * 100, 2)


def get_ai_feedback(resume, jd):

    # Clean text
    resume_clean = re.sub(r"[^\w\s]", "", resume.lower())
    jd_clean = re.sub(r"[^\w\s]", "", jd.lower())

    resume_words = set(resume_clean.split())
    jd_words = set(jd_clean.split())

    stopwords = {
        "and", "or", "the", "a", "an", "with", "we", "are",
        "to", "of", "for", "in", "on", "have", "should"
    }

    missing = jd_words - resume_words - stopwords
    missing_skills = list(missing)[:12]

    return f"""
🔎 Missing Skills (Top Matches):
{', '.join(missing_skills)}

✅ Suggestions:
• Add missing technical skills if relevant  
• Highlight project experience clearly  
• Add measurable achievements (numbers/results)  
• Improve keyword optimization for ATS  

✨ Resume Improvement Tip:
Use strong action verbs like analyzed, developed, automated, optimized.
"""