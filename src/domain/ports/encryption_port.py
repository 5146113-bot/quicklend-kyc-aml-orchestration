from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class EncryptionPort(ABC):
    """Encryption abstraction used by the KMS/data-access layer."""

    @abstractmethod
    def encrypt(self, plaintext: bytes, key_id: str | None = None) -> dict[str, Any]:
        """Encrypt bytes and return the encrypted envelope metadata."""

    @abstractmethod
    def decrypt(self, ciphertext: bytes, key_id: str | None = None) -> bytes:
        """Decrypt a previously encrypted payload."""

    @abstractmethod
    def rotate_key(self, new_key_id: str) -> None:
        """Rotate the active key material for subsequent encryption."""
