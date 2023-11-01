from fastapi import FastAPI, Request, UploadFile, File
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from PIL import Image
import io
import numpy as np
from app.model import recognize_image

app = FastAPI()

# Mount the /static route to serve static files from the "static" directory
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

def resize_image(image_data, target_size=(256, 256)):
    image = Image.open(io.BytesIO(image_data))
    image = image.resize(target_size)
    return np.array(image)


@app.post("/upload/")
async def upload_image(file: UploadFile):
    if file:
        image = await file.read()

        image = resize_image(image)

        result = recognize_image(image)
        c= result['class']
        confidence=result['confidence']
        return f"Result: Class:{result['class']} Confidence:{result['confidence']}"
    return {"result": "No image provided"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, port=2000)
