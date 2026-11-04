"""
Context Injector — VespaFlow's safe-context layer.

Enriches a raw CI failure event with structured security context before
handing it to the fix-generation agent. All enrichment is read-only: this
module never modifies the repository or triggers any external mutation.
"""

from __future__ import annotations

import re
import textwrap
from dataclasses import dataclass, field
from pathlib import Path
from typing import Optional


@dataclass
class FailureEvent:
    """Normalised representation of a
