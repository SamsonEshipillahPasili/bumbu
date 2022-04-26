from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('faq/', include('faq.urls')),
    path('contact_us/', include('contact_us.urls'))
]
