

from flask import Blueprint, request, jsonify
from services.skill_service import get_skill_gap_analysis
from utils.validators import validate_skill_gap_input


skill_bp = Blueprint("skill", __name__, url_prefix="/api/skill")


@skill_bp.route("/gap-analysis", methods=["POST"])
def analyze_skill_gap():
    """
    POST /api/skill/gap-analysis

    PURPOSE:
        Compare user's current skills against what's needed for
        their target career. Shows what they know, what they're
        missing, and how to fill the gaps.

    EXAMPLE REQUEST:
        POST http://localhost:5000/api/skill/gap-analysis
        Body:
        {
            "current_skills": ["HTML", "CSS", "Basic JavaScript"],
            "target_career": "Frontend Developer"
        }

    EXAMPLE RESPONSE:
        {
            "success": true,
            "message": "Skill gap analysis completed successfully.",
            "data": {
                "target_career": "Frontend Developer",
                "skill_assessment": [ ... ],
                "overall_readiness": "45%",
                "priority_skills": [ ... ]
            }
        }
    """

  
    data = request.get_json()

    is_valid, error_message = validate_skill_gap_input(data)

    if not is_valid:
        return jsonify({
            "success": False,
            "error": error_message
        }), 400

    current_skills = data["current_skills"]
    target_career = data["target_career"]

    result = get_skill_gap_analysis(current_skills, target_career)

    return jsonify(result), 200
