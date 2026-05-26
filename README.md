# 🕵️ AI Fact-Check Agent

An AI-powered fact verification system that extracts factual claims from PDF documents and verifies them using live web search and Large Language Models (LLMs).

Built using:
- Streamlit
- Groq LLM
- DuckDuckGo Search
- PDFPlumber

---

# 🚀 Features

✅ Upload PDF documents  
✅ Extract important factual claims  
✅ Detect fake or inaccurate information  
✅ Live web-based verification  
✅ Beautiful modern UI  
✅ Real-time verification results  
✅ AI-powered fact-checking system  

---

# 📌 How It Works

The application follows this workflow:

1. User uploads a PDF file
2. PDF text is extracted using PDFPlumber
3. AI extracts factual claims from the text
4. Live web search gathers related information
5. Groq LLM verifies the claims
6. Results are displayed as:
   - VERIFIED
   - INACCURATE
   - FALSE

---

# 🧠 Technologies Used

| Technology | Purpose |
|---|---|
| Streamlit | Frontend UI |
| Groq API | LLM-based reasoning |
| DuckDuckGo Search | Live web search |
| PDFPlumber | PDF text extraction |
| Python | Backend logic |

---

# 📂 Project Structure

```bash
fact-check-agent/
│
├── assets/
├── temp/
│
├── utils/
│   ├── extractor.py
│   ├── verifier.py
│   └── prompts.py
│
├── .env
├── .gitignore
├── app.py
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

## 1️⃣ Clone Repository

```bash
git clone YOUR_GITHUB_REPO_LINK
```

---

## 2️⃣ Open Project Folder

```bash
cd fact-check-agent
```

---

## 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Setup API Key

Create a `.env` file in the root directory.

Add:

```env
GROQ_API_KEY=your_api_key_here
```

---

# ▶️ Run Application

```bash
streamlit run app.py
```

---

# 🌐 Application Flow

### PDF Upload
Users upload any PDF document.

### Claim Extraction
The system extracts:
- statistics
- percentages
- dates
- factual statements
- financial figures

### Verification
Claims are verified using:
- live web search
- AI reasoning

### Result Categories

| Status | Meaning |
|---|---|
| VERIFIED | Claim is correct |
| INACCURATE | Claim is partially incorrect or outdated |
| FALSE | Claim is fake or unsupported |

---

# 🎯 Example Claims

Example extracted claims:

```text
India GDP is 10 trillion dollars.
OpenAI was founded in 2012.
Tesla was founded in 1998.
```

Example verification results:

```text
Status: INACCURATE
Correct Info: India GDP is around 3.5 trillion dollars.
```

---

# 🎨 UI Features

✅ Dark modern UI  
✅ Interactive cards  
✅ Animated hover effects  
✅ Status-based color indicators  
✅ Responsive layout  

---

# 📦 requirements.txt

```txt
streamlit
pdfplumber
duckduckgo-search
requests
groq
python-dotenv
```

---

# ☁️ Deployment (Streamlit Cloud)

## Step 1 — Push to GitHub

```bash
git init
git add .
git commit -m "Initial Commit"
git branch -M main
git remote add origin YOUR_REPO_URL
git push -u origin main
```

---

## Step 2 — Deploy on Streamlit Cloud

Visit:

https://streamlit.io/cloud

Steps:
1. Login with GitHub
2. Click "New App"
3. Select repository
4. Select `app.py`
5. Click Deploy

---

## Step 3 — Add Secrets

In Streamlit Cloud:

Settings → Secrets

Add:

```toml
GROQ_API_KEY="your_api_key"
```

---

# 📹 Demo Video

Create a short demo video showing:
- PDF upload
- claim extraction
- verification results

---

# 👨‍💻 Developer

Developed by **Ajeet Kumar**

---

# 📜 License

This project is developed for educational and assessment purposes.