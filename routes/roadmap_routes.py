

from flask import Blueprint, request, jsonify
from services.roadmap_service import get_learning_roadmap
from utils.validators import validate_roadmap_input



roadmap_bp = Blueprint("roadmap", __name__, url_prefix="/api/roadmap")


@roadmap_bp.route("/generate", methods=["POST"])
def generate_roadmap():
    """
    POST /api/roadmap/generate

    PURPOSE:
        Generate a step-by-step learning roadmap for a target career.
        The roadmap is divided into phases with goals, resources,
        and milestones.

    EXAMPLE REQUEST:
        POST http://localhost:5000/api/roadmap/generate
        Body:
        {
            "target_career": "Data Scientist",
            "current_skills": ["Python", "Basic SQL"],
            "timeline_months": 6
        }

    NOTE:
        "timeline_months" is optional and defaults to 6 if not provided.

    EXAMPLE RESPONSE:
        {
            "success": true,
            "data": {
                "target_career": "Data Scientist",
                "total_timeline": "6 months",
                "phases": [ ... ],
                "tips": [ ... ]
            }
        }
    """

    data = request.get_json()

    is_valid, error_message = validate_roadmap_input(data)

    if not is_valid:
        return jsonify({
            "success": False,
            "error": error_message
        }), 400

    target_career = data["target_career"]
    current_skills = data["current_skills"]

    timeline_months = data.get("timeline_months", 6)

    result = get_learning_roadmap(target_career, current_skills, timeline_months)

    return jsonify(result), 200
