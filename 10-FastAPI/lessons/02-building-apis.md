# FastAPI — Building and Testing APIs

## API basics
An API exposes operations over a defined interface. REST APIs commonly use HTTP methods: GET reads, POST creates or triggers processing, PUT replaces, PATCH partially updates, and DELETE removes. Use appropriate status codes and validate request data.

## FastAPI concepts
FastAPI uses Python type annotations and Pydantic models to validate request bodies. It generates OpenAPI documentation automatically. Keep route handlers small and move business logic into testable functions or service modules.

## Reliability and security
Validate inputs, avoid exposing stack traces or secrets, configure CORS narrowly, use authentication and authorization when needed, set request limits, log safely, and manage errors consistently. Do not place API keys in source control.

## Run
Install with `python -m pip install fastapi uvicorn`. Save the example as `examples/02_main.py`, then run `python -m uvicorn examples.02_main:app --reload` if the examples directory is importable as a package; alternatively run from the examples directory with `uvicorn 02_main:app --reload`.

## Testing
Use FastAPI's `TestClient` to test successful responses, invalid requests, and error conditions. Add integration tests for database or model dependencies.
