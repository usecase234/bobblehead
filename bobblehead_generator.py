
from PIL import Image
import io
import os

def generate_bobblehead_image(user_img):
    base_img = Image.open("assets/base_body.png").convert("RGBA")
    logo_img = Image.open("assets/bobbleheads_logo.png").convert("RGBA")

    head_img = user_img.convert("RGBA").resize((100, 100))
    head_position = ((base_img.width - head_img.width) // 2, 100)
    composite_img = base_img.copy()
    composite_img.paste(head_img, head_position, head_img)

    logo = logo_img.copy()
    logo.thumbnail((60, 60))
    logo_position = (composite_img.width - logo.width - 10, composite_img.height - logo.height - 10)
    composite_img.paste(logo, logo_position, logo)

    # Save to bytes
    output_bytes = io.BytesIO()
    composite_img.save(output_bytes, format="PNG")
    output_bytes.seek(0)
    return output_bytes
