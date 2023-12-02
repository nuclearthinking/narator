from click import ClickException


class NaratorException(Exception):
    """Base class for Narator exceptions"""


class UnableToReadConfigFile(NaratorException):
    """Raised when unable to read config file"""


class UnableToWriteConfigFile(Exception):
    """Raised when unable to write config file"""


class DisplayableException(NaratorException, ClickException):
    """Base class for exceptions that can be displayed to the user"""
