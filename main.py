from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import subprocess

app = FastAPI()

class CodeRequest(BaseModel):
    code: str

@app.post("/run-python")
def run_python(code_request: CodeRequest):
    try:
        result = subprocess.run(
            ["python", "-c", code_request.code],
            capture_output=True, text=True, timeout=5
        )
        return {"output": result.stdout, "error": result.stderr}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
