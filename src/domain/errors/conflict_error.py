from __future__ import annotations

from src.domain.errors.domain_errors import ConflictError


class KycConflictError(ConflictError):
    """Domain-specific conflict error for invalid KYC transitions."""

    def __init__(self, from_state: str, to_state: str, trigger: str) -> None:
        message = (
            f"Invalid KYC transition from '{from_state}' to '{to_state}' "
            f"for trigger '{trigger}'."
        )
        super().__init__(message)
