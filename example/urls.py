from django.conf.urls import url, include

from rest_framework.routers import DefaultRouter

from example import views


router = DefaultRouter()
router.register(r'a', views.A)
router.register(r'b', views.B)

urlpatterns = [
    url('^', include(router.urls)),
    url('^api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]