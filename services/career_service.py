import json
from services.llm_service import client, MODEL



def get_career_recommendations(skills, interests, education, experience_level):
    """
    Generate career recommendations using an AI model.
    """

    prompt = f"""
    You are an expert AI career counselor.

    Analyze the following student profile and recommend exactly 3 suitable careers.

    Student Profile:
    Skills: {skills}
    Interests: {interests}
    Education: {education}
    Experience Level: {experience_level}

    Return ONLY valid JSON in this exact structure:

    {{
        "recommendations": [
            {{
                "career_title": "Career Name",
                "match_score": 90,
                "description": "Career description",
                "why_good_fit": "Why this career suits the student",
                "average_salary": "Approximate salary range in India",
                "growth_outlook": "Career growth outlook",
                "key_skills_needed": ["Skill 1", "Skill 2", "Skill 3"]
            }}
        ]
    }}

    Instructions:
    - Recommend exactly 3 careers.
    - Match careers to the student's skills and interests.
    - Match score must be between 0 and 100.
    - Salary information should be approximate, not guaranteed.
    - Keep descriptions clear and student-friendly.
    - Do not include markdown or text outside the JSON.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional AI career counselor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            max_tokens=1500
        )

        ai_result = response.choices[0].message.content

        parsed_result = json.loads(ai_result)

        recommendations = parsed_result["recommendations"]

        result = {
            "success": True,
            "message": "Career recommendations generated successfully.",
            "data": {
                "user_profile": {
                    "skills": skills,
                    "interests": interests,
                    "education": education,
                    "experience_level": experience_level,
                },
                "recommendations": recommendations,
                "total_recommendations": len(recommendations),
            },
        }

        return result

    except Exception as e:
        return {
            "success": False,
            "message": "Failed to generate career recommendations.",
            "error": str(e),
        }
