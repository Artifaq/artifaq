from artifaq.apps.router import router_config, BaseRouter, router

@router_config(prefix="/example", tags=["example"])
class ExampleRouter(BaseRouter):

    @router.get("/common-route")
    def common_route(self):
        return {"message": "This uses the common dependency"}

    @router.get("/specific-route")
    def specific_route(self):
        return {"message": "This uses a specific dependency"}