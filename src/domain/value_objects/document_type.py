from __future__ import annotations

from enum import Enum


class DocumentType(str, Enum):
    """Canonical document types required during onboarding and re-verification."""

    PAN = "pan"
    AADHAAR = "aadhaar"
    PASSPORT = "passport"
    DRIVING_LICENSE = "driving_license"
    UTILITY_BILL = "utility_bill"
    BANK_STATEMENT = "bank_statement"
    PHOTO = "photo"
    ADDRESS_PROOF = "address_proof"
