# app.py

import streamlit as st
from utils.extractor import extract_text_from_pdf, extract_claims
from utils.verifier import verify_claim

st.set_page_config(
    page_title="AI Fact-Check Agent",
    page_icon="🕵️",
    layout="wide"
)

# ---------- CUSTOM CSS ----------

st.markdown("""
<style>

.main {
    background-color: #0E1117;
}

/* Headings */

h1, h2, h3 {
    color: white;
}

/* Claim Cards */

.claim-box {
    background: linear-gradient(145deg, #1c1f26, #232833);
    padding: 22px;
    border-radius: 18px;
    margin-bottom: 18px;
    border-left: 6px solid #4F8BF9;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.35);
    transition: 0.3s ease-in-out;
}

.claim-box:hover {
    transform: scale(1.01);
    box-shadow: 0px 6px 20px rgba(79,139,249,0.25);
}

/* Status Variants */

.verified {
    border-left: 6px solid #00C853;
}

.false {
    border-left: 6px solid #FF1744;
}

.inaccurate {
    border-left: 6px solid #FFD600;
}

/* Card Title */

.claim-title {
    font-size: 20px;
    font-weight: 700;
    color: white;
    margin-bottom: 12px;
}

/* Status Text */

.status-text {
    font-size: 16px;
    margin-top: 8px;
    color: #E0E0E0;
}

/* Correct Info */

.correct-info {
    margin-top: 10px;
    padding: 12px;
    background-color: rgba(255,255,255,0.05);
    border-radius: 10px;
    color: #D6D6D6;
    line-height: 1.6;
}

/* Metric Cards */

[data-testid="metric-container"] {
    background: linear-gradient(145deg, #1c1f26, #232833);
    border: 1px solid rgba(255,255,255,0.08);
    padding: 18px;
    border-radius: 18px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.3);
}

/* Upload Section */

section[data-testid="stFileUploader"] {
    background: linear-gradient(145deg, #1c1f26, #232833);
    padding: 20px;
    border-radius: 18px;
    border: 1px dashed #4F8BF9;
}

/* Footer */

.footer {
    margin-top: 50px;
    padding: 25px;
    text-align: center;
    color: #B0B0B0;
    font-size: 14px;
    border-top: 1px solid rgba(255,255,255,0.08);
}

.footer strong {
    color: white;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------

st.title("🕵️ AI Fact-Check Agent")

st.markdown("""
### 🚀 AI-Powered Fact Verification System

Upload a PDF document and automatically verify claims using:
- Live Web Search
- AI Verification
- Real-Time Fact Checking
""")

st.divider()

# ---------- FILE UPLOAD ----------

uploaded_file = st.file_uploader(
    "📄 Upload PDF File",
    type=["pdf"]
)

# ---------- MAIN LOGIC ----------

if uploaded_file:

    temp_path = f"temp/{uploaded_file.name}"

    with open(temp_path, "wb") as f:
        f.write(uploaded_file.read())

    st.success("✅ PDF Uploaded Successfully!")

    # ---------- TEXT EXTRACTION ----------

    with st.spinner("📚 Extracting text from PDF..."):
        text = extract_text_from_pdf(temp_path)

    # ---------- CLAIM EXTRACTION ----------

    with st.spinner("🧠 Extracting factual claims..."):
        claims = extract_claims(text)

    if claims:

        st.divider()

        st.subheader("📌 Extracted Claims")

        for claim in claims:

            st.markdown(f'''
            <div class="claim-box">
            {claim}
            </div>
            ''', unsafe_allow_html=True)

        st.divider()

        st.subheader("✅ Verification Results")

        results = []

        progress = st.progress(0)

        verified_count = 0
        inaccurate_count = 0
        false_count = 0

        for i, claim in enumerate(claims):

            status, info = verify_claim(claim)

            results.append({
                "Claim": claim,
                "Status": status,
                "Correct Info": info
            })

            if "VERIFIED" in status:
                verified_count += 1

            elif "FALSE" in status:
                false_count += 1

            else:
                inaccurate_count += 1

            progress.progress((i + 1) / len(claims))

        # ---------- METRICS ----------

        col1, col2, col3 = st.columns(3)

        with col1:
            st.metric("✅ Verified", verified_count)

        with col2:
            st.metric("⚠️ Inaccurate", inaccurate_count)

        with col3:
            st.metric("❌ False", false_count)

        st.divider()

        # ---------- RESULTS DISPLAY ----------

        for row in results:

            status = row["Status"]

            css_class = "claim-box"

            if "VERIFIED" in status:
                css_class += " verified"

            elif "FALSE" in status:
                css_class += " false"

            else:
                css_class += " inaccurate"

            st.markdown(f'''
            <div class="{css_class}">

            <div class="claim-title">
            📌 {row['Claim']}
            </div>
            <div class="status-text">
            <b>Status:</b> <span style="font-weight:700;">{row['Status']}</span>
            </div>
            <div class="correct-info">
            <b>Correct Information:</b><br>
            {row['Correct Info']}
            </div>
            </div>
            ''', unsafe_allow_html=True)

    else:
        st.warning("⚠️ No claims found in the document.")

# ---------- FOOTER ----------

st.markdown("""
<div class="footer">

🚀 <strong>AI Fact-Check Agent</strong><br>
Powered by Groq LLM + Live Web Verification + Streamlit<br><br>
Developed by <strong>Ajeet Kumar</strong>
</div>
""", unsafe_allow_html=True)