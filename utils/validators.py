


def validate_career_input(data):
    """
    Validates input for the career recommendation endpoint.

    Expected input:
    {
        "skills": ["Python", "SQL"],          ← required, non-empty list
        "interests": ["AI", "Web Dev"],       ← required, non-empty list
        "education": "B.Tech CSE",            ← required, non-empty string
        "experience_level": "beginner"        ← required, non-empty string
    }

    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not data:
        return False, "Request body is empty. Please send JSON data."


    required_fields = ["skills", "interests", "education", "experience_level"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: '{field}'"

    if not isinstance(data["skills"], list) or len(data["skills"]) == 0:
        return False, "'skills' must be a non-empty list. Example: [\"Python\", \"SQL\"]"


    if not isinstance(data["interests"], list) or len(data["interests"]) == 0:
        return False, "'interests' must be a non-empty list. Example: [\"AI\", \"Web Dev\"]"

    if not isinstance(data["education"], str) or data["education"].strip() == "":
        return False, "'education' must be a non-empty string. Example: \"B.Tech CSE\""

    if not isinstance(data["experience_level"], str) or data["experience_level"].strip() == "":
        return False, "'experience_level' must be a non-empty string. Example: \"beginner\""

    return True, None


def validate_skill_gap_input(data):
    """
    Validates input for the skill gap analysis endpoint.

    Expected input:
    {
        "current_skills": ["HTML", "CSS"],    ← required, non-empty list
        "target_career": "Frontend Developer" ← required, non-empty string
    }

    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not data:
        return False, "Request body is empty. Please send JSON data."

    required_fields = ["current_skills", "target_career"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: '{field}'"

    if not isinstance(data["current_skills"], list) or len(data["current_skills"]) == 0:
        return False, "'current_skills' must be a non-empty list."

    if not isinstance(data["target_career"], str) or data["target_career"].strip() == "":
        return False, "'target_career' must be a non-empty string."

    return True, None


def validate_roadmap_input(data):
    """
    Validates input for the learning roadmap endpoint.

    Expected input:
    {
        "target_career": "Data Scientist",   ← required, non-empty string
        "current_skills": ["Python"],        ← required, non-empty list
        "timeline_months": 6                 ← optional, defaults to 6
    }

    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not data:
        return False, "Request body is empty. Please send JSON data."

    required_fields = ["target_career", "current_skills"]

    for field in required_fields:
        if field not in data:
            return False, f"Missing required field: '{field}'"

    if not isinstance(data["target_career"], str) or data["target_career"].strip() == "":
        return False, "'target_career' must be a non-empty string."

    if not isinstance(data["current_skills"], list) or len(data["current_skills"]) == 0:
        return False, "'current_skills' must be a non-empty list."

    if "timeline_months" in data:
        if not isinstance(data["timeline_months"], (int, float)) or data["timeline_months"] <= 0:
            return False, "'timeline_months' must be a positive number."

    return True, None


def validate_compare_input(data):
    """
    Validates input for the career comparison endpoint.

    Expected input:
    {
        "careers": ["Data Scientist", "Software Engineer"]  ← required, at least 2
    }

    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not data:
        return False, "Request body is empty. Please send JSON data."

    if "careers" not in data:
        return False, "Missing required field: 'careers'"

    if not isinstance(data["careers"], list) or len(data["careers"]) < 2:
        return False, "'careers' must be a list with at least 2 careers to compare."

    return True, None


def validate_guidance_input(data):
    """
    Validates input for the career guidance/advice endpoint.

    Expected input:
    {
        "question": "Should I learn AI or Web Dev?",     ← required, non-empty string
        "context": {                                      ← optional
            "skills": ["Python"],
            "education": "B.Tech",
            "interests": ["AI"]
        }
    }

    Returns:
        tuple: (is_valid: bool, error_message: str or None)
    """
    if not data:
        return False, "Request body is empty. Please send JSON data."

    if "question" not in data:
        return False, "Missing required field: 'question'"

    if not isinstance(data["question"], str) or data["question"].strip() == "":
        return False, "'question' must be a non-empty string."

    return True, None
