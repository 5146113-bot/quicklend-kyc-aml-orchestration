from __future__ import annotations

from enum import Enum


class KycState(str, Enum):
    """Canonical state list. Manual escalation leads into VERIFIED or REJECTED."""

    INITIATED = "initiated"
    DOCUMENTS_REQUIRED = "documents_required"
    IN_REVIEW = "in_review"
    MANUAL_ESCALATION = "manual_escalation"
    VERIFIED = "verified"
    REJECTED = "rejected"


class KycTransition:
    """Represents the trigger, source state, and destination state for one domain transition."""

    def __init__(self, from_state: KycState, to_state: KycState, trigger: str) -> None:
        self.from_state = from_state
        self.to_state = to_state
        self.trigger = trigger

    def __repr__(self) -> str:
        return (
            f"KycTransition(from_state={self.from_state.value}, "
            f"to_state={self.to_state.value}, trigger={self.trigger!r})"
        )
