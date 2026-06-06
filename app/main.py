from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
def home():

    return """
    <html>
    <body style="font-family:Arial;padding:20px;">
        <h2>Macro Risk Parity System vFinal</h2>
        <p>System Running ✅</p>
    </body>
    </html>
    """
