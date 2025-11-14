from transformers import VisionEncoderDecoderModel, ViTImageProcessor, AutoTokenizer
from PIL import Image
import os

def run_vitgpt2():
    model_name = "nlpconnect/vit-gpt2-image-captioning"

    model = VisionEncoderDecoderModel.from_pretrained(model_name)
    processor = ViTImageProcessor.from_pretrained(model_name)
    tokenizer = AutoTokenizer.from_pretrained(model_name)

    img_dir = "img"
    output_dir = "outputs/model_2"
    os.makedirs(output_dir, exist_ok=True)

    print("[MODEL 2 – ViT-GPT2] Generating captions...\n")

    for root, _, files in os.walk(img_dir):
        for f in files:
            if f.lower().endswith((".jpg", ".jpeg", ".png")):
                img_path = os.path.join(root, f)
                img = Image.open(img_path).convert("RGB")

                inputs = processor(img, return_tensors="pt")
                output_ids = model.generate(**inputs)
                caption = tokenizer.decode(output_ids[0], skip_special_tokens=True)

                out_file = os.path.join(output_dir, f + ".txt")
                with open(out_file, "w") as out:
                    out.write(caption)

                print(f"{f}: {caption}")

    print("\n[OK] Captions stored in outputs/model_2/")
