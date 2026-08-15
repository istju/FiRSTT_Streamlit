# FiRSTT Symbol Registry v2.0

**Status:** permanent base document  
**Language:** Hungarian (English translation layer planned)  
**Purpose:** Shared, stable notation foundation for the FiRSTT theoretical documents and the Streamlit mathematical interface.

> **Core principle**  
> This registry does **not** rewrite the mathematical content of the A–H source files.  
> It preserves the original source notation and resolves previous collisions by **layered representation**:
>
> 1. **SOURCE** — original component notation (unchanged)
> 2. **RECONSTRUCTED / UNIFIED** — normalised form for mathematical clarity
> 3. **FiRSTT INTERPRETATION** — hypothesis-level reading (not a mathematical consequence)
>
> Layering handles notational collisions. It does **not** prove that the original A–H use of identical component letters was historically or mathematically intentional.

---

## 1. Quaternion convention (standard mathematics)

**Block ID:** `SYM-QUAT-STD`

The computational reference implementation uses the classical Hamilton form:

\[ q = w + xi + yj + zk \]

Component mapping:

| Mathematical component | Python attribute |
|------------------------|------------------|
| scalar part            | `w`              |
| \(i\)-component        | `x`              |
| \(j\)-component        | `y`              |
| \(k\)-component        | `z`              |
| vector part            | `(x, y, z)`      |

This is **standard mathematics**, not FiRSTT-specific.

---

## 2. Differential operator

**Block ID:** `SYM-NABLA`

Source form:

\[ \nabla = \mathbf{i}\frac{\partial}{\partial x} + \mathbf{j}\frac{\partial}{\partial y} + \mathbf{k}\frac{\partial}{\partial z} \]

Related operator forms used in the reconstruction:

\[ \nabla\times\mathbf{A},\quad
\nabla\times\mathbf{H},\quad
\nabla\cdot\mathbf{D},\quad
\nabla\cdot\mathbf{J}_{\mathrm{total}},\quad
\nabla\cdot\mathbf{J}_{\mathrm{conduction}} \]

The full algebraic interpretation of a quaternionic gradient operator is left to a later mathematical specification.

---

## 3. Fields and potentials

### 3.1 Vector potential \(\mathbf{A}\)

**Block ID:** `SYM-A`

**SOURCE**  
\(\mathbf{A} = (f, g, h)\)

**RECONSTRUCTED / UNIFIED**  
\(\mathbf{A} = (f_A, g_A, h_A)\)  
Streamlit / code: `A_x, A_y, A_z`

**FiRSTT INTERPRETATION**  
Appears in the magnetic force and electromotive force equations.  
Any deeper role together with the longitudinal component is hypothesis-level.

### 3.2 Scalar potential \(\Psi\)

**Block ID:** `SYM-PSI`

**SOURCE**  
\(\Psi\)

**RECONSTRUCTED / UNIFIED**  
\(\Psi\)  
Streamlit / code: `Psi`

**FiRSTT INTERPRETATION**  
\(-\nabla\Psi\) appears as a highlighted longitudinal component in the D-equations.  
This reading is a hypothesis, not a mathematical consequence of the source.

### 3.3 Electric field strength \(\mathbf{E}\)

**Block ID:** `SYM-E`

**SOURCE**  
\(\mathbf{E} = (P, Q, R)\)

**RECONSTRUCTED / UNIFIED**  
\(\mathbf{E} = (P, Q, R)\)  
Streamlit / code: `E_x, E_y, E_z`

### 3.4 Magnetic field strength \(\mathbf{H}\)

**Block ID:** `SYM-H`

**SOURCE**  
\(\mathbf{H} = (\alpha, \beta, \gamma)\)

**RECONSTRUCTED / UNIFIED**  
\(\mathbf{H} = (\alpha, \beta, \gamma)\)  
Streamlit / code: `H_x, H_y, H_z`

---

## 4. Electric displacement \(\mathbf{D}\)

**Block ID:** `SYM-D`

**SOURCE**  
\(\mathbf{D} = (f, g, h)\)

**RECONSTRUCTED / UNIFIED**  
\(\mathbf{D} = (f_D, g_D, h_D)\)  
Streamlit / code: `D_x, D_y, D_z`

**FiRSTT INTERPRETATION**  
The source material used the same letters \(f,g,h\) for both \(\mathbf{A}\) and \(\mathbf{D}\).  
Layered representation resolves the collision for computation and display.  
It does **not** claim that the original identical lettering was intentional.

**Status:** RESOLVED_BY_REPRESENTATION_LAYER  
(Állapot: RÉTEGEZETT ÁBRÁZOLÁSSAL KEZELVE)

---

## 5. Currents

### 5.1 Conduction current density

**Block ID:** `SYM-J-COND`

**SOURCE**  
\(\mathbf{J}_{\mathrm{conduction}} = (u, v, w)\)  
(sources often write simply \(\mathbf{J} = (u,v,w)\))

**RECONSTRUCTED / UNIFIED**  
always \(\mathbf{J}_{\mathrm{conduction}} = (u, v, w)\)  
Streamlit / code: `J_cond_x, J_cond_y, J_cond_z`

### 5.2 Total current density

**Block ID:** `SYM-J-TOTAL`

**SOURCE**  
- Group A: \(\mathbf{J}_{\mathrm{total}} = (p, q, r)\)
- Group C: \(\mathbf{J} = (p, q, r)\) (text identifies it as total current)

**RECONSTRUCTED / UNIFIED**  
always \(\mathbf{J}_{\mathrm{total}} = (p, q, r)\)  
Streamlit / code: `J_total_x, J_total_y, J_total_z`

Component form (from source A; \(f,g,h\) refer to the source components of \(\mathbf{D}\)):

\[ p = u + \frac{\partial f}{\partial t},\qquad
q = v + \frac{\partial g}{\partial t},\qquad
r = w + \frac{\partial h}{\partial t} \]

**FiRSTT INTERPRETATION**  
The C-source notation \(\mathbf{J}=(p,q,r)\) meant total current.  
In the reconstructed layer the meaning is made explicit as \(\mathbf{J}_{\mathrm{total}}\).  
The original source notation itself is left unchanged.

**Status:** RESOLVED_BY_REPRESENTATION_LAYER  
(Állapot: RÉTEGEZETT ÁBRÁZOLÁSSAL KEZELVE)

---

## 6. Charge density

**Block ID:** `SYM-RHO-E`

**SOURCE**  
\(\rho_e\) = free charge density

**RECONSTRUCTED / UNIFIED**  
\(\rho_e\)  
Streamlit / code: `rho_e`

---

## 7. Material and electromagnetic parameters

**Block ID:** `SYM-PARAMS`

| Symbol | Meaning                  | Notes                                      |
|--------|--------------------------|--------------------------------------------|
| \(\mu\) | magnetic permeability   |                                            |
| \(k\)  | \(k = 1/\varepsilon\)   | used in \(\mathbf{D} = \frac{1}{4\pi k}\mathbf{E}\) |
| \(\rho\) | resistivity            | used in \(\mathbf{E} = \rho\,\mathbf{J}_{\mathrm{conduction}}\) |
| \(\rho_e\) | free charge density  | distinct from \(\rho\)                     |

Typography and code must keep \(\rho\) and \(\rho_e\) clearly separated (`rho` vs `rho_e`).

---

## 8. Velocity vector

**Block ID:** `SYM-V`

Appears in the electromotive-force equations:

\[ \mathbf{v} = \left( \frac{\partial x}{\partial t},\ \frac{\partial y}{\partial t},\ \frac{\partial z}{\partial t} \right) \]

\[ \mathbf{E} = \mu(\mathbf{v}\times\mathbf{H}) - \frac{\partial\mathbf{A}}{\partial t} - \nabla\Psi \]

---

## 9. Coordinates and time

**Block ID:** `SYM-COORDS`

- Spatial coordinates in the sources: \(x,\ y,\ z\)
- Time coordinate: \(t\)

**FiRSTT base assumption (hypothesis)**  
The project treats time as primary and investigates the theoretical emergence of space from an underlying temporal structure.  
This is recorded as a conceptual hypothesis, **not** as a proven physical fact and **not** as a mathematical consequence of the present formalism.

---

## 10. FiRSTT-specific concepts (hypothesis level)

**Block ID:** `SYM-FIRSTT-CONCEPTS`

| Concept              | Status                          | Remark |
|----------------------|---------------------------------|--------|
| Time as source       | Hypothesis                      | Central project hypothesis |
| Torsion              | Open mathematical definition    | Must be defined explicitly later |
| Spin                 | Linked to quaternion vector part| Geometric / spin-like structure |
| Longitudinal component | \(-\nabla\Psi\) highlighted   | Hypothesis-level reading |

---

## 11. Implementation convention — quaternion_v2

**Block ID:** `SYM-QUAT-IMPL`

Reference file: `quaternion_v2.py` (or `src/quaternion.py` in the Streamlit project)

The system is organised in **four strictly separated layers**:

### 11.1 Standard mathematical layer (Hamilton \(\mathbb{H}\))

Classical quaternion algebra:

\[ q = w + xi + yj + zk \]

Operations: addition, Hamilton product, conjugate, norm, inverse, rotation representation.  
This layer is **not** FiRSTT-specific.

### 11.2 FiRSTT-specific mathematical construction — torsion_product

\[ T_g(q_1,q_2)
= q_1q_2 + \frac{g}{2}(q_1q_2 - q_2q_1)
= \Bigl(1+\frac{g}{2}\Bigr)q_1q_2 - \frac{g}{2}q_2q_1 \]

**Mathematical properties** (not interpretation):
- \(g = 0\) recovers the standard Hamilton product.
- \(g \neq 0\) introduces a non-commutative correction.
- The construction utilises the commutator-like part of the quaternion product.

Registered as: **FiRSTT-specific torsional product construction**.  
Physical interpretation (spacetime torsion, etc.): **open / hypothesis**.  
It is **not** automatically identified with the standard product and is **not** claimed to be a mathematical proof of physical torsion.

Open mathematical questions:
- dimension of \(g\)
- whether \(g\) is a constant or a field
- algebraic properties and invariants
- explicit scalar and vector parts of the commutator in the decomposition \(q_1=a+\mathbf{A}\), \(q_2=b+\mathbf{B}\)

### 11.3 Numerical demonstration layer

`evolve_quaternion_field()` is a **simplified, artificial evolutionary model**.

- Performs a time-parameterised numerical step \(q(t+\Delta t)=q(t)+\ldots\)
- Is **not** a numerical solver of the Maxwell equations
- Is **not** a derivation of time → space emergence
- Must be clearly labelled as a demonstration / toy model in the Streamlit interface

### 11.4 FiRSTT physical hypothesis layer

The following statements remain at hypothesis level.  
Neither the code nor the mathematical constructions prove or derive them:

- primacy of time
- emergence of space from time
- physical relation of `torsion_product` to spacetime torsion

The implementation treats quaternions primarily as an **algebraic representation** and a **numerical computational object**.  
One must not automatically claim that the 4-tuple \((w,x,y,z)\) constitutes coordinates of a physical four-dimensional space.

### 11.5 Hierarchy summary

FiRSTT mathematical system
│
├── STANDARD MATHEMATICS
│   ├── Quaternion algebra (Hamilton ℍ)
│   └── Numerical representation (NumPy batch)
│
├── FiRSTT-SPECIFIC MATHEMATICAL CONSTRUCTION
│   └── torsion_product T_g(q₁, q₂)
│
├── NUMERICAL MODEL (demonstration)
│   └── evolve_quaternion_field()
│
└── FiRSTT PHYSICAL HYPOTHESIS
├── primacy of time
├── emergence of space
└── physical interpretation of torsion

This four-layer separation prevents a numerical result or Streamlit visualisation from being misread as a proof of the FiRSTT physical claims.

---

## 12. Summary notation table

**Block ID:** `SYM-TABLE`

| Physical quantity                        | SOURCE              | RECONSTRUCTED / UNIFIED          | Streamlit / code                 |
|------------------------------------------|---------------------|----------------------------------|----------------------------------|
| Vector potential \(\mathbf{A}\)          | \((f,g,h)\)         | \((f_A,g_A,h_A)\)                | `A_x, A_y, A_z`                  |
| Electric displacement \(\mathbf{D}\)     | \((f,g,h)\)         | \((f_D,g_D,h_D)\)                | `D_x, D_y, D_z`                  |
| Conduction current \(\mathbf{J}_{\mathrm{conduction}}\) | \((u,v,w)\) | \((u,v,w)\)                      | `J_cond_x, J_cond_y, J_cond_z`   |
| Total current \(\mathbf{J}_{\mathrm{total}}\) | \((p,q,r)\)     | \((p,q,r)\)                      | `J_total_x, J_total_y, J_total_z`|
| Electric field \(\mathbf{E}\)            | \((P,Q,R)\)         | \((P,Q,R)\)                      | `E_x, E_y, E_z`                  |
| Magnetic field \(\mathbf{H}\)            | \((\alpha,\beta,\gamma)\) | \((\alpha,\beta,\gamma)\) | `H_x, H_y, H_z`                  |
| Scalar potential                         | \(\Psi\)            | \(\Psi\)                         | `Psi`                            |
| Charge density                           | \(\rho_e\)          | \(\rho_e\)                       | `rho_e`                          |
| Resistivity                              | \(\rho\)            | \(\rho\)                         | `rho`                            |

---

## 13. Registry rules

**Block ID:** `SYM-RULES`

1. The meaning of a symbol is not changed from chapter to chapter.
2. Source collisions are not hidden by silent renaming; they are handled by layered representation.
3. Historical Maxwell notation (SOURCE), reconstructed mathematical form, and FiRSTT interpretation remain strictly separate layers.
4. Standard mathematics and FiRSTT-specific constructions are clearly distinguished.
5. The four layers of `quaternion_v2` (standard → FiRSTT construction → numerical demonstration → physical hypothesis) must not be mixed. The implementation is not regarded as physical proof and is not identified with a physical 4-D space.
6. Simulation placeholders serve mathematical illustration; their demonstration / toy character must be labelled.
7. Experimental results belong to a later, separate document.
8. Items previously marked `REVIEW_REQUIRED` are now **RESOLVED_BY_REPRESENTATION_LAYER**. The source remains unchanged; layering resolves the notational collision without claiming intentionality of the original lettering.
9. `torsion_product` is a FiRSTT-specific mathematical construction; its physical interpretation remains open / hypothesis.

---

**Document status:** permanent base document (v2.0)  
**Next possible step:** Streamlit symbol browser and equation viewer modules.
