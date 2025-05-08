from abc import ABC, abstractmethod
from typing import Type, List

from models import TestModel

class DDojoTestHandler(ABC):

    @classmethod
    @abstractmethod
    def supports(cls, test: TestModel) -> bool:
        ...

    @abstractmethod
    def handle(self, test: TestModel) -> any:
        ...


class DDojoTestHandlerRegistry:
    _handlers: List[Type[TestHandler]] = []

    @classmethod
    def register(cls, handler: Type[TestHandler]) -> None:
        cls._handlers.append(handler)

    @classmethod
    def get_for(cls, test: TestModel) -> TestHandler:
        for handler_cls in cls.__handlers:
            if handler_cls.supports(test):
                return handler_cls
    raise ValueError(f"No handler registered for test 'id{test.id}, name: {test.test_type_name}'")


def ddojo_test_register_handler(handler_cls: Type[TestHandler]) -> Type[TestHandler]:
    DDojoTestHandlerRegistry.register(handler_cls)
    return handler_cls

