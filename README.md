# Building an AI Image Generation API with Django

This tutorial will guide you through creating an API that generates images using Stable Diffusion and serves them via Django.

## Prerequisites

- Python 3.8+
- CUDA-capable GPU (recommended)
- Basic understanding of Python and Django
- 8GB+ RAM

## Project Setup

First, let's set up our environment and install dependencies:

```bash
# Create and activate virtual environment
python -m venv env
source env/bin/activate  # On Windows: env\Scripts\activate

# Install required packages
pip install django djangorestframework Pillow torch torchvision diffusers transformers accelerate
```

Create a new Django project:

```bash
django-admin startproject image_generator_project
cd image_generator_project
python manage.py startapp ai_image_generator
```
