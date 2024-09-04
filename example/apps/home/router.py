from fastapi import Depends

from artifaq.apps.router import router_config, router, RouterBase


def get_user_id(test: str):
    return "user_123"

@router_config(prefix="/example", tags=["example"])
class HomeRouter(RouterBase):
    @router.get("/common-route")
    def common_route(user_id: str = Depends(get_user_id)):
        return {"message": "This uses the common dependency", "user_id": user_id}

    @router.post("/specific-route")
    def specific_route(user_id: str = Depends(get_user_id)):
        return {"message": "This uses a specific dependency", "user_id": user_id}