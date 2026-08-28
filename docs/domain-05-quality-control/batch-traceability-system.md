---
description: "Batch Traceability System - Full-Chain from Seed to Ship — Potato flake and powder quality control methods"
---

# Batch Traceability System — Full-Chain from Seed to Ship

**Document Code:** HJ-QA-035  
**Version:** 2.0  
**Effective Date:** 2026-04-01  
**Prepared by:** Traceability & Compliance Team, Hongji Agriculture Co., Ltd.

---

## 1. Introduction

Traceability is a fundamental pillar of Hongji Agriculture's quality and food safety management system. In the event of a quality incident, regulatory inquiry, or customer complaint, Hongji must be able to trace any finished product lot back to its raw material origins — including the specific farm field, seed variety, harvest date, and processing conditions — and trace forward to every customer shipment. This document describes the complete batch traceability system, including the coding architecture, information system support, traceability performance metrics, and mock recall procedures.

Hongji's traceability system is designed to meet the requirements of:

- **ISO 22000:2018** — Clause 7.1.6 (Traceability system)
- **FSSC 22000** — Additional requirement for traceability and food fraud prevention
- **EU Regulation 178/2002** — General Food Law, Article 18 (Traceability)
- **China Food Safety Law** — Article 42 (Traceability requirements)
- **Global Food Safety Initiative (GFSI)** benchmarked standards
- **Customer-specific traceability requirements** (e.g., one-up/one-down, full chain)

---

## 2. Traceability Coding Architecture

### 2.1 Lot Number Structure

Hongji's lot number is a 22-character alphanumeric code structured to encode the maximum amount of traceable information within a compact identifier.

```
Format:  HJ - XX - YY - ZZZZZZ - DD - N

Example: HJ - AT - R2 - 260715 - 01 - A
```

| Segment | Position | Length | Code | Meaning |
|---------|----------|--------|------|---------|
| **Company Prefix** | 1–2 | 2 letters | HJ | Hongji Agriculture |
| **Variety Code** | 3–4 | 2 letters | AT | Atlantic |
| | | | SH | Shepody |
| | | | RB | Russet Burbank |
| | | | YS | Yanshu (domestic variety) |
| | | | OT | Other (specified in internal system) |
| **Production Base / Field** | 5–6 | 2 characters | R2 | Zhangbei Base, Field Block 2 |
| | | | S4 | Shangyi Base, Field Block 4 |
| | | | K1 | Kangbao Base, Field Block 1 |
| | | | T3 | Tengnapo Base, Field Block 3 |
| | | | PL | Plant / Processing facility code (if rework) |
| **Production Date (YYMMDD)** | 7–12 | 6 digits | 260715 | 2026-07-15 |
| **Production Line** | 13–14 | 2 digits | 01 | Processing Line 1 |
| | | | 02 | Processing Line 2 |
| **Shift / Sub-Lot** | 15 | 1 letter | A, B, C | Shift A (06:00–14:00), B (14:00–22:00), C (22:00–06:00) |

**Example Full Breakdown:**

```
Lot: HJ-AT-R2-260715-01-A

AT = Atlantic variety
R2  = Zhangbei Base, Field Block 2
260715  = Produced 15 July 2026
01  = Processing Line 1
A   = Shift A (morning shift)
```

### 2.2 Additional Identifiers

| Identifier | Format | Example | Usage |
|------------|--------|---------|-------|
| **Pallet Label** | LOTNO-PPP (3-digit pallet sequence) | HJ-AT-R2-260715-01-A-001 | Per-pallet tracking |
| **Carton Label** | LOTNO-CCC (5-digit carton sequence) | HJ-AT-R2-260715-01-A-00001 | Per-carton barcode |
| **Bulk Container ID** | LOTNO-CTNR | HJ-AT-R2-260715-01-A-BL01 | Big bag / tote identification |
| **Raw Material Receipt ID** | IN-YYMMDD-NNNN | IN-260715-0037 | Incoming potato lot tracking |
| **Semi-Product ID** | WIP-YYMMDD-LINE-NNNN | WIP-260715-L01-0012 | In-process identification |

---

## 3. Full-Chain Traceability Path

The traceability system spans six key stages from seed potato to finished product shipment.

### 3.1 Traceability Data Map

| Stage | Data Captured | Identifier Created | System | Responsible Dept. |
|-------|---------------|--------------------|--------|-------------------|
| **1. Seed Potato Allocation** | Variety, seed lot origin, treatment records | Seed-Lot-YYYY-NNNN | ERP (Seed Module) | Seed Operations |
| **2. Field Planting & Cultivation** | Field ID, planting date, fertilizer/pesticide applications, irrigation records | Field-Year-Session (e.g., R2-26-01) | GAP Field Data System | Field Agronomy |
| **3. Harvest** | Harvest date, field location, mechanical harvester ID, operator | Field-Harvest-Date-Block (linked to Raw Material ID) | Harvest Control System | Harvest Operations |
| **4. Raw Material Intake** | Variety verification, net weight, dry matter, defect %, storage bin assignment | IN-YYMMDD-NNNN | ERP / WMS | Raw Material QA |
| **5. Processing** | Lot blending record, CCP parameters (time/temp/pressure), additive dosage, sieve size, metal detector log | WIP-YYMMDD-LINE-NNNN | MES (Manufacturing Execution System) | Production + QA |
| **6. Finished Product & Shipment** | Final QC results (COA), packaging date, pallet ID, container number, customer PO, shipping document | HJ-XXXX-YY-ZZZZZZ-DD-N | ERP / WMS / LIMS | Finished Product QA + Logistics |

### 3.2 Critical Data Links

The following fields must be accurately linked across stages for full traceability:

| Forward Link | Backward Link | Data Field | Verification Point |
|--------------|---------------|------------|-------------------|
| Seed Lot → Field | Field → Seed Lot | Seed-lot-number | Planting record reconciliation |
| Field → Harvest | Harvest → Field | Field-ID | Harvest ticket |
| Harvest → Intake | Intake → Harvest | IN-number assigned at weighbridge | Weighbridge system log |
| Intake → Processing | Processing → Intake | IN-numbers used in daily blend sheet | Production batch sheet |
| Processing → Finished Product | Finished Product → Processing | WIP-numbers associated with final lot | MES batch report |
| Finished Product → Customer | Customer → Finished Product | Lot number on packing list | Customer's receiving record + COA |

---

## 4. Information System Architecture

Hongji's traceability system is supported by integrated information platforms covering:

| System Function | Traceability Role |
|-----------------|-------------------|
| **ERP (Enterprise Resource Planning)** | Financial, purchase order, shipment, and inventory records |
| **Manufacturing / Factory records** | CCP monitoring, line data, downtime logging |
| **Warehouse Management** | Bin tracking, FIFO control, pallet labels |
| **Laboratory Information** | QC results, COA generation, stability data |

### 4.1 Manufacturing Records — Detail

Production records capture the core traceability data for each batch:

| Record Function | Traceability Data Generated |
|----------------|-----------------------------|
| **Recipe Management** | Ingredient/batch recipe used for each production run |
| **CCP Data Logging** | Blanch temp/time, drum steam pressure, metal detector events |
| **Material Consumption** | Linking raw material IN-numbers to output WIP-numbers |
| **Yield Recording** | Input weight → output weight → yield % per lot |
| **Machine Parameters** | Line speed, drum RPM, residence time, drying air temperature |
| **Operator Tracking** | Personnel ID per shift per station |

### 4.2 Barcode Labeling System

| Level | Label Type | Barcode Standard | Information Encoded |
|-------|------------|------------------|---------------------|
| Pallet | GS1-128 | Code 128 | Lot number, pallet sequence, product code, net weight, production date |
| Carton | GS1 DataBar | GS1 DataMatrix | GTIN + lot number + carton sequence |
| Big Bag | GS1-128 | Code 128 | Lot number, net weight, best-before date |
| Shipping Container | SSCC-18 | GS1-128 | Serial Shipping Container Code (linked to lot numbers within) |

### 4.3 Data Retention and Backup

| Data Type | Retention Period | Backup Frequency |
|-----------|------------------|------------------|
| ERP transactional data | 5 years | Daily |
| Manufacturing batch records | 5 years | Daily |
| Laboratory test results | 5 years | Daily |
| CCP monitoring logs | 3 years | Weekly rolling |
| Traceability records | At least 3 years | As generated |
| CCTV footage (production area) | 90 days | Rolling |

---

## 5. Traceability Performance Metrics

### 5.1 Key Performance Indicators

| KPI | Definition | Target |
|-----|------------|--------|
| **T1 — Backward Trace Time** | Time to trace from finished product to raw material source (field level) | ≤4 hours |
| **T2 — Forward Trace Time** | Time to trace from finished product to all customer delivery points | ≤8 hours |
| **Trace Success Rate (1 step)** | % of trace exercises achieving one-step traceability (finished product → production batch OR raw material → processing line) | 100% |
| **Trace Success Rate (Full chain)** | % of trace exercises achieving full end-to-end traceability (finished product → seed lot and finished product → all customers) | ≥95% |
| **Data Completeness** | % of required data fields populated for a given lot | 100% |
| **Label Accuracy** | % of barcode scans matching database records | ≥99.9% |

### 5.2 Measurement Methodology

Trace times are measured using stopwatch from the moment the traceability team receives the request until the requested information is documented in a traceability report:

- **Backward trace (T1):** Start with a finished product lot number. End when the specific field block and seed lot are identified.
- **Forward trace (T2):** Start with a raw material receipt ID or an intermediate WIP number. End when all customer shipments containing that material are identified.

---

## 6. Mock Recall Procedure

Hongji conducts a minimum of **two mock recalls per year** as a regulatory and certification requirement (FSSC 22000, ISO 22000). These exercises validate the effectiveness of the traceability system under simulated crisis conditions.

### 6.1 Mock Recall Process Flow

```
Step 1 — Trigger (QA Director selects random lot)
        │
Step 2 — Notification (QA team notified; clock starts)
        │
Step 3 — Backward Trace (→ field level)
        │
Step 4 — Forward Trace (→ all customer shipments)
        │
Step 5 — Data Compilation (traceability report generated)
        │
Step 6 — Verification (independent QA auditor verifies data accuracy)
        │
Step 7 — Debrief (lessons learned, CAPA if needed)
        │
Step 8 — Report (submitted within 5 working days to COO and certification body)
```

### 6.2 Mock Recall Scenario Examples

Hongji conducts mock recalls covering typical scenarios such as customer complaints on quality parameters, regulatory traceability investigations, and contaminant cross-contact simulations. Each exercise validates backward trace (finished product → raw material) and forward trace (finished product → all customer shipments). Results are documented and used for continuous improvement.

### 6.3 Mock Recall Scoring

| Criterion | Max Score | Scoring Guidelines |
|-----------|-----------|--------------------|
| Backward trace completion time | 25 | ≤2 h = 25; 2–3 h = 20; 3–4 h = 15; >4 h = 0 |
| Forward trace completion time | 25 | ≤4 h = 25; 4–6 h = 20; 6–8 h = 15; >8 h = 0 |
| Data accuracy | 30 | 100% complete & accurate = 30; every error −5 |
| Report quality | 20 | Clear, complete, actionable = 20; gaps −5 each |
| **Total** | **100** | **Pass: ≥80** |

Hongji's average mock recall score for 2025 was **92/100**.

---

## 7. Food Fraud Vulnerability and Traceability

Under FSSC 22000 requirements, Hongji has assessed food fraud vulnerability across the supply chain. The following control measures link to the traceability system:

| Vulnerability | Risk Level | Traceability-based Control |
|---------------|------------|----------------------------|
| Variety substitution (e.g., cheaper variety sold as premium) | Medium | DNA fingerprint verification on incoming potatoes; variety code in lot number |
| Origin misrepresentation | Low | GPS coordinates recorded per field block; third-party origin verification |
| Adulteration with non-potato starch | Low | Starch purity analysis (microscopy + DSC) per lot |
| Re-packaged products with false labels | Medium | Tamper-evident packaging; QR-verified eCOA system |
| Counterfeit goods | Medium | Customer-accessible verification portal for COA QR codes |

---

## 8. Customer Traceability Support

### 8.1 Information Available Upon Request

| Information Type | Availability | Delivery Format |
|------------------|--------------|-----------------|
| Full traceability report for a specific lot | Within 4 hours request | PDF report |
| Raw material origin declaration | At order confirmation | Digital document |
| Processing line and equipment list | Upon request | Digital document |
| Field location GPS coordinates | Per contract agreement | GIS file (KML/SHP) |
| Seed potato origin certificate | Per contract agreement | PDF |

### 8.2 Customer Traceability Expectations

Hongji fully supports customer-specific traceability requirements, including:

- Audit of the traceability system during customer on-site visits
- Customized lot numbering schemes (if contractually agreed)
- Integration of customer's GTIN/GLN into Hongji's labeling
- API-based access to traceability data for large-volume customers
- Participation in customer's mock recall exercises

---

## 9. Continuous Improvement

The traceability system is subject to a formal annual review covering:

1. **System Performance:** Review of T1/T2 KPIs, labeling accuracy, and data completeness
2. **Regulatory Updates:** Changes in traceability regulations in major markets (China, EU, US, Japan)
3. **Technology Upgrades:** Evaluation of new technologies (blockchain, IoT sensors, RFID) for traceability enhancement
4. **Mock Recall Lessons Learned:** Incorporation of findings into system and procedure updates
5. **Customer Feedback:** Analysis of customer traceability audit results and special requirements

---

## 10. Conclusion

Hongji Agriculture's batch traceability system provides a robust, verified, and continuously improving mechanism for full-chain traceability from seed potato to shipped product. With a 4-hour backward trace capability, seamless ERP-MES-LIMS integration, and annual mock recall exercises scoring consistently above 90%, the system delivers the transparency, speed, and reliability demanded by global food manufacturers and regulatory authorities.

---

## 11. References

- ISO 22000:2018 — Food safety management systems — Requirements for any organization in the food chain
- FSSC 22000 Scheme Document Version 6.0 — Part II: Requirements for Certification
- EU Regulation 178/2002 — Laying down the general principles and requirements of food law
- China Food Safety Law (Revised 2021) — Article 42: Food safety traceability system
- GS1 General Specification — Application of GS1 barcode standards for supply chain traceability
- Codex Alimentarius CAC/GL 60-2006 — Principles for Traceability/Product Tracing as a Tool within a Food Inspection and Certification System

---

*End of Document*

## References

- ISO (International Organization for Standardization). Horizontal methods for food microbiology and physicochemical analysis.
- European Commission. Regulation (EC) No 1881/2006 — setting maximum levels for certain contaminants in foodstuffs.
- Codex Alimentarius. General Principles of Food Hygiene (CXC 1-1969) and commodity standards.
- FSSC 22000. Food Safety System Certification standard.
- Hongji Agriculture Technology Co., Ltd. 2026. "Batch Traceability System — Full-Chain from Seed to Ship." Hongji Agriculture Knowledge Center.


---

*This document is part of the Hongji Agriculture (弘基农业) Technical Documentation Series. For more information about our vertically integrated potato supply chain — from seed breeding and cultivation to processing and global export — visit our official B2B website: [https://hjpotatoflakes.com](https://hjpotatoflakes.com)*
