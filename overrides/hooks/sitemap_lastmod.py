"""Set sitemap lastmod from page frontmatter dates.

MkDocs core sitemap.xml reads `page.update_date`. By default MkDocs sets that
to the build date. This hook prefers `dateModified` and falls back to `date`,
so content agents can control lastmod without touching rendered body text.
"""
from __future__ import annotations

from datetime import date, datetime, timezone
from typing import Any


def _normalize_date(value: Any) -> str:
    """Return an ISO date string for a frontmatter date value."""
    if isinstance(value, datetime):
        if value.tzinfo is None:
            value = value.replace(tzinfo=timezone.utc)
        else:
            value = value.astimezone(timezone.utc)
        return value.date().isoformat()

    if isinstance(value, date):
        return value.isoformat()

    text = str(value).strip()
    try:
        parsed = datetime.fromisoformat(text.replace("Z", "+00:00"))
        if parsed.tzinfo is not None:
            parsed = parsed.astimezone(timezone.utc)
        return parsed.date().isoformat()
    except ValueError:
        return text


def on_page_context(context: dict, **kwargs) -> dict:
    page = kwargs["page"]
    raw_date = page.meta.get("dateModified") or page.meta.get("date")
    if raw_date:
        page.update_date = _normalize_date(raw_date)
    return context
