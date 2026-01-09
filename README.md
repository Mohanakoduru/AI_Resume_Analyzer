# 📄 AI Resume Analyzer – ATS Intelligence System

An AI-powered resume analysis application that evaluates resumes based on Applicant Tracking System (ATS) standards. The system extracts resume content, analyzes strengths and weaknesses, generates an ATS compatibility score, and provides actionable improvement suggestions to enhance job shortlisting success.

This project is built as a production-ready, client-facing application using Streamlit and Groq LLM APIs.

---

## 🚀 Features

- Upload and analyze single or multiple resume PDFs
- Automatic resume text extraction
- AI-powered identification of:
  - Resume strengths
  - Resume weaknesses
  - ATS compatibility score (0–100)
  - Improvement recommendations
- Visual ATS score progress bar
- Batch resume analysis support
- Downloadable PDF analysis reports
- High-contrast, professional UI for end users
- Secure API key handling using environment variables

---

## 🧠 How It Works

1. User uploads one or more resume PDFs
2. Resume text is extracted from the PDF documents
3. Resume content is processed using a Large Language Model via Groq API
4. The system generates:
   - Strengths
   - Weaknesses
   - ATS score
   - Improvement tips
5. Results are displayed in the Streamlit UI and exported as a downloadable PDF report

---

## 🛠️ Technologies Used

- Python
- Streamlit (Frontend & UI)
- Groq API (Large Language Model)
- Natural Language Processing (NLP)
- PyPDF (PDF text extraction)
- ReportLab (PDF report generation)
- python-dotenv (Environment variable management)

---

## 📁 Project Structure

ai_resume_analyzer/
│
├── app.py                # Main Streamlit application
├── requirements.txt      # Python dependencies
├── .env.example          # Environment variable template
└── README.md             # Project documentation

---

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

git clone https://github.com/your-username/ai-resume-analyzer.git  
cd ai-resume-analyzer

---

### 2️⃣ Create Virtual Environment

python -m venv venv  
venv\Scripts\activate   (Windows)

---

### 3️⃣ Install Dependencies

pip install -r requirements.txt

---

### 4️⃣ Configure Environment Variables

Create a `.env` file in the root directory:

GROQ_API_KEY=your_groq_api_key_here

---

## ▶️ Run the Application

streamlit run app.py

The application will launch in your default browser.

---

## 🔐 Security & Best Practices

- API keys are stored securely using environment variables
- `.env` file is excluded from version control
- Robust error handling prevents runtime crashes
- Safe default values are used for AI-generated outputs

---

## 🎯 Use Cases

- Job seekers optimizing resumes for ATS systems
- Career coaches offering professional resume reviews
- Recruitment agencies screening candidate resumes
- Freelancers providing AI resume analysis services

---

## 📈 Future Enhancements

- Resume keyword gap analysis
- Job description matching
- ATS keyword heatmap
- Branded PDF reports
- Email delivery of analysis reports
- Admin analytics dashboard


---

## ⭐ Support

If you find this project useful, consider starring the repository ⭐.
Contributions and improvements are welcome.
