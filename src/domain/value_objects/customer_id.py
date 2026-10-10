from __future__ import annotations

from dataclasses import dataclass

from src.domain.errors.domain_errors import ValidationError


@dataclass(frozen=True, slots=True)
class CustomerId:
    """Strongly typed identifier for a customer entity."""

    value: str

    def __post_init__(self) -> None:
        if not self.value or not self.value.strip():
            raise ValidationError("CustomerId cannot be blank.")

    def __str__(self) -> str:
        return self.value
