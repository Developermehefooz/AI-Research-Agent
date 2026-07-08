import os
from dotenv import load_dotenv
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini API
genai.configure(
    api_key=os.getenv("GOOGLE_API_KEY")
)

# Gemini Model
model = genai.GenerativeModel(
    "gemini-2.5-flash"
)


def generate_report(topic, content):

    prompt = f"""
You are a professional research analyst.

Create a detailed, professional research report on:

{topic}

Requirements:

- Use professional business language.
- Do NOT use markdown symbols.
- Do NOT use *, **, #, ##, ###.
- Use numbered sections only.
- Use proper headings.
- Make the report easy to read.
- Use complete paragraphs.
- Include practical examples where relevant.

Structure:

1. Executive Summary

2. Introduction

3. Key Concepts

4. Benefits and Advantages

5. Challenges and Limitations

6. Current Trends and Innovations

7. Future Scope

8. Conclusion

Research Data:

{content[:6000]}
"""

    response = model.generate_content(prompt)

    report = response.text

    # Clean unwanted markdown formatting
    report = report.replace("**", "")
    report = report.replace("* ", "")
    report = report.replace("*", "")
    report = report.replace("###", "")
    report = report.replace("##", "")
    report = report.replace("#", "")

    return report