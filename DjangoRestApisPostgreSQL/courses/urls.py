from DjangoRestApisPostgreSQL.router import api_v1_router
from courses import views


def register(router):
    router.register(r'users', views.AuthorViewSet)
    router.register(r'groups', views.CourseViewSet)