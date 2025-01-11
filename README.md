# FastAPI GPT-2 Text Generation App

This is a simple FastAPI application that provides an API to generate text using the GPT-2 model from the `transformers` library.

## Features

- Generate text based on input prompts using the GPT-2 model.
- Self-documenting API with FastAPI's automatic interactive API docs.

## Installation

1. **Clone the repository:**

    ```sh
    git clone https://github.com/hwang2006/fastapi-app.git
    cd fastapi-app
    ```

2. **Create a virtual environment:**

    ```sh
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

        ```sh
        venv\Scripts\activate
        ```

    - On macOS and Linux:

        ```sh
        source venv/bin/activate
        ```

4. **Install the required dependencies:**

    ```sh
    pip install -r requirements.txt
    ```

## Usage

1. **Run the FastAPI application:**

    ```sh
    uvicorn main:app --host 0.0.0.0 --port 8000
    ```

2. **Access the application:**

    - Open your browser and navigate to `http://0.0.0.0:8000` to see the root endpoint.
    - For interactive API documentation, go to `http://0.0.0.0:8000/docs`.

## Endpoints

### Root Endpoint

- **URL:** `/`
- **Method:** `GET`
- **Response:** Returns a simple HTML message.

### Generate Text

- **URL:** `/generate`
- **Method:** `POST`
- **Request Body:**

    ```json
    {
        "text": "Your input text here"
    }
    ```

- **Response:** Returns the generated text based on the input provided.

    ```json
    {
        "generated_text": "Generated text here"
    }
    ```

## Example Requests

### cURL Example

1. **Root Endpoint:**

    ```sh
    curl -X GET http://localhost:8000/
    ```

2. **Generate Text:**
    ```sh
    curl -X POST http://localhost:8000/generate \
    -H "Content-Type: application/json" \
    -d '{"text": "Once upon a time"}'
    ```
