
from flask import Flask, jsonify
from flask_cors import CORS
from config import Config
from routes import career_bp, skill_bp, guidance_bp, roadmap_bp



"""
Application Factory Function.

WHY USE A FUNCTION INSTEAD OF CREATING THE APP DIRECTLY?
    This pattern is called the "Application Factory". It's a best practice
    because:
    1. You can create multiple instances (useful for testing)
    2. Configuration is applied cleanly inside the function
    3. It keeps the global scope clean

Returns:
    Flask: The configured Flask application instance.
"""

app = Flask(__name__)

app.config.from_object(Config)

CORS(app, resources={r"/api/*": {"origins": Config.CORS_ORIGINS}})

app.register_blueprint(career_bp)
app.register_blueprint(skill_bp)
app.register_blueprint(roadmap_bp)
app.register_blueprint(guidance_bp)


@app.route("/", methods=["GET"])
def health_check():
    """
    GET /

    A simple endpoint to check if the server is running.
    Useful for:
    - Testing if the server started correctly
    - Monitoring in production (health checks)
    - Quick sanity check during development
    """
    return jsonify({
        "success": True,
        "status": "healthy",
        "message": "AI Career Compass API is running!",
        "version": "1.0.0",
        "endpoints": {
            "career_recommendations": "POST /api/career/recommend",
            "skill_gap_analysis": "POST /api/skill/gap-analysis",
            "learning_roadmap": "POST /api/roadmap/generate",
            "career_comparison": "POST /api/guidance/compare",
            "career_advice": "POST /api/guidance/advice",
        }
    }), 200




if __name__ == "__main__":
    print("=" * 55)
    print("  AI Career Compass API Server")
    print("=" * 55)
    print(f"  Running at: http://localhost:{Config.PORT}")
    print(f"  Debug mode: {Config.DEBUG}")
    print("  Available endpoints:")
    print("     GET  /api/health              - Health check")
    print("     POST /api/career/recommend    - Career recommendations")
    print("     POST /api/skill/gap-analysis  - Skill gap analysis")
    print("     POST /api/roadmap/generate    - Learning roadmap")
    print("     POST /api/guidance/compare    - Compare careers")
    print("     POST /api/guidance/advice     - Career advice")
    print("=" * 55)

 
    app.run(
        host=Config.HOST,
        port=Config.PORT,
        debug=Config.DEBUG,
    )
