from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from models import ProofreadRequest, ProofreadResponse
from validation import is_empty, is_too_long
from proofread import proofread_text_with_openai

app = FastAPI()

origins = [
    "http://localhost",
    "http://localhost:8080",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post('/proofread')
async def proofread_text(request: ProofreadRequest) -> ProofreadResponse:
    """
    Simulate a proofreading operation.
    In a real application, this would call an external service or library.
    """
    
    # Verify the input text
    if is_empty(request.text):
        error_msg = "No text is provided."
        return {"result": "Failure", "proofread_text": None, "error_msg": error_msg, "provided_text": f"{request.text}"}
    if is_too_long(request.text):
        error_msg = "Text is too long."
        return {"result": "Failure", "proofread_text": None, "error_msg": error_msg, "provided_text": f"{request.text}"}
    
    # proofread_text = request.text.replace("teh", "the").replace("Teh", "The")    # TODO: Use GPT
    proofread_text = proofread_text_with_openai(request.text)
    
    return {"result": "Success", "proofread_text": proofread_text, "error_msg": None, "provided_text": f"{request.text}"}