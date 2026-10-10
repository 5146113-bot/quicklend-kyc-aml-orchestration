from __future__ import annotations

from enum import Enum


class VerificationStatus(str, Enum):
    """Canonical KYC lifecycle states."""

    INITIATED = "initiated"
    DOCUMENTS_REQUIRED = "documents_required"
    IN_REVIEW = "in_review"
    MANUAL_ESCALATION = "manual_escalation"
    VERIFIED = "verified"
    REJECTED = "rejected"
