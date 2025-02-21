from rest_framework import serializers
from .models import ImageGeneration 

class ImageGenerationSerializer(serializers.ModelSerializer):
    image_url = serializers.SerializerMethodField()

    class Meta:
        model = ImageGeneration
        fields = [
            'id', 'prompt', 'negative_prompt', 'image_url', 
            'created_at', 'seed', 'width', 'height',
            'num_inference_steps', 'guidance_scale'
        ]
        read_only_fields = ['image_url', 'created_at', 'seed']

    def get_image_url(self, obj):
        return obj.get_image_url()