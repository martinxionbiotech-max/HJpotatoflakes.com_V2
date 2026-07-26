#!/usr/bin/env python3
"""
Schema.org JSON-LD Injector for Hongji Agriculture Technical Documentation

Usage:
  python3 inject-schema.py <path-to-built-site>

Injects Organization, WebSite, and TechArticle schemas into each HTML file.
Run after building the static site (MkDocs, Docusaurus, etc.) or
use with a simple render script.
"""

import json
import os
import re
import sys

ORGANIZATION_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "Organization",
    "@id": "https://hjpotatoflakes.com/#organization",
    "name": "Hongji Agriculture Technology Co., Ltd.",
    "alternateName": "弘基农业",
    "url": "https://hjpotatoflakes.com",
    "description": (
        "China's leading vertically integrated potato flake and powder "
        "manufacturer — from seed breeding and cultivation to processing "
        "and global export."
    ),
    "brand": {
        "@type": "Brand",
        "name": "Hongji Agriculture"
    },
    "contactPoint": {
        "@type": "ContactPoint",
        "email": "sales@hjpotatoflakes.com",
        "contactType": "sales",
        "availableLanguage": ["English", "Chinese"]
    }
}

WEBSITE_SCHEMA = {
    "@context": "https://schema.org",
    "@type": "WebSite",
    "@id": "https://hjpotatoflakes.com/#website",
    "url": "https://hjpotatoflakes.com",
    "name": "Hongji Agriculture — Technical Documentation Knowledge Center",
    "description": (
        "Technical documentation knowledge base for Hongji Agriculture's "
        "vertically integrated potato flake and powder products — covering "
        "variety breeding, farming, storage, processing, quality control, "
        "product application, and industry compliance."
    ),
    "publisher": {"@id": "https://hjpotatoflakes.com/#organization"}
}


def inject_schema(html_path: str) -> bool:
    """Inject JSON-LD schemas into an HTML file. Returns True if modified."""
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    if 'application/ld+json' in html:
        return False  # Already has schema

    # Try to extract page title for TechArticle
    title_match = re.search(r'<title>(.*?)</title>', html, re.IGNORECASE)
    page_title = title_match.group(1) if title_match else "Technical Documentation"

    # Remove "| Hongji Agriculture" suffix for clean headline
    headline = re.sub(r'\s*[|-]\s*Hongji Agriculture.*$', '', page_title).strip()

    tech_article_schema = {
        "@context": "https://schema.org",
        "@type": "TechArticle",
        "@id": f"https://hjpotatoflakes.com/{os.path.relpath(html_path, html_path.split('/')[0])}#article",
        "headline": headline,
        "url": f"https://hjpotatoflakes.com/{os.path.relpath(html_path, html_path.split('/')[0])}",
        "author": {"@type": "Organization", "@id": "https://hjpotatoflakes.com/#organization"},
        "publisher": {"@type": "Organization", "@id": "https://hjpotatoflakes.com/#organization"},
        "mainEntityOfPage": {"@type": "WebPage", "@id": f"https://hjpotatoflakes.com/{os.path.relpath(html_path, html_path.split('/')[0])}"}
    }

    schema_blocks = (
        f'<script type="application/ld+json">{json.dumps(ORGANIZATION_SCHEMA, indent=2)}</script>\n'
        f'<script type="application/ld+json">{json.dumps(WEBSITE_SCHEMA, indent=2)}</script>\n'
        f'<script type="application/ld+json">{json.dumps(tech_article_schema, indent=2)}</script>\n'
    )

    # Inject right before </head>
    html = html.replace('</head>', f'{schema_blocks}</head>')

    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    return True


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 inject-schema.py <site-directory>")
        sys.exit(1)

    site_dir = sys.argv[1]
    modified = 0
    skipped = 0

    for root, dirs, files in os.walk(site_dir):
        for fn in files:
            if fn.endswith('.html'):
                path = os.path.join(root, fn)
                if inject_schema(path):
                    print(f"  ✅ {os.path.relpath(path, site_dir)}")
                    modified += 1
                else:
                    skipped += 1

    print(f"\nDone: {modified} files modified, {skipped} already had schema")


if __name__ == "__main__":
    main()
