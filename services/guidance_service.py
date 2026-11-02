import json
from services.llm_service import client, MODEL


def get_career_comparison(careers):
    """
    Compare careers using AI.
    """

    prompt = f"""
    You are an expert career counselor.

    Compare these careers: {careers}

    Return ONLY valid JSON with this structure:
    {{
        "careers_compared": {careers},
        "comparison": [
            {{
                "career_title": "Career Name",
                "average_salary": "Approximate salary in India",
                "growth_outlook": "High, Moderate, or Low with explanation",
                "education_required": "Required education",
                "key_skills": ["Skill 1", "Skill 2"],
                "work_life_balance": "Description",
                "pros": ["Pro 1", "Pro 2"],
                "cons": ["Con 1", "Con 2"]
            }}
        ],
        "recommendation": "Personalized comparison summary"
    }}

    Instructions:
    - Include one comparison entry for every career provided.
    - Compare salary, skills, education, growth, work-life balance, pros and cons.
    - Salary estimates must be approximate and relevant to India.
    - Do not claim that salaries or growth are guaranteed.
    - Make the comparison balanced and practical.
    - Do not include markdown outside the JSON.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional career comparison counselor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            max_tokens=2000
        )

        ai_result = response.choices[0].message.content
        comparison_data = json.loads(ai_result)

        result = {
            "success": True,
            "message": f"Comparison of {len(careers)} careers completed successfully.",
            "data": comparison_data,
        }

        return result

    except Exception as e:
        return {
            "success": False,
            "message": "Career comparison failed.",
            "error": str(e),
        }


def get_career_advice(question, context):
    """
    Generate personalized career guidance using AI.
    """

    prompt = f"""
    You are an experienced career counselor.

    Student's Question:
    {question}

    Student's Context:
    {context if context else "No additional context provided."}

    Return ONLY valid JSON with this structure:
    {{
        "question": "Original question",
        "context_received": "Student context",
        "advice": {{
            "summary": "Short summary of the advice",
            "detailed_response": "Detailed personalized career guidance",
            "action_steps": [
                "Action step 1",
                "Action step 2",
                "Action step 3"
            ],
            "resources": [
                {{
                    "name": "Resource Name",
                    "type": "Course, Tutorial, or Guide",
                    "url": "https://example.com"
                }}
            ]
        }}
    }}

    Instructions:
    - Answer the student's actual question.
    - Personalize the advice using the context.
    - Provide practical and realistic action steps.
    - Include useful learning resources when appropriate.
    - Avoid guaranteeing jobs, salaries, or career outcomes.
    - Do not include markdown outside the JSON.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a helpful and professional career guidance counselor."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            max_tokens=2000
        )

        ai_result = response.choices[0].message.content
        advice = json.loads(ai_result)

        result = {
            "success": True,
            "message": "Career guidance generated successfully.",
            "data": advice,
        }

        return result

    except Exception as e:
        return {
            "success": False,
            "message": "Career guidance generation failed.",
            "error": str(e),
        }
