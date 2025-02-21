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

When we install a virtual environment, the activation script sometimes fails to work, and we encounter an error.
We can activate it either through the Command Prompt (CMD) or by setting the command in the terminal of Visual Studio. Visual Studio has its own terminal where this can be done

' Set-ExecutionPolicy RemoteSigned -Scope Process '

# Install required packages
pip install django djangorestframework Pillow torch torchvision diffusers transformers accelerate
```

Create a new Django project:

```bash
django-admin startproject image_generator_project
cd image_generator_project
python manage.py startapp ai_image_generator
```

## Note This

## Configuration

Update `image_generator_project/settings.py`:

```python
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'ai_image_generator',
]

# Add media settings
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
```
