To run Django locally over HTTPS, you need to add the following configurations to your Django settings.py file:

python
Copy code
import os
from django.contrib.staticfiles.urls import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# ... other settings ...

# HTTPS settings
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
SECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True

# Serve media files in development
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Serve static files in development
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')

# Add these two lines at the bottom of your settings.py
def static(request, path, insecure=False, **kwargs):
    """
    Serve static files below a given point in the directory structure.
    """
    return staticfiles_urlpatterns(request, path, insecure, **kwargs)

def media(request, path, insecure=False, **kwargs):
    """
    Serve static files below a given point in the directory structure.
    """
    return staticfiles_urlpatterns(request, path, insecure, **kwargs)
You'll also need to generate a self-signed SSL certificate, which you can do with the following command:

csharp
Copy code
openssl req -x509 -newkey rsa:4096 -nodes -out cert.pem -keyout key.pem -days 365
Then, add the following to your urls.py file:

python
Copy code
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('your_app_name.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
Finally, you can run your Django server with the following command:

css
Copy code
python manage.py runserver --cert cert.pem --key key.pem
Now, you should be able to access your Django site over HTTPS locally. Note that this setup is not recommended for production use as the self-signed certificate is not trusted by browsers and users will see a security warning.
