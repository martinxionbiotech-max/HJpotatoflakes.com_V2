---
description: "Certificate of Analysis - Guide and Interpretation — Potato flake and powder quality control methods"
---

# Certificate of Analysis — Guide and Interpretation

**Document Code:** HJ-QA-030  
**Version:** 2.1  
**Effective Date:** 2026-03-10  
**Prepared by:** Finished Product Laboratory & Customer Technical Support, Hongji Agriculture Co., Ltd.

---

## 1. Introduction

The Certificate of Analysis (COA) is the primary document through which Hongji Agriculture communicates the quality status of each production lot to its B2B customers. A properly designed and accurately completed COA enables the customer's receiving quality team to make rapid, informed decisions about lot acceptance, storage, and process integration.

This guide provides:
- A detailed explanation of the COA standard template and each parameter
- The analytical method referenced for every test
- The specification range and how measured values should be interpreted
- Guidance for buyers on using COA data in procurement decisions
- Hongji's batch consistency evaluation methodology
- Overview of the electronic COA (eCOA) system

---

## 2. COA Standard Template

Below is the complete COA template used for all Hongji potato flake and potato powder shipments. Each field is described in detail in subsequent sections.

### 2.1 Template Structure

```
─────────────────────────────────────────────────────────────────────
            HONGJI AGRICULTURE CO., LTD.
            CERTIFICATE OF ANALYSIS

COA No.: HJ-COA-2026-XXXXX             Issue Date: YYYY-MM-DD

Product Name: Potato Flakes (Standard)        Grade: Premium
Customer: [Customer Name]
PO No.: PO-XXXXXX-XXXX                       Lot No.: HJ-AT-R2-260715-A

Production Date: 2026-07-15                  Expiry Date: 2027-07-14
Net Weight: 20 kg × 500 bags = 10,000 kg
Pallet IDs: P260715-01 through P260715-20

─────────────────────────────────────────────────────────────────────
PARAMETER                     UNIT       SPECIFICATION      RESULT   STATUS
─────────────────────────────────────────────────────────────────────

PHYSICAL PROPERTIES
  Moisture                    %          6.0 – 8.0          6.8      PASS
  Particle Size (D50)         μm         700 – 1200          920      PASS
  Particle Size (D90)         μm         ≤ 2000             1530     PASS
  Loose Bulk Density          g/mL       0.40 – 0.55         0.47    PASS
  Tapped Bulk Density         g/mL       0.50 – 0.65         0.58    PASS
  Color L*                    —          ≥ 87.0              89.3    PASS
  Color a*                    —          −2.5 to +1.5        −1.2    PASS
  Color b*                    —          ≤ 22.0              17.5    PASS
  Whiteness (WG)              —          ≥ 78.0              81.2    PASS
  Dark Particles              per 250 g  ≤ 15                3       PASS

CHEMICAL PROPERTIES
  Dry Matter                  %          92.0 – 94.0         93.2    PASS
  Starch (% DM)               %          70.0 – 80.0         74.8    PASS
  Reducing Sugars             %          ≤ 3.5               1.2     PASS
  Protein (N × 6.25)          % DM       5.5 – 8.5           6.4     PASS
  Ash                         % DM       ≤ 4.5               3.2     PASS
  SO₂ Residue                 mg/kg      ≤ 400               86      PASS

MICROBIOLOGICAL PROPERTIES
  APC                         CFU/g      ≤ 5.0 × 10⁴         1.2 × 10³   PASS
  Coliforms                   CFU/g      ≤ 5.0 × 10²         <10     PASS
  E. coli                     CFU/g      ≤ 1.0 × 10²         <10     PASS
  Salmonella                  /25g       Absent              Absent  PASS
  S. aureus                   CFU/g      ≤ 1.0 × 10³         <10     PASS
  Yeasts                      CFU/g      ≤ 5.0 × 10²         <10     PASS
  Molds                       CFU/g      ≤ 5.0 × 10²         25      PASS

FUNCTIONAL PROPERTIES
  Rehydration Ratio           g/g        ≥ 7.0               7.8     PASS

─────────────────────────────────────────────────────────────────────

DISPOSITION: ✅ APPROVED FOR RELEASE
Verified by: [Name], QA Supervisor       Date: YYYY-MM-DD
Digitally Signed: [SHA-256 Hash]
─────────────────────────────────────────────────────────────────────
```

---

## 3. Parameter-by-Parameter Interpretation

### 3.1 Physical Properties

| Parameter | Analytical Method | What It Tells the Buyer | Red Flags |
|-----------|-------------------|------------------------|-----------|
| **Moisture (%)** | AOAC 934.06 (oven drying) | Determines yield, shelf life, microbiological stability. High moisture (>8.5%) = shorter shelf life, potential mold; low moisture (<5.5%) = overdried, may have reduced RR | >8.5%: request extended shelf-life data; <5.5%: test rehydration |
| **Particle Size D50 (μm)** | Sieve analysis (HJ-QA-010) | Median particle diameter indicates texture and hydration behavior. Higher D50 = coarser texture; lower = smoother | Values outside spec may cause clumping, uneven mixing, or off-spec mouthfeel in customer's product |
| **Particle Size D90 (μm)** | Sieve analysis | Maximum particle size. High D90 indicates oversized particles that may cause gritty texture | >2500 μm: may require re-milling by buyer |
| **Bulk Density (Loose/Tapped)** | ASTM D1895 | Influences packaging density, transport cost, and volumetric dosing. Low loose BD = high air entrapment = more packaging volume per kg | Significant deviation from historical average may indicate altered process conditions |
| **Color (L\*a\*b\*)** | CIELAB (D65/10°) | Visual consistency indicator. L\* reflects whiteness; a\* indicates browning; b\* measures yellowness. Critical for brand-consistent finished product | ΔE > 3.0 from buyer's reference: may cause visible difference in finished product |
| **Dark Particles** | Manual sorting (HJ-QA-010) | Visible quality metric. Higher counts = raw material quality issues or process debris | >20/250g: often triggers customer complaint |
| **Whiteness (W_G)** | Ganz whiteness formula | Important for white-sauce, beverage, and bakery applications | <75: may produce off-white final product color |

### 3.2 Chemical Properties

| Parameter | Analytical Method | What It Tells the Buyer | Red Flags |
|-----------|-------------------|------------------------|-----------|
| **Dry Matter (%)** | AOAC 934.06 | Inverse of moisture; 92–94% DM means 6–8% moisture | <91.5% DM: microbial stability risk |
| **Starch (% DM)** | ISO 10520 (Ewers) | Core functional component. Determines thickening power, water binding. | <68% DM: reduced yield in customer's thickening application |
| **Reducing Sugars (%)** | DNS colorimetric | Primary driver of Maillard browning. High reducing sugars = darker fries/snacks, shorter fry oil life | >3.5%: increased browning risk for customers producing fried products |
| **Protein (% DM)** | Kjeldahl (N × 6.25) | Minor but relevant for nutritional labeling and Maillard reactivity | Values outside expected range may require nutritional label adjustment |
| **Ash (% DM)** | AOAC 923.03 (muffle furnace) | Mineral content indicator. High ash may indicate soil contamination or high mineral water | >5.0% DM: investigate soil/residue issue |
| **SO₂ Residue (mg/kg)** | Modified Monier-Williams | Preservative for color retention. Must meet regulatory limits of destination country | >400 mg/kg: may violate EU/China regulations; >10 mg/kg requires label declaration in US |

### 3.3 Microbiological Properties

| Parameter | Analytical Method | What It Tells the Buyer | Red Flags |
|-----------|-------------------|------------------------|-----------|
| **APC (CFU/g)** | ISO 4833-1 | General hygiene indicator. Low count = good process sanitation | >1 × 10⁵ CFU/g: marginal shelf life; investigate process hygiene |
| ***Salmonella* (/25g)** | ISO 6579-1 | Critical pathogen. Zero tolerance in most markets | Detection triggers immediate recall evaluation |
| **Yeasts & Molds** | ISO 21527-1 | Storage stability indicator. >500 CFU/g may signal moisture ingress or packaging failure | >1 × 10³ CFU/g: increased spoilage risk during transport/storage |

### 3.4 Functional Properties

| Parameter | Analytical Method | What It Tells the Buyer | Red Flags |
|-----------|-------------------|------------------------|-----------|
| **Rehydration Ratio (g/g)** | HJ-QA-025 (70°C, 5 min) | Core functional parameter. Determines yield in mashed potato reconstitution and water binding in formulations | <7.0: poor water absorption; may require recipe reformulation by buyer |

---

## 4. How COA Data Guides Buyer Procurement Decisions

### 4.1 Lot Acceptance Decision Matrix

Buyers should evaluate COAs against a three-tier decision framework:

| Criterion | Green — Accept | Yellow — Conditional | Red — Reject |
|-----------|----------------|---------------------|--------------|
| All parameters within spec | ✓ | — | — |
| 1–2 minor parameters marginally outside spec (e.g., color b\* = 23.5 vs. ≤22.0) | — | Accept with deviation agreement or discounted price | — |
| Any pathogen positive (Salmonella, confirmation required) | — | — | **Reject immediately** |
| Moisture > 9.0% | — | — | **Reject** |
| SO₂ > regulatory limit for destination | — | — | **Reject** |
| RR < 6.0 | — | — | **Reject** |

### 4.2 Trend Analysis for Strategic Buying

The most sophisticated buyers track COA data over time to build supplier performance profiles:

| Metric | Calculation | Signal |
|--------|------------|--------|
| **Cpk (Process Capability Index)** | (USL − μ) / 3σ or (μ − LSL) / 3σ (whichever is smaller) | Cpk ≥ 1.33 = capable process; 1.0–1.33 = marginally capable; <1.0 = process improvement needed |
| **Ppk (Process Performance Index)** | Same formula using overall standard deviation | >1.67 = excellent supplier; customer audits likely low priority |
| **Standard Deviation (σ)** of key parameters | Across the last 20+ lots | Lower σ = more consistent supplier; enables tighter customer spec |
| **Z-Score** for each parameter | (Individual value − Batch mean) / σ | |Z| > 2: outlier lot; investigate |

Example — Cpk analysis for 25 consecutive lots of Standard Flakes:

| Parameter | Target | USL | LSL | Mean | σ | Cpk | Rating |
|-----------|--------|-----|-----|------|---|-----|--------|
| Moisture (%) | 7.0 | 8.0 | 6.0 | 6.9 | 0.35 | 1.05 | Marginal |
| RR (g/g) | 7.5 | — | 7.0 | 7.7 | 0.15 | 1.56 | Excellent |

---

## 5. Batch Consistency Evaluation

### 5.1 Within-Lot Variability

For each production lot, Hongji tests 3 composite samples (beginning, middle, and end of the run). The within-lot coefficient of variation (CV) is reported:

$$CV = \frac{\sigma_{within-lot}}{\bar{x}} \times 100\%$$

| Parameter | Typical CV (%) | Acceptable CV (%) | Alert CV (%) |
|-----------|----------------|-------------------|--------------|
| Moisture | 1.0–2.0 | ≤3.0 | >3.0 |
| Reducing Sugars | 2.0–5.0 | ≤8.0 | >8.0 |
| Rehydration Ratio | 1.5–3.0 | ≤5.0 | >5.0 |
| Bulk Density | 1.0–2.5 | ≤4.0 | >4.0 |

### 5.2 Between-Lot Variability (Rolling 20-Lot Window)

Hongji's internal target for between-lot CV is ≤5% for all critical parameters. A rolling window of the last 20 lots is continuously monitored.

Monthly reports showing between-lot trends are available upon request for qualified customers.

---

## 6. Electronic Certificate of Analysis (eCOA) System

### 6.1 System Overview

Hongji has implemented a fully digital eCOA system, allowing customers to access, download, and integrate quality data into their own systems.

| Feature | Capability |
|---------|------------|
| **Portal Access** | Secure customer portal: https://qa.hjpotatoflakes.com |
| **API Integration** | RESTful API for automated COA retrieval (JSON / XML) |
| **Real-Time Availability** | COA published within 2 hours of lot release |
| **Historical Archive** | All COAs retained for minimum 5 years |
| **Digital Signature** | SHA-256 signed PDF with visible QR code for verification |
| **Multi-Format Export** | PDF, CSV, XML, JSON |

### 6.2 QR Code Verification

Every Hongji eCOA includes a QR code containing:
- Lot number
- COA number
- SHA-256 hash of the COA content
- Public verification URL

Buyers can scan the QR code or visit the verification URL to confirm the COA authenticity.

### 6.3 API Specification Summary

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/coa/{lot_number}` | GET | Retrieve COA by lot number |
| `/api/v1/coa/list?from=YYYY-MM-DD&to=YYYY-MM-DD` | GET | List COAs by date range |
| `/api/v1/coa/verify` | POST | Verify COA authenticity (submit SHA-256 hash) |

API access requires pre-registration and issuance of API credentials by Hongji's IT department.

---

## 7. Common Customer Questions About COA Data

| Question | Answer |
|----------|--------|
| "My lab's result differs from the COA — which do I trust?" | Inter-laboratory variation is normal (up to ±5% for chemical parameters, ±0.5 log for microbiological). Hongji participates in FAPAS proficiency testing (avg. z-score = 1.3). Discrepancies > ±10% should trigger a joint investigation. |
| "Can you add tests to the COA?" | Yes. Custom COA formats can be arranged during contract negotiation. Additional tests may incur a fee. |
| "Do you provide a COA for each pallet?" | Standard: one COA per production lot (up to 20 MT). For contracts requiring per-pallet COAs (e.g., pharmaceutical-grade food ingredients), add a surcharge. |
| "How long after production is the COA available?" | Within 24 hours (standard) or within 2 hours (eCOA portal). |

---

## 8. Quality Commitment

Hongji Agriculture stands behind every COA we issue. If a lot fails to meet the documented specifications and the deviation is confirmed by a mutually agreed third-party laboratory, we will:

1. Accept return of non-conforming goods at our cost
2. Issue a credit or replacement lot within 10 working days
3. Conduct a full root cause investigation and share findings

---

## 9. References

- ISO 9001:2015 — Clause 8.2.3: Review of requirements for products and services
- ISO 22000:2018 — Clause 8.7: Control of nonconforming outputs
- FSSC 22000 Scheme Document — Part 3: Certification Requirements
- GB/T 15000.3: Statistical methods for use in proficiency testing
- Hongji Internal Document HJ-QA-COA-SOP-01: COA Generation and Management Procedure

---

*End of Document*

---

## References

- AOAC International. Official Methods of Analysis, 21st edition. Gaithersburg, MD.
- ISO (International Organization for Standardization). Horizontal methods for food microbiology and physicochemical analysis.
- ASTM International. Standard test methods for particle size and bulk density.
- FSSC 22000. Food Safety System Certification standard.
- Hongji Agriculture Technology Co., Ltd. 2026. "Certificate of Analysis — Guide and Interpretation." Hongji Agriculture Knowledge Center.


---

*This document is part of the Hongji Agriculture (弘基农业) Technical Documentation Series. For more information about our vertically integrated potato supply chain — from seed breeding and cultivation to processing and global export — visit our official B2B website: [https://hjpotatoflakes.com](https://hjpotatoflakes.com)*
