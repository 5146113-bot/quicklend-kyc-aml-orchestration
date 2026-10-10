from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class KycVendorPort(ABC):
    """Port for all KYC vendor interactions. Vendor-specific logic lives in adapters."""

    @abstractmethod
    def initiate_verification(self, customer_id: str, workflow: str, payload: dict[str, Any]) -> str:
        """Create a verification request and return a vendor reference."""

    @abstractmethod
    def check_status(self, reference_id: str) -> dict[str, Any]:
        """Fetch current verification status for a vendor reference."""

    @abstractmethod
    def fetch_result(self, reference_id: str) -> dict[str, Any]:
        """Return a verification result payload for a given reference."""

    @abstractmethod
    def handle_callback(self, payload: dict[str, Any]) -> dict[str, Any]:
        """Process vendor callback payloads and return normalized domain data."""

    @abstractmethod
    def get_health_status(self) -> dict[str, Any]:
        """Expose adapter health and circuit breaker state."""
