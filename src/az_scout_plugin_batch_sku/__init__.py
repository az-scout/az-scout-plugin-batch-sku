"""az-scout Batch SKU plugin.

Lists Azure Batch-compatible VM SKUs per region, grouped by VM family.
"""

from collections.abc import Callable
from pathlib import Path
from typing import Any

from az_scout.plugin_api import TabDefinition
from fastapi import APIRouter

try:
    from az_scout_plugin_batch_sku._version import __version__
except ModuleNotFoundError:  # editable install or dev mode
    __version__ = "0.0.0.dev0"

_STATIC_DIR = Path(__file__).parent / "static"


class BatchSkuPlugin:
    """Plugin that lists Batch-compatible VM SKUs per region."""

    name = "batch_sku"
    version = __version__

    def get_router(self) -> APIRouter | None:
        """Return API routes, or None to skip."""
        from az_scout_plugin_batch_sku.routes import router

        return router

    def get_mcp_tools(self) -> list[Callable[..., Any]] | None:
        """Return MCP tool functions, or None to skip."""
        from az_scout_plugin_batch_sku.tools import list_batch_skus

        return [list_batch_skus]

    def get_static_dir(self) -> Path | None:
        """Return path to static assets directory, or None to skip."""
        return _STATIC_DIR

    def get_tabs(self) -> list[TabDefinition] | None:
        """Return UI tab definitions, or None to skip."""
        return [
            TabDefinition(
                id="batch_sku",
                label="Batch SKUs",
                icon="bi bi-gpu-card",
                js_entry="js/batch-sku-tab.js",
                css_entry="css/batch-sku.css",
            )
        ]

    def get_chat_modes(self) -> list["Any"] | None:
        """Return chat mode definitions, or None to skip."""
        return None


# Module-level instance — referenced by the entry point
plugin = BatchSkuPlugin()
