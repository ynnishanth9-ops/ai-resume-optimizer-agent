"""
AI Resume Optimizer Agent

A starter AI automation project that compares a resume against a job description
and identifies missing skills, matched keywords, and improvement suggestions.
"""


def extract_keywords(text):
    keywords = [
        "python", "sql", "power bi", "excel", "machine learning",
        "data analysis", "automation", "api", "langchain",
        "communication", "stakeholder", "dashboard"
    ]

    text_lower = text.lower()
    return [keyword for keyword in keywords if keyword in text_lower]


def compare_resume_to_job(resume_text, job_description):
    resume_keywords = set(extract_keywords(resume_text))
    job_keywords = set(extract_keywords(job_description))

    matched_keywords = resume_keywords.intersection(job_keywords)
    missing_keywords = job_keywords.difference(resume_keywords)

    return matched_keywords, missing_keywords


def generate_recommendations(missing_keywords):
    if not missing_keywords:
        return ["Resume is well aligned with the job description."]

    return [
        f"Consider adding evidence of experience with {keyword}."
        for keyword in missing_keywords
    ]


def main():
    resume_text = """
    Data analyst with experience in Python, SQL, Excel, dashboards,
    automation, and stakeholder communication.
    """

    job_description = """
    We are looking for a data analyst with Python, SQL, Power BI,
    dashboard development, API integration, and automation experience.
    """

    matched, missing = compare_resume_to_job(resume_text, job_description)
    recommendations = generate_recommendations(missing)

    print("Matched Keywords:", sorted(matched))
    print("Missing Keywords:", sorted(missing))
    print("Recommendations:")
    for item in recommendations:
        print("-", item)


if __name__ == "__main__":
    main()