from artifaq.apps.router import BaseRouter, depends, router, router_config


@router_config(
    prefix="/",
    tags=["home"],
)
class HomeRouter(BaseRouter):

    @depends
    def injected_depends(self):
        return {
            "home_config": "HomeConfig",
        }

    @router.get("/")
    async def home(self):
        return "blabla"

    @router.get("/about")
    async def about(self):
        return "test"
