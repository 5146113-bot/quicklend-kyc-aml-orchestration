from __future__ import annotations

from dataclasses import dataclass, field

from src.domain.errors.domain_errors import ValidationError
from src.domain.value_objects.customer_id import CustomerId


@dataclass(slots=True)
class Customer:
    """Customer aggregate root identity and profile information."""

    customer_id: CustomerId
    full_name: str
    phone_number: str | None = None
    email: str | None = None
    is_active: bool = True
    metadata: dict[str, str] = field(default_factory=dict)

    def __post_init__(self) -> None:
        if not self.full_name or not self.full_name.strip():
            raise ValidationError("Customer full_name cannot be blank.")
