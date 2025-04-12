import os
from PIL import Image
import io

def generate_bobblehead_image(user_img):
    try:
        # Find this script's directory
        base_dir = os.path.dirname(os.path.abspath(__file__))
        assets_dir = os.path.join(base_dir, "assets")

        # Log debug info (visible in logs via "Manage App")
        print("Looking for assets in:", assets_dir)
        print("Files in assets_dir:", os.listdir(assets_dir))

        base_img_path = os.path.join(assets_dir, "base_body.png")
        logo_img_path = os.path.join(assets_dir, "bobbleheads_logo.png")

        # Confirm files exist
        if not os.path.exists(base_img_path):
            raise FileNotFoundError(f"Missing base_body.png at {base_img_path}")
        if not os.path.exists(logo_img_path):
            raise FileNotFoundError(f"Missing logo at {logo_img_path}")

        base_img = Image.open(base_img_path).convert("RGBA")
        logo_img = Image.open(logo_img_path).convert("RGBA")

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

    except Exception as e:
        # Catch-all error handler that will surface in Streamlit logs
        raise RuntimeError(f"Bobblehead generation failed: {e}")
