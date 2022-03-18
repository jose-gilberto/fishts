from typing import Any, List
from .base import BaseTransformer


class Compose:
    def __init__(self, transformers: List[BaseTransformer]) -> None:
        self.transformers = transformers

    def __call__(self, data) -> Any:
        for transform in self.transformers:
            data = transform(data)
        return data
