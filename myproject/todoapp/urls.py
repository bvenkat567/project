from django.conf import urls
from . import views
from .views import index_view

urlpatterns = [
    urls(r'', views.index_view)
]