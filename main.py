import streamlit as st
import openai
import pandas as pd
from config.settings import get_settings
from compare import compare_resume_job
from calculate_fit import calculate_fit_percentage
from extract_text_from_pdf import extract_text_from_pdf
import time
import pyautogui



settings = get_settings()
openai.api_key = settings.API_KEY
st.set_page_config(page_title="Align Talents", page_icon=":robot:", layout="wide")

def main():
    st.title("🤖Aligning Talents")
    st.write("A Comparative Analysis of Resumes and Job Descriptions...")
    resumes = st.file_uploader("Upload multiple resumes (e.g., 5 resumes)", accept_multiple_files=True, type=['pdf', 'txt'])
    job_description = st.text_area("Paste the job description here:")
    max_tokens=st.sidebar.text_input("Maximum Tokens")
    if not max_tokens:
        st.warning("Please provide a maximum tokens value.")
    temperature=st.sidebar.slider("Temperature", min_value=0.0, max_value=1.0, step=0.1)
    if st.button("Analyze Resumes"):
        if not resumes or not job_description:
            st.warning("Please provide both resumes and a job description.")
        else:
            fit_results = []
            for resume in resumes:
                resume_text = extract_text_from_pdf(resume)
                fit_percentage = calculate_fit_percentage(resume_text, job_description)
                llm_analysis = compare_resume_job(resume_text, job_description,int(max_tokens),temperature)
                print(llm_analysis)
                fit_results.append((resume.name, fit_percentage,llm_analysis))
            with st.spinner("Analyzing resumes..."):
                time.sleep(10)
                df = pd.DataFrame(fit_results, columns=["Candidate Name", "Fit Percentage(Cosine similarity)","LLM Analysis"])
                st.success("Resume analysis complete!")
                st.write("JOB Analysis Results:")
                st.dataframe(df)
    if st.sidebar.button("Reload Session"):
        pyautogui.hotkey("ctrl","F5")


# Run the main function
if __name__ == "__main__":
    main()
