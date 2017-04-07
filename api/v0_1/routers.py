from rest_framework import routers


class LinkRouter(routers.SimpleRouter):
    """
    Router of the Link resource
    """
    routes = [
        # List route.
        routers.Route(
            url=r"^{prefix}{trailing_slash}$",
            mapping={
                "get": "list",
                "post": "create", },
            name="{basename}-list",
            initkwargs={"suffix": "List", }
        ),
    ]
