import streamlit as st
from utils import extract_text_from_pdf, calculate_match_score, get_ai_feedback

st.title("📄 Resume + Job Match AI Tool")

uploaded_file = st.file_uploader("Upload Resume (PDF)", type="pdf")
jd_text = st.text_area("Paste Job Description")

if uploaded_file and jd_text:

    resume_text = extract_text_from_pdf(uploaded_file)

    score = calculate_match_score(resume_text, jd_text)

    st.subheader(f"Match Score: {score}%")

    if st.button("Get AI Suggestions"):
        feedback = get_ai_feedback(resume_text, jd_text)
        st.write(feedback)