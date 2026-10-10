from __future__ import annotations

from src.domain.errors.domain_errors import ValidationError
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.verification_status import VerificationStatus


def test_valid_transitions() -> None:
    assert VerificationStatus.INITIATED.value == "initiated"
    assert VerificationStatus.MANUAL_ESCALATION.value == "manual_escalation"


def test_customer_id_requires_value() -> None:
    try:
        CustomerId("")
        raise AssertionError("Expected ValidationError for blank CustomerId")
    except ValidationError:
        pass


def test_verify_manual_escalation_to_verified() -> None:
    from src.domain.state_machine.kyc_state import KycState
    from src.domain.state_machine.kyc_state_machine import KycStateMachine

    assert KycStateMachine.can_transition(KycState.MANUAL_ESCALATION, KycState.VERIFIED)
    assert KycStateMachine.can_transition(KycState.MANUAL_ESCALATION, KycState.REJECTED)


def test_invalid_transition_raises_conflict() -> None:
    from src.domain.errors.conflict_error import KycConflictError
    from src.domain.state_machine.kyc_state import KycState
    from src.domain.state_machine.kyc_state_machine import KycStateMachine

    try:
        KycStateMachine.assert_transition(KycState.VERIFIED, KycState.IN_REVIEW, "reopen")
        raise AssertionError("Expected KycConflictError for invalid transition")
    except KycConflictError:
        pass
