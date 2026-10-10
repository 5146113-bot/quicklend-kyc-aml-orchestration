from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class NotificationPort(ABC):
    """Abstraction for notifications to customers, ops, or downstream systems."""

    @abstractmethod
    def send(self, channel: str, recipient: str, message: str, metadata: dict[str, Any]) -> None:
        """Send a notification using the configured channel."""
