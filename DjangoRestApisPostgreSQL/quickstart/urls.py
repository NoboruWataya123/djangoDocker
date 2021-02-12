from DjangoRestApisPostgreSQL.router import api_v1_router
from quickstart import views


def register(router):
    router.register(r'users', views.UserViewSet)
    router.register(r'groups', views.GroupViewSet)