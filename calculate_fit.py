"""Calculate fit module """

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_fit_percentage(resume_text, job_description):
    vectorizer = CountVectorizer()

    vectorized_documents = vectorizer.fit_transform([resume_text, job_description])

    resume_vector = vectorized_documents[0]
    job_vector = vectorized_documents[1]

    cosine_sim = cosine_similarity(resume_vector, job_vector)

    fit_percentage = cosine_sim[0][0] * 100

    return fit_percentage
