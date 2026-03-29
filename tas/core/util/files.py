from pathlib import Path
"""
File system utility helpers for safe and consistent file operations.

This module provides abstractions for common file and directory operations,
ensuring that paths are created safely and files are written reliably.

Features:
- Automatic directory creation (including parent directories)
- Safe file writing with encoding support
- Path handling using pathlib for cross-platform compatibility

Typical Use Cases:
- Writing test artifacts (logs, reports, screenshots)
- Creating output directories for test runs
- Managing file-based test data

Functions:
- ensure_dir(): Ensures a directory exists, creating it if necessary
- write_text(): Writes text content to a file, ensuring parent directories exist

Design Note:
This module is part of the Automation Core Layer (Common Utilities)
and supports artifact management and reporting components.
"""

def ensure_dir(path: Path) -> Path:
    path.mkdir(parents=True, exist_ok=True)
    return path

def write_text(path: Path, content: str, encoding: str = "utf-8") -> Path:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding=encoding)
    return path
