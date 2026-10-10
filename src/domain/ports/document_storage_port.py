from __future__ import annotations

from abc import ABC, abstractmethod
from typing import Any


class DocumentStoragePort(ABC):
    """Persistence abstraction for documents and evidence artifacts."""

    @abstractmethod
    def store(self, document_id: str, content: bytes, metadata: dict[str, Any]) -> str:
        """Persist a document and return an immutable storage key."""

    @abstractmethod
    def fetch(self, storage_key: str) -> bytes:
        """Fetch the bytes for a stored document."""

    @abstractmethod
    def delete(self, storage_key: str) -> None:
        """Delete a document from storage."""
