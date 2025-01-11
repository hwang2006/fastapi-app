from transformers import pipeline
from fastapi import FastAPI, Response
from pydantic import BaseModel
from typing import Dict, Any

# Initialize the text generation pipeline with the GPT-2 model
generator = pipeline('text-generation', model='gpt2')

# Create a FastAPI application
app = FastAPI()

# Define the request body schema using Pydantic
class Body(BaseModel):
    text: str

# Define a root endpoint that returns a simple HTML message
@app.get('/')
def root() -> Response:
    return Response("<h1>A self-documenting API to interact with a GPT2 model and generate text</h1>")

# Define an endpoint that generates text based on the input provided in the request body
@app.post('/generate')
def predict(body: Body) -> Dict[str, Any]:
    try:
        # Use the generator to generate text based on the input
        results = generator(body.text, max_length=35, num_return_sequences=1)
        return results[0]
    except Exception as e:
        # Handle any exceptions that occur and return an error message
        return {"error": str(e)}

# Run the application using the command: uvicorn main:app --host 0.0.0.0 --port 8000