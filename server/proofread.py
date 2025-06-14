import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()  # Load environment variables from a .env file

def get_openai_client() -> OpenAI:
    """
    Initialize and return an OpenAI client.
    This function can be extended to include API keys or other configurations.
    """
    # You can set your OpenAI API key here or use environment variables
    api_key = os.getenv("OPENAI_API_KEY")
    client = OpenAI(api_key=api_key)  # Replace with your actual API key
    return client

def proofread_text_with_openai(text: str) -> str:
    """
    Use OpenAI's API to proofread the provided text.
    This function sends a request to OpenAI's language model to correct the text.
    """
    client = get_openai_client()
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant that proofreads text."},
            {"role": "user", "content": "Please proofread the following text and correct any grammatical errors."},
            {"role": "user", "content": "Only return the corrected text without any additional comments."},
            {"role": "user", "content": text}
        ],
        max_tokens=4000,
        temperature=0.5
    )
    
    if not response.choices or not response.choices[0].message:
        raise ValueError("No valid response from OpenAI API.")
    
    return response.choices[0].message.content