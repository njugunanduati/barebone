from django.urls import path
from . import view1 
from . import view2


urlpatterns = [
    path('', view1.home, name='accounts-home'),
    path('about/', view2.about, name='accounts-about'),
]
