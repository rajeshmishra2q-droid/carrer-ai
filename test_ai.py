from dotenv import load_dotenv
load_dotenv()

from services.llm_service import client, MODEL

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {
                "role": "user",
                "content": "Say hello to my AI Career Compass project in one sentence."
            }
        ],
        max_tokens=100
    )

    print("AI Response:")
    print(response.choices[0].message.content)

except Exception as e:
    print("Error connecting to AI:")
    print(e)