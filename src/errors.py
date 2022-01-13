class errors(Exception):
    """Base class for other exceptions"""
    pass


class ValueTooSmallError(errors):
    """Raised when the input value is too small"""
    pass


class ValueTooLargeError(errors):
    """Raised when the input value is too large"""
    pass