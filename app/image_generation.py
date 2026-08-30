import base64
import os

from openai import OpenAI


client = OpenAI(
    api_key=os.getenv("OPENAI_API_KEY")
)


def generate_design_image(prompt: str) -> str:
    response = client.images.generate(
        model="gpt-image-2",
        prompt=prompt,
        size="1024x1536",
        quality="medium",
    )

    image_base64 = response.data[0].b64_json

    return image_base64