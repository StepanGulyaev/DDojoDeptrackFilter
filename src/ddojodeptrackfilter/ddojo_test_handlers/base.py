from abc import ABC, abstractmethod
from typing import Type, List
from ddojodeptrackfilter.client import DefectDojoClient

from ddojodeptrackfilter.models.api.test import TestModel

class DDojoTestHandler(ABC):

    @classmethod
    @abstractmethod
    def supports(cls, test: TestModel) -> bool:
        ...

    @abstractmethod
    def handle(self, test: TestModel, client: DefectDojoClient):
        ...


class DDojoTestHandlerRegistry:
    _handlers: List[Type[DDojoTestHandler]] = []

    @classmethod
    def register(cls, handler: Type[DDojoTestHandler]) -> None:
        cls._handlers.append(handler)

    @classmethod
    def get_for(cls, test: TestModel) -> DDojoTestHandler:
        for handler_cls in cls._handlers:
            if handler_cls.supports(test):
                return handler_cls()
        print(f"No handler registered for test 'id{test.id}, name: {test.test_type_name}'")


def ddojo_test_register_handler(handler_cls: Type[DDojoTestHandler]) -> Type[DDojoTestHandler]:
    DDojoTestHandlerRegistry.register(handler_cls)
    return handler_cls

