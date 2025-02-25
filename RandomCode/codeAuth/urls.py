from django.urls import path
from django.views.generic.base import TemplateView

from .views import RandNumView, RanNumAuthView


urlpatterns = [
    path('', TemplateView.as_view(template_name='code-apps/index.html'), name='index'),
    path('code-no-auth/', RandNumView.as_view(), name='code1'),
    path('code-auth/', RanNumAuthView.as_view(), name='code2'),
]
