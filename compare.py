import openai

"""Compare Resume JOB using LLM"""
def compare_resume_job(resume_text, job_description,max_tokens,temperature):
    # Call OpenAI API to compare resume and job description
    comparison_result = openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
        {"role": "system", "content": f"You are a helpful assistant that can compare and analyze the resume to the job description and provide the percentage of similarity to conclude whether the candidate should take this job or not. Display just the analysis without any additional information with the language that you can detect from the job description."},
        {"role": "user", "content": f"Resume {resume_text} , and the job description {job_description}"},
        ],
        temperature=temperature,
        max_tokens=max_tokens,
        stream=False,
    )
    return comparison_result.choices[0].message.content
