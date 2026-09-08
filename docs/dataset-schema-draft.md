# hjpotatoflakes.com — Dataset 静态 JSON 草案

> 用途：把 docs.hjpotatoflakes.com 的"Quick Reference 技术参数表"（水分/干物质/淀粉/复水比等）做成机器可读的静态 JSON，供 AI 直接抽取引用。
> 落地：构建期静态生成（`public/data/*.json`），零后端。
> 数据来源：弘基农业官方技术文档（ISO 22000 / FSSC 22000 / HACCP 体系下）。

## 文件清单

| 文件 | 内容 |
|---|---|
| `/data/catalog.json` | 数据集索引（Schema.org `Dataset`） |
| `/data/specs.json` | 土豆雪花粉 + 土豆粉技术规格（参数表机器化） |
| `/data/varieties.json` | 土豆品种（Atlantic / Shepody / Russet Burbank）加工特性 |

---

## 1. `/data/catalog.json`（Dataset 索引）

```json
{
  "@context": "https://schema.org",
  "@type": "Dataset",
  "name": "Hongji Agriculture Potato Flakes & Powder Technical Specifications",
  "description": "Machine-readable technical specifications for Hongji potato flakes and potato powder (60 mesh): moisture, dry matter, starch, rehydration ratio, bulk density, particle size, colour, and microbiological limits under ISO 22000 / FSSC 22000 / HACCP.",
  "url": "https://hjpotatoflakes.com/data/catalog.json",
  "creator": {
    "@type": "Organization",
    "name": "Hongji Agriculture Technology Co., Ltd.",
    "alternateName": "张家口弘基农业科技开发有限责任公司",
    "url": "https://hjpotatoflakes.com/"
  },
  "dateModified": "2026-09-08",
  "isAccessibleForFree": true,
  "distribution": [
    { "@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://hjpotatoflakes.com/data/specs.json" },
    { "@type": "DataDownload", "encodingFormat": "application/json", "contentUrl": "https://hjpotatoflakes.com/data/varieties.json" }
  ],
  "variableMeasured": [
    { "@type": "PropertyValue", "name": "moisture_pct", "unitText": "%" },
    { "@type": "PropertyValue", "name": "dry_matter_pct", "unitText": "%" },
    { "@type": "PropertyValue", "name": "starch_pct", "unitText": "%" },
    { "@type": "PropertyValue", "name": "rehydration_ratio", "unitText": "ratio" },
    { "@type": "PropertyValue", "name": "bulk_density", "unitText": "g/mL" }
  ]
}
```

---

## 2. `/data/specs.json`（技术参数表机器化）

```json
{
  "dataset": "hongji-potato-specs",
  "version": "2026-08",
  "certifications": ["ISO 22000:2018", "FSSC 22000", "HACCP", "Halal", "Kosher", "Organic (EU/USDA)", "GlobalG.A.P."],
  "products": [
    {
      "product": "Potato Flakes",
      "product_id": "HJ-PF",
      "description": "Drum-dried, flaked, screened to 0.25–2.0 mm. Fast rehydration, creamy texture.",
      "specs": [
        { "parameter": "Moisture", "value": "≤6.0", "unit": "%", "test_method": "AOAC 934.01" },
        { "parameter": "Dry Matter", "value": "≥94.0", "unit": "%", "test_method": "Calculation" },
        { "parameter": "Starch", "value": "75-82", "unit": "%", "test_method": "AOAC 996.11" },
        { "parameter": "Reducing Sugars", "value": "≤1.5", "unit": "%", "test_method": "DNS / Fehling's" },
        { "parameter": "Protein", "value": "7-10", "unit": "%", "test_method": "Kjeldahl (N×6.25)" },
        { "parameter": "Rehydration Ratio", "value": "≥7.0", "unit": "ratio", "test_method": "Internal method" },
        { "parameter": "Bulk Density (loose)", "value": "0.35-0.55", "unit": "g/mL", "test_method": "ASTM B527" },
        { "parameter": "Particle Size", "value": "0.25-2.0", "unit": "mm", "test_method": "Sieve analysis" },
        { "parameter": "Colour (L*)", "value": "≥85.0", "unit": "L*", "test_method": "CIE Lab*" },
        { "parameter": "Total Plate Count", "value": "≤10000", "unit": "CFU/g", "test_method": "ISO 4833" },
        { "parameter": "Coliforms", "value": "≤10", "unit": "CFU/g", "test_method": "ISO 4832" },
        { "parameter": "Salmonella", "value": "Negative", "unit": "/25g", "test_method": "ISO 6579" }
      ]
    },
    {
      "product": "Potato Powder",
      "product_id": "HJ-PP-60",
      "description": "60-mesh milled potato flakes (≤250 µm). Superior dispersion for dry mixes, soup powders, seasonings.",
      "specs": [
        { "parameter": "Moisture", "value": "≤6.0", "unit": "%", "test_method": "AOAC 934.01" },
        { "parameter": "Dry Matter", "value": "≥94.0", "unit": "%", "test_method": "Calculation" },
        { "parameter": "Starch", "value": "75-82", "unit": "%", "test_method": "AOAC 996.11" },
        { "parameter": "Reducing Sugars", "value": "≤1.5", "unit": "%", "test_method": "DNS / Fehling's" },
        { "parameter": "Protein", "value": "7-10", "unit": "%", "test_method": "Kjeldahl (N×6.25)" },
        { "parameter": "Rehydration Ratio", "value": "≥7.5", "unit": "ratio", "test_method": "Internal method" },
        { "parameter": "Bulk Density (loose)", "value": "0.50-0.70", "unit": "g/mL", "test_method": "ASTM B527" },
        { "parameter": "Particle Size", "value": "≤250", "unit": "µm", "test_method": "Sieve analysis (60 mesh)" },
        { "parameter": "Colour (L*)", "value": "≥87.0", "unit": "L*", "test_method": "CIE Lab*" },
        { "parameter": "Total Plate Count", "value": "≤10000", "unit": "CFU/g", "test_method": "ISO 4833" },
        { "parameter": "Coliforms", "value": "≤10", "unit": "CFU/g", "test_method": "ISO 4832" },
        { "parameter": "Salmonella", "value": "Negative", "unit": "/25g", "test_method": "ISO 6579" }
      ]
    }
  ]
}
```

---

## 3. `/data/varieties.json`（品种加工特性）

```json
{
  "dataset": "hongji-potato-varieties",
  "version": "2026-08",
  "varieties": [
    {
      "name": "Atlantic",
      "role": "Primary flake variety",
      "traits": ["high dry matter", "naturally white flesh", "low black spot incidence"],
      "note": "Gold standard for flake processing"
    },
    {
      "name": "Shepody",
      "role": "Processing variety",
      "traits": ["good processing performance", "white flesh"]
    },
    {
      "name": "Russet Burbank",
      "role": "Processing variety",
      "traits": ["high dry matter", "excellent processing"]
    }
  ]
}
```

---

## 落地要点

1. **构建期静态生成**，零后端（符合"静态 > 运行时"原则）。
2. **`test_method` 字段是关键**——AOAC/ISO/ASTM 检测标准号让数据可被专业买家/AI 直接核验，这是 B2B 数据的信任核心，必须保留。
3. **认证清单**写进 specs 顶层，供 AI 抽取"这个厂有什么认证"。
4. **不暴露**：价格、客户、未公开配方、内部工艺参数。
5. **Schema 补强**：docs 的参数表页加 `Dataset` JSON-LD 指向 `/data/catalog.json`；主站产品页加 `Product` schema 引用 specs。
6. **与 llms.txt 打通**：docs 的 llms.txt 加一节 `## Data` 指向这三个 JSON。
