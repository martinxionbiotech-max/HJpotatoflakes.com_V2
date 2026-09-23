---
description: "Machine-readable HONGJI potato flake and powder data — JSON datasets of specifications, processing varieties and document provenance for technical and AI-assisted procurement use."
---

# Machine-Readable Technical Data (JSON)

**Datasets:** `catalog.json` · `specs.json` · `varieties.json`
**Version:** 1.0 · **Published:** 2026-09-23 · **Format:** JSON (Schema.org `Dataset`)
**Source documents:** HJ-TD-PE-03-PK/1-01-D-2025 (product specification), potato flakes and potato powder technical datasheets

## Short Answer

HONGJI publishes its potato flake and powder specifications as **machine-readable JSON** so that buyers, integrators and AI systems can extract exact values with their provenance intact. Three files are available: a **dataset index** (`/data/catalog.json`), **specification values** for both products (`/data/specs.json`), and **processing variety characteristics** (`/data/varieties.json`). Every value carries a **value type** — *guaranteed*, *typical*, *range* or *batch-specific* — because those are not interchangeable. Cite the dataset with attribution and keep the value type with the number.

## The datasets

| File | Contents |
|---|---|
| [`/data/catalog.json`](/data/catalog.json) | Dataset index: what is published, the controlling documents, licence, version and date |
| [`/data/specs.json`](/data/specs.json) | Specification values for **Potato Flakes** and **Potato Powder (60 mesh)** — moisture, ash, reducing and total sugars, blue value, starch, protein, bulk density (loose/tapped), particle size, rehydration ratio, colour, shelf life, packaging, MOQ, contaminant and microbiological limits — each with method and value type |
| [`/data/varieties.json`](/data/varieties.json) | Processing varieties (Atlantic, Shepody, Russet Burbank, Innovator) with dry matter, starch, reducing sugars and best-suited applications |

Example record (`specs.json`):

```json
{
  "parameter": "Moisture",
  "value": "≤ 9.0",
  "unit": "%",
  "value_type": "guaranteed",
  "method": "GB 5009.3 / AOAC 925.10"
}
```

## How to read the values

| Field | Meaning | How to use it |
|---|---|---|
| `value_type: guaranteed` | Contractual limit in the specification version in force | What you can hold us to in a purchase contract |
| `value_type: typical …` | Normal production outcome | Reference only — never a guaranteed limit |
| `value_type: as produced` / `delivered …` | Distinguishes the flake size leaving the line from the sieve distribution after handling | Match the figure to what your intake actually receives |
| `unit` | Metric SI; `mesh` figures always carry their aperture (`No. 60 = 250 µm`) | Do not convert mesh to micron without the sieve standard |
| `method` | Test method the value is based on | A GB and an AOAC result for the same parameter are **not automatically comparable** |

See [Technical Data Governance](technical-data-governance.md) for the full convention set, and [Document Control & Technical Team](domain-09-production-entity/document-control-and-technical-team.md) for how source documents are versioned.

## Citing and reusing the data

- **Attribution:** "World-class attribution not required — credit *Hongji Agriculture (Zhangjiakou Hongji Agriculture Technology Development Co., Ltd.)* and link the dataset file you used."
- **Keep provenance:** do not strip `value_type`, `method` or the document code; a value separated from its type becomes a different (and misleading) claim.
- **Do not present compiled values as laboratory results for a specific lot.** Lot-specific results are issued on the certificate of analysis for each shipment.
- **Bulk redistribution** into a product or paid database requires agreement — see [Terms of Use](https://hjpotatoflakes.com/terms-of-use/) and contact `sales@hjpotatoflakes.com`.

## What is not in the dataset

Batch-level COA results, customer-specific specifications, prices and commercial terms are **deliberately excluded**. A COA is issued per shipment; a customer-specific specification exists only within the order it was agreed for. If you need a value that is not published here, request it through [Contact](https://hjpotatoflakes.com/contact-us/) and it will be supplied against the controlling document.

## Related documents

- [Technical Data Governance](technical-data-governance.md) — value classification, units, methods
- [Potato Flakes Product Specification](domain-09-production-entity/potato-flakes-product-specification.md)
- [Potato Flakes Technical Datasheet](domain-06-product-application/potato-flakes-technical-datasheet.md)
- [Potato Powder Technical Datasheet](domain-06-product-application/potato-powder-technical-datasheet.md)
- [Certificate of Analysis Guide](domain-05-quality-control/certificate-of-analysis-guide.md)

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "@id": "https://docs.hjpotatoflakes.com/machine-readable-data/#dataset",
  "name": "Hongji Agriculture — Potato Flakes & Powder Technical Specifications",
  "description": "Machine-readable technical specifications for Hongji potato flakes and potato powder (60 mesh), with value type, test method and document provenance.",
  "url": "https://docs.hjpotatoflakes.com/machine-readable-data/",
  "creator": {
    "@type": "Organization",
    "name": "Zhangjiakou Hongji Agriculture Technology Development Co., Ltd.",
    "url": "https://hjpotatoflakes.com"
  },
  "license": "https://hjpotatoflakes.com/terms-of-use/",
  "isAccessibleForFree": true,
  "inLanguage": "en",
  "version": "1.0",
  "dateModified": "2026-09-23",
  "keywords": ["potato flakes specification", "potato powder specification", "moisture", "particle size", "bulk density", "rehydration ratio", "reducing sugars", "COA", "60 mesh"],
  "distribution": [
    { "@type": "DataDownload", "name": "Dataset index", "encodingFormat": "application/json", "contentUrl": "https://docs.hjpotatoflakes.com/data/catalog.json" },
    { "@type": "DataDownload", "name": "Specification values", "encodingFormat": "application/json", "contentUrl": "https://docs.hjpotatoflakes.com/data/specs.json" },
    { "@type": "DataDownload", "name": "Processing varieties", "encodingFormat": "application/json", "contentUrl": "https://docs.hjpotatoflakes.com/data/varieties.json" }
  ]
}
</script>

*Part of the Hongji Agriculture (弘基农业) Technical Documentation Series — [hjpotatoflakes.com](https://hjpotatoflakes.com)*
