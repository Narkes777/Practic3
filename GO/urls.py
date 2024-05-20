from . import views
from django.urls import path
from rest_framework import routers

router = routers.SimpleRouter()
router.register('messages', views.MessageViewSet, basename='name')
router.register('comments', views.СommentsViewSet)
router.register('subscribers', views.SubscribersViewSet)

urlpatterns = []

urlpatterns += router.urls