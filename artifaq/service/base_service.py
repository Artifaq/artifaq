from typing import Generic, TypeVar

from artifaq.repository.base_repository import BaseRepository

T = TypeVar('T')

class BaseService(Generic[T]):
    def __init__(self, repository: BaseRepository[T]):
        self.repository = repository

    def get(self, id: int) -> T:
        return self.repository.get(id)

    def get_all(self):
        return self.repository.get_all()

    def create(self, obj: T) -> T:
        return self.repository.create(obj)

    def update(self, obj: T) -> T:
        return self.repository.update(obj)

    def delete(self, id: int) -> bool:
        return self.repository.delete(id)