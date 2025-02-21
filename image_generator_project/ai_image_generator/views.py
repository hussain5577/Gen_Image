from rest_framework import viewsets
from rest_framework.response import Response
from django.core.files.base import ContentFile
import io
from .models import ImageGeneration
from .serializers import ImageGenerationSerializer 

from .services import ImageGeneratorService

class ImageGenerationViewSet(viewsets.ModelViewSet):
    queryset = ImageGeneration.objects.all()
    serializer_class = ImageGenerationSerializer
    generator_service = ImageGeneratorService()

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        # Generate image
        image, seed = self.generator_service.generate_image(
            prompt=serializer.validated_data['prompt'],
            negative_prompt=serializer.validated_data.get('negative_prompt'),
            width=serializer.validated_data.get('width', 512),
            height=serializer.validated_data.get('height', 512),
            num_inference_steps=serializer.validated_data.get('num_inference_steps', 50),
            guidance_scale=serializer.validated_data.get('guidance_scale', 7.5)
        )

        # Save image to bytes
        image_io = io.BytesIO()
        image.save(image_io, format='PNG')

        # Create model instance
        instance = ImageGeneration(
            prompt=serializer.validated_data['prompt'],
            negative_prompt=serializer.validated_data.get('negative_prompt'),
            seed=seed,
            width=serializer.validated_data.get('width', 512),
            height=serializer.validated_data.get('height', 512),
            num_inference_steps=serializer.validated_data.get('num_inference_steps', 50),
            guidance_scale=serializer.validated_data.get('guidance_scale', 7.5)
        )

        # Save image file
        instance.image.save(
            f'generation_{instance.id}.png',
            ContentFile(image_io.getvalue()),
            save=False
        )
        instance.save()

        response_serializer = self.get_serializer(instance)
        return Response(response_serializer.data)