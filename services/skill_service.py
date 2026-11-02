import json
from services.llm_service import client, MODEL



def get_skill_gap_analysis(current_skills, target_career):
    """
    Analyze the gap between current skills and target career requirements using AI.
    """

    prompt = f"""
    You are an expert technical career counselor.

    Analyze the student's current skills and identify the skills needed
    for their target career.

    Current Skills: {current_skills}
    Target Career: {target_career}

    Return ONLY valid JSON in this exact structure:

    {{
        "target_career": "{target_career}",
        "current_skills": {current_skills},
        "skill_assessment": [
            {{
                "skill": "Skill Name",
                "status": "possessed or missing",
                "proficiency": "beginner, intermediate, advanced, or none",
                "recommendation": "Specific advice for learning or improving this skill"
            }}
        ],
        "overall_readiness": "45%",
        "priority_skills": ["Skill 1", "Skill 2", "Skill 3"],
        "estimated_time_to_fill_gaps": "3-5 months with consistent learning"
    }}

    Instructions:
    - Identify the important skills required for the target career.
    - Mark a skill as possessed only if it appears in the student's current skills.
    - Mark other required skills as missing.
    - Give practical learning recommendations.
    - Estimate readiness from 0% to 100%.
    - Include 5 to 10 relevant skills.
    - List the most important missing skills in priority_skills.
    - Give a realistic learning time estimate.
    - Do not include markdown or text outside the JSON.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional skill gap analysis counselor."
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
        skill_analysis = json.loads(ai_result)

        result = {
            "success": True,
            "message": "Skill gap analysis completed successfully.",
            "data": skill_analysis,
        }

        return result

    except Exception as e:
        return {
            "success": False,
            "message": "Skill gap analysis failed.",
            "error": str(e),
        }
