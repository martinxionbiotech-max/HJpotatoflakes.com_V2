---
description: "Chemical Analysis: Dry Matter, Starch, and Sugars — Potato flake and powder quality control methods — physical, chemical, and microbiological testing, rehydration performance evaluation, COA interpretation, and batch traceability."
---

# Chemical Analysis: Dry Matter, Starch, and Sugars

**Document Code:** HJ-QA-015  
**Version:** 3.0  
**Effective Date:** 2026-07-01  
**Prepared by:** Chemical Laboratory, Hongji Agriculture Co., Ltd.

---

## 1. Introduction

The chemical composition of potato flakes and potato powder directly determines functional performance in the customer's application — texture, water absorption, browning behavior, and nutritional value. Accurate and reproducible chemical analysis is essential for process control, product specification compliance, regulatory adherence, and customer confidence.

This document describes the standardized analytical methods employed at Hongji's chemical laboratory for the determination of dry matter, starch, reducing sugars, sucrose, protein, ash, crude fat, crude fiber, and sulfite residues. All methods are validated against international reference methods (AOAC, ISO, AACC, GB) and participate in quarterly inter-laboratory proficiency testing programs (FAPAS / BIPEA). Method performance parameters (repeatability, reproducibility, LOD, LOQ) are provided for each key analyte.

---

## 2. Dry Matter Content

Dry matter (DM) content is the single most important compositional parameter in the potato flake industry. It determines yield efficiency in processing and the water-binding capacity of the final product. In the raw tuber, DM ranges from 18–26% (fresh weight); after dehydration, target DM in flakes is 92–94%.

### 2.1 Reference Method — Air Oven Drying (AOAC 934.06)

| Parameter | Specification |
|-----------|---------------|
| **AOAC Reference** | AOAC Official Method 934.06 (Moisture in Dried Fruits) — adapted for potato flakes |
| **Apparatus** | Forced-air oven (Memmert UF-110 or equivalent), ±1.0°C temperature accuracy, calibrated quarterly |
| **Sample Weight** | 5.0 ± 0.1 g (ground to pass 1 mm sieve if particle D50 >2 mm) |
| **Container** | Aluminum weighing dish with tight-fitting lid, pre-dried (103°C, 2 h) and tared |
| **Drying Temperature** | 103 ± 2°C |
| **Drying Time** | 16–18 hours (overnight) or to constant weight (±0.003 g change after an additional 2 h drying) |
| **Cooling** | Desiccator with active silica gel or molecular sieve desiccant, minimum 30 min cooling |
| **Weighing** | Analytical balance (0.0001 g resolution); weigh immediately after cooling to avoid moisture re-adsorption |

**Calculation:**

$$Dry\ Matter\ (\%) = \frac{m_{after\_drying}}{m_{initial}} \times 100$$

$$Moisture\ (\%) = 100 - Dry\ Matter\ (\%)$$

**Correction Factor for High-Fat Samples:**

If crude fat content exceeds 3% DM (not typical for potato products but relevant for specialty formulations), a correction factor is applied to account for volatile fat oxidation products lost during drying:

$$DM_{corrected} = DM_{measured} + 0.15 \times Fat\ (\%\ DM)$$

### 2.2 Rapid Method — Halogen Moisture Analyzer (Production QC)

For in-process control and rapid release decisions, Hongji uses a halogen moisture analyzer (Mettler Toledo HB43-S or Sartorius MA37).

| Parameter | Specification |
|-----------|---------------|
| Sample Weight | 3.0 ± 0.5 g |
| Drying Temperature | 105°C (standard program), 130°C (fast program for in-process samples only) |
| Drying Endpoint | Automatic — weight change <1 mg per 30 seconds |
| Typical Duration | 8–12 minutes (standard); 4–6 minutes (fast) |
| Correlation Check | Calibrated against reference oven method weekly; r² ≥ 0.995; max allowed bias ±0.2% absolute |

**Calibration Protocol:**

1. Each Monday, run 5 representative samples on both the halogen analyzer and the reference oven method.
2. Perform linear regression: DM_oven = a × DM_halogen + b
3. If slope (a) deviates from 1.000 by more than ±0.02, or intercept (b) exceeds ±0.3, the halogen analyzer is serviced and recalibrated.
4. Store the current calibration coefficients in LIMS and apply automatically.

### 2.3 Near-Infrared (NIR) Rapid Analysis Method

For high-throughput screening of incoming raw tubers and intermediate process streams, Hongji employs a Fourier-Transform NIR analyzer (Bruker Matrix-F or FOSS DS2500).

| Parameter | Specification |
|-----------|---------------|
| **Instrument** | FOSS DS2500 (reflectance mode) or Bruker Matrix-F |
| **Wavelength Range** | 1100–2500 nm (full spectrum) |
| **Spectral Resolution** | 2 nm |
| **Sample Presentation** | Rotating cup (50 mm diameter), filled uniformly to 15 mm depth |
| **Measurement Time** | 30 seconds per sample |
| **Calibration Model** | PLS (Partial Least Squares) regression, 100+ calibration samples |
| **Calibration Update** | Every 6 months, with min. 20 validation samples |

**NIR Calibration Performance for Key Parameters:**

| Parameter | R² (Calibration) | R² (Cross-Validation) | RMSEP (Root Mean Square Error of Prediction) | SEC (Standard Error of Calibration) |
|-----------|------------------|----------------------|---------------------------------------------|-------------------------------------|
| Dry Matter (%) | 0.992 | 0.985 | ±0.35% | ±0.25% |
| Total Starch (% DM) | 0.978 | 0.965 | ±1.2% | ±0.9% |
| Reducing Sugars (% DM) | 0.961 | 0.948 | ±0.15% | ±0.10% |
| Protein (% DM) | 0.985 | 0.975 | ±0.25% | ±0.18% |

**Validation Protocol per ASTM E1655:**

1. Collect NIR spectra and reference (wet chemistry) values for a minimum of 20 validation samples quarterly.
2. Calculate bias = mean(reference − NIR). Bias must be ≤ ±0.3% for dry matter.
3. Calculate SEP (Standard Error of Prediction) = √(Σ(reference − NIR)² / (n−1)). SEP must be ≤ 0.5% for dry matter.
4. If bias or SEP exceeds limits, the model is recalibrated with expanded sample sets.

### 2.4 Dry Matter Calculation Formula with Correction Factors

$$DM_{report} = DM_{measured} \times F_{hygroscopic} \times F_{volatiles}$$

Where:
- **F_hygroscopic** = Correction for moisture re-adsorption during cooling. Standard factor = 1.000 (with desiccator in good condition). If desiccator silica gel is >50% saturated (color change indicators on blue gel), F = 1.002 to compensate.
- **F_volatiles** = Correction for volatile organic compounds lost during drying. Standard factor = 1.000 for potato flakes. For samples with added volatile flavorings, F = 1.005–1.015 depending on formulation.

### 2.5 Acceptance Limits

| Product Type | Moisture (%) | Dry Matter (%) | Test Method for Release |
|--------------|--------------|----------------|------------------------|
| Potato Flakes (Standard) | 6.0–8.0 | 92.0–94.0 | Halogen (verified by oven weekly) |
| Potato Flakes (Fine) | 5.5–7.5 | 92.5–94.5 | Halogen (verified by oven weekly) |
| Potato Powder (Standard) | 6.5–8.5 | 91.5–93.5 | Halogen (verified by oven weekly) |
| Potato Powder (Fine) | 6.0–8.0 | 92.0–94.0 | Halogen (verified by oven weekly) |
| Raw Potato Tubers | 74–82% | 18–26% | NIR (rapid) — verified by oven daily |

*Note: Contractual moisture specifications may be tighter per customer requirements.*

---

## 3. Starch Content

Starch is the dominant component of potato dry matter (typically 70–80% of DM in flakes). The starch content, gelatinization degree, amylose/amylopectin ratio, and level of starch damage all control the rehydration characteristics and final product texture.

### 3.1 Method — Ewers Polarimetric Method (ISO 10520 / EU 2009/90/EC)

| Parameter | Specification |
|-----------|---------------|
| **Reference** | ISO 10520: Determination of starch content — Ewers polarimetric method |
| **Principle** | Acid hydrolysis of starch to soluble sugars followed by polarimetric measurement of optical rotation |
| **Sample Weight** | 2.50 ± 0.01 g (ground to <500 μm) |
| **Hydrolysis** | 30 min at boiling with 25 mL 1.128 M HCl (density 1.0189 g/mL at 25°C) |
| **Filtration** | Through fluted filter paper (Whatman No. 4); discard first 10 mL of filtrate; ensure filtrate is completely clear |
| **Clarification** | If filtrate is colored or turbid, add 1–2 mL of Carrez I (K₄[Fe(CN)₆]·3H₂O, 150 g/L) and Carrez II (ZnSO₄·7H₂O, 300 g/L) solution, filter again |
| **Polarimeter Reading** | Saccharimeter or polarimeter with sodium D-line (λ = 589 nm); 200 mm tube; constant temperature at 20.0 ± 0.5°C |
| **Reference Rotation** | [α]D for potato starch in 1.128 M HCl = +185.2° (at 20°C) |

**Calculation:**

$$Starch\ (\%) = \frac{\alpha \times 2000}{[\alpha]_D \times L \times m}$$

Where:
- α = polarimeter reading (angular degrees)
- [α]D = specific rotation of potato starch in HCl = +185.2°
- L = tube length (200 mm = 2.0 dm)
- m = sample mass (g)
- 2000 = combined factor for dilution and conversion

**Interference Correction:**

If sucrose content exceeds 2% of sample, a separate sucrose determination must be performed and the result subtracted from the apparent starch content:

$$Starch\ (corrected)\ (\%) = Starch\ (apparent) - Sucrose \times 0.9$$

### 3.2 Starch Gelatinization Degree (DG)

The degree of starch gelatinization (DG) is a critical quality attribute for instant potato flakes, directly correlating with rehydration performance.

| Parameter | Specification |
|-----------|---------------|
| **Method** | Enzymatic / amyloglucosidase method (modified AACC 76-13) |
| **Principle** | Amyloglucosidase (AMG) selectively hydrolyzes gelatinized starch to glucose. Measure glucose released before and after complete cooking of the same sample. The ratio gives DG |
| **Enzyme** | Amyloglucosidase from *Aspergillus niger* (Megazyme E-AMGDF or equivalent), ≥300 U/mL |
| **Buffer** | Sodium acetate buffer, 100 mM, pH 4.5 |
| **Glucose Assay** | Glucose oxidase/peroxidase (GOD-POD) reagent, measured at 510 nm |

**Procedure:**

1. **Raw (uncooked) digest:** 100 mg sample + 5 mL buffer + 0.1 mL AMG → 40°C, 20 min. Stop with 10 mL ethanol. Centrifuge. Measure glucose in supernatant.
2. **Total (cooked) digest:** 100 mg sample + 5 mL buffer → boil 30 min → cool → add 0.1 mL AMG → 40°C, 20 min. Stop with 10 mL ethanol. Centrifuge. Measure glucose in supernatant.

**Calculation:**

$$DG\ (\%) = \frac{Glucose\ (raw\ digest)}{Glucose\ (cooked\ digest)} \times 100$$

**Acceptable Range:**

| Product Grade | DG Target (%) | Action if Outside Range |
|---------------|---------------|------------------------|
| Premium Flakes | 88–93 | Adjust blanching time ±30 s |
| Standard Flakes | 85–92 | Adjust drum speed ±0.5 RPM |
| Economy Flakes | 82–90 | Acceptable; review if <80% |
| Powder | 80–88 | Adjust milling intensity |

### 3.3 Starch Damage Measurement (AACC 76-31)

Mechanical starch damage during milling and sieving affects water absorption and can cause undesirable stickiness.

| Parameter | Specification |
|-----------|---------------|
| **Reference** | AACC Approved Method 76-31 (Spectrophotometric Method) |
| **Principle** | Damaged starch granules are more susceptible to enzymatic hydrolysis by α-amylase. The glucose released is measured colorimetrically |
| **Enzyme** | α-Amylase from *Bacillus subtilis* (Megazyme or equivalent) |
| **Reagent** | Glucose oxidase/peroxidase (GOD-POD) |
| **Calculation** | Starch damage (%) = Glucose (mg) × 0.9 / Sample mass (mg) × 100 |

**Interpretation:**

| Starch Damage (%) | Category | Effect on Rehydration | Action |
|-------------------|----------|----------------------|--------|
| <3 | Low | Clean texture; normal water absorption | No action needed |
| 3–5 | Acceptable | Slightly faster hydration but still good texture | No action needed |
| 5–8 | Moderate | Noticeably faster hydration; slightly sticky | Reduce milling speed or increase sieve aperture |
| >8 | High | Pasty texture; excessive stickiness; high WSI | Immediate investigation and corrective action |

### 3.4 Amylose / Amylopectin Ratio (ISO 6647)

The ratio influences gel strength, retrogradation tendency, and freeze-thaw stability.

| Parameter | Specification |
|-----------|---------------|
| **Reference** | ISO 6647: Rice — Determination of amylose content (adapted for potato) |
| **Principle** | Amylose-iodine complex measured at 620 nm |
| **Defatting** | Remove lipids by Soxhlet extraction with 85% methanol for 4 h before analysis |
| **Standard Curve** | Purified potato amylose (Sigma A-0512), 0–100 μg/mL in 0.5% acetic acid |
| **Measurement** | UV-Vis at 620 nm after 20 min color development |

**Variety-Specific Typical Values:**

| Variety | Typical Amylose Content (%) | Amylopectin (%) | Suitability for Drying |
|---------|---------------------------|-----------------|----------------------|
| Atlantic | 21–24 | 76–79 | Good gel firmness; moderate retrogradation |
| Shepody | 22–25 | 75–78 | Excellent flake texture; moderate retrogradation |
| Russet Burbank | 23–26 | 74–77 | High dry matter; preferred for industrial dehydration |
| Innovator | 20–23 | 77–80 | Lower amylose → slower retrogradation → better shelf life |
| Agria | 22–25 | 75–78 | Balanced; widely used in European processing |

**Effect on Processing:**

| Amylose Content | Retrogradation Rate | Gel Strength | Freeze-Thaw Stability | Best Use |
|-----------------|-------------------|--------------|----------------------|----------|
| 20–22% (low) | Slow | Weak | Excellent | Frozen products, soups |
| 22–24% (medium) | Moderate | Moderate | Good | Standard table mash |
| 24–27% (high) | Rapid | Strong | Poor | Coatings, breadings |

### 3.5 Acceptance Limits — Starch Parameters

| Parameter | Flakes (Standard) | Flakes (Fine) | Powder | Test Method |
|-----------|-------------------|---------------|--------|-------------|
| Total Starch (% DM) | 70.0–80.0 | 72.0–82.0 | 68.0–78.0 | ISO 10520 (Ewers) |
| Gelatinization Degree (%) | 85–95 | 85–95 | 80–90 | Enzymatic (AACC 76-13 mod.) |
| Starch Damage (%) | ≤5.0 | ≤5.0 | ≤8.0 | AACC 76-31 |
| Amylose (% of starch) | 22–26 | 22–26 | 22–26 | ISO 6647 |

---

## 4. Reducing Sugar Content

Reducing sugars (primarily glucose and fructose) are the primary drivers of Maillard browning during hot preparation and influence the color stability of the finished product. Tight control of reducing sugars is essential for maintaining the light color (high L*) that premium customers expect.

### 4.1 Primary Method — DNS (3,5-Dinitrosalicylic Acid) Colorimetric Method

| Parameter | Specification |
|-----------|---------------|
| **Principle** | DNS reacts with reducing sugars in alkaline medium to form 3-amino-5-nitrosalicylic acid (orange-red complex), measured at 540 nm |
| **AOAC Equivalence** | Similar in principle to AOAC 977.20 (Malt Beverages and Brewing Materials — Reducing Sugars) |
| **Sample Preparation** | 5.0 ± 0.1 g sample extracted with 50 mL 80% ethanol (v/v) at 80°C for 30 min with occasional swirling; centrifuge at 3000 × g for 10 min; collect supernatant; repeat extraction once; combine supernatants; dilute to 100 mL with 80% ethanol |
| **Aliquot** | 1.0 mL of extract (adjust if sugar concentration is outside calibration range) |
| **DNS Reagent** | Mix: 1.0% DNS (w/v), 0.2% phenol (w/v), 0.05% Na₂SO₃ (w/v), 1.0% NaOH (w/v). Store in amber bottle at 4°C, stable for 2 weeks |
| **Reaction** | Add 3.0 mL DNS reagent → mix → boil in water bath for exactly 5 min → cool in ice water bath → dilute to 25 mL with distilled water |
| **Measurement** | UV-Vis spectrophotometer at 540 nm, against reagent blank |
| **Standard Curve** | Anhydrous D-glucose, 0, 0.2, 0.4, 0.6, 0.8, 1.0 mg/mL (freshly prepared weekly) |
| **Quantitation Range** | 0.05–2.0% reducing sugars (as glucose equivalent) in sample |

**Calculation:**

$$Reducing\ Sugars\ (\%\ w/w) = \frac{C \times V \times D}{m \times 10^6} \times 100$$

Where:
- C = concentration from standard curve (μg/mL)
- V = final volume of diluted colored solution (25 mL)
- D = dilution factor (if aliquot was diluted before reaction)
- m = sample mass (g)

### 4.2 Secondary Method — Fehling's Titration (Lane-Eynon Method)

Used as a complementary verification method when DNS results are borderline or when disputing results with a customer.

| Parameter | Specification |
|-----------|---------------|
| **Reference** | AOAC 923.09 (Lane and Eynon Method) |
| **Reagent A** | CuSO₄·5H₂O, 69.28 g/L in distilled water |
| **Reagent B** | Potassium sodium tartrate (Rochelle salt), 346 g/L + NaOH, 100 g/L in distilled water |
| **Indicator** | Methylene blue, 1% (w/v) in ethanol |
| **Principle** | Reducing sugars reduce Cu²⁺ to Cu₂O (brick-red precipitate) in hot alkaline solution. The endpoint (last trace of blue) is detected visually |
| **Titration** | Pre-mix equal volumes (10 mL each) of A and B, add 50 mL water and 10 mL sample extract. Heat to boiling, titrate while boiling with additional sample extract until blue color disappears |
| **Endpoint** | Blue → brick-red (should disappear within 15 s of last addition) |

**Comparison: DNS vs. Fehling's**

| Aspect | DNS Method | Fehling's (Lane-Eynon) |
|--------|-----------|------------------------|
| Precision (RSDr) | ±2.5% | ±4.0% |
| Subjectivity | None (spectrophotometric) | Operator-dependent (visual endpoint) |
| Throughput | High (batch analysis; 40 samples/run) | Low (one at a time) |
| Interference | Less affected by non-sugar reducing agents | Affected by other reducing substances |
| Typical Use | Routine QC; R&D investigations | Verification; dispute resolution |

### 4.3 Sucrose Determination

Sucrose is measured by the difference between total sugars (after enzymatic inversion) and reducing sugars.

| Parameter | Specification |
|-----------|---------------|
| **Method** | Enzymatic inversion (AOAC 2013.12) |
| **Invertase Solution** | β-Fructosidase from yeast (≥200 U/mL), in acetate buffer, pH 4.6 |
| **Inversion** | 10 mL sample extract + 0.2 mL invertase → 55°C, 15 min |
| **Measurement** | Total reducing sugars after inversion by DNS method (Section 4.1) |
| **Calculation** | Sucrose (%) = (Total sugars after inversion − Reducing sugars before inversion) × 0.95 |

### 4.4 Individual Sugar Analysis (Glucose and Fructose)

For detailed sugar profiling, Hongji uses enzymatic test kits:

| Sugar | Method | AOAC Ref | Typical Range (% DM) |
|-------|--------|----------|----------------------|
| D-Glucose | Glucose oxidase/peroxidase (GOD-POD), 505 nm | AOAC 2011.14 | 0.3–1.5 |
| D-Fructose | Fructose dehydrogenase (FDH), 570 nm | AOAC 2011.14 (with hexokinase adaptation) | 0.3–1.5 |
| Sucrose | Invertase + GOD-POD (difference method) | AOAC 2013.12 | ≤3.0 |

### 4.5 Acceptance Limits — Sugars

| Sugar Parameter | Premium (% DM) | Standard (% DM) | Economy (% DM) | Method |
|-----------------|----------------|-----------------|-----------------|--------|
| Total Reducing Sugars (as glucose) | ≤2.0 | ≤2.5 | ≤3.5 | DNS (Section 4.1) |
| Glucose | ≤1.2 | ≤1.5 | ≤2.0 | GOD-POD |
| Fructose | ≤1.2 | ≤1.5 | ≤2.0 | FDH |
| Sucrose | ≤2.5 | ≤3.0 | ≤3.5 | Enzymatic (Section 4.3) |
| Total Sugars (sum) | ≤4.5 | ≤5.5 | ≤7.0 | Calculated |

---

## 5. Protein Content (AOAC 981.10)

### 5.1 Method — Kjeldahl Nitrogen Determination

| Parameter | Specification |
|-----------|---------------|
| **AOAC Reference** | AOAC Official Method 981.10 (Crude Protein in Meat — Block Digestion Method, adapted) |
| **ISO Reference** | ISO 1871: Food and feed products — General guidelines for the determination of nitrogen by the Kjeldahl method |
| **Sample Weight** | 1.0 ± 0.1 g (ground to pass 1 mm sieve) |
| **Catalyst** | CuSO₄·5H₂O + K₂SO₄ in 1:10 ratio, ~6.6 g total (one Kjeldahl tablet, e.g., Foss Kjeltabs) |
| **Digestion Acid** | 15 mL concentrated H₂SO₄ (95–98%, analytical grade) |
| **Digestion Conditions** | 420°C, 90 min (or until solution is clear pale green). Cool to room temperature |
| **Distillation** | Kjeldahl distillation unit (FOSS Kjeltec 8400 or equivalent). Add 80 mL distilled water + 50 mL 40% NaOH |
| **Recovery Trap** | 25 mL of 4% boric acid solution containing methyl red/bromocresol green mixed indicator |
| **Titration** | 0.1 N HCl (standardized against tris(hydroxymethyl)aminomethane weekly) |
| **Nitrogen-to-Protein Factor** | 6.25 (general potato protein factor; note: some potato protein fractions have alternative factors ranging from 5.7 to 6.25) |

**Calculation:**

$$Protein\ (\%) = \frac{(V_{sample} - V_{blank}) \times N \times 14.007 \times F}{m \times 10} \times 100$$

Where:
- V_sample = HCl titrant volume for sample (mL)
- V_blank = HCl titrant volume for blank (mL)
- N = exact normality of HCl (≈0.1 N)
- 14.007 = atomic mass of nitrogen (g/mol)
- F = conversion factor (6.25)
- m = sample mass (g)

### 5.2 Alternative — Dumas Combustion Method (AOAC 990.03)

For high-throughput testing, Hongji also operates a Dumas nitrogen analyzer (LECO FP-628 or Elementar Rapid N Exceed).

| Parameter | Specification |
|-----------|---------------|
| **Sample Weight** | 150–250 mg |
| **Combustion** | 950°C in pure oxygen |
| **Detection** | Thermal conductivity detection (TCD) of N₂ |
| **Analysis Time** | ≤4 minutes per sample |
| **Correlation** | Dumas nitrogen results correlate with Kjeldahl with r² > 0.99; bias correction: Protein_Dumas = 1.005 × Protein_Kjeldahl |

### 5.3 Acceptance Limits

| Product | Protein (% as-is) | Protein (% DM) | Typical Range |
|---------|-------------------|----------------|---------------|
| Flakes (All Grades) | 5.0–8.0 | 5.5–8.5 | 6.0–7.5 (most common) |
| Powder (All Grades) | 5.0–7.5 | 5.5–8.0 | 5.5–7.0 (most common) |

---

## 6. Ash, Crude Fat, and Crude Fiber

### 6.1 Ash Content (AOAC 923.03)

| Parameter | Specification |
|-----------|---------------|
| **AOAC Reference** | AOAC Official Method 923.03 (Ash of Flour) |
| **Crucible** | Porcelain, 30 mL capacity, pre-ignited at 550°C for 2 h, cooled in desiccator, tared |
| **Sample Weight** | 3.0 ± 0.1 g |
| **Pre-ashing** | Heat gently on a hot plate or over a Bunsen burner until smoking stops and sample is charred (15–20 min) |
| **Muffle Furnace** | 550 ± 10°C, 4–6 hours, until ash is white or light gray (no dark carbon specks visible) |
| **Cooling** | Desiccator, 45 min (minimum) |
| **Weighing** | Analytical balance (0.0001 g). Repeat ignition/weighing until weight change <0.5 mg |
| **Typical Range** | 3.0–4.5% (DM basis) |
| **Acceptance Limit** | ≤4.5% DM (all grades) |

### 6.2 Crude Fat (AOAC 920.39 — Soxhlet Extraction)

| Parameter | Specification |
|-----------|---------------|
| **AOAC Reference** | AOAC Official Method 920.39 (Fat (Crude) or Ether Extract in Animal Feed) |
| **Sample Weight** | 5.0 ± 0.1 g, dried at 103°C for 2 h before extraction |
| **Extraction Thimble** | Cellulose, pre-extracted with petroleum ether and dried |
| **Solvent** | Petroleum ether, boiling range 40–60°C (analytical grade) |
| **Extraction Time** | 6 hours minimum, ensuring at least 30 siphon cycles (approximately 50 cycles for standard setup) |
| **Solvent Removal** | Rotary evaporator at 40°C under vacuum, then oven at 80°C for 30 min |
| **Cooling** | Desiccator, 30 min |
| **Typical Range** | 0.2–1.0% (DM basis) |
| **Acceptance Limit** | ≤1.0% DM (all grades) |

### 6.3 Crude Fiber (AOAC 962.09)

| Parameter | Specification |
|-----------|---------------|
| **AOAC Reference** | AOAC Official Method 962.09 (Fiber (Crude) in Animal Feed and Pet Food) |
| **Apparatus** | FOSS Fibertec 2010 or equivalent (fiber digestion system) |
| **Sample** | 2.0 ± 0.1 g, defatted (petroleum ether, 4 h) |
| **Acid Digestion** | 200 mL of 1.25% H₂SO₄ (0.255 N), boiling for 30 min with reflux |
| **Filtration** | Vacuum filtration through a sintered glass crucible (porosity 2) |
| **Alkali Digestion** | 200 mL of 1.25% NaOH (0.313 N), boiling for 30 min with reflux |
| **Rinse** | Hot distilled water (3 × 50 mL), then 1% HCl (50 mL, to remove calcium residues), then hot water (2 × 50 mL), then acetone (25 mL) |
| **Drying** | 130°C, 2 h |
| **Ashing** | 550°C, 3 h |
| **Calculation** | Crude Fiber (%) = (Loss of weight on ashing / Sample mass) × 100 |
| **Typical Range** | 1.0–2.5% (DM basis) |
| **Acceptance Limit** | ≤3.0% DM (all grades) |

### 6.4 Summary Table — Proximate Composition

| Component | Method Reference | Flakes (Standard, DM basis) | Flakes (Fine, DM basis) | Powder (DM basis) |
|-----------|------------------|----------------------------|--------------------------|-------------------|
| Dry Matter | AOAC 934.06 / HJ-QA-015 | 92.0–94.0% | 92.5–94.5% | 91.5–93.5% |
| Total Starch | ISO 10520 (Ewers) | 70.0–80.0% | 72.0–82.0% | 68.0–78.0% |
| Reducing Sugars (total) | DNS (Section 4.1) | ≤3.5% | ≤2.5% | ≤3.5% |
| Sucrose | Enzymatic (Section 4.3) | ≤3.0% | ≤3.0% | ≤3.0% |
| Protein (N × 6.25) | AOAC 981.10 / HJ-QA-015 | 5.5–8.5% | 5.5–8.5% | 5.5–8.0% |
| Ash | AOAC 923.03 | ≤4.5% | ≤4.5% | ≤4.5% |
| Crude Fat | AOAC 920.39 (Soxhlet) | ≤1.0% | ≤1.0% | ≤1.0% |
| Crude Fiber | AOAC 962.09 | ≤3.0% | ≤3.0% | ≤3.0% |
| SO₂ Residue | AOAC 990.28 (see Section 7) | ≤400 ppm | ≤300 ppm | ≤400 ppm |

---

## 7. Sulfite (SO₂) Residue

Sulfur dioxide is added during processing (typically at the blanching or washing stage) as a color preservative (anti-browning agent) and antimicrobial. Residual levels must be controlled to meet both regulatory limits and customer specifications.

### 7.1 Reference Method — Modified Monier-Williams Distillation (AOAC 990.28 / EN 1988-1)

| Parameter | Specification |
|-----------|---------------|
| **AOAC Reference** | AOAC Official Method 990.28 (Sulfites in Foods — Optimized Monier-Williams Method) |
| **EN Reference** | EN 1988-1: Foodstuffs — Determination of sulfite — Part 1: Optimized Monier-Williams method |
| **Principle** | SO₂ is liberated from the sample by acid distillation under reflux, carried by nitrogen or air stream, trapped in H₂O₂ as H₂SO₄, and titrated with NaOH |
| **Sample Weight** | 10.0 ± 0.1 g |
| **Distillation Acid** | 50 mL of 3 M HCl (add through dropping funnel after flask reaches boiling) |
| **Carrier Gas** | Nitrogen or CO₂-free air, 60–80 mL/min |
| **Distillation Time** | 75 min (30 min pre-heat + 45 min after acid addition) |
| **Trapping Solution** | 30 mL of 3% H₂O₂ (freshly prepared), neutralized to methyl red endpoint |
| **Titration** | 0.01 N NaOH (standardized weekly); endpoints: H₂O₂ trap changes from pink to yellow |
| **Expression** | SO₂ (mg/kg) = (V_NaOH × N × 32.03 × 1000) / m |

### 7.2 Rapid Screening — Sulfite Test Strips (Production QC)

| Parameter | Specification |
|-----------|---------------|
| **Product** | Quantofix Sulfite (Macherey-Nagel) or equivalent |
| **Range** | 0–1000 ppm SO₃²⁻ equivalent (as Na₂SO₃) |
| **Sample Prep** | 10 g sample + 100 mL distilled water, blend 30 s, filter through Whatman No. 1 |
| **Detection Limit** | ~10 mg/kg |
| **Accuracy** | ±20% of reading |
| **Use** | In-process screening only; not suitable for COA certification |

### 7.3 Regulatory and Customer SO₂ Limits

| Market / Customer Type | Maximum SO₂ Residue | Regulation Reference |
|------------------------|---------------------|----------------------|
| China | ≤400 mg/kg | GB 2760-2024 |
| European Union | ≤400 mg/kg | Regulation (EC) 1333/2008 |
| USA / FDA | ≤500 mg/kg (declared if >10 ppm) | 21 CFR 182.3862 |
| Japan | ≤300 mg/kg (dried potato) | Food Sanitation Act |
| Codex Alimentarius | ≤400 mg/kg | CXS 301-2023 |
| Premium Customer Spec | ≤300 mg/kg | Individual contract |
| Standard Customer Spec | ≤400 mg/kg | Individual contract |
| "No Sulfite Added" Declared | ≤10 mg/kg | Per EU/US labeling regulations |

---

## 8. Method Performance — Accuracy and Precision

### 8.1 Method Performance Parameters

| Parameter | Method | RSDr (%) (Repeatability) | RSDR (%) (Reproducibility) | LOD | LOQ |
|-----------|--------|--------------------------|---------------------------|------|------|
| Dry Matter (oven) | AOAC 934.06 | ≤0.3 | ≤0.5 | 0.02% | 0.05% |
| Dry Matter (halogen) | Rapid | ≤0.4 | ≤0.7 | 0.05% | 0.10% |
| Dry Matter (NIR) | FT-NIR | ≤0.5 | ≤0.8 | 0.1% | 0.2% |
| Total Starch | ISO 10520 | ≤1.0 | ≤2.0 | 0.2% DM | 0.5% DM |
| Gelatinization Degree | Enzymatic | ≤2.0 | ≤3.5 | 1.0% | 3.0% |
| Starch Damage | AACC 76-31 | ≤3.0 | ≤5.0 | 0.1% | 0.3% |
| Reducing Sugars (DNS) | Section 4.1 | ≤3.0 | ≤5.0 | 5 mg/100g | 15 mg/100g |
| Reducing Sugars (Fehling) | Section 4.2 | ≤4.0 | ≤7.0 | 10 mg/100g | 30 mg/100g |
| Glucose (GOD-POD) | Enzymatic | ≤2.0 | ≤4.0 | 1 mg/100g | 3 mg/100g |
| Protein (Kjeldahl) | AOAC 981.10 | ≤1.5 | ≤3.0 | 0.1% | 0.3% |
| Protein (Dumas) | AOAC 990.03 | ≤1.0 | ≤2.5 | 0.05% | 0.15% |
| Ash | AOAC 923.03 | ≤1.5 | ≤3.0 | 0.01% | 0.03% |
| Crude Fat (Soxhlet) | AOAC 920.39 | ≤3.0 | ≤5.0 | 0.02% | 0.05% |
| Crude Fiber | AOAC 962.09 | ≤4.0 | ≤6.0 | 0.05% | 0.15% |
| SO₂ (Monier-Williams) | AOAC 990.28 | ≤2.5 | ≤5.0 | 0.5 mg/kg | 2.0 mg/kg |

### 8.2 Proficiency Testing

The chemical laboratory participates in quarterly proficiency testing programs (FAPAS or BIPEA) for all key parameters. Performance is evaluated using z-scores:

| z-Score | Performance | Action |
|---------|-------------|--------|
| \|Z\| ≤ 2.0 | Satisfactory | Continue routine operations |
| 2.0 < \|Z\| < 3.0 | Questionable | Investigate method, reagents, and operator performance |
| \|Z\| ≥ 3.0 | Unsatisfactory | Immediate CAPA; halt testing for that analyte until root cause is identified and corrected |

**Hongji 12-Month Average z-Scores (2025–2026):**

| Parameter | Avg z-Score | No. of Rounds | Best Performer in FAPAS? |
|-----------|-------------|---------------|--------------------------|
| Dry Matter | +0.8 | 4 | 1/4 rounds |
| Starch | −0.6 | 4 | 2/4 rounds |
| Reducing Sugars | +1.1 | 4 | 0/4 rounds |
| Protein | +0.4 | 4 | 1/4 rounds |
| SO₂ | −0.9 | 2 | 1/2 rounds |
| **Overall** | **1.3 (avg absolute)** | **4** | — |

### 8.3 Accepted Specification Limits — Quick Reference

| Parameter | Premium Flakes | Standard Flakes | Economy Flakes | Fine Powder |
|-----------|----------------|-----------------|----------------|-------------|
| Moisture (%) | 6.0–7.5 | 6.0–8.0 | 6.5–8.5 | 6.0–8.0 |
| Dry Matter (%) | 92.5–94.0 | 92.0–94.0 | 91.5–93.5 | 92.0–94.0 |
| Total Starch (% DM) | 72–80 | 70–80 | 68–78 | 72–82 |
| Gelatinization Degree (%) | 88–93 | 85–92 | 82–90 | 80–88 |
| Starch Damage (%) | ≤5.0 | ≤5.0 | ≤6.0 | ≤8.0 |
| Reducing Sugars (% DM) | ≤2.0 | ≤2.5 | ≤3.5 | ≤2.5 |
| Protein (% DM) | 5.5–8.5 | 5.5–8.5 | 5.0–8.0 | 5.5–8.0 |
| Ash (% DM) | ≤4.0 | ≤4.5 | ≤5.0 | ≤4.5 |
| Crude Fat (% DM) | ≤0.8 | ≤1.0 | ≤1.2 | ≤1.0 |
| Crude Fiber (% DM) | ≤2.5 | ≤3.0 | ≤3.5 | ≤3.0 |
| SO₂ (mg/kg) | ≤300 | ≤400 | ≤400 | ≤300 |

---

## 9. Quality Control and Method Validation

### 9.1 Internal Quality Control

| QC Practice | Frequency | Acceptance Criterion |
|-------------|-----------|----------------------|
| Blank analysis | Each run | ≤LOD for each analyte |
| Standard reference material (SRM) | Each run | Recovery 95–105% of certified value |
| Duplicate analysis | Every 10th sample | RPD < 2 × RSDr |
| Control chart (X̄-R) | Updated monthly | All points within 3σ limits |
| Reagent checks (blank titrant, indicator, etc.) | Daily | Within control limits |

### 9.2 External QC

| Practice | Frequency | Organization |
|----------|-----------|-------------|
| Proficiency testing | Quarterly | FAPAS (Fera Science Ltd., UK) or BIPEA (France) |
| Instrument calibration (balance, oven, spectrophotometer) | Annually (minimum) | CNAS-accredited calibration laboratory |
| Method cross-laboratory validation | Every 2 years | In collaboration with China National Food Quality Supervision and Inspection Center |

### 9.3 LIMS Integration

All results are recorded in the Laboratory Information Management System (LIMS) with:

- Sample identifiers (lot number, date, sampler)
- Operator ID and analysis date/time
- Method reference
- Raw data and calculations
- Control chart flags (automated)
- COA generation (auto-populated)

---

## 10. Method Cross-Reference Table

| Parameter | AOAC Method | ISO Method | AACC Method | GB (China) Method | Hongji SOP |
|-----------|-------------|------------|-------------|-------------------|------------|
| Dry Matter (Moisture) | 934.06 | ISO 24557 | AACC 44-15.02 | GB 5009.3 | HJ-QA-015-SOP-01 |
| Total Starch | 996.11 (amyloglucosidase) | ISO 10520 (Ewers) | AACC 76-13 | GB 5009.9 | HJ-QA-015-SOP-02 |
| Starch Gelatinization | — | — | AACC 76-13 (mod.) | — | HJ-QA-015-SOP-03 |
| Starch Damage | — | — | AACC 76-31 | — | HJ-QA-015-SOP-04 |
| Reducing Sugars | 977.20 (DNS) | ISO 7510 | AACC 80-04 | GB 5009.7 | HJ-QA-015-SOP-05 |
| Sucrose | 2013.12 | ISO 10520 (indirect) | — | GB 5009.8 | HJ-QA-015-SOP-06 |
| Glucose/Fructose | 2011.14 (enzymatic) | ISO 13965 | — | GB 5009.8 | HJ-QA-015-SOP-07 |
| Protein (Kjeldahl) | 981.10 | ISO 1871 | AACC 46-09 | GB 5009.5 | HJ-QA-015-SOP-08 |
| Protein (Dumas) | 990.03 | ISO 16634 | AACC 46-30 | GB 5009.5 | HJ-QA-015-SOP-09 |
| Ash | 923.03 | ISO 2171 | AACC 08-01 | GB 5009.4 | HJ-QA-015-SOP-10 |
| Crude Fat | 920.39 | ISO 6492 | AACC 30-10 | GB 5009.6 | HJ-QA-015-SOP-11 |
| Crude Fiber | 962.09 | ISO 5498 | AACC 32-10 | GB/T 5009.10 | HJ-QA-015-SOP-12 |
| Sulfite (SO₂) | 990.28 | EN 1988-1 | — | GB 5009.34 | HJ-QA-015-SOP-13 |

---

## 11. References

- AOAC International (2024). *Official Methods of Analysis of AOAC International*, 22nd Edition.
- ISO 10520:1997. Determination of starch content — Ewers polarimetric method.
- ISO 6647:2020. Rice — Determination of amylose content (adapted for potato).
- ISO 1871:2009. Food and feed products — General guidelines for the determination of nitrogen by the Kjeldahl method.
- AACC International. *Approved Methods of Analysis*, 12th Edition.
- GB 2760-2024: National Food Safety Standard — Uses of Food Additives (China).
- EU Regulation (EC) No 1333/2008: Food Additives.
- EN 1988-1:1998. Foodstuffs — Determination of sulfite — Part 1: Optimized Monier-Williams method.
- ASTM E1655: Standard Practices for Infrared Multivariate Quantitative Analysis.
- FAPAS Proficiency Testing Reports (series, 2025–2026, available upon request).
- Singh, J. & Kaur, L. (Eds.). (2016). *Advances in Potato Chemistry and Technology*, 2nd Ed. Academic Press.

---

*End of Document*

---

*This document is part of the Hongji Agriculture (弘基农业) Technical Documentation Series. For more information about our vertically integrated potato supply chain — from seed breeding and cultivation to processing and global export — visit our official B2B website: [https://hjpotatoflakes.com](https://hjpotatoflakes.com)*
