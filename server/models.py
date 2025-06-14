from pydantic import BaseModel


class ProofreadRequest(BaseModel):
    text: str

class ProofreadResponse(BaseModel):
    result: str
    proofread_text: str | None
    error_msg: str | None
    provided_text: str