import json
from services.llm_service import client, MODEL



def get_learning_roadmap(target_career, current_skills, timeline_months):
    """
    Generate a personalized learning roadmap using AI.
    """

    prompt = f"""
    You are an expert career mentor and learning roadmap planner.

    Create a personalized step-by-step learning roadmap for the student.

    Target Career: {target_career}
    Current Skills: {current_skills}
    Available Timeline: {timeline_months} months

    Return ONLY valid JSON in this exact structure:

    {{
        "target_career": "{target_career}",
        "current_skills": {current_skills},
        "total_timeline": "{timeline_months} months",
        "phases": [
            {{
                "phase": 1,
                "title": "Foundation Building",
                "duration": "Month 1",
                "goals": [
                    "Goal 1",
                    "Goal 2"
                ],
                "resources": [
                    {{
                        "name": "Resource Name",
                        "type": "Free Course",
                        "url": "https://example.com"
                    }}
                ],
                "milestone": "A measurable achievement"
            }}
        ],
        "tips": [
            "Practical learning tip 1",
            "Practical learning tip 2"
        ]
    }}

    Instructions:
    - Divide the roadmap into 3 to 5 phases.
    - Respect the student's available timeline.
    - Do not exceed the given number of months.
    - Start from the student's existing skill level.
    - Include practical goals and projects.
    - Include useful learning resources.
    - Use valid URLs only when you know them.
    - Each phase must have a measurable milestone.
    - Provide realistic learning tips.
    - Do not include markdown or text outside the JSON.
    """

    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages=[
                {
                    "role": "system",
                    "content": "You are a professional learning roadmap planner."
                },
                {
                    "role": "user",
                    "content": prompt
                }
            ],
            response_format={"type": "json_object"},
            max_tokens=2500
        )

        ai_result = response.choices[0].message.content
        roadmap = json.loads(ai_result)

        result = {
            "success": True,
            "message": "Learning roadmap generated successfully.",
            "data": roadmap,
        }

        return result

    except Exception as e:
        return {
            "success": False,
            "message": "Learning roadmap generation failed.",
            "error": str(e),
        }
