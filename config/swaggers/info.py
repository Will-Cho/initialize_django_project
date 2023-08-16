# System
from drf_yasg import openapi
import os


api_v1_info = openapi.Info(
    title="API V1",
    default_version="v1",
    terms_of_service="https://policies.google.com/terms",
    url=os.environ.get("SWAGGER_URL"),
)
