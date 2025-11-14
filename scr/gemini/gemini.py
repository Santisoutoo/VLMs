import os
import base64
from pathlib import Path
from PIL import Image

import google.generativeai as genai
from dotenv import load_dotenv


def encode_image(img_path: str) -> str:
    """
    Convierte la imagen a base64 para enviarla a Gemini.
    """
    with open(img_path, "rb") as f:
        return base64.b64encode(f.read()).decode("utf-8")


def run_gemini():
    # Cargar variables desde .env
    load_dotenv()

    api_key = os.getenv("GEMINI_API")
    if not api_key:
        raise ValueError("ERROR: No se encontró GEMINI_API en el archivo .env")

    genai.configure(api_key=api_key)

    model = genai.GenerativeModel("gemini-2.5-pro")

    img_dir = Path("img")
    output_dir = Path("outputs/gemini")
    output_dir.mkdir(parents=True, exist_ok=True)

    for img_path in img_dir.rglob("*"):
        if img_path.suffix.lower() in [".jpg", ".jpeg", ".png"]:
            try:
                encoded = encode_image(str(img_path))
                prompt = (
                    "Proporciona UNA sola descripción breve y clara que describa la imagen. "
                    "Devuelve únicamente un párrafo corto descriptivo."
                )

                response = model.generate_content(
                    [
                        {"mime_type": "image/jpeg", "data": encoded},
                        prompt,
                    ]
                )

                caption = response.text.strip()
                (output_dir / f"{img_path.name}.txt").write_text(caption)

                print(f"{img_path.name}: {caption}")

            except Exception as e:
                print(f"Error en {img_path.name}: {e}")

    print("\nCaptions stored in outputs/gemini/")
