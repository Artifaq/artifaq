from artifaq.apps.config_router import config_router
from artifaq.apps.router import ArtifaqRouter


@config_router({
    'name': 'example.apps.home',
    'verbose_name': 'Home',
    'label': 'home',
    'icon': 'home',
    'order': 0,
})
class Router(ArtifaqRouter):

    @router('/')
    def home(self):
        return 'Home'
