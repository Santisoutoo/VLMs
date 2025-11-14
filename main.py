from scr.models.model_1.blip_captioner import run_blip
from scr.models.model_2.vitgpt2_captioner import run_vitgpt2
from scr.gemini.gemini import run_gemini
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--model", type=str, required=True)
    args = parser.parse_args()

    if args.model == "model_1":
        run_blip()
    elif args.model == "model_2":
        run_vitgpt2()
    elif args.model == "gemini":
        run_gemini()
    else:
        raise ValueError("Model must be: model_1, model_2 or gemini")
