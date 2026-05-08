"""
Voice calibration — run once before first newsletter send.
Reads sample writing from config/voice-samples/ and builds
a system prompt that GPT-4o uses to match your style.
"""
import os, json
from pathlib import Path
from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])
SAMPLES_DIR = Path("config/voice-samples")
OUTPUT_FILE = Path("config/voice-prompt.txt")


def load_samples() -> str:
    samples = []
    for f in SAMPLES_DIR.glob("*.txt"):
        samples.append(f.read_text())
    return "\n\n---\n\n".join(samples)


def calibrate(samples: str) -> str:
    resp = client.chat.completions.create(
        model="gpt-4o",
        messages=[{
            "role": "user",
            "content": f"""Analyze the writing style in these samples and write a concise
            system prompt that instructs an AI to write in the same voice.
            Focus on: sentence rhythm, vocabulary level, tone (formal vs casual),
            use of humor, paragraph length, how they handle CTAs.

            Samples:
            {samples}

            Return ONLY the system prompt, nothing else."""
        }]
    )
    return resp.choices[0].message.content


if __name__ == "__main__":
    print("Loading writing samples...")
    samples = load_samples()
    print(f"Loaded {len(samples)} characters of sample text")
    print("Calibrating voice with GPT-4o...")
    prompt = calibrate(samples)
    OUTPUT_FILE.write_text(prompt)
    print(f"Voice prompt saved to {OUTPUT_FILE}")
    print("\nPreview:")
    print(prompt[:300] + "...")
