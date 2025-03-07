from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import StudentViewSet, SubjectViewSet, MarksViewSet

router = DefaultRouter()
router.register(r'students', StudentViewSet)
router.register(r'subjects', SubjectViewSet)
router.register(r'marks', MarksViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
