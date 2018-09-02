from django.conf.urls.static import static
from django.urls import path, include
from django.contrib import admin
from django.conf import settings

import core.urls
import user.urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('user/', include(user.urls, namespace='user')),
    path('', include(core.urls, namespace='core')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)

if settings.DEBUG:
    import debug_toolbar
    urlpatterns = [
        path('__debug__/', include(debug_toolbar.urls)),
    ] + urlpatterns
