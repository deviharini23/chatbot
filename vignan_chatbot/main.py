from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
import google.generativeai as genai

# API Key setup
GOOGLE_API_KEY = "AIzaSyCcFfnOM5qndAZO3OM8VN-KT5zFqmtpPmI"
genai.configure(api_key=GOOGLE_API_KEY)
model = genai.GenerativeModel('gemini-2.0-flash')
chat = model.start_chat(history=[])

# FastAPI app and templates
app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_chat(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/ask")
async def ask_question(request: Request):
    data = await request.json()
    message = data.get("message", "")
    try:
        response = chat.send_message(message)
        return JSONResponse({"response": response.text})
    except Exception as e:
        return JSONResponse({"response": f"Error: {str(e)}"})


