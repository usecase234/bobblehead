
from fastapi import FastAPI, UploadFile, File
from fastapi.responses import StreamingResponse
from bobblehead_generator import generate_bobblehead_image
from PIL import Image
import io

app = FastAPI()

@app.post("/generate")
async def generate(file: UploadFile = File(...)):
    contents = await file.read()
    image = Image.open(io.BytesIO(contents))
    result = generate_bobblehead_image(image)
    return StreamingResponse(result, media_type="image/png")
