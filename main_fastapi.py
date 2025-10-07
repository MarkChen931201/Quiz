from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()

@app.get("/", response_class=HTMLResponse)
async def home():
    html_content = """
    <html>
        <head>
            <title>FastAPI Test</title>
        </head>
        <body>
            <h1>Hello FastAPI!</h1>
            <p>這個網頁已經成功啟動 FastAPI。</p>
        </body>
    </html>
    """
    return HTMLResponse(content=html_content)
