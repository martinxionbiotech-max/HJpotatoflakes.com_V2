---
description: "Physical Specifications: Particle Size, Bulk Density, and Color Measurement — Potato flake and powder quality control methods"
---

# Physical Specifications: Particle Size, Bulk Density, and Color Measurement

**Document Code:** HJ-QA-010  
**Version:** 3.0  
**Effective Date:** 2026-07-01  
**Prepared by:** Finished Product Laboratory, Hongji Agriculture Co., Ltd.

---

## 1. Introduction

Physical attributes — particle size distribution, bulk density, color, whiteness, and visible defect counts — are primary quality parameters for potato flakes and potato powder. These properties directly influence the customer's downstream process performance, including reconstitution behavior, mixing uniformity, flowability, packaging density, and final product appearance. Consistent physical specifications are the foundation of customer satisfaction and are maintained through rigorous, statistically monitored QC protocols.

This document defines the standard test methods, acceptance criteria, reporting protocols, and statistical process control procedures for all physical specification parameters across Hongji's product grades. All methods reference applicable international standards (ASTM, ISO, AACCI, CIE, GB) and are validated for the specific physical characteristics of dehydrated potato products.

---

## 2. Particle Size Distribution

Particle size distribution (PSD) governs the rehydration rate, mouthfeel in finished applications, and blending behavior in dry mixes. Two complementary methods are employed: mechanical sieve analysis for routine QC and laser diffraction for verification and fine powder characterization.

### 2.1 Sieve Analysis (Mechanical Screening)

The primary method for routine QC, following a modified ASTM E11 / ISO 3310-1 protocol.

**Equipment:**
- Vibratory sieve shaker (Retsch AS 200 control or equivalent)
- Certified test sieves (stainless steel, Ø200 mm full-height): 2000 μm (#10), 1400 μm (#14), 1000 μm (#18), 710 μm (#25), 500 μm (#35), 250 μm (#60), 125 μm (#120), and bottom pan
- Electronic balance (0.01 g resolution, calibrated daily)
- Sieve cleaning brush (brass wire, fine bristle)
- Anti-static spray (optional, for powders <250 μm)

**Sieve Specification per ASTM E11:**

| ASTM E11 Designation | ISO 3310-1 Designation | Nominal Opening (μm) | Typical Wire Diameter (mm) |
|----------------------|------------------------|----------------------|---------------------------|
| No. 10               | 2.00 mm                | 2000                 | 0.900                     |
| No. 14               | 1.40 mm                | 1400                 | 0.700                     |
| No. 18               | 1.00 mm                | 1000                 | 0.630                     |
| No. 25               | 710 μm                 | 710                  | 0.500                     |
| No. 35               | 500 μm                 | 500                  | 0.315                     |
| No. 60               | 250 μm                 | 250                  | 0.200                     |
| No. 120              | 125 μm                 | 125                  | 0.090                     |

**Procedure:**

1. **Sample preparation:** Weigh 100.0 ± 0.1 g of representative sample, equilibrated to room temperature (22 ± 2°C) in a sealed container for at least 30 minutes to avoid moisture gradient effects.
2. **Sieve stacking:** Stack sieves in descending mesh size order (2000 μm at top, pan at bottom). Verify that all sieves are clean, undamaged, and within their calibration validity period (12 months maximum).
3. **Loading:** Gently pour the sample onto the top sieve. Close with a lid.
4. **Sieving:** Run the sieve shaker for 10 minutes at amplitude 2.0 mm (or equivalent setting producing a consistent vertical oscillation of ~3 mm). For fine powders (D90 < 500 μm), add five 9.5 mm rubber cubes per sieve to break agglomerates.
5. **Weighing:** Carefully remove each sieve, brush loose particles from the underside, and weigh the retained mass on each sieve and the pan. Record to nearest 0.01 g.
6. **Mass balance check:** Confirm total recovered mass is 100 ± 2 g. If mass loss exceeds 2 g, the test is invalid and must be repeated.
7. **Calculation:**
   - Retained (%) per sieve = (Mass_retained / Total_mass) × 100
   - Cumulative passing (%) = 100 − Σ(retained % above current sieve)
   - D50, D90, D10 are interpolated from the cumulative passing curve using a log-linear plot

**Empty-Sieve Tare Procedure:**

All sieves are pre-weighed and recorded in LIMS before each test. After sieving, the sieve + retained material is weighed, and the empty-sieve tare is subtracted. This eliminates the need to physically empty each sieve for weighing, reducing analysis time and particle loss.

### 2.2 Laser Diffraction (Secondary / Verification Method)

Used for fine powder grades (particle D90 < 500 μm) and for method cross-validation when sieve analysis results are borderline or disputed.

**Equipment:**
- Malvern Mastersizer 3000 with Aero S (dry dispersion) or Hydro MV (wet dispersion), or equivalent (Sympatec HELOS, Beckman Coulter LS 13 320)
- Dispersant: Isopropanol (refractive index 1.39) for wet method; compressed air (2–4 bar) for dry method

**Measurement Parameters:**

| Parameter | Wet Dispersion (Fine Powders) | Dry Dispersion (Flakes) |
|-----------|------------------------------|------------------------|
| Particle RI | 1.53 | 1.53 |
| Dispersant RI | 1.39 (isopropanol) | 1.00 (air) |
| Obscuration | 10–20% | 0.5–5% |
| Stirrer speed | 2000 rpm | N/A |
| Dispersion pressure | N/A | 1.5 bar (adjustable) |
| Measurement time | 12 s (6 s background + 12 s measurement) | 5 s (per measurement, 3 replicates) |
| Analysis model | Mie theory (recommended for <100 μm) | Fraunhofer approximation (for >100 μm) |

**Validation Criteria:**

Laser diffraction results are considered equivalent to sieve analysis when the D50 values agree within ±8% (relative) for the same sample. If deviation exceeds 8%, an investigation into sample dispersion quality or instrument calibration is initiated.

### 2.3 Correlation Table: Particle Size vs. Functional Properties

Understanding the relationship between particle size and functional behavior allows Hongji to tailor PSD targets to specific customer applications.

| PSD Parameter | Functional Property | Correlation | Practical Consequence |
|---------------|---------------------|-------------|----------------------|
| D50 increase | Rehydration rate | ↓ (slower) | Coarser flakes require longer hydration times; may produce lumpier mash if not properly mixed |
| D50 decrease | Bulk density | ↑ (higher) | More fines pack tightly; benefits packaging efficiency but may cause clumping |
| Fines fraction (<125 μm) | Flowability (HR) | ↓ (worse) | Hausner ratio increases; bridging and rat-holing in hoppers becomes problematic when fines >15% |
| Coarse fraction (>2000 μm) | Dispersion uniformity | ↓ (worse) | Large flakes may not fully hydrate; visible undispersed particles in finished product |
| Span = (D90−D10)/D50 | Texture consistency | ↓ (narrower span = more uniform texture) | Wide span produces heterogeneous mash (some areas pasty, some still dry) |
| D90 increase | Dispersion time | ↑ (longer) | Larger maximum particles require extended mixing or higher shear to fully incorporate |

### 2.4 Product Grade PSD Limits

| Product Grade | Application | D10 (μm) | D50 (μm) | D90 (μm) | Max Retained 2000 μm (%) | Max Pass 125 μm (%) | Target Span |
|---------------|-------------|-----------|----------|-----------|--------------------------|---------------------|-------------|
| Flakes — Standard | Mashed potato, bakery, snacks | 300–500 | 700–1200 | ≤2000 | ≤3.0 | ≤8.0 | 1.5–2.5 |
| Flakes — Fine | Instant mixes, soups | 200–400 | 500–900 | ≤1400 | ≤1.0 | ≤12.0 | 1.2–2.0 |
| Flakes — Coarse | Coatings, breadings | 500–800 | 1000–1600 | ≤2500 | ≤5.0 | ≤3.0 | 1.5–2.8 |
| Powder — Standard | Thickening, blending | 100–200 | 250–500 | ≤800 | ≤0.5 | ≤15.0 | 1.0–2.0 |
| Powder — Fine | Beverage, infant food | 50–100 | 150–300 | ≤500 | 0 | ≤25.0 | 0.8–1.5 |

---

## 3. Bulk Density

Bulk density affects packaging efficiency, transport costs, volumetric dosing behavior in customer production lines, and the sensory experience of reconstitution. Both loose and tapped bulk density are routinely measured, and the derived Hausner ratio and Carr index provide quantitative flowability assessment.

### 3.1 Loose Bulk Density (Apparent Density)

**Method:** Modified ASTM D1895 / ISO 60

**Equipment:**
- 100 ± 1 mL graduated glass cylinder (tarred)
- Funnel with 10 mm internal diameter outlet
- Funnel stand with adjustable height

**Procedure:**

1. Ensure the graduated cylinder is clean, dry, and at room temperature. Tare on the analytical balance.
2. Mount the funnel on the stand such that its outlet is positioned 25 ± 2 mm above the top rim of the graduated cylinder.
3. Close the funnel outlet temporarily (with a finger or stopper) and fill the funnel with sufficient sample (approximately 120 mL).
4. Open the funnel outlet and allow the sample to flow freely into the cylinder. Do not tap, vibrate, or shake the cylinder during filling.
5. Once filled, level the top surface of the powder by gently scraping a straight-edge across the rim from the center outward in one smooth motion. Do not compact.
6. Weigh the filled cylinder on the analytical balance. Record mass to nearest 0.01 g.
7. **Calculation:** Loose Bulk Density (g/mL) = Sample Mass (g) / 100 mL
8. Report to three significant figures (e.g., 0.475 g/mL).

### 3.2 Tapped Bulk Density

**Method:** ASTM B527 (Standard Test Method for Tap Density of Metal Powders and Compounds) — adapted for food powders

**Equipment:**
- Tap density tester (Quantachrome Autotap, Hosokawa Micron Powder Tester, or equivalent)
- Same sample and 100 mL graduated cylinder from the loose density test (do not empty or repack)

**Standard Procedure:**

1. Mount the graduated cylinder (still containing the loose-density sample) on the tapping apparatus.
2. Set the apparatus to deliver a drop height of 3.0 ± 0.2 mm at a frequency of 250 ± 15 taps per minute.
3. Tap the sample 500 taps initially. Read and record the volume.
4. Continue tapping in increments of 125 taps until the volume change between successive increments is less than 2 mL (or 2% of the current volume, whichever is smaller).
5. Record the final stable volume (V_final).
6. **Calculation:** Tapped Bulk Density (g/mL) = Sample Mass (g) / V_final

**Typical tap count for Hongji products:**

| Product Type | Taps Required to Stability |
|--------------|---------------------------|
| Flakes — Standard | 500–1000 |
| Flakes — Fine | 1000–1250 |
| Flakes — Coarse | 500–750 |
| Powder — Standard | 1000–1500 |
| Powder — Fine | 1250–2000 |

### 3.3 Hausner Ratio and Carr Index

These derived indices provide a standardized assessment of powder flowability and compressibility.

| Metric | Formula | Significance | Typical Range (Flakes) | Typical Range (Powder) |
|--------|---------|--------------|------------------------|------------------------|
| **Hausner Ratio (HR)** | Tapped BD / Loose BD | Flowability: HR <1.25 = excellent/good; 1.25–1.40 = fair; >1.40 = poor (cohesive, poor flow) | 1.12–1.25 | 1.15–1.28 |
| **Carr Index (CI)** | (Tapped BD − Loose BD) / Tapped BD × 100 | Compressibility: CI <10 = excellent; 10–15 = good; 16–20 = fair; 21–25 = passable; >25 = very poor | 10–18% | 12–20% |

### 3.4 Bulk Density Limits by Product Grade

| Product Grade | Loose BD (g/mL) | Tapped BD (g/mL) | Hausner Ratio (max) | Carr Index (max %) | Typical Application |
|---------------|-----------------|------------------|---------------------|-------------------|---------------------|
| Flakes — Standard | 0.40–0.55 | 0.50–0.65 | ≤1.25 | ≤20 | Gravity-fed blending lines |
| Flakes — Fine | 0.45–0.60 | 0.55–0.70 | ≤1.25 | ≤20 | Auger-fed packaging; instant mixes |
| Flakes — Coarse | 0.35–0.50 | 0.45–0.60 | ≤1.30 | ≤23 | Hand-scoop; breading line |
| Powder — Standard | 0.55–0.70 | 0.70–0.85 | ≤1.20 | ≤18 | Pneumatic conveying; hoppers |
| Powder — Fine | 0.50–0.65 | 0.65–0.80 | ≤1.25 | ≤20 | High-speed packaging; VFFS machines |

---

## 4. Color Measurement (L\*a\*b\*)

Color consistency is critical for customer product appearance, particularly in mashed potato, snack seasoning, and bakery applications where visual uniformity is expected batch-to-batch.

### 4.1 Instrument and Method

| Parameter | Specification |
|-----------|---------------|
| Instrument | Konica Minolta CR-400 / CM-5 or HunterLab ColorFlex EZ (or equivalent, with calibration certificate valid within 12 months) |
| Illuminant | D65 (daylight, 6500K) |
| Observer Angle | 10° (standard observer) |
| Aperture | 30 mm (standard), 8 mm (small area for fine powders) |
| Calibration | White calibration tile (supplied with instrument); zero-calibration with light trap; perform before each measurement session and after every 60 minutes of continuous use |
| Sample Preparation | Fill sample cup (50 mm Ø, 20 mm minimum depth) with uniform, non-compacted sample. Gently level surface. Measure at 3 different locations on the cup with ~120° rotation between measurements. Report the arithmetic mean. For fine powders, also measure a second cup preparation to verify repeatability |
| Color Space | CIELAB (L\*, a\*, b\*) — CIE Publication 15:2018 |

**HunterLab vs. Konica Minolta Cross-Calibration:**

When different instruments are used across production sites, a cross-calibration exercise is performed quarterly using five reference powder samples spanning the expected L\*, a\*, b\* range. Linear correction factors are calculated:

- L*_corrected = a₁ × L*_measured + a₀
- a*_corrected = b₁ × a*_measured + b₀
- b*_corrected = c₁ × b*_measured + c₀

The correction coefficients are stored in LIMS and applied automatically to all QC color results.

### 4.2 Interpretation of Values

| Parameter | Range (Potato Flakes/Powder) | Interpretation |
|-----------|------------------------------|----------------|
| **L\*** (Lightness) | 85–95 (typical) | Higher = whiter/brighter; raw material and processing conditions (blanching, sulfite level) affect L\* |
| **a\*** (Red-Green) | −3.0 to +1.5 | Negative = greenish tinge (under-blanched); positive = browning (excess heat/Maillard reaction) |
| **b\*** (Yellow-Blue) | 10.0–25.0 (typical) | Higher = more yellow; affected by tuber carotenoid content and heat exposure |

**Effect of Processing Parameters on Color:**

| Processing Step | Effect on L* | Effect on a* | Effect on b* |
|----------------|--------------|--------------|--------------|
| Blanching (adequate) | ↑ (+2–5) | ↓ (more negative, −0.5 to −1.0) | No significant change |
| Sulfite addition (400 ppm) | ↑ (+3–8) | ↓ (−0.5 to −1.5) | ↓ (−1 to −3) |
| Over-blanching | ↓ (−3–8) | ↑ (+1.0–2.5) | ↑ (+2–5) |
| High drying temperature (>150°C) | ↓ (−5–12) | ↑ (+1.5–4.0) | ↑ (+3–8) |
| Extended storage (>12 months) | ↓ (−2–5) | ↑ (+0.5–2.0) | ↑ (+1–3) |

### 4.3 Acceptance Limits

| Grade | L\* (min) | a\* (range) | b\* (max) | ΔE (batch-to-batch, max) |
|-------|-----------|-------------|-----------|--------------------------|
| Premium (Food Service / Retail) | ≥90.0 | −2.0 to +1.0 | ≤18.0 | ≤2.0 |
| Standard (Industrial) | ≥87.0 | −2.5 to +1.5 | ≤22.0 | ≤3.0 |
| Economy / Second Grade | ≥83.0 | −3.0 to +2.0 | ≤25.0 | ≤4.0 |

Where ΔE (total color difference) is calculated as:

$$\Delta E = \sqrt{(\Delta L^*)^2 + (\Delta a^*)^2 + (\Delta b^*)^2}$$

The reference standard (L*₀, a*₀, b*₀) is established annually by averaging the results of the top 25% of production lots from the previous calendar year, stratified by grade. This dynamic baseline ensures that color targets evolve with raw material and process improvements.

### 4.4 Whiteness Measurement — Ganz Whiteness Index (W_G)

For applications where visual whiteness is a specific customer requirement (beverage powders, white sauces), the Ganz whiteness index (W_G) is reported alongside L\*a\*b\*.

**Instrument:** Same as L\*a\*b\* measurement (Konica Minolta CM-5 or HunterLab ColorFlex EZ)

**Formula (Ganz whiteness index for D65/10°):**

$$W_G = Y + 800(x_n - x) + 1700(y_n - y)$$

Where:
- Y = CIE tristimulus Y value (luminance factor, 0–100)
- x, y = CIE chromaticity coordinates of the sample
- x_n, y_n = Chromaticity coordinates of the perfect diffuser for D65/10° (x_n = 0.3138, y_n = 0.3310)

**Alternative — CIE Whiteness Index (W_CIE):**

Some customers specify the CIE whiteness index instead:

$$W_{CIE} = Y + 800(0.3138 - x) + 1700(0.3310 - y)$$

The two indices give numerically equivalent results for potato flakes. Hongji reports W_G (Ganz) by default, but converts to W_CIE upon customer request using the formula:

$$W_{CIE} = W_G \quad \text{(identical for D65/10°)}$$

**Acceptance Limits:**

| Product Grade | W_G (min) | Typical Range |
|---------------|-----------|---------------|
| Premium | ≥82.0 | 82–90 |
| Standard | ≥78.0 | 78–85 |
| Economy | ≥73.0 | 73–82 |

---

## 5. Black Spec / Dark Particle Count

Visible black specks and dark particles originating from potato eyes, soil residues, burnt processing deposits, or metallic debris are a common quality complaint in the global potato flake trade.

### 5.1 Manual Detection Method

| Parameter | Specification |
|-----------|---------------|
| Method | Modified AACCI 45-40.01 (Visual Examination for Foreign Material) |
| Sample Size | 250 ± 5 g |
| Instrument | Light box (fluorescent tubes, 3600 lux minimum at work surface, 45° incident angle from two sides) |
| Background | Black matte tray (non-reflective, 400 × 300 mm, with raised edges) |
| Procedure | Spread sample in thin uniform layer (5–8 mm depth); systematically scan the entire tray surface using tweezers or forceps to pick out all visually detectable dark particles (>200 μm contrast threshold); count and weigh |
| Reporting | Dark particles per 250 g (count), or mg/kg (mass basis) |

**Operator Qualification:**

Operators performing manual black spec counting must pass annual visual acuity certification (Ishihara color vision test, minimum 12/14 plates correctly identified) and demonstrate <20% inter-operator variability on a reference sample set containing known levels of dark specks.

### 5.2 Automated Image Analysis (Secondary Method)

An automated vision system (Eigenmann & Veronelli SORTEX or CAMSIZER XT) is used for high-volume screening:

| Parameter | Setting |
|-----------|---------|
| Detection Threshold | Gray level ≤ 70 (0 = black, 255 = white), adjustable per product grade |
| Minimum Detectable Size | 200 μm (configurable to 100 μm for premium grade) |
| Sample Feed | Vibrating trough at 50 g/min |
| Illumination | LED backlight and top-light (diffuse) |
| Output | Count per size category: <500 μm, 500–1000 μm, >1000 μm; also reports mass-equivalent and mg/kg |

**Correlation with Manual Method:**

The automated method is calibrated against manual counts weekly. A correction factor (f_auto = manual_count / auto_count) is maintained. If f_auto drifts outside 0.7–1.3, the instrument is recalibrated.

### 5.3 Acceptance Limits

| Grade | Manual Count (per 250 g) | Automated Count (particles/g) | Mass Limit (mg/kg, max) |
|-------|--------------------------|-------------------------------|-------------------------|
| Premium | ≤5 | ≤0.5 | ≤20 |
| Standard | ≤15 | ≤1.5 | ≤50 |
| Economy | ≤30 | ≤3.0 | ≤100 |

---

## 6. Statistical Process Control (SPC) for Physical Parameters

Hongji uses real-time SPC to monitor physical parameter stability and detect drift before it produces out-of-spec product.

### 6.1 SPC Chart Types

| Parameter | Chart Type | Subgroup Size | Sampling Frequency | Control Limits |
|-----------|------------|---------------|-------------------|----------------|
| D50 (PSD) | X̄-R (mean and range) | n = 4 (consecutive bags) | Every 2 hours | Mean ± 3σ (calculated from ≥25 subgroups) |
| Loose BD | X̄-R | n = 4 | Every 4 hours | Mean ± 3σ |
| L\* (Color) | X̄-R | n = 3 (3 locations per sample) | Every 2 hours | Mean ± 3σ |
| Dark particle count | c-chart (count per sample) | n = 1 (250 g) | Every 2 hours | c̄ ± 3√c̄ |

### 6.2 Process Capability (Cp, Cpk)

Hongji targets the following minimum process capability indices for all physical parameters:

| Parameter | Target Cp | Target Cpk | Action if Cpk < 1.33 |
|-----------|-----------|------------|----------------------|
| D50 | ≥1.67 | ≥1.50 | Process improvement investigation |
| Bulk Density (Loose) | ≥1.50 | ≥1.33 | Adjust drying/cooling parameters |
| L\* (Lightness) | ≥1.50 | ≥1.33 | Review blanching/sulfite dosage |
| Dark Particles | ≥1.33 | ≥1.33 | Review raw material grading or cleaning efficiency |

### 6.3 Out-of-Control Action Plan (OCAP)

When a data point falls outside the control limits (±3σ):

1. **Immediate:** QC Technician flags the result in LIMS and notifies the production shift supervisor.
2. **Short-stop:** Production is advised to hold output from the affected line for 1 hour (or until 3 consecutive in-control subgroups are confirmed).
3. **Investigation:** Shift supervisor and QC lead investigate root cause using the Ishikawa (fishbone) diagram structured around:
   - Raw material (tuber variety, storage age, dry matter content)
   - Machine (drum speed, steam pressure, knife wear)
   - Method (sampling technique, sieve calibration)
   - Manpower (operator technique, training level)
   - Measurement (instrument drift, environmental conditions)
4. **Resolution:** Document findings in LIMS and release production once process returns to control.

---

## 7. Sampling Frequency

| Parameter | Sampling Point | Frequency |
|-----------|----------------|-----------|
| PSD (Sieve) | Final product packaging line | Every 2 hours per line |
| PSD (Laser) | Laboratory verification | 1× per shift (composite from 4 two-hourly samples) |
| Bulk Density (Loose & Tapped) | Final product packaging line | Every 4 hours per line |
| L\*a\*b\* Color | Final product packaging line | Every 2 hours per line |
| Whiteness (W_G) | Final product packaging line | 1× per shift |
| Black Spec (Manual) | Final product packaging line | Every bag in 1:20 ratio; composite per 2-hour period |
| Black Spec (Automated) | Laboratory (reserve samples) | 1× per 10 MT production |
| SPC Chart Update | LIMS auto-generates | After each measurement entry |

---

## 8. Industry Reference Standards — Cross-Reference Table

| Parameter | Hongji Method Reference | ASTM | ISO | AOAC / AACCI | GB (China) |
|-----------|------------------------|------|-----|--------------|------------|
| Sieve Analysis | HJ-QA-010-SOP-01 | ASTM E11 (sieve spec) | ISO 3310-1 | — | GB/T 6003.1 |
| Loose Bulk Density | HJ-QA-010-SOP-02 | ASTM D1895 | ISO 60 | — | GB/T 1636 |
| Tapped Bulk Density | HJ-QA-010-SOP-03 | ASTM B527 | ISO 3953 | — | GB/T 5162 |
| Color (L\*a\*b\*) | HJ-QA-010-SOP-04 | ASTM D2244 | ISO 11664-4 | — | GB/T 3977 |
| Whiteness Index | HJ-QA-010-SOP-05 | ASTM E313 | ISO 11475 | — | GB/T 2913 |
| Dark Particle Count | HJ-QA-010-SOP-06 | — | — | AACCI 45-40.01 | — |

---

## 9. Reporting

All physical test results are recorded in the Laboratory Information Management System (LIMS) and populate the Certificate of Analysis (COA). Results must fall within the specified grade limits. Out-of-specification (OOS) results trigger the procedure defined in Section 10.

The standard COA for physical parameters includes:
- D10, D50, D90 (μm) and span
- Cumulative sieve retained percentages
- Loose bulk density (g/mL)
- Tapped bulk density (g/mL)
- Hausner ratio
- L\*, a\*, b\*, ΔE (vs. reference)
- Ganz whiteness index (W_G)
- Dark particle count (per 250 g and mg/kg)
- Grade conformance statement

---

## 10. Out-of-Specification (OOS) Procedure

1. **Immediate Notification:** QC Technician notifies the Shift Supervisor and Finished Product QA Manager within 15 minutes of confirmed OOS.
2. **Holding Action:** The affected lot is placed on hold pending investigation (flagged in LIMS as "QA HOLD").
3. **Root Cause Analysis:** QA investigates possible causes (raw material change, process drift, equipment malfunction, sieve tear).
4. **Re-Testing:** A 2× sample (duplicate from same lot and a fresh composite from retained samples) is tested.
5. **Disposition Options:**
   - Regression test passes → release with note.
   - Falls within 2nd grade spec → downgrade with customer notification if required.
   - Fails all grades → rework (re-screening, blending with compliant material) or discard.
6. **CAPA:** For recurring OOS events (≥3 instances of the same parameter within 30 days), a formal Corrective and Preventive Action (CAPA) is opened per HJ-QA-9001 procedure.

---

## 11. References

- ASTM E11: Standard Specification for Woven Wire Test Sieve Cloth and Test Sieves
- ASTM D1895: Standard Test Methods for Apparent Density, Bulk Factor, and Pourability of Plastic Materials
- ASTM B527: Standard Test Method for Tap Density of Metal Powders and Compounds
- ASTM D2244: Standard Practice for Calculation of Color Tolerances and Color Differences from Instrumentally Measured Color Coordinates
- ASTM E313: Standard Practice for Calculating Yellowness and Whiteness Indices from Instrumentally Measured Color Coordinates
- ISO 60: Plastics — Determination of apparent density of material that can be poured from a specified funnel
- ISO 3310-1: Test sieves — Technical requirements and testing — Part 1: Test sieves of metal wire cloth
- ISO 3953: Metallic powders — Determination of tap density
- ISO 11664-4: Colorimetry — Part 4: CIE 1976 L\*a\*b\* colour space
- ISO 11475: Paper and board — Determination of CIE whiteness, D65/10° (outdoor daylight)
- AACCI 45-40.01: Visual Examination for Foreign Material
- CIE Publication 15:2018: Colorimetry, 4th Edition
- GB/T 6003.1: Test sieves — Technical requirements and testing — Part 1: Test sieves of metal wire cloth
- GB/T 3977: Specification of colors
- GB/T 5162: Metallic powders — Determination of tap density
- GB/T 5527-2010: Inspection of grain and oils — Determination of color of grain and oil

---

*End of Document*

## References

- ISO (International Organization for Standardization). Horizontal methods for food microbiology and physicochemical analysis.
- ASTM International. Standard test methods for particle size and bulk density.
- Hongji Agriculture Technology Co., Ltd. 2026. "Physical Specifications: Particle Size, Bulk Density, and Color Measurement." Hongji Agriculture Knowledge Center.


---

*This document is part of the Hongji Agriculture (弘基农业) Technical Documentation Series. For more information about our vertically integrated potato supply chain — from seed breeding and cultivation to processing and global export — visit our official B2B website: [https://hjpotatoflakes.com](https://hjpotatoflakes.com)*
