import streamlit as st
from dotenv import load_dotenv
import os
from groq import Groq
from pypdf import PdfReader
from reportlab.lib.pagesizes import LETTER
from reportlab.pdfgen import canvas
import tempfile
import re

# ======================
# ENV + CLIENT
# ======================
load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

# ======================
# PAGE CONFIG
# ======================
st.set_page_config(
    page_title="AI Resume Analyzer",
    page_icon="📄",
    layout="centered"
)

# ======================
# HIGH-QUALITY BACKGROUND
# ======================
BACKGROUND_IMAGE_URL = (
    "https://images.unsplash.com/photo-1522071820081-009f0129c71c"
    "?auto=format&fit=crop&w=3840&q=95"
)

st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url("{BACKGROUND_IMAGE_URL}");
        background-size: cover;
        background-position: center;
        background-attachment: fixed;
    }}

    .glass {{
        background: rgba(2, 6, 23, 0.92);
        border-radius: 18px;
        padding: 30px;
        margin-bottom: 25px;
        box-shadow: 0 10px 30px rgba(0,0,0,0.4);
    }}

    h1 {{
        font-size: 34px;
        color: #F9FAFB !important;
    }}

    h3 {{
        color: #E5E7EB !important;
    }}

    p, label, span {{
        color: #E5E7EB !important;
        font-size: 16px;
    }}

    pre {{
        color: #F9FAFB !important;
        font-size: 15px;
    }}
    </style>
    """,
    unsafe_allow_html=True
)

# ======================
# HEADER
# ======================
st.markdown(
    """
    <div class="glass">
        <h1>AI Resume Analyzer</h1>
        <p>ATS Score • Strengths • Weaknesses • PDF Report • Batch Analysis</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ======================
# FILE UPLOAD (BATCH)
# ======================
uploaded_files = st.file_uploader(
    "Upload Resume PDFs",
    type=["pdf"],
    accept_multiple_files=True
)

# ======================
# PDF TEXT EXTRACTION
# ======================
def extract_text(pdf):
    reader = PdfReader(pdf)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()

# ======================
# AI ANALYSIS
# ======================
def analyze_resume(resume_text):
    prompt = f"""
You are a professional ATS resume evaluator.

Analyze the resume and respond strictly in this format:

STRENGTHS:
- ...

WEAKNESSES:
- ...

ATS SCORE:
<number between 0 and 100>

IMPROVEMENT TIPS:
- ...

Resume:
{resume_text}
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.2,
        max_tokens=900
    )

    return response.choices[0].message.content

# ======================
# SAFE ATS SCORE PARSER
# ======================
def extract_ats_score(text):
    match = re.search(r"ATS SCORE\s*:\s*(\d{1,3})", text)
    if match:
        score = int(match.group(1))
        return min(score, 100)
    return 0  # SAFE DEFAULT

# ======================
# PDF REPORT
# ======================
def generate_pdf(report_text):
    temp = tempfile.NamedTemporaryFile(delete=False, suffix=".pdf")
    c = canvas.Canvas(temp.name, pagesize=LETTER)
    width, height = LETTER

    y = height - 40
    for line in report_text.split("\n"):
        c.drawString(40, y, line[:110])
        y -= 14
        if y < 40:
            c.showPage()
            y = height - 40

    c.save()
    return temp.name

# ======================
# PROCESS
# ======================
if uploaded_files:
    for file in uploaded_files:
        with st.spinner(f"Analyzing {file.name}..."):
            resume_text = extract_text(file)

            if len(resume_text) < 100:
                st.error(f"{file.name} could not be analyzed.")
                continue

            result = analyze_resume(resume_text)
            ats_score = extract_ats_score(result)

            st.markdown(
                f"<div class='glass'><h3>{file.name}</h3></div>",
                unsafe_allow_html=True
            )

            # ATS SCORE BAR
            st.progress(ats_score / 100)
            st.write(f"**ATS Score:** {ats_score}/100")

            # RESULT DISPLAY
            st.markdown(
                f"""
                <div class="glass">
                    <pre style="white-space: pre-wrap;">{result}</pre>
                </div>
                """,
                unsafe_allow_html=True
            )

            # PDF DOWNLOAD
            pdf_path = generate_pdf(result)
            with open(pdf_path, "rb") as f:
                st.download_button(
                    "Download PDF Report",
                    data=f,
                    file_name=f"{file.name}_analysis.pdf",
                    mime="application/pdf"
                )


# FOOTER
# ======================
st.markdown(
    """
    <div class="glass" style="text-align:center;">
        <p>Developed by @MOHAN KODURU | AI Automator</p>
    </div>
    """,
    unsafe_allow_html=True
)
