from __future__ import annotations

from dataclasses import dataclass, field
from typing import Any

from src.domain.errors.domain_errors import ValidationError
from src.domain.value_objects.customer_id import CustomerId
from src.domain.value_objects.document_type import DocumentType
from src.domain.value_objects.verification_status import VerificationStatus


@dataclass(slots=True)
class KycCase:
    """Aggregate root for KYC workflow state and required document tracking."""

    case_id: str
    customer_id: CustomerId
    workflow: str = "minimum_kyc"
    status: VerificationStatus = VerificationStatus.INITIATED
    required_documents: set[DocumentType] = field(default_factory=set)
    submitted_documents: set[DocumentType] = field(default_factory=set)
    metadata: dict[str, Any] = field(default_factory=dict)
    version: int = 0

    def __post_init__(self) -> None:
        if not self.case_id or not self.case_id.strip():
            raise ValidationError("case_id cannot be blank.")

    def add_required_document(self, document_type: DocumentType) -> None:
        self.required_documents.add(document_type)

    def mark_document_submitted(self, document_type: DocumentType) -> None:
        self.submitted_documents.add(document_type)

    def transition_to(self, next_status: VerificationStatus, trigger: str) -> None:
        """Apply a state transition only if it is allowed by the domain state machine."""
        from src.domain.state_machine.kyc_state_machine import KycStateMachine

        KycStateMachine.assert_transition(self.status, next_status, trigger)
        self.status = next_status
        self.version += 1
