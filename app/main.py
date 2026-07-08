"""
main.py
--------
This is the entry point of our FastAPI application.

It defines a very small backend server with exactly two endpoints:
    1. GET /         -> returns a simple greeting message.
    2. GET /profile  -> returns basic information about the developer.

FastAPI automatically generates interactive API documentation for us
at the "/docs" URL (Swagger UI) using the metadata we provide below.
"""

# We import FastAPI, the web framework we use to build this API.
from fastapi import FastAPI

# ---------------------------------------------------------------------------
# Create the FastAPI application instance.
# The title, description, and version show up automatically in the
# auto-generated Swagger docs at http://127.0.0.1:8000/docs
# ---------------------------------------------------------------------------
app = FastAPI(
    title="FlyRank Backend AI Engineering API",
    description=(
        "A minimal FastAPI backend built as part of the FlyRank "
        "Backend AI Engineering assignment. It exposes two simple "
        "JSON endpoints: a greeting endpoint and a profile endpoint."
    ),
    version="1.0.0",
)


# ---------------------------------------------------------------------------
# Endpoint 1: Root endpoint
# ---------------------------------------------------------------------------
@app.get("/")
def read_root() -> dict[str, str]:
    """
    Root endpoint.

    Returns a simple JSON greeting message to confirm the server
    is up and running.

    Returns:
        dict: A JSON object containing a "message" key.
    """
    return {"message": "Hello, FlyRank!"}


# ---------------------------------------------------------------------------
# Endpoint 2: Profile endpoint
# ---------------------------------------------------------------------------
@app.get("/profile")
def read_profile() -> dict[str, str]:
    """
    Profile endpoint.

    Returns basic information about the developer who built this
    project, as required by the assignment.

    Returns:
        dict: A JSON object containing name, university, major, and track.
    """
    return {
        "name": "Ahmed Atef Elnadi",
        "university": "Egypt-Japan University of Science and Technology",
        "major": "Electronics and Communications Engineering",
        "track": "Backend AI Engineering",
    }
