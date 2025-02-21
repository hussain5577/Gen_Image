import torch
from diffusers import StableDiffusionPipeline
from PIL import Image
import numpy as np

class ImageGeneratorService:
    def __init__(self):
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        self.model_id = "runwayml/stable-diffusion-v1-5"
        self.pipe = None

    def load_model(self):
        if self.pipe is None:
            self.pipe = StableDiffusionPipeline.from_pretrained(
                self.model_id,
                torch_dtype=torch.float16 if self.device == "cuda" else torch.float32
            )
            self.pipe = self.pipe.to(self.device)

    def generate_image(
        self,
        prompt,
        negative_prompt=None,
        width=512,
        height=512,
        num_inference_steps=50,
        guidance_scale=7.5,
        seed=None
    ):
        self.load_model()

        if seed is None:
            seed = np.random.randint(0, 2147483647)

        generator = torch.Generator(device=self.device).manual_seed(seed)

        image = self.pipe(
            prompt,
            negative_prompt=negative_prompt,
            width=width,
            height=height,
            num_inference_steps=num_inference_steps,
            guidance_scale=guidance_scale,
            generator=generator
        ).images[0]

        return image, seed