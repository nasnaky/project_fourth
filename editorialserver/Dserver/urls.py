from django.urls import path, include

from .views import status1, CAMERA_link, last_HUMIDITY, last_REMNANT_W, last_TEMPERATURE, list_TEMPERATURE, \
    list_HUMIDITY, AVG_TEMPERATURE, AVG_HUMIDITY, CAMARA_LINK_C, M_list_TEMPERATURE, M_list_HUMIDITY

urlpatterns = [
    path("", status1),

    path("CMA/", CAMARA_LINK_C),
    path("CMA/<int:pk>", CAMERA_link),

    path("LH/", last_HUMIDITY),
    path("LWT/", last_REMNANT_W),
    path("LT/", last_TEMPERATURE),

    path("LT/<int:i>/", list_TEMPERATURE),
    path("LH/<int:i>/", list_HUMIDITY),

    path("MLT/<int:i>", M_list_TEMPERATURE),
    path("MLH/<int:i>", M_list_HUMIDITY),

    path("AT/", AVG_TEMPERATURE),
    path("AH/", AVG_HUMIDITY),
]
