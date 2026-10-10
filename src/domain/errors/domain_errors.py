from __future__ import annotations


class DomainError(Exception):
    """Base exception for domain-level validation and state errors."""


class ValidationError(DomainError):
    """Raised when a domain object or request is invalid."""


class NotFoundError(DomainError):
    """Raised when an expected domain entity cannot be located."""


class ConflictError(DomainError):
    """Raised when a state transition or domain rule is violated."""


class AuthenticationError(DomainError):
    """Raised when caller authentication fails."""


class AuthorisationError(DomainError):
    """Raised when a caller lacks permission for a requested action."""


class RateLimitError(DomainError):
    """Raised when the system is rate limited by the platform or vendor."""


class VendorError(DomainError):
    """Raised when a vendor returns an error that is not transient."""


class VendorUnavailableError(VendorError):
    """Raised when a vendor is temporarily unavailable or unhealthy."""


class InternalError(DomainError):
    """Raised when an unexpected internal condition occurs."""
