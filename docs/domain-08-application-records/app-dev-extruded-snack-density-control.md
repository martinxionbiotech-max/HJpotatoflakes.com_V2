---
description: "Application Development Record: Extruded Snack Bulk Density Control via Twin-Screw Extrusion"
---

# Application Development Record: Extruded Snack Bulk Density Control via Twin-Screw Extrusion

**Document No.:** HJA-APP-2024-008-03  
**Product Line:** Potato Flakes (Extruded Snack Application)  
**Development Date:** April – August 2024  
**Version:** 1.2

---

## 1. Customer Requirement

### 1.1 Customer Background

A Southeast Asian extruded snack manufacturer (based in Bangkok, Thailand) produces direct-expanded potato-based snack pellets for the domestic and ASEAN snack market. Their flagship product is a cheese-flavored expanded curl sold through convenience store chains. The current manufacturing process uses a blend of potato flakes (40%) and corn grits (60%) fed through a co-rotating twin-screw extruder.

### 1.2 Problem Statement

The customer's product has a bulk density of approximately 0.45 g/mL, which positions it in the "medium-dense" expanded snack category. The marketing team has identified a market opportunity for a "lighter, crispier" variant with a bulk density target of **0.38 g/mL** — a 15.6% reduction — that would offer improved mouthfeel and perceived premium quality. However, previous in-house attempts to reduce density by simply increasing screw speed resulted in burned flavors and unacceptable product blistering.

| Parameter | Current Value | Target Value | Gap |
|-----------|:-------------:|:------------:|:---:|
| Bulk density (g/mL) | 0.45 ± 0.02 | 0.38 ± 0.02 | −15.6% |
| Expansion ratio (ER, radial) | 3.2 ± 0.2 | ≥ 3.8 | +18.8% |
| Hardness (N, puncture test) | 18.5 ± 1.5 | ≤ 14.0 | −24.3% |
| Oil uptake (%, post-frying) | 28.0 ± 1.0 | ≤ 24.0 | −14.3% |
| Process stability (Cv of density) | ≤ 5% | ≤ 5% | Maintain |

### 1.3 Customer Constraints

| Constraint | Details |
|------------|---------|
| Equipment | Clextral BC45 twin-screw extruder, L/D = 20:1 |
| Die diameter | 3.5 mm (round) |
| Screw configuration | Co-rotating, medium shear profile (existing) |
| Drying section | Belt dryer, 95°C × 8 min |
| Frying section | Continuous fryer, 180°C × 45 s |
| Raw materials | Cannot change base blend (40% potato flakes + 60% corn grits) |
| Production rate | Minimum 80 kg/h |

### 1.4 Development Objectives

1. Reduce bulk density from 0.45 to ≤ 0.38 g/mL
2. Increase expansion ratio from 3.2 to ≥ 3.8
3. Reduce hardness to ≤ 14.0 N while maintaining crispy fracture characteristics
4. Reduce oil uptake by ≥ 14%
5. Maintain process Cv ≤ 5% for consistent industrial production
6. No off-flavors (burned, bitter, or stale notes)

---

## 2. Raw Material Selection Basis

### 2.1 Potato Flake Selection

The customer's existing formulation uses standard potato flakes (Grade A). For this optimization, two alternative flake variants were evaluated to determine if modification could simplify the extrusion parameter search:

| Variant | Starch (db%) | Free Starch (%) | WHC (g/g) | Particle Size D50 (µm) | Amylose Content (%) | Suitability Rating |
|---------|:-----------:|:---------------:|:---------:|:---------------------:|:-------------------:|:-----------------:|
| Standard Flakes | 73.8 | 2.1 | 5.8 | 180 | 22.3 | Good |
| **High-Starch Flakes** | **79.2** | **1.8** | **6.5** | **150** | **24.1** | **Best** |
| Fine Granules | 71.5 | 3.5 | 5.2 | 90 | 21.8 | Poor |

**Selection:** High-Starch Flakes (79.2% starch db, 24.1% amylose) were selected for this development. The higher amylose content promotes greater expansion during extrusion because amylose contributes to bubble wall stabilization. The fine, uniform particle size (150 µm D50) also ensures more even moisture distribution during preconditioning.

### 2.2 Corn Grit Specification

| Parameter | Value | Justification |
|-----------|-------|---------------|
| Source | Dent corn, Grade #2 | Standard industrial grit |
| Particle size | 500 – 850 µm | Matches twin-screw feed section |
| Moisture | 12.0 – 13.5% | As-received |
| Starch content | ≥ 85% db | — |
| Fat content | ≤ 0.8% | Lower fat prevents expansion interference |
| Protein content | 7.0 – 8.5% | Impacts texture and expansion |

### 2.3 Final Blend Composition

| Ingredient | Percentage | Function |
|------------|:----------:|----------|
| Potato flakes (High-Starch) | 40% | Expansion promoter, flavor base |
| Corn grits | 58% | Structural matrix, cost base |
| Salt | 1.5% | Flavor |
| Sugar | 0.5% | Browning control |
| Mono-diglyceride (emulsifier) | 0.3% | Cell structure uniformity |

### 2.4 Key Quality Indicators for Raw Materials

| Parameter | Potato Flakes | Corn Grits | Test Method |
|-----------|:------------:|:----------:|-------------|
| Moisture | ≤ 5.5% | 12.0–13.5% | AOAC 925.10 |
| Starch (db) | 78–80% | ≥ 85% | Ewers method |
| Bulk density | 0.34–0.36 g/mL | 0.65–0.72 g/mL | — |
| Fat | ≤ 0.5% | ≤ 0.8% | Soxhlet |
| Free starch | ≤ 2.0% | — | — |

---

## 3. Experimental Design

### 3.1 Orthogonal Array: L9(3⁴)

A four-factor, three-level orthogonal experiment (L9 orthogonal array) was designed to efficiently explore the parameter space with only 9 runs.

#### 3.1.1 Factors and Levels

| Factor | Symbol | Level 1 | Level 2 | Level 3 |
|--------|:------:|:-------:|:-------:|:-------:|
| Feed moisture content (%) | A | **14** | **18** | **22** |
| Screw speed (rpm) | B | **250** | **350** | **450** |
| Barrel temperature — Zone 1 (°C) | C₁ | 130 | 140 | 150 |
| Barrel temperature — Zone 2 (°C) | C₂ | 140 | 150 | 160 |
| Barrel temperature — Zone 3 (°C) | C₃ | 150 | 160 | 170 |

> Note: Zones 1, 2, and 3 are treated as a combined temperature profile factor with three levels representing low, medium, and high profiles.

#### 3.1.2 L9 Experimental Matrix

| Run | A (Moisture, %) | B (Screw Speed, rpm) | C (Temp Profile: T1/T2/T3, °C) |
|:---:|:---------------:|:--------------------:|:-------------------------------:|
| 1 | 14 | 250 | 130/140/150 |
| 2 | 14 | 350 | 140/150/160 |
| 3 | 14 | 450 | 150/160/170 |
| 4 | 18 | 250 | 140/150/160 |
| **5** | **18** | **350** | **150/160/170** |
| 6 | 18 | 450 | 130/140/150 |
| 7 | 22 | 250 | 150/160/170 |
| 8 | 22 | 350 | 130/140/150 |
| 9 | 22 | 450 | 140/150/160 |

### 3.2 Fixed Process Parameters

| Parameter | Value |
|-----------|-------|
| Feed rate | 80 kg/h (constant) |
| Die diameter | 3.5 mm, round orifice |
| Knife speed | 600 rpm (dry pellets) |
| Pellet drying | 95°C / 8 min to ≤ 10% moisture |
| Frying | 180°C / 45 s |
| Post-frying seasoning | Cheese powder 8%, salt 1% (standard) |

### 3.3 Response Variables

| Response | Symbol | Method |
|----------|:------:|--------|
| Bulk density (g/mL) | BD | Graduated cylinder + weighing, 100 g sample |
| Radial expansion ratio | ER | Calliper measurement of pellet diameter ÷ die diameter (n = 30) |
| Longitudinal expansion index | LEI | Length per unit mass (mm/g) |
| Hardness (N) | H | TA.XTplusC, 3-point bend rig, 5 mm/s |
| Crispness (fracture count) | FC | Number of force peaks during 80% compression |
| Oil uptake (%) | OU | Soxhlet extraction on ground fried pellets |
| Color (L*, a*, b*) | Color | HunterLab ColorQuest |
| Sensory score (1–9) | SS | Internal panel, n = 12 |

### 3.4 Replication

Each of the 9 runs was performed in **duplicate** (two separate extrusion sessions on different days). Measurements were taken in triplicate for density, expansion, and texture, and in duplicate for oil uptake and color.

---

## 4. Test Data Tables

### 4.1 L9 Orthogonal Experiment Results — Physical Properties

| Run | BD (g/mL) | ER (radial) | LEI (mm/g) | H (N) | FC | OU (%) | L* (color) | SS (1–9) |
|:---:|:---------:|:-----------:|:----------:|:-----:|:--:|:------:|:----------:|:--------:|
| 1 | 0.48 | 3.05 | 22.4 | 21.2 | 8 | 30.1 | 72.3 | 4.5 |
| 2 | 0.42 | 3.45 | 26.1 | 17.8 | 12 | 27.8 | 68.5 | 6.2 |
| 3 | 0.39 | 3.72 | 28.8 | 14.9 | 15 | 25.4 | 62.1 | 7.1 |
| 4 | 0.44 | 3.28 | 24.5 | 19.5 | 10 | 28.9 | 74.8 | 5.3 |
| **5** | **0.37** | **3.95** | **31.2** | **12.8** | **18** | **23.1** | 69.4 | **8.2** |
| 6 | 0.41 | 3.55 | 27.9 | 16.1 | 13 | 26.5 | 65.2 | 6.8 |
| 7 | 0.49 | 2.95 | 21.8 | 22.5 | 7 | 31.2 | 78.5 | 3.8 |
| 8 | 0.46 | 3.12 | 23.5 | 20.8 | 9 | 29.8 | 71.0 | 4.2 |
| 9 | 0.43 | 3.38 | 25.2 | 18.4 | 11 | 27.2 | 66.8 | 5.9 |

**Bold row (Run 5):** Identified as the optimal run with bulk density **0.37 g/mL** (below the 0.38 target), ER **3.95** (exceeds 3.8 target), hardness **12.8 N** (below 14.0 N), lowest oil uptake **23.1%** (target ≤ 24%), and highest sensory score **8.2/9**.

### 4.2 Range Analysis (直观分析法)

| Response | Metric | A (Moisture) | B (Screw Speed) | C (Temperature) |
|----------|:------:|:------------:|:---------------:|:---------------:|
| **BD** | K1 avg | 0.430 | 0.470 | 0.450 |
| | K2 avg | 0.407 | 0.417 | 0.430 |
| | K3 avg | 0.460 | 0.410 | **0.417** |
| | **Range R** | **0.053** | **0.060** | **0.033** |
| | **Rank** | 2 | **1** | 3 |
| **ER** | K1 avg | 3.41 | 3.09 | 3.24 |
| | K2 avg | **3.59** | 3.51 | 3.37 |
| | K3 avg | 3.15 | **3.55** | **3.54** |
| | **Range R** | 0.44 | 0.46 | 0.30 |
| | **Rank** | 2 | **1** | 3 |
| **H** | K1 avg | 17.97 | 21.07 | 19.37 |
| | K2 avg | **16.13** | **17.13** | 18.57 |
| | K3 avg | 20.57 | 16.47 | **16.73** |
| | **Range R** | 4.44 | 4.60 | 2.64 |
| | **Rank** | 2 | **1** | 3 |
| **OU** | K1 avg | 27.77 | 30.07 | 28.80 |
| | K2 avg | **26.17** | **26.90** | 27.97 |
| | K3 avg | 29.40 | 26.37 | **26.57** |
| | **Range R** | 3.23 | 3.70 | 2.23 |
| | **Rank** | 2 | **1** | 3 |

**Range Analysis Interpretation:**
- **Screw speed (B)** is the most influential factor for all four primary responses (BD, ER, H, OU), with the largest range values
- **Feed moisture (A)** is the second most important factor
- **Temperature profile (C)** has the smallest but still significant effect
- The optimal level combination is **A2 B2 C3**: Moisture = 18%, Screw speed = 350 rpm, Temperature profile = 150/160/170°C

### 4.3 ANOVA Results

| Response | Factor | SS | df | MS | F-ratio | Significance |
|----------|--------|:--:|:--:|:--:|:-------:|:-----------:|
| **BD** | A (Moisture) | 0.00427 | 2 | 0.00214 | 47.6 | ** |
| | B (Speed) | 0.00647 | 2 | 0.00324 | 72.0 | *** |
| | C (Temp) | 0.00167 | 2 | 0.00084 | 18.7 | * |
| | Error | 0.00009 | 2 | 0.00005 | | |
| **ER** | A | 0.291 | 2 | 0.146 | 48.7 | ** |
| | B | 0.419 | 2 | 0.210 | 70.0 | *** |
| | C | 0.135 | 2 | 0.068 | 22.7 | * |
| | Error | 0.006 | 2 | 0.003 | | |
| **H** | A | 29.6 | 2 | 14.8 | 37.0 | ** |
| | B | 37.8 | 2 | 18.9 | 47.3 | ** |
| | C | 10.9 | 2 | 5.5 | 13.8 | ns |
| | Error | 0.8 | 2 | 0.4 | | |

*** p < 0.001, ** p < 0.01, * p < 0.05, ns = not significant

### 4.4 Main Effects Summary

**Factor A (Moisture Content):**
- 14% → 18%: BD decreases, ER increases, H decreases → beneficial
- 18% → 22%: Trend reverses → BD increases, ER decreases → excessive moisture reduces melt elasticity

**Factor B (Screw Speed):**
- 250 → 350 rpm: All responses improve (lower BD, higher ER, lower H)
- 350 → 450 rpm: Diminishing returns, slight further improvement in BD but ER stabilizes
- 350 rpm balances expansion with residence time for adequate cooking

**Factor C (Temperature Profile):**
- Higher temperatures (150/160/170°C) favor expansion because superheated water vaporizes more rapidly at the die exit, producing greater bubble growth
- However, excessively high temperatures risk scorching (seen in Run 3 where L* dropped to 62.1)

### 4.5 Response Surface Verification

The optimal condition (A2B2C3: 18% moisture, 350 rpm, 150/160/170°C / Run 5) was replicated three additional times for verification:

| Replicate | BD (g/mL) | ER | H (N) | OU (%) | Sensory |
|:---------:|:---------:|:--:|:-----:|:------:|:-------:|
| Run 5 (original) | 0.37 | 3.95 | 12.8 | 23.1 | 8.2 |
| Verification 1 | 0.375 | 3.88 | 13.1 | 23.5 | 8.0 |
| Verification 2 | 0.365 | 3.92 | 12.6 | 22.8 | 8.3 |
| Verification 3 | 0.38 | 3.90 | 13.0 | 23.3 | 8.1 |
| **Mean ± SD** | **0.373 ± 0.006** | **3.91 ± 0.03** | **12.9 ± 0.22** | **23.2 ± 0.30** | **8.15 ± 0.13** |
| **Cv (%)** | **1.6%** | **0.8%** | **1.7%** | **1.3%** | **1.6%** |

The process Cv of 1.6% for bulk density is well within the customer's 5% requirement, confirming industrial robustness.

### 4.6 Comparative Summary: Current vs Optimal

| Parameter | Current Process (Rough baseline) | Run 5 Optimal | Improvement |
|-----------|:-------------------------------:|:-------------:|:-----------:|
| Bulk density (g/mL) | 0.45 ± 0.02 | **0.37 ± 0.01** | −17.8% |
| Expansion ratio (radial) | 3.2 ± 0.2 | **3.91 ± 0.03** | +22.2% |
| Hardness (N) | 18.5 ± 1.5 | **12.9 ± 0.2** | −30.3% |
| Oil uptake (%) | 28.0 ± 1.0 | **23.2 ± 0.3** | −17.1% |
| Crispness (fracture count) | 8 ± 2 | **18 ± 1** | +125% |
| Sensory score (1–9) | 4.5 (estimated) | **8.2** | +82% |

---

## 5. Results & Analysis

### 5.1 Optimal Process Conditions

The optimal twin-screw extrusion parameters for achieving bulk density ≤ 0.38 g/mL are:

| Parameter | Optimal Value | Operating Window |
|-----------|:------------:|:----------------:|
| Feed moisture | 18% | 17 – 19% |
| Screw speed | 350 rpm | 320 – 380 rpm |
| Zone 1 (feed → kneading) | 150°C | 145 – 155°C |
| Zone 2 (kneading → metering) | 160°C | 155 – 165°C |
| Zone 3 (metering → die) | 170°C | 165 – 175°C |
| Die temperature | 165 – 170°C | Monitor |

### 5.2 Mechanism of Density Reduction

The reduction in bulk density from 0.45 to 0.37 g/mL (17.8% reduction) is achieved through the following mechanisms:

1. **Optimal Moisture (18%):** At 18% moisture, the potato starch and corn starch reach the ideal gelatinization extent (measured as 92.3% degree of gelatinization via DSC). This maximizes melt elasticity without leaving ungelatinized starch particles that would weaken bubble walls. Below 18% moisture (14%), expansion is limited because insufficient steam is generated; above 18% (22%), excess water plasticizes the melt, reducing its elasticity and causing bubble collapse.

2. **Moderate Screw Speed (350 rpm):** At 250 rpm, the residence time is too long (≈ 45 s), causing excessive starch degradation (measured as 14% damaged starch via enzymatic method). At 450 rpm, residence time is too short (≈ 18 s), resulting in incomplete cooking (degree of gelatinization only 78%). At 350 rpm, residence time (≈ 28 s) balances complete gelatinization with minimal degradation.

3. **Elevated Temperature Profile (150/160/170°C):** The 170°C die-zone temperature ensures that the melt exits at approximately 165°C, well above the boiling point of water at die pressure. The instantaneous flash evaporation creates rapid bubble nucleation. The three-zone gradient (increasing 150 → 160 → 170°C) provides gradual starch melting without thermal shocking.

### 5.3 Oil Uptake Reduction

Oil uptake decreased from 28.0% to 23.2% (17.1% reduction). This is attributed to:
- **Denser, thinner cell walls** in the expanded structure (walls measure 0.12 ± 0.02 mm vs 0.18 ± 0.03 mm in the control)
- **Smaller, more numerous gas cells** (mean cell area reduced from 0.42 to 0.31 mm² per C-Cell analysis)
- **Reduced surface porosity** due to more uniform expansion
- The relationship between expansion ratio and oil uptake follows a power law: OU = 38.5 × ER^(−0.42), R² = 0.89

### 5.4 Texture Improvement

Hardness decreased by 30.3% (18.5 → 12.9 N), while crispness (fracture count) more than doubled (8 → 18 peaks). Panelists described the optimal product as: *"Light, airy, and shatteringly crisp — similar to premium puffed snacks."* The fracture count increase is particularly important because it correlates strongly (r = 0.91) with sensory crispness perception — higher fracture counts produce a more satisfying audible and tactile breakdown in the mouth.

### 5.5 Color and Visual Quality

The optimal product (Run 5) had L* = 69.4, which represents a moderate golden-yellow color without the burned appearance seen in Run 3 (L* = 62.1, temperature profile 150/160/170°C but also combined with 14% moisture and 450 rpm). The combination of 18% moisture and 350 rpm at the same temperatures prevents localized overheating. The a* value was 2.8 (slight red-orange) and b* was 22.5 (yellow), producing an appetizing snack color.

### 5.6 Conclusion

The orthogonal experiment successfully identified process conditions that achieve a bulk density of **0.37 g/mL** (below the 0.38 target), representing a **17.8% reduction** from the current product. All secondary targets were met or exceeded:
- ER: 3.91 (target ≥ 3.8) ✅
- Hardness: 12.9 N (target ≤ 14.0 N) ✅
- Oil uptake: 23.2% (target ≤ 24.0%) ✅
- Process Cv: 1.6% (target ≤ 5%) ✅

The optimal conditions — **feed moisture 18%, screw speed 350 rpm, and temperature profile 150/160/170°C** — are suitable for industrial implementation without equipment modification.

---

## 6. Commercial Delivery Parameters

### 6.1 Recommended Process Settings

| Parameter | Setting | Tolerance | Alarm Limit |
|-----------|:-------:|:---------:|:-----------:|
| Feed rate | 80 kg/h | ± 2 kg/h | ± 5 kg/h |
| Preconditioner water | 18% of feed rate | ± 0.5% | ± 1.0% |
| Screw speed | 350 rpm | ± 15 rpm | ± 25 rpm |
| Zone 1 (°C) | 150 | ± 3 | ± 5 |
| Zone 2 (°C) | 160 | ± 3 | ± 5 |
| Zone 3 (°C) | 170 | ± 3 | ± 5 |
| Die pressure (bar) | 45 – 55 | — | < 35 or > 70 |
| Knife speed | 600 rpm | ± 25 rpm | ± 50 rpm |
| Pellet drying temp | 95°C | ± 3°C | ± 5°C |
| Pellet drying time | 8 min | ± 30 s | ± 1 min |
| Pellet moisture (post-dry) | 8 – 10% | — | > 10.5% |
| Fryer temp | 180°C | ± 3°C | ± 5°C |
| Fryer residence | 45 s | ± 3 s | ± 5 s |

### 6.2 Product Specification (Final Fried Snack)

| Parameter | Specification | Method | Frequency |
|-----------|:------------:|--------|:---------:|
| Bulk density | 0.36 – 0.40 g/mL | Volumetric | Every 30 min |
| Radial expansion ratio | ≥ 3.8 | Calliper | Every hour |
| Hardness | 11 – 14 N | TA.XTplusC | Every 2 h |
| Oil content | 22 – 24% | Soxhlet | Every batch |
| Moisture | ≤ 2.5% | Infra-red balance | Every 30 min |
| L* (color) | 68 – 72 | HunterLab | Every batch |
| a* | 2 – 4 | HunterLab | Every batch |
| b* | 20 – 25 | HunterLab | Every batch |
| Sensory overall | ≥ 7.0/9 | Panel (n ≥ 8) | Weekly |

### 6.3 Raw Material Specification

| Ingredient | Specification | Supplier QC Frequency |
|------------|:-------------|:---------------------|
| Potato flakes (High-Starch) | Starch ≥ 78% db, moisture ≤ 5.5% | Every batch |
| Corn grits | Grade #2 dent corn, 500–850 µm | Every batch |
| Salt | Purity ≥ 99.5% | Certificate of analysis |
| Mono-diglyceride | Emulsifier, ≥ 95% monoester | Certificate of analysis |

### 6.4 Scale-Up Notes

| Consideration | Recommendation |
|---------------|---------------|
| Extruder scale-up | For larger extruders (BC72 or BC82), use specific mechanical energy (SME) as the primary scale-up parameter. Target SME: 120 – 140 Wh/kg |
| Die configuration | Single 3.5 mm round die used in this study. For multi-die configurations (2–4 dies), reduce die flow area proportionally to maintain die pressure |
| Ambient conditions | High ambient humidity (> 80% RH) may require reduction of preconditioner water by 0.5 – 1.0% |
| Production rate scaling | If increasing from 80 to 120 kg/h, increase screw speed proportionally (to ≈ 525 rpm) to maintain SME |

### 6.5 Packaging and Shelf Life

| Parameter | Specification |
|-----------|--------------|
| Packaging | Metalized PET/PE pouch |
| Gas flushing | Nitrogen, residual O₂ ≤ 3% |
| Shelf life | 9 months at 25°C, 6 months at 35°C (tropical) |
| Storage | < 65% RH, no direct sunlight |

## References

- AOAC International. Official Methods of Analysis, 21st edition. Gaithersburg, MD.
- Hongji Agriculture Technology Co., Ltd. 2026. "Application Development Record: Extruded Snack Bulk Density Control via Twin-Screw Extrusion." Hongji Agriculture Knowledge Center.


---

*This document is part of the Hongji Agriculture (弘基农业) Technical Documentation Series. For more information, visit our official B2B website: [https://hjpotatoflakes.com](https://hjpotatoflakes.com)*
