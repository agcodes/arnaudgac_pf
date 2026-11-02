# ASGI config for django_cv project
import os
from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_cv.settings')

application = get_asgi_application()
