from abc import ABC


class BaseTransformer(ABC):
    def __init__(self, **kwargs) -> None:
        super().__init__()

    def __call__(self, **kwargs):
        pass