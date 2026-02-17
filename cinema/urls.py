from django.urls import path
from rest_framework import routers
from cinema.views import (
    MovieViewSet,
    GenreList,
    GenreDetail,
    ActorList,
    ActorDetail,
    CinemaHallList,
    CinemaHallDetail,
)

router = routers.DefaultRouter()
router.register("movies", MovieViewSet, basename="movies")

urlpatterns = [
    path("genres/", GenreList.as_view(), name="genres-list"),
    path("genres/<int:pk>/", GenreDetail.as_view(), name="genres-detail"),
    path("actors/", ActorList.as_view(), name="actors-list"),
    path("actors/<int:pk>/", ActorDetail.as_view(), name="actors-detail"),
    path("cinema-hall/", CinemaHallList.as_view(), name="cinema-hall-list"),
    path(
        "cinema-hall/<int:pk>/",
        CinemaHallDetail.as_view(),
        name="cinema-hall-detail"
    ),
]

urlpatterns += router.urls

app_name = "cinema"
