# -------------------------------------------------------
# routes/guidance_routes.py — Career Comparison & Guidance Routes
# -------------------------------------------------------
# This Blueprint handles TWO endpoints:
#   1. /api/guidance/compare  → Compare careers side-by-side
#   2. /api/guidance/advice   → Get general career advice
#
# WHY TWO ROUTES IN ONE FILE?
#   Both are related to "career guidance", so it makes sense
#   to group them under the same Blueprint with the same
#   URL prefix: /api/guidance
# -------------------------------------------------------

from flask import Blueprint, request, jsonify
from services.guidance_service import get_career_comparison, get_career_advice
from utils.validators import validate_compare_input, validate_guidance_input


# Create Blueprint with url_prefix="/api/guidance"
guidance_bp = Blueprint("guidance", __name__, url_prefix="/api/guidance")


@guidance_bp.route("/compare", methods=["POST"])
def compare_careers():
    """
    POST /api/guidance/compare

    PURPOSE:
        Compare two or more careers side-by-side.
        Shows salary, skills, growth, pros/cons for each.

    EXAMPLE REQUEST:
        POST http://localhost:5000/api/guidance/compare
        Body:
        {
            "careers": ["Data Scientist", "Software Engineer"]
        }

    EXAMPLE RESPONSE:
        {
            "success": true,
            "data": {
                "careers_compared": [...],
                "comparison": [ { career details }, { career details } ],
                "recommendation": "..."
            }
        }
    """

    data = request.get_json()

    is_valid, error_message = validate_compare_input(data)

    if not is_valid:
        return jsonify({
            "success": False,
            "error": error_message
        }), 400

    careers = data["careers"]

    result = get_career_comparison(careers)

    return jsonify(result), 200


@guidance_bp.route("/advice", methods=["POST"])
def get_advice():
    """
    POST /api/guidance/advice

    PURPOSE:
        Answer a user's career-related question with personalized
        advice, action steps, and resources.

    EXAMPLE REQUEST:
        POST http://localhost:5000/api/guidance/advice
        Body:
        {
            "question": "Should I learn AI or Web Development?",
            "context": {
                "skills": ["Python", "HTML"],
                "education": "B.Tech CSE, 3rd year",
                "interests": ["Machine Learning", "Building websites"]
            }
        }

    NOTE:
        "context" is optional but helps generate better advice.

    EXAMPLE RESPONSE:
        {
            "success": true,
            "data": {
                "question": "...",
                "advice": {
                    "summary": "...",
                    "detailed_response": "...",
                    "action_steps": [...],
                    "resources": [...]
                }
            }
        }
    """

    data = request.get_json()

    is_valid, error_message = validate_guidance_input(data)

    if not is_valid:
        return jsonify({
            "success": False,
            "error": error_message
        }), 400

    question = data["question"]
    
    context = data.get("context", None)

    result = get_career_advice(question, context)

    return jsonify(result), 200
