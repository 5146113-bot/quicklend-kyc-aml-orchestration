from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class AuditTrailPort(ABC):
    """Append-only audit trail interface; the infrastructure implementation owns storage."""

    @abstractmethod
    def save(self, event: dict[str, Any]) -> None:
        """Persist an event in the append-only audit log."""

    @abstractmethod
    def find(self, customer_id: str) -> list[dict[str, Any]]:
        """Return all audit events for the given customer."""
