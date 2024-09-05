from fastapi import Depends

from artifaq.apps.router import router_config, router, RouterBase


def get_user_id(test: str):
    return "user_123" + test

@router_config(prefix="/test", tags=["test"])
class HomeRouter(RouterBase):
    @router.get("/two-common-route")
    def common_route(user_id: str = Depends(get_user_id)):
        return {"message": "This uses the common dependency", "user_id": user_id}

    @router.post("/two-specific-route")
    def specific_route(user_id: str = Depends(get_user_id)):
        return {"message": "This uses a specific dependency", "user_id": user_id}