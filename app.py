import streamlit as st
from pathlib import Path

# ============================================================
# FiRSTT Streamlit Base v2
# Maxwell–Quaternion Reconstruction
# ============================================================

BASE = Path(__file__).parent
DATA = BASE / "data"

st.set_page_config(
    page_title="FiRSTT — Maxwell Reconstruction",
    page_icon="∿",
    layout="wide"
)


# ============================================================
# LANGUAGE
# ============================================================

if "language" not in st.session_state:
    st.session_state.language = "HU"

st.sidebar.header("🌐 Language / Nyelv")

language = st.sidebar.radio(
    "Válassz nyelvet / Select language:",
    ["HU", "EN"],
    index=0 if st.session_state.language == "HU" else 1,
    horizontal=True
)

st.session_state.language = language


# ============================================================
# FILE LOADER
# ============================================================

def load(name):
    path = DATA / name

    if not path.exists():
        return f"⚠️ Dokumentum nem található: `{name}`"

    return path.read_text(encoding="utf-8")


# ============================================================
# LANGUAGE DEPENDENT FILES
# ============================================================

if language == "HU":

    MAXWELL_FILE = "maxwell_history.md"
    EQUATION_FILE = "equation_registry_v2.md"
    SYMBOL_FILE = "symbol_registry_v2.md"

    PAGE_TITLE = "FiRSTT — Maxwell–kvaternió rekonstrukció"

    APP_CAPTION = (
        "Kiindulási dokumentáció • történeti háttér • "
        "jelölési és egyenlet-regiszter"
    )

    TAB_OVERVIEW = "Áttekintés"
    TAB_MAXWELL = "Maxwell — történeti háttér"
    TAB_EQUATIONS = "Egyenletek"
    TAB_SYMBOLS = "Jelölések"
    TAB_QUATERNION = "Kvaternió-alap"
    TAB_SIMULATION = "Szimulációk"

else:

    MAXWELL_FILE = "maxwell_history_en.md"
    EQUATION_FILE = "equation_registry_v2_en.md"
    SYMBOL_FILE = "symbol_registry_v2_en.md"

    PAGE_TITLE = "FiRSTT — Maxwell–Quaternion Reconstruction"

    APP_CAPTION = (
        "Foundational documentation • historical background • "
        "symbol and equation registry"
    )

    TAB_OVERVIEW = "Overview"
    TAB_MAXWELL = "Maxwell — historical background"
    TAB_EQUATIONS = "Equations"
    TAB_SYMBOLS = "Symbols"
    TAB_QUATERNION = "Quaternion foundation"
    TAB_SIMULATION = "Simulations"


# ============================================================
# HEADER
# ============================================================

st.title(PAGE_TITLE)
st.caption(APP_CAPTION)


# ============================================================
# INTRODUCTION
# ============================================================

if language == "HU":

    st.markdown(
        """
> **Cél:** egyetlen, áttekinthető helyen megmutatni azt a
> matematikai kiindulási rendszert, amelyből a FiRSTT gondolkodási
> kerete elindul.
>
> Ez az oldal **nem állítja, hogy a FiRSTT hipotézisei bizonyítottak**.
> A történeti Maxwell-anyag, a rekonstruált matematikai alak és a
> FiRSTT értelmezési lehetősége külön rétegben jelenik meg.
"""
    )

else:

    st.markdown(
        """
> **Purpose:** to provide a single, structured view of the
> mathematical starting system from which the FiRSTT conceptual
> framework emerged.
>
> This page **does not claim that the FiRSTT hypotheses are proven**.
> The historical Maxwell material, the reconstructed mathematical
> form, and the possible FiRSTT interpretations are presented as
> separate layers.
"""
    )


# ============================================================
# TABS
# ============================================================

tabs = st.tabs(
    [
        TAB_OVERVIEW,
        TAB_MAXWELL,
        TAB_EQUATIONS,
        TAB_SYMBOLS,
        TAB_QUATERNION,
        TAB_SIMULATION,
    ]
)


# ============================================================
# TAB 1 — OVERVIEW
# ============================================================

with tabs[0]:

    if language == "HU":

        st.header("A kiindulási pont")

        st.markdown(
            """
A projekt jelen dokumentációs rétege nem a teljes FiRSTT-elmélet
publikálása.

A cél a **kiindulási matematikai rendszer dokumentálása Maxwell
munkájának tiszteletben tartásával**, valamint annak megmutatása,
hogy a kvaterniós formalizmus milyen további vizsgálati lehetőségeket
kínálhat.

### Rétegek

1. **Történeti / forrásréteg** — mit ír és milyen jelöléseket használ a forrás.
2. **Rekonstruált matematikai réteg** — egységesített, számítható jelölés.
3. **FiRSTT-értelmezési réteg** — lehetséges értelmezési irányok, nem bizonyítás.
4. **Numerikus / szimulációs réteg** — későbbi vizsgálatok helye.

A mostani Streamlit-verzió szándékosan dokumentációs alap.

A szimulációk helye fenn van tartva, de nincs kész fizikai modellként
bemutatva.
"""
        )

    else:

        st.header("The starting point")

        st.markdown(
            """
The current documentation layer of the project is not intended to
publish the complete FiRSTT theory.

Its purpose is to **document the mathematical starting system while
respecting Maxwell's work**, and to show what further investigative
possibilities may be offered by a quaternionic formalism.

### Layers

1. **Historical / source layer** — what the sources state and which notation they use.
2. **Reconstructed mathematical layer** — unified and computable notation.
3. **FiRSTT interpretation layer** — possible interpretations, not proofs.
4. **Numerical / simulation layer** — reserved for later investigation.

The current Streamlit version is deliberately a documentation base.

The simulation layer is reserved, but is not presented as a completed
physical model.
"""
        )


# ============================================================
# TAB 2 — MAXWELL HISTORY
# ============================================================

with tabs[1]:

    st.header(TAB_MAXWELL)

    st.markdown(
        load(MAXWELL_FILE)
    )


# ============================================================
# TAB 3 — EQUATION REGISTRY
# ============================================================

with tabs[2]:

    if language == "HU":
        st.header("FiRSTT Equation Registry v2")
        st.caption(
            "A–H forrásokból rekonstruált egyenletrendszer — "
            "LaTeX matematikai megjelenítéssel"
        )
    else:
        st.header("FiRSTT Equation Registry v2")
        st.caption(
            "Equation system reconstructed from sources A–H — "
            "LaTeX mathematical rendering"
        )

    # --------------------------------------------------------
    # IMPORTANT:
    # Equation Registry is rendered directly as Markdown.
    # Streamlit automatically renders:
    #
    # \[
    # equation
    # \]
    #
    # and
    #
    # $$
    # equation
    # $$
    #
    # as LaTeX.
    # --------------------------------------------------------

    equation_text = load(EQUATION_FILE)

    st.markdown(
        equation_text
    )


# ============================================================
# TAB 4 — SYMBOL REGISTRY
# ============================================================

with tabs[3]:

    st.header(
        "FiRSTT Symbol Registry v2.0"
    )

    st.markdown(
        load(SYMBOL_FILE)
    )


# ============================================================
# TAB 5 — QUATERNION FOUNDATION
# ============================================================

with tabs[4]:

    if language == "HU":

        st.header("Kvaternió-alap")

        st.markdown(
            r"""
A dokumentációs alap a Hamilton-féle kvaternió:

\[
q=w+xi+yj+zk.
\]

Komponensenként:

\[
q\leftrightarrow(w,x,y,z).
\]

A kvaternió itt **algebrai reprezentáció és számítási eszköz**,
nem automatikusan fizikai négydimenziós koordinátarendszer.

### Hamilton-féle szorzás

\[
\begin{aligned}
w &= w_1w_2-x_1x_2-y_1y_2-z_1z_2,\\
x &= w_1x_2+x_1w_2+y_1z_2-z_1y_2,\\
y &= w_1y_2-x_1z_2+y_1w_2+z_1x_2,\\
z &= w_1z_2+x_1y_2-y_1x_2+z_1w_2.
\end{aligned}
\]

A teljes, fejlesztés alatt álló `quaternion_v2.py` külön marad.

Ez az oldal az alapvető matematikai struktúrát dokumentálja;
nem publikálja a fejlesztés alatt álló teljes numerikus implementációt.
"""
        )

    else:

        st.header("Quaternion foundation")

        st.markdown(
            r"""
The mathematical foundation is the Hamilton quaternion:

\[
q=w+xi+yj+zk.
\]

Component representation:

\[
q\leftrightarrow(w,x,y,z).
\]

Here the quaternion is treated as an **algebraic representation and
computational object**, not automatically as a physical four-dimensional
coordinate system.

### Hamilton product

\[
\begin{aligned}
w &= w_1w_2-x_1x_2-y_1y_2-z_1z_2,\\
x &= w_1x_2+x_1w_2+y_1z_2-z_1y_2,\\
y &= w_1y_2-x_1z_2+y_1w_2+z_1x_2,\\
z &= w_1z_2+x_1y_2-y_1x_2+z_1w_2.
\end{aligned}
\]

The complete `quaternion_v2.py` implementation under development
remains separate.

This page documents the fundamental mathematical structure without
publishing the complete experimental numerical implementation.
"""
        )


# ============================================================
# TAB 6 — SIMULATION LAB
# ============================================================

with tabs[5]:

    if language == "HU":

        st.header("Szimulációs labor — fenntartott hely")

        st.info(
            "A szimulációs modul ebben a verzióban szándékosan nincs implementálva."
        )

        st.markdown(
            """
Ide kerülhetnek később:

- kvaterniómezők,
- komponensvizsgálatok,
- nemkommutatív műveletek,
- torziós konstrukciók,
- 3D vektor- és mezőábrázolás,
- a rekonstruált egyenletrendszer numerikus tesztjei,
- interaktív paraméterezés.

### Fontos

A szimulációs réteg **demonstrációs / kutatási eszköz**.

Egy numerikus demonstráció önmagában nem fizikai bizonyítás.
"""
        )

    else:

        st.header("Simulation laboratory — reserved")

        st.info(
            "The simulation module is intentionally not implemented in this version."
        )

        st.markdown(
            """
Future modules may include:

- quaternion fields,
- component analysis,
- non-commutative operations,
- torsion constructions,
- 3D vector and field visualization,
- numerical tests of the reconstructed equation system,
- interactive parameter exploration.

### Important

The simulation layer is a **demonstration / research tool**.

A numerical demonstration by itself does not constitute physical proof.
"""
        )


# ============================================================
# SIDEBAR
# ============================================================

st.sidebar.markdown("---")

if language == "HU":

    st.sidebar.header("FiRSTT Streamlit Base v2")

    st.sidebar.markdown(
        """
**Dokumentációs alap**

- Maxwell történeti háttér
- Equation Registry v2
- Symbol Registry v2
- kvaternió-alap
- fenntartott szimulációs labor
"""
    )

else:

    st.sidebar.header("FiRSTT Streamlit Base v2")

    st.sidebar.markdown(
        """
**Documentation foundation**

- Maxwell historical background
- Equation Registry v2
- Symbol Registry v2
- quaternion foundation
- reserved simulation laboratory
"""
    )

st.sidebar.markdown("---")

st.sidebar.caption(
    "FiRSTT — Foundational Mathematical Documentation"
)
