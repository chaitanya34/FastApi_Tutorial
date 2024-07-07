from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def index():
    """
    Base url
    """
    return {"status":"EndPoint connected"}

@app.get("/healthCheck")
def healtCheck():
    """
    Verifies server deployed and configured properly
    """
    return {"status":"healthy"}
