from django.urls import path
# from apps.pupies import views
from rest_framework.routers import SimpleRouter
from apps.accounts.api.views import MyProfileAPIView

router = SimpleRouter()
urlpatterns = router.urls

urlpatterns += [
    path('my_profile/',MyProfileAPIView.as_view(),name='my_profile')
]