from __future__ import annotations

from src.domain.value_objects.verification_status import VerificationStatus


def verification_status_to_kyc_state(status: VerificationStatus) -> str:
    """Compatibility helper for converting the typed status enum to the canonical state string."""
    return status.value
