"""Scroll Transition tool interface."""

import re
from pathlib import Path
from typing import Optional

from ethereum_test_exceptions import (
    EOFException,
    ExceptionMapper,
    ExceptionMessage,
    TransactionException,
)
from ethereum_test_forks import Fork

from ..transition_tool import TransitionTool

class ScrollOpenVMTransitionTool(TransitionTool):
    """Scroll OpenVM Transition tool interface wrapper class."""

    default_binary = Path("openvm-t8n")
    detect_binary_pattern = re.compile(r"^openvm-t8n\b")
    version_flag: str = "--version"
    t8n_use_stream = True

    def __init__(
        self,
        *,
        binary: Optional[Path] = None,
        trace: bool = False,
    ):
        """Initialize the EthereumJS Transition tool interface."""
        super().__init__(exception_mapper=None, binary=binary, trace=trace)

    def is_fork_supported(self, fork: Fork) -> bool:
        """
        Return True if the fork is supported by the tool.
        Currently, EthereumJS-t8n provides no way to determine supported forks.
        """
        return True