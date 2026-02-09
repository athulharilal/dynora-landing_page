from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI(
    title="Dynora",
    description="Dynora – Visualizing the future of mobility",
    version="0.1.0"
)

# Mount static files (CSS, images)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Templates directory
templates = Jinja2Templates(directory="app/templates")


@app.get("/", response_class=HTMLResponse)
async def landing_page(request: Request):
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "title": "Dynora",
            "tagline": "Visualizing the future of mobility",
            "subtext": "Bikes • Cars • EVs • Beyond"
        }
    )
