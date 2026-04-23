# SPDX-FileCopyrightText: © 2026 Olivier Delrée <olivierdelree@protonmail.com>
#
# SPDX-License-Identifier: MIT

"""Custom errors."""

import abc
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import pathlib


class ParsingError(Exception, abc.ABC):
    """Parsing of an NCDU file failed."""

    _reason: str
    _path: str | None

    def __init__(self, reason: str, path: str | pathlib.Path | None = None) -> None:
        path_string = "" if path is None else f" ({path})"
        message = f"Parsing failed: {reason}{path_string}"

        super().__init__(message)

        self._reason = reason
        self._path = path if path is None else str(path)

    @property
    def reason(self) -> str:
        """Reason for the exception."""
        return self._reason

    @property
    def path(self) -> str | None:
        """Path to the file whose content caused the exception."""
        return self._path


class CBORError(ParsingError):
    """CBOR failed to parse data."""


class NCDUError(ParsingError):
    """NCDU failed to parse data."""
