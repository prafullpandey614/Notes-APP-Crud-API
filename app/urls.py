from .views import NotesAPIView,GetSingleNoteAPIView,NoteSearchAPIView,NotesUpdateAPIView
from django.urls import path, re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Your Project API",
      default_version='v1',
      description="API documentation for your Django project",
      terms_of_service="https://www.google.com/policies/terms/",
      contact=openapi.Contact(email="contact@yourproject.local"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
   permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('notes', NotesAPIView.as_view(),name='notes'),
    path('get-note/<int:pk>', GetSingleNoteAPIView.as_view(),name='get-single-note'),
    path('search-note', NoteSearchAPIView.as_view(),name='note-search'),
    path('update-note/<int:pk>', NotesUpdateAPIView.as_view(),name='notes-update'),
    re_path(r'^swagger(?P<format>\.json|\.yaml)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
