# FiRSTT Equation Registry v2.0

**Status:** permanent base document  
**Language:** Hungarian (English translation layer planned)  
**Purpose:** Unified identification of the 20 reconstructed equations, preservation of source mathematical form, and clean mapping to later LaTeX / Python / Streamlit layers.

> **Core principle**  
> The equations document the reconstruction according to the available A–H source files.  
> The registry does **not** judge historical correctness or physical validation in advance.
>
> Every equation is presented in three strictly separated blocks:
>
> 1. **SOURCE** — original component form (unchanged)
> 2. **RECONSTRUCTED / UNIFIED** — normalised operator form for mathematical clarity
> 3. **FiRSTT INTERPRETATION** — hypothesis-level reading (not a mathematical consequence)
>
> Layering resolves notational collisions. It does **not** prove that the original A–H lettering was historically or mathematically intentional.

---

## A — Total current

**Group ID:** `EQ-A`  
**Simulation placeholder:** `SIM-A-01`

### EQ-A-01

**SOURCE**

$$
p = u + \frac{\partial f}{\partial t}
$$

Role: x-component of total current.  
(The letter $f$ belongs to the source components of $\mathbf{D}$.)

### EQ-A-02

**SOURCE**

$$
q = v + \frac{\partial g}{\partial t}
$$

Role: y-component of total current.

### EQ-A-03

**SOURCE**

$$
r = w + \frac{\partial h}{\partial t}
$$

Role: z-component of total current.

**RECONSTRUCTED / UNIFIED**

$$
\mathbf{J}_{\mathrm{total}}
=
\mathbf{J}_{\mathrm{conduction}}
+
\frac{\partial\mathbf{D}}{\partial t}
$$

**FiRSTT INTERPRETATION**  
Total current is the sum of conduction current and displacement current.  
Any emphasis on the temporal change of the fields as primary is a hypothesis-level reading.

---

## B — Magnetic force

**Group ID:** `EQ-B`  
**Simulation placeholder:** `SIM-B-01`

### EQ-B-01

**SOURCE**

$$
\mu\alpha = \frac{\partial h}{\partial y} - \frac{\partial g}{\partial z}
$$

### EQ-B-02

**SOURCE**

$$
\mu\beta = \frac{\partial f}{\partial z} - \frac{\partial h}{\partial x}
$$

### EQ-B-03

**SOURCE**

$$
\mu\gamma = \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}
$$

**RECONSTRUCTED / UNIFIED**

$$
\mu\mathbf{H} = \nabla\times\mathbf{A}
$$

(The letters $f,g,h$ here belong to the source components of $\mathbf{A}$.)

**FiRSTT INTERPRETATION**  
Magnetic field strength is obtained from the curl of the vector potential.  
Possible links to torsion remain at hypothesis level.

---

## C — Ampère–Maxwell law

**Group ID:** `EQ-C`  
**Simulation placeholder:** `SIM-C-01`

### EQ-C-01

**SOURCE**

$$
\frac{\partial\gamma}{\partial y} - \frac{\partial\beta}{\partial z} = 4\pi p
$$

### EQ-C-02

**SOURCE**

$$
\frac{\partial\alpha}{\partial z} - \frac{\partial\gamma}{\partial x} = 4\pi q
$$

### EQ-C-03

**SOURCE**

$$
\frac{\partial\beta}{\partial x} - \frac{\partial\alpha}{\partial y} = 4\pi r
$$

**RECONSTRUCTED / UNIFIED**

$$
\nabla\times\mathbf{H} = 4\pi\mathbf{J}_{\mathrm{total}}
$$

**FiRSTT INTERPRETATION**  
The C-source notation $\mathbf{J}=(p,q,r)$ already meant total current.  
In the reconstructed layer the meaning is made explicit as $\mathbf{J}_{\mathrm{total}}$.  
The original source notation itself is left unchanged.

**Status:** RESOLVED_BY_REPRESENTATION_LAYER  
(Állapot: RÉTEGEZETT ÁBRÁZOLÁSSAL KEZELVE)

---

## D — Electromotive force

**Group ID:** `EQ-D`  
**Simulation placeholder:** `SIM-D-01`

### EQ-D-01

**SOURCE**

$$
P = \mu\Bigl(\gamma\frac{\partial y}{\partial t} - \beta\frac{\partial z}{\partial t}\Bigr)
- \frac{\partial f}{\partial t} - \frac{\partial\Psi}{\partial x}
$$

### EQ-D-02

**SOURCE**

$$
Q = \mu\Bigl(\alpha\frac{\partial z}{\partial t} - \gamma\frac{\partial x}{\partial t}\Bigr)
- \frac{\partial g}{\partial t} - \frac{\partial\Psi}{\partial y}
$$

### EQ-D-03

**SOURCE**

$$
R = \mu\Bigl(\beta\frac{\partial x}{\partial t} - \alpha\frac{\partial y}{\partial t}\Bigr)
- \frac{\partial h}{\partial t} - \frac{\partial\Psi}{\partial z}
$$

**RECONSTRUCTED / UNIFIED**

$$
\mathbf{E}
=
\mu(\mathbf{v}\times\mathbf{H})
-
\frac{\partial\mathbf{A}}{\partial t}
-
\nabla\Psi
$$

where

$$
\mathbf{v}
=
\Bigl(
\frac{\partial x}{\partial t},\ 
\frac{\partial y}{\partial t},\ 
\frac{\partial z}{\partial t}
\Bigr)
$$

(The letters $f,g,h$ here belong to the source components of $\mathbf{A}$.)

**FiRSTT INTERPRETATION**  
$-\nabla\Psi$ is treated as a highlighted longitudinal component.  
This reading is hypothesis-level, not a mathematical consequence of the source.

---

## E — Electric displacement

**Group ID:** `EQ-E`  
**Simulation placeholder:** `SIM-E-01`

### EQ-E-01

**SOURCE**

$$
f = \frac{1}{4\pi k}P
$$

### EQ-E-02

**SOURCE**

$$
g = \frac{1}{4\pi k}Q
$$

### EQ-E-03

**SOURCE**

$$
h = \frac{1}{4\pi k}R
$$

**RECONSTRUCTED / UNIFIED**

$$
\mathbf{D} = \frac{1}{4\pi k}\mathbf{E}
$$

with

$$
k = \frac{1}{\varepsilon}
$$

**FiRSTT INTERPRETATION**  
Source E assigns (f,g,h) to **D**, while sources A/B/D assign the same letters to **A**.  
Layered representation resolves the collision for display and computation.  
It does **not** claim that the original identical lettering was intentional.

**Status:** RESOLVED_BY_REPRESENTATION_LAYER  
(Állapot: RÉTEGEZETT ÁBRÁZOLÁSSAL KEZELVE)

---

## F — Conduction current / local Ohm’s law

**Group ID:** `EQ-F`  
**Simulation placeholder:** `SIM-F-01`

### EQ-F-01

**SOURCE**

$$
P = \rho u
$$

### EQ-F-02

**SOURCE**

$$
Q = \rho v
$$

### EQ-F-03

**SOURCE**

$$
R = \rho w
$$

**RECONSTRUCTED / UNIFIED**

$$
\mathbf{E} = \rho\,\mathbf{J}_{\mathrm{conduction}}
$$

where the source defines

$$
\mathbf{J}_{\mathrm{conduction}} = (u,v,w)
$$

**FiRSTT INTERPRETATION**  
Local Ohm’s law.  
Any deeper reading of material parameters remains at hypothesis level.

---

## G — Gauss’s law

**Group ID:** `EQ-G`  
**Simulation placeholder:** `SIM-G-01`

### EQ-G-01

**SOURCE**

$$
\frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z} = \rho_e
$$

**RECONSTRUCTED / UNIFIED**

$$
\nabla\cdot\mathbf{D} = \rho_e
$$

(The letters $f,g,h$ here belong to the source components of $\mathbf{D}$.)

**FiRSTT INTERPRETATION**  
Divergence law.  
Possible links between charge density and the temporal origin of the fields remain hypothesis-level.

---

## H — Continuity equation

**Group ID:** `EQ-H`  
**Simulation placeholder:** `SIM-H-01`

### EQ-H-01

**SOURCE**

$$
\frac{\partial\rho_e}{\partial t}
+
\frac{\partial u}{\partial x}
+
\frac{\partial v}{\partial y}
+
\frac{\partial w}{\partial z}
= 0
$$

**RECONSTRUCTED / UNIFIED**

$$
\frac{\partial\rho_e}{\partial t}
+
\nabla\cdot\mathbf{J}_{\mathrm{conduction}}
= 0
$$

(The source uses $\mathbf{J}=(u,v,w)$ for conduction current; the reconstructed form uses the full name.)

**FiRSTT INTERPRETATION**  
Expresses charge conservation.  
Any reading that privileges the primacy of time over spatial divergence is hypothesis-level.

---

## Summary index of the 20 equations

**Block ID:** `EQ-INDEX`

| ID  | Group                | Count | Main reconstructed relation                                      |
|-----|----------------------|-------|------------------------------------------------------------------|
| A   | Total current        | 3     | $\mathbf{J}_{\mathrm{total}}=\mathbf{J}_{\mathrm{conduction}}+\partial_t\mathbf{D}$ |
| B   | Magnetic force       | 3     | $\mu\mathbf{H}=\nabla\times\mathbf{A}$                         |
| C   | Ampère–Maxwell       | 3     | $\nabla\times\mathbf{H}=4\pi\mathbf{J}_{\mathrm{total}}$        |
| D   | Electromotive force  | 3     | $\mathbf{E}=\mu(\mathbf{v}\times\mathbf{H})-\partial_t\mathbf{A}-\nabla\Psi$ |
| E   | Electric displacement| 3     | $\mathbf{D}=(4\pi k)^{-1}\mathbf{E}$                           |
| F   | Conduction current   | 3     | $\mathbf{E}=\rho\,\mathbf{J}_{\mathrm{conduction}}$             |
| G   | Gauss                | 1     | $\nabla\cdot\mathbf{D}=\rho_e$                                 |
| H   | Continuity           | 1     | $\partial_t\rho_e+\nabla\cdot\mathbf{J}_{\mathrm{conduction}}=0$ |
|     | **Total**            | **20**|                                                                  |

---

## Mapping to Streamlit / simulation layer

**Block ID:** `EQ-SIM-MAP`

Every equation group has a reserved identifier:

$$
\mathrm{EQ\text{-}A\text{-}01}\ \leftrightarrow\ \mathrm{SIM\text{-}A\text{-}01}
$$

(and similarly for the other groups).

The `SIM-*` identifiers are currently **placeholders**, not experimental results.

Intended pipeline for later mathematical Streamlit modules:

$$
\text{equation}
\ \rightarrow\
\text{numerical representation}
\ \rightarrow\
\text{mathematical visualisation}
$$

A simulation does **not** by itself constitute experimental evidence.

---

## Source-preservation and layering rules

**Block ID:** `EQ-RULES`

1. Every EQ identifier carries three strictly separated blocks:  
   **SOURCE** → **RECONSTRUCTED / UNIFIED** → **FiRSTT INTERPRETATION**.
2. These three layers must never be mixed.
3. FiRSTT interpretation is a **hypothesis**, not an automatic physical claim derived from the mathematics.
4. Layering resolves notational collisions; it does not prove intentionality of the original source lettering.
5. Simulation placeholders remain clearly labelled as mathematical illustration / demonstration.

---

**Document status:** permanent base document (v2.0)  
**Related document:** FiRSTT Symbol Registry v2.0  
**Next possible step:** Streamlit equation viewer and symbol browser modules.

