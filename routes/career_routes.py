# -------------------------------------------------------
# routes/career_routes.py — Career Recommendation Routes
# -------------------------------------------------------
# WHAT IS A BLUEPRINT?
#   A Blueprint is Flask's way of organizing routes into
#   separate files. Instead of putting ALL routes in app.py,
#   we group related routes together in their own file.
#
#   Think of it like chapters in a book:
#     - career_routes.py  → Chapter on career recommendations
#     - skill_routes.py   → Chapter on skill gap analysis
#     - etc.
#
# HOW IT WORKS:
#   1. We create a Blueprint with a name and a URL prefix
#   2. We define routes on the Blueprint (not on the app)
#   3. In app.py, we "register" the Blueprint with the app
# -------------------------------------------------------

from flask import Blueprint, request, jsonify
# ↑ Blueprint  → to create a route group
# ↑ request    → to access the JSON data sent by the client
# ↑ jsonify    → to convert a Python dict into a JSON response

from services.career_service import get_career_recommendations
# ↑ Import the business logic function from our service layer

from utils.validators import validate_career_input
# ↑ Import the input validation function


# Create a Blueprint named "career"
# url_prefix="/api/career" means all routes here start with /api/career
career_bp = Blueprint("career", __name__, url_prefix="/api/career")


@career_bp.route("/recommend", methods=["POST"])
def recommend_careers():
    """
    POST /api/career/recommend

    PURPOSE:
        Takes a user's profile (skills, interests, education, experience)
        and returns personalized career recommendations.

    HOW THIS ROUTE WORKS (step by step):
        1. The client (React app or Postman) sends a POST request
           with JSON data in the body
        2. We extract that JSON using request.get_json()
        3. We validate the input to make sure nothing is missing
        4. If valid, we call the service function to get recommendations
        5. We return the result as JSON with a 200 status code

    EXAMPLE REQUEST (send this from Postman or React):
        POST http://localhost:5000/api/career/recommend
        Headers: Content-Type: application/json
        Body:
        {
            "skills": ["Python", "SQL", "Machine Learning"],
            "interests": ["Artificial Intelligence", "Data Analysis"],
            "education": "B.Tech Computer Science",
            "experience_level": "beginner"
        }

    EXAMPLE RESPONSE:
        {
            "success": true,
            "message": "Career recommendations generated successfully.",
            "data": {
                "user_profile": { ... },
                "recommendations": [ ... ],
                "total_recommendations": 3
            }
        }
    """

    # STEP 1: Get the JSON data from the request body
    # request.get_json() parses the raw JSON into a Python dictionary
    # If the client didn't send JSON, this returns None
    data = request.get_json()

    # STEP 2: Validate the input
    # This checks for missing fields, wrong types, empty lists, etc.
    is_valid, error_message = validate_career_input(data)

    if not is_valid:
        # Return a 400 (Bad Request) error with a helpful message
        # 400 = "Hey client, YOU sent something wrong"
        return jsonify({
            "success": False,
            "error": error_message
        }), 400

    # STEP 3: Extract individual fields from the validated data
    skills = data["skills"]
    interests = data["interests"]
    education = data["education"]
    experience_level = data["experience_level"]

    # STEP 4: Call the service function to get recommendations
    # This is where the LLM call will happen later
    result = get_career_recommendations(skills, interests, education, experience_level)

    # STEP 5: Return the result as JSON with 200 (OK) status
    # 200 = "Everything went well, here's your data"
    return jsonify(result), 200