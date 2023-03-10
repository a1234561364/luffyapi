from django.urls import path, re_path, include
# from luffyapi.apps.home import views
from . import views
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register('pay', views.PayView, 'pay')
urlpatterns = [
    path('', include(router.urls)),
    path('success/', views.SuccessView.as_view()),
]
