# Import the FastAPI class from the fastapi module.
from fastapi import FastAPI
 
# Declare an instance of the FastAPI class.
app = FastAPI()
 
# use the app instance as a decorator to handle an
# HTTP route and HTTP method.
@app.get("/")
def read_index():
    """
    Return a Python Dictionary that supports JSON serialization.
    """
    return {"Hello": "on the Road - most welcome! Deploying Ansible workflow via GitHub - using GitHub Actions for pushing containers to dockerhub"}

@app.get("/api/v1/hello-world/")
def read_hello_world():
    """
    Return an API-like response.
    """
    return {"what": "road", "where": "kubernetes", "version": "v1"}
