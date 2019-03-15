from django.contrib import admin
from django.conf.urls import url, include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url('admin/', admin.site.urls),
    url('', include('hr.urls'))
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
admin.site.site_header = "HR Bison Agency"
admin.site.site_title = "HR Bison Agency"
admin.site.index_title = "Welcome to HR Bison Agency"
