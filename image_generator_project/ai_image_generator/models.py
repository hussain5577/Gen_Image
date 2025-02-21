from django.db import models
import os

class ImageGeneration(models.Model):
    prompt = models.TextField()
    negative_prompt = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='generated_images')
    created_at = models.DateTimeField(auto_now_add=True)
    seed = models.IntegerField(null=True)
    width = models.IntegerField(default=512)
    height = models.IntegerField(default=512)
    num_inference_steps = models.IntegerField(default=50)
    guidance_scale = models.FloatField(default=7.5)

    def __str__(self):
        return f"Generation for: {self.prompt[:50]}..."

    def get_image_url(self):
        return os.path.join('/media/generated_images', os.path.basename(self.image.name))