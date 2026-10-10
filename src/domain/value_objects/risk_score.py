from __future__ import annotations

from dataclasses import dataclass

from src.domain.errors.domain_errors import ValidationError


@dataclass(frozen=True, slots=True)
class RiskScore:
    """Domain value object for risk scoring; constrained to a 0-100 scale."""

    value: float

    def __post_init__(self) -> None:
        if not 0.0 <= float(self.value) <= 100.0:
            raise ValidationError("RiskScore must be between 0 and 100 inclusive.")

    def __float__(self) -> float:
        return float(self.value)

    def __str__(self) -> str:
        return str(self.value)
