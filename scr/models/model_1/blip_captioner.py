from transformers import BlipProcessor, BlipForConditionalGeneration
from PIL import Image
import os

def run_blip():
    model_name = "Salesforce/blip-image-captioning-base"

    processor = BlipProcessor.from_pretrained(model_name)
    model = BlipForConditionalGeneration.from_pretrained(model_name)

    img_dir = "img"
    output_dir = "outputs/model_1"
    os.makedirs(output_dir, exist_ok=True)

    print("[MODEL 1 – BLIP] Generating captions...\n")

    for root, _, files in os.walk(img_dir):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(root, f)
                img = Image.open(img_path).convert("RGB")

                inputs = processor(images=img, return_tensors="pt")
                output = model.generate(**inputs)
                caption = processor.decode(output[0], skip_special_tokens=True)

                out_file = os.path.join(output_dir, f + ".txt")
                with open(out_file, "w") as out:
                    out.write(caption)

                print(f"{f}: {caption}")

    print("\n[OK] Captions stored in outputs/model_1/")
