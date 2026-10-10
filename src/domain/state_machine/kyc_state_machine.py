from __future__ import annotations

from src.domain.errors.conflict_error import KycConflictError
from src.domain.state_machine.kyc_state import KycState


class KycStateMachine:
    """Validates KYC status transitions and raises descriptive conflict errors."""

    _allowed_transitions: dict[KycState, set[KycState]] = {
        KycState.INITIATED: {KycState.DOCUMENTS_REQUIRED, KycState.IN_REVIEW},
        KycState.DOCUMENTS_REQUIRED: {KycState.IN_REVIEW},
        KycState.IN_REVIEW: {KycState.MANUAL_ESCALATION, KycState.VERIFIED, KycState.REJECTED},
        KycState.MANUAL_ESCALATION: {KycState.VERIFIED, KycState.REJECTED},
        KycState.VERIFIED: set(),
        KycState.REJECTED: set(),
    }

    @classmethod
    def can_transition(cls, from_state: KycState, to_state: KycState) -> bool:
        return to_state in cls._allowed_transitions.get(from_state, set())

    @classmethod
    def assert_transition(cls, from_state: KycState, to_state: KycState, trigger: str) -> None:
        if not cls.can_transition(from_state, to_state):
            raise KycConflictError(from_state.value, to_state.value, trigger)

    @classmethod
    def valid_next_states(cls, current_state: KycState) -> set[KycState]:
        return cls._allowed_transitions.get(current_state, set())
