from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, HttpUrl
from fastapi.responses import StreamingResponse
from bobblehead_generator import generate_bobblehead_image
from PIL import Image
import requests
import io

app = FastAPI()

class ImageRequest(BaseModel):
    photo_url: HttpUrl

@app.post("/generate")
async def generate(request: ImageRequest):
    try:
        response = requests.get(request.photo_url)
        if response.status_code != 200:
            raise HTTPException(status_code=400, detail="Failed to fetch image from URL")
        image = Image.open(io.BytesIO(response.content))
        result = generate_bobblehead_image(image)
        return StreamingResponse(result, media_type="image/png")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Image processing failed: {str(e)}")