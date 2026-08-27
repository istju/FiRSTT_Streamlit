"""
FiRSTT Streamlit Base v2
========================
Maxwell reconstruction interface with clean layered notation,
language switch (EN default), light/dark theme, and reserved
slots for FiRSTT-specific content, simulations and sources.

Run:
    streamlit run app.py
"""

from __future__ import annotations

import streamlit as st
from pathlib import Path
from typing import Dict

# ---------------------------------------------------------------------------
# Paths
# ---------------------------------------------------------------------------
BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR / "data"

SYMBOL_REGISTRY_PATH = DATA_DIR / "symbol_registry_v2.md"
EQUATION_REGISTRY_PATH = DATA_DIR / "equation_registry_v2.md"
#MAXWELL_HISTORY_PATH = DATA_DIR / "maxwell_history.md"
# A régi MAXWELL_HISTORY_PATH helyett már nem kell fix path,
# mert a page_home dinamikusan választ.

# ---------------------------------------------------------------------------
# i18n – English is the default language
# ---------------------------------------------------------------------------
TRANSLATIONS: Dict[str, Dict[str, str]] = {
    "en": {
        "app_title": "FiRSTT · Maxwell Reconstruction",
        "app_subtitle": "Quaternion-based reconstruction of Maxwell’s equations with clarified notation",
        "nav_home": "Maxwell Reconstruction",
        "nav_symbols": "Symbol Registry",
        "nav_equations": "Equation Registry",
        "nav_simulations": "Simulations",
        "nav_firstt": "FiRSTT Project",
        "nav_sources": "Sources & Acknowledgements",
        "lang_label": "Language",
        "theme_label": "Theme",
        "theme_light": "Light",
        "theme_dark": "Dark",
        "section_history": "Historical background",
        "section_symbols_overview": "Notation overview",
        "section_equations_overview": "Reconstructed equations",
        "placeholder_sim": "Simulation modules will appear here.",
        "placeholder_sim_note": "Reserved for mathematical visualisations and later 3-D field demonstrations. Currently placeholders only (SIM-A-01 … SIM-H-01).",
        "placeholder_firstt": "FiRSTT project presentation, specific equations and mathematical formalism will be placed here.",
        "placeholder_firstt_note": "This section is reserved for the FiRSTT-specific layer (hypothesis level). It is kept strictly separate from the reconstructed Maxwell equations.",
        "sources_title": "Sources & Acknowledgements",
        "sources_intro": "This interface is built on a careful, source-preserving reconstruction of Maxwell’s equations. The work draws on historical material and on collaborative clarification of notation.",
        "sources_thanks": "Acknowledgements",
        "sources_links": "Source / reference links (to be filled)",
        "layer_source": "SOURCE",
        "layer_reconstructed": "RECONSTRUCTED / UNIFIED",
        "layer_firstt": "FiRSTT INTERPRETATION",
        "status_resolved": "RESOLVED_BY_REPRESENTATION_LAYER",
        "footer": "FiRSTT Streamlit Base v2 · Layered reconstruction · Not a claim of experimental proof",
    },
    "hu": {
        "app_title": "FiRSTT · Maxwell rekonstrukció",
        "app_subtitle": "Kvaternió-alapú Maxwell-egyenletek rekonstruált, egyértelműsített jelöléssel",
        "nav_home": "Maxwell rekonstrukció",
        "nav_symbols": "Szimbólum jegyzék",
        "nav_equations": "Egyenlet jegyzék",
        "nav_simulations": "Szimulációk",
        "nav_firstt": "FiRSTT projekt",
        "nav_sources": "Források & Köszönet",
        "lang_label": "Nyelv",
        "theme_label": "Téma",
        "theme_light": "Világos",
        "theme_dark": "Sötét",
        "section_history": "Történeti háttér",
        "section_symbols_overview": "Jelölési áttekintés",
        "section_equations_overview": "Rekonstruált egyenletek",
        "placeholder_sim": "A szimulációs modulok itt fognak megjelenni.",
        "placeholder_sim_note": "Fenntartott hely a matematikai vizualizációknak és későbbi 3D mező-demonstrációknak. Jelenleg csak helyfoglalók (SIM-A-01 … SIM-H-01).",
        "placeholder_firstt": "A FiRSTT projekt bemutatása, specifikus egyenletek és matematikai formalizmus itt kap helyet.",
        "placeholder_firstt_note": "Ez a szekció a FiRSTT-specifikus rétegnek (hipotézis szint) van fenntartva. Szigorúan elkülönül a rekonstruált Maxwell-egyenletektől.",
        "sources_title": "Források & Köszönetnyilvánítás",
        "sources_intro": "Ez a felület a Maxwell-egyenletek forrásőrző, gondos rekonstrukciójára épül. A munka történeti anyagra és a jelölés közös tisztázására támaszkodik.",
        "sources_thanks": "Köszönet",
        "sources_links": "Forrás- / hivatkozási linkek (később kitöltendő)",
        "layer_source": "FORRÁS",
        "layer_reconstructed": "REKONSTRUÁLT / EGYSÉGES",
        "layer_firstt": "FiRSTT ÉRTELMEZÉS",
        "status_resolved": "RÉTEGEZETT ÁBRÁZOLÁSSAL KEZELVE",
        "footer": "FiRSTT Streamlit Base v2 · Rétegezett rekonstrukció · Nem kísérleti bizonyíték",
    },
}


def t(key: str) -> str:
    """Simple translation helper. Falls back to English."""
    lang = st.session_state.get("lang", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)


# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------
def load_markdown(path: Path) -> str:
    """Load a markdown file; return a short message if missing."""
    if path.exists():
        return path.read_text(encoding="utf-8")
    return f"*(File not found: `{path.name}`. Place it in the `data/` folder.)*"



def inject_theme_css(theme: str) -> None:
    """Stronger CSS override so the in-app Light/Dark toggle actually works
    even when the browser or OS prefers the opposite scheme.
    Also styles the sidebar collapse control and the top header bar.
    """
    if theme == "dark":
        css = """
        <style>
        /* ===== DARK ===== */
        html, body, [data-testid="stAppViewContainer"],
        .stApp, .main, .block-container {
            background-color: #0e1117 !important;
            color: #fafafa !important;
        }

        /* Header bar */
        header[data-testid="stHeader"],
        div[data-testid="stHeader"] {
            background-color: #0e1117 !important;
        }
        header[data-testid="stHeader"] *,
        div[data-testid="stHeader"] * {
            color: #e8e8e8 !important;
            fill: #e8e8e8 !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"],
        div[data-testid="stSidebar"],
        div[data-testid="stSidebar"] > div {
            background-color: #1a1d24 !important;
        }
        section[data-testid="stSidebar"] *,
        div[data-testid="stSidebar"] * {
            color: #e8e8e8 !important;
        }

        /* Collapse / expand control */
        button[kind="header"],
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapsedControl"],
        div[data-testid="stSidebarCollapsedControl"] {
            background-color: #1a1d24 !important;
            color: #e8e8e8 !important;
            border: 1px solid #444 !important;
        }
        [data-testid="collapsedControl"] svg,
        [data-testid="stSidebarCollapsedControl"] svg,
        header svg, [data-testid="stHeader"] svg {
            fill: #e8e8e8 !important;
            stroke: #e8e8e8 !important;
            color: #e8e8e8 !important;
        }

        h1, h2, h3, h4, h5, h6, p, label, span, li {
            color: #fafafa !important;
        }
        .stMarkdown, .stMarkdown p, .stCaption {
            color: #e6e6e6 !important;
        }
        div[data-testid="stExpander"] {
            background-color: #1a1d24 !important;
            border-color: #333 !important;
        }
        hr { border-color: #333 !important; }
        .block-container { padding-top: 1.5rem; }
        </style>
        """
    else:
        css = """
        <style>
        /* ===== LIGHT ===== */
        html, body, [data-testid="stAppViewContainer"],
        .stApp, .main, .block-container {
            background-color: #ffffff !important;
            color: #111111 !important;
        }

        /* Header bar */
        header[data-testid="stHeader"],
        div[data-testid="stHeader"] {
            background-color: #ffffff !important;
        }
        header[data-testid="stHeader"] *,
        div[data-testid="stHeader"] * {
            color: #111111 !important;
            fill: #111111 !important;
        }

        /* Sidebar */
        section[data-testid="stSidebar"],
        div[data-testid="stSidebar"],
        div[data-testid="stSidebar"] > div,
        section[data-testid="stSidebar"] > div {
            background-color: #f0f2f6 !important;
            background-image: none !important;
        }
        section[data-testid="stSidebar"] *,
        div[data-testid="stSidebar"] * {
            color: #111111 !important;
        }

        /* Collapse / expand control */
        button[kind="header"],
        [data-testid="collapsedControl"],
        [data-testid="stSidebarCollapsedControl"],
        div[data-testid="stSidebarCollapsedControl"] {
            background-color: #f0f2f6 !important;
            color: #111111 !important;
            border: 1px solid #ccc !important;
        }
        [data-testid="collapsedControl"] svg,
        [data-testid="stSidebarCollapsedControl"] svg,
        header svg, [data-testid="stHeader"] svg {
            fill: #111111 !important;
            stroke: #111111 !important;
            color: #111111 !important;
        }

        h1, h2, h3, h4, h5, h6, p, label, span, li {
            color: #111111 !important;
        }
        .stMarkdown, .stMarkdown p, .stCaption {
            color: #222222 !important;
        }
        div[data-testid="stExpander"] {
            background-color: #ffffff !important;
            border-color: #ddd !important;
        }
        hr { border-color: #ddd !important; }
        .block-container { padding-top: 1.5rem; }
        </style>
        """
    st.markdown(css, unsafe_allow_html=True)

# ---------------------------------------------------------------------------
# Page renderers
# ---------------------------------------------------------------------------
def page_home() -> None:
    st.header(t("nav_home"))
    st.markdown(t("app_subtitle"))

    st.subheader(t("section_history"))

    # Language-aware history file
    lang = st.session_state.get("lang", "en")
    history_path = DATA_DIR / f"maxwell_history_{lang}.md"
    history = load_markdown(history_path)
    st.markdown(history)

    st.divider()
    st.subheader(t("section_symbols_overview"))
    # ... a többi változatlan
    st.info(
        "The full layered Symbol Registry is available under the **Symbol Registry** menu. "
        "Key principle: SOURCE → RECONSTRUCTED / UNIFIED → FiRSTT INTERPRETATION remain strictly separate."
    )

    st.subheader(t("section_equations_overview"))
    st.info(
        "The 20 reconstructed equations (groups A–H) are available under the **Equation Registry** menu. "
        "Each equation carries the three-layer structure."
    )


def page_symbols() -> None:
    st.header(t("nav_symbols"))
    st.caption(
        "Layered notation: **SOURCE** → **RECONSTRUCTED / UNIFIED** → **FiRSTT INTERPRETATION**. "
        "Collisions are resolved by representation layers, not by silent renaming."
    )

    # ------------------------------------------------------------------
    # 1. Quaternion convention
    # ------------------------------------------------------------------
    with st.expander("1. Quaternion convention (standard mathematics)", expanded=False):
        st.markdown("**Block ID:** `SYM-QUAT-STD`")
        st.markdown("Classical Hamilton form:")
        st.latex(r"q = w + xi + yj + zk")
        st.markdown(
            """
| Mathematical component | Python attribute |
|------------------------|------------------|
| scalar part            | `w`              |
| \( i \)-component          | `x`              |
| \( j \)-component          | `y`              |
| \( k \)-component          | `z`              |
| vector part            | `(x, y, z)`      |
"""
        )
        st.info("This is **standard mathematics**, not FiRSTT-specific.")

    # ------------------------------------------------------------------
    # 2. Differential operator
    # ------------------------------------------------------------------
    with st.expander("2. Differential operator", expanded=False):
        st.markdown("**Block ID:** `SYM-NABLA`")
        st.markdown("Source form:")
        st.latex(
            r"\nabla = \mathbf{i}\frac{\partial}{\partial x} + \mathbf{j}\frac{\partial}{\partial y} + \mathbf{k}\frac{\partial}{\partial z}"
        )
        st.markdown("Related operator forms:")
        st.latex(
            r"\nabla\times\mathbf{A},\quad \nabla\times\mathbf{H},\quad \nabla\cdot\mathbf{D},\quad \nabla\cdot\mathbf{J}_{\mathrm{total}},\quad \nabla\cdot\mathbf{J}_{\mathrm{conduction}}"
        )

    # ------------------------------------------------------------------
    # 3. Fields and potentials
    # ------------------------------------------------------------------
    with st.expander("3. Fields and potentials", expanded=False):
        st.markdown("#### 3.1 Vector potential \( \\mathbf{A} \)")
        st.markdown("**Block ID:** `SYM-A`")
        st.markdown(f"**{t('layer_source')}**")
        st.latex(r"\mathbf{A} = (f, g, h)")
        st.markdown(f"**{t('layer_reconstructed')}**")
        st.latex(r"\mathbf{A} = (f_A, g_A, h_A)")
        st.caption("Streamlit / code: `A_x, A_y, A_z`")
        st.markdown(f"**{t('layer_firstt')}**")
        st.markdown("Appears in the magnetic force and electromotive force equations. Any deeper role together with the longitudinal component is hypothesis-level.")

        st.divider()
        st.markdown("#### 3.2 Scalar potential \( \\Psi \)")
        st.markdown("**Block ID:** `SYM-PSI`")
        st.latex(r"\Psi")
        st.caption("Streamlit / code: `Psi`")
        st.markdown("\( -\\nabla\\Psi \) appears as a highlighted longitudinal component (hypothesis-level reading).")

        st.divider()
        st.markdown("#### 3.3 Electric field \( \\mathbf{E} \)")
        st.markdown("**Block ID:** `SYM-E`")
        st.latex(r"\mathbf{E} = (P, Q, R)")
        st.caption("Streamlit / code: `E_x, E_y, E_z`")

        st.divider()
        st.markdown("#### 3.4 Magnetic field \( \\mathbf{H} \)")
        st.markdown("**Block ID:** `SYM-H`")
        st.latex(r"\mathbf{H} = (\alpha, \beta, \gamma)")
        st.caption("Streamlit / code: `H_x, H_y, H_z`")

    # ------------------------------------------------------------------
    # 4. Electric displacement D
    # ------------------------------------------------------------------
    with st.expander("4. Electric displacement \( \\mathbf{D} \)", expanded=False):
        st.markdown("**Block ID:** `SYM-D`")
        st.markdown(f"**{t('layer_source')}**")
        st.latex(r"\mathbf{D} = (f, g, h)")
        st.markdown(f"**{t('layer_reconstructed')}**")
        st.latex(r"\mathbf{D} = (f_D, g_D, h_D)")
        st.caption("Streamlit / code: `D_x, D_y, D_z`")
        st.markdown(f"**{t('layer_firstt')}**")
        st.markdown(
            "The source material used the same letters \( f,g,h \) for both \( \\mathbf{A} \) and \( \\mathbf{D} \). "
            "Layered representation resolves the collision for computation and display. "
            "It does **not** claim that the original identical lettering was intentional."
        )
        st.info("**Status:** RESOLVED_BY_REPRESENTATION_LAYER")

def page_symbols() -> None:
    st.header(t("nav_symbols"))
    lang = st.session_state.get("lang", "en")
    hu = lang == "hu"

    if hu:
        st.caption(
            "Rétegezett jelölés: **FORRÁS** → **REKONSTRUÁLT / EGYSÉGES** → **FiRSTT ÉRTELMEZÉS**. "
            "Az ütközéseket rétegezett ábrázolás oldja fel, nem csendes átnevezés."
        )
    else:
        st.caption(
            "Layered notation: **SOURCE** → **RECONSTRUCTED / UNIFIED** → **FiRSTT INTERPRETATION**. "
            "Collisions are resolved by representation layers, not by silent renaming."
        )

    # ------------------------------------------------------------------
    # 1. Quaternion convention
    # ------------------------------------------------------------------
    with st.expander(
        "1. Kvaternió konvenció (standard matematika)" if hu
        else "1. Quaternion convention (standard mathematics)",
        expanded=False,
    ):
        st.markdown("**Block ID:** `SYM-QUAT-STD`")
        st.markdown("Klasszikus Hamilton-forma:" if hu else "Classical Hamilton form:")
        st.latex(r"q = w + xi + yj + zk")
        if hu:
            st.markdown(
                """
| Matematikai komponens | Python attribútum |
|-----------------------|-------------------|
| skalár rész           | `w`               |
| \( i \)-komponens         | `x`               |
| \( j \)-komponens         | `y`               |
| \( k \)-komponens         | `z`               |
| vektor rész           | `(x, y, z)`       |
"""
            )
            st.info("Ez **standard matematika**, nem FiRSTT-specifikus.")
        else:
            st.markdown(
                """
| Mathematical component | Python attribute |
|------------------------|------------------|
| scalar part            | `w`              |
| \( i \)-component          | `x`              |
| \( j \)-component          | `y`              |
| \( k \)-component          | `z`              |
| vector part            | `(x, y, z)`      |
"""
            )
            st.info("This is **standard mathematics**, not FiRSTT-specific.")

    # ------------------------------------------------------------------
    # 2. Differential operator
    # ------------------------------------------------------------------
    with st.expander(
        "2. Differenciáloperátor" if hu else "2. Differential operator",
        expanded=False,
    ):
        st.markdown("**Block ID:** `SYM-NABLA`")
        st.markdown("Forrásforma:" if hu else "Source form:")
        st.latex(
            r"\nabla = \mathbf{i}\frac{\partial}{\partial x} + \mathbf{j}\frac{\partial}{\partial y} + \mathbf{k}\frac{\partial}{\partial z}"
        )
        st.markdown(
            "Kapcsolódó operátorformák:" if hu else "Related operator forms:"
        )
        st.latex(
            r"\nabla\times\mathbf{A},\quad \nabla\times\mathbf{H},\quad \nabla\cdot\mathbf{D},\quad \nabla\cdot\mathbf{J}_{\mathrm{total}},\quad \nabla\cdot\mathbf{J}_{\mathrm{conduction}}"
        )

    # ------------------------------------------------------------------
    # 3. Fields and potentials
    # ------------------------------------------------------------------
    with st.expander(
        "3. Mezők és potenciálok" if hu else "3. Fields and potentials",
        expanded=False,
    ):
        st.markdown(
            "#### 3.1 Vektorpotenciál **(A)**" if hu
            else "#### 3.1 Vector potential **(A)**"
        )
        st.markdown("**Block ID:** `SYM-A`")
        st.markdown(f"**{t('layer_source')}**")
        st.latex(r"\mathbf{A} = (f, g, h)")
        st.markdown(f"**{t('layer_reconstructed')}**")
        st.latex(r"\mathbf{A} = (f_A, g_A, h_A)")
        st.caption("Streamlit / code: `A_x, A_y, A_z`")
        st.markdown(f"**{t('layer_firstt')}**")
        st.markdown(
            "A mágneses erő és az elektromotoros erő egyenleteiben jelenik meg. "
            "A longitudinális komponenssel való mélyebb szerep hipotézis szintű."
            if hu else
            "Appears in the magnetic force and electromotive force equations. "
            "Any deeper role together with the longitudinal component is hypothesis-level."
        )

        st.divider()
        st.markdown(
            "#### 3.2 Skalárpotenciál \( \\Psi \)" if hu
            else "#### 3.2 Scalar potential \( \\Psi \)"
        )
        st.markdown("**Block ID:** `SYM-PSI`")
        st.latex(r"\Psi")
        st.caption("Streamlit / code: `Psi`")
        st.markdown(
            "A \( -\\nabla\\Psi \) kiemelt longitudinális komponensként jelenik meg (hipotézis szintű olvasat)."
            if hu else
            "\( -\\nabla\\Psi \) appears as a highlighted longitudinal component (hypothesis-level reading)."
        )

        st.divider()
        st.markdown(
            "#### 3.3 Elektromos térerősség \( \\mathbf{E} \)" if hu
            else "#### 3.3 Electric field \( \\mathbf{E} \)"
        )
        st.markdown("**Block ID:** `SYM-E`")
        st.latex(r"\mathbf{E} = (P, Q, R)")
        st.caption("Streamlit / code: `E_x, E_y, E_z`")

        st.divider()
        st.markdown(
            "#### 3.4 Mágneses térerősség \( \\mathbf{H} \)" if hu
            else "#### 3.4 Magnetic field \( \\mathbf{H} \)"
        )
        st.markdown("**Block ID:** `SYM-H`")
        st.latex(r"\mathbf{H} = (\alpha, \beta, \gamma)")
        st.caption("Streamlit / code: `H_x, H_y, H_z`")

    # ------------------------------------------------------------------
    # 4. Electric displacement D
    # ------------------------------------------------------------------
    with st.expander(
        "4. Elektromos elmozdulás **(D)**" if hu
        else "4. Electric displacement **(D)**",
        expanded=False,
    ):
        st.markdown("**Block ID:** `SYM-D`")
        st.markdown(f"**{t('layer_source')}**")
        st.latex(r"\mathbf{D} = (f, g, h)")
        st.markdown(f"**{t('layer_reconstructed')}**")
        st.latex(r"\mathbf{D} = (f_D, g_D, h_D)")
        st.caption("Streamlit / code: `D_x, D_y, D_z`")
        st.markdown(f"**{t('layer_firstt')}**")
        st.markdown(
            "A forrásanyag ugyanazokat az \( f,g,h \) betűket használta az **A**-hoz és a **D**-hez. "
            "A rétegezett ábrázolás feloldja az ütközést a számítás és a megjelenítés számára. "
            "**Nem** állítja, hogy az eredeti azonos betűhasználat szándékos volt."
            if hu else
            "The source material used the same letters \( f,g,h \) for both **A** and **D**. "
            "Layered representation resolves the collision for computation and display. "
            "It does **not** claim that the original identical lettering was intentional."
        )
        st.info(
            ("**Állapot:** " if hu else "**Status:** ")
            + "RESOLVED_BY_REPRESENTATION_LAYER"
        )

    # ------------------------------------------------------------------
    # 5. Currents
    # ------------------------------------------------------------------
    with st.expander(
        "5. Áramok" if hu else "5. Currents",
        expanded=False,
    ):
        st.markdown(
            "#### 5.1 Vezetési áram" if hu else "#### 5.1 Conduction current"
        )
        st.markdown("**Block ID:** `SYM-J-COND`")
        st.latex(r"\mathbf{J}_{\mathrm{conduction}} = (u, v, w)")
        st.caption("Streamlit / code: `J_cond_x, J_cond_y, J_cond_z`")

        st.divider()
        st.markdown(
            "#### 5.2 Teljes áram" if hu else "#### 5.2 Total current"
        )
        st.markdown("**Block ID:** `SYM-J-TOTAL`")
        st.markdown(f"**{t('layer_source')}**")
        if hu:
            st.markdown("- A csoport: \( \\mathbf{J}_{\\mathrm{total}} = (p, q, r) \)")
            st.markdown("- C csoport: \( \\mathbf{J} = (p, q, r) \) (a szöveg teljes áramként azonosítja)")
        else:
            st.markdown("- Group A: \( \\mathbf{J}_{\\mathrm{total}} = (p, q, r) \)")
            st.markdown("- Group C: \( \\mathbf{J} = (p, q, r) \) (text identifies it as total current)")
        st.markdown(f"**{t('layer_reconstructed')}**")
        st.latex(r"\mathbf{J}_{\mathrm{total}} = (p, q, r)")
        st.caption("Streamlit / code: `J_total_x, J_total_y, J_total_z`")
        st.latex(
            r"p = u + \frac{\partial f}{\partial t},\quad q = v + \frac{\partial g}{\partial t},\quad r = w + \frac{\partial h}{\partial t}"
        )
        st.markdown(f"**{t('layer_firstt')}**")
        st.markdown(
            "A C-forrás jelölése már a teljes áramot jelentette. "
            "A rekonstruált rétegben a jelentés explicitté válik: **J_total**. "
            "Az eredeti forrásjelölés változatlan."
            if hu else
            "The C-source notation already meant total current. "
            "In the reconstructed layer the meaning is made explicit as **J_total**. "
            "Original source notation is left unchanged."
        )
        st.info(
            ("**Állapot:** " if hu else "**Status:** ")
            + "RESOLVED_BY_REPRESENTATION_LAYER"
        )

    # -# ------------------------------------------------------------------
    # 6–8. Charge, parameters, velocity
    # ------------------------------------------------------------------
    with st.expander(
        "6–8. Töltéssűrűség, paraméterek, sebesség" if hu
        else "6–8. Charge density, parameters, velocity",
        expanded=False,
    ):
        st.markdown(
            "#### Töltéssűrűség" if hu else "#### Charge density"
        )
        st.latex(r"\rho_e")
        st.caption(
            "Streamlit / code: `rho_e`  ·  szabad töltéssűrűség" if hu
            else "Streamlit / code: `rho_e`  ·  free charge density"
        )

        st.divider()
        st.markdown(
            "#### Anyagi paraméterek" if hu else "#### Material parameters"
        )
        if hu:
            st.markdown(
                """
| Szimbólum | Jelentés | Megjegyzés |
|-----------|----------|------------|
| **mu** | mágneses permeabilitás | |
| **k** | **k = 1/eps | **D = E / (4*pi*k)** |
| **rho** | fajlagos ellenállás | **E = rho * J_conduction** |
| **rho_e** | szabad töltéssűrűség | elkülönül a **rho**-tól |
"""
            )
            st.caption("A `rho` és `rho_e` kódban és tipográfiában is legyen egyértelműen elválasztva.")
        else:
            st.markdown(
                """
| Symbol | Meaning | Notes |
|--------|---------|-------|
| **mu** | magnetic permeability | |
| **k** | **k = 1/eps | **D = E / (4*pi*k)** |
| **rho** | resistivity | **E = rho * J_conduction** |
| **rho_e** | free charge density | distinct from **rho** |
"""
            )
            st.caption("Keep `rho` and `rho_e` clearly separated in code and typography.")

        st.divider()
        st.markdown(
            "#### Sebességvektor" if hu else "#### Velocity vector"
        )
        st.latex(
            r"\mathbf{v} = \left( \frac{\partial x}{\partial t},\ \frac{\partial y}{\partial t},\ \frac{\partial z}{\partial t} \right)"
        )
        st.latex(
            r"\mathbf{E} = \mu(\mathbf{v}\times\mathbf{H}) - \frac{\partial\mathbf{A}}{\partial t} - \nabla\Psi"
        )

    # ------------------------------------------------------------------
    # 9–10. Coordinates, time, FiRSTT concepts
    # ------------------------------------------------------------------
    with st.expander(
        "9–10. Koordináták, idő és FiRSTT fogalmak (hipotézis)" if hu
        else "9–10. Coordinates, time & FiRSTT concepts (hypothesis)",
        expanded=False,
    ):
        st.markdown(
            "Térbeli koordináták: \( x,\\ y,\\ z \)  ·  Idő: \( t \)" if hu
            else "Spatial coordinates: \( x,\\ y,\\ z \)  ·  Time: \( t \)"
        )
        st.markdown(
            "**FiRSTT alapfeltevés (hipotézis):** az időt elsődlegesnek tekintjük; "
            "a tér elméleti emergenciáját egy mögöttes időbeli struktúrából vizsgáljuk. "
            "Ez **nem** bizonyított fizikai tény, és **nem** a jelen formalizmus matematikai következménye."
            if hu else
            "**FiRSTT base assumption (hypothesis):** time is treated as primary; "
            "the theoretical emergence of space from an underlying temporal structure is investigated. "
            "This is **not** a proven physical fact and **not** a mathematical consequence of the present formalism."
        )
        if hu:
            st.markdown(
                """
| Fogalom | Státusz | Megjegyzés |
|---------|---------|------------|
| Idő mint forrás | Hipotézis | A projekt központi hipotézise |
| Torzió | Nyitott matematikai definíció | Később expliciten definiálandó |
| Spin | A kvaternió vektorrészéhez kötve | Geometriai / spin-szerű struktúra |
| Longitudinális komponens | \( -\\nabla\\Psi \) kiemelve | Hipotézis szintű olvasat |
"""
            )
        else:
            st.markdown(
                """
| Concept | Status | Remark |
|---------|--------|--------|
| Time as source | Hypothesis | Central project hypothesis |
| Torsion | Open mathematical definition | Must be defined explicitly later |
| Spin | Linked to quaternion vector part | Geometric / spin-like structure |
| Longitudinal component | \( -\\nabla\\Psi \) highlighted | Hypothesis-level reading |
"""
            )

    # ------------------------------------------------------------------
    # 11. Implementation convention — quaternion_v2
    # ------------------------------------------------------------------
    with st.expander(
        "11. Implementációs konvenció — quaternion_v2 (négy réteg)" if hu
        else "11. Implementation convention — quaternion_v2 (four layers)",
        expanded=True,
    ):
        st.markdown("**Block ID:** `SYM-QUAT-IMPL`")
        st.markdown(
            "Referencia: `quaternion_v2.py` / `src/quaternion.py`" if hu
            else "Reference: `quaternion_v2.py` / `src/quaternion.py`"
        )

        st.markdown(
            "#### 11.1 Standard matematikai réteg (Hamilton \( \\mathbb{H} \))" if hu
            else "#### 11.1 Standard mathematical layer (Hamilton \( \\mathbb{H} \))"
        )
        st.latex(r"q = w + xi + yj + zk")
        st.markdown(
            "Műveletek: összeadás, Hamilton-szorzat, konjugált, norma, inverz, forgatásreprezentáció. "
            "Ez a réteg **nem** FiRSTT-specifikus."
            if hu else
            "Operations: addition, Hamilton product, conjugate, norm, inverse, rotation representation. "
            "This layer is **not** FiRSTT-specific."
        )

        st.markdown(
            "#### 11.2 FiRSTT-specifikus konstrukció — torsion_product" if hu
            else "#### 11.2 FiRSTT-specific construction — torsion_product"
        )
        st.latex(
            r"T_g(q_1,q_2) = q_1q_2 + \frac{g}{2}(q_1q_2 - q_2q_1) = \Bigl(1+\frac{g}{2}\Bigr)q_1q_2 - \frac{g}{2}q_2q_1"
        )
        if hu:
            st.markdown(
                """
**Matematikai tulajdonságok** (nem értelmezés):
- \( g = 0 \) visszaadja a standard Hamilton-szorzatot
- \( g \\neq 0 \) nemkommutatív korrekciót vezet be
- A kvaterniószorzat kommutátor-szerű részét használja

Regisztrálva mint: **FiRSTT-specifikus torziós szorzat-konstrukció**.  
Fizikai értelmezés (téridő-torzió stb.): **nyitott / hipotézis**.
"""
            )
        else:
            st.markdown(
                """
**Mathematical properties** (not interpretation):
- \( g = 0 \) recovers the standard Hamilton product
- \( g \\neq 0 \) introduces a non-commutative correction
- Utilises the commutator-like part of the quaternion product

Registered as: **FiRSTT-specific torsional product construction**.  
Physical interpretation (spacetime torsion, etc.): **open / hypothesis**.
"""
            )

        st.markdown(
            "#### 11.3 Numerikus demonstrációs réteg" if hu
            else "#### 11.3 Numerical demonstration layer"
        )
        st.markdown(
            "Az `evolve_quaternion_field()` **egyszerűsített, mesterséges evolúciós modell**. "
            "**Nem** Maxwell-solver, és **nem** az idő → tér emergencia levezetése. "
            "Demonstráció / toy model címkével kell ellátni."
            if hu else
            "`evolve_quaternion_field()` is a **simplified, artificial evolutionary model**. "
            "It is **not** a Maxwell solver and **not** a derivation of time → space emergence. "
            "Must be labelled as demonstration / toy model."
        )

        st.markdown(
            "#### 11.4 FiRSTT fizikai hipotézis réteg" if hu
            else "#### 11.4 FiRSTT physical hypothesis layer"
        )
        st.markdown(
            "Az idő elsődlegessége, a tér emergenciája és a `torsion_product` fizikai kapcsolata "
            "a téridő-torzióhoz **hipotézis** szinten marad. "
            "A kód a kvaterniókat algebrai reprezentációként és numerikus számítási objektumként kezeli."
            if hu else
            "Primacy of time, emergence of space, and physical relation of `torsion_product` "
            "to spacetime torsion remain at **hypothesis** level. "
            "The code treats quaternions as algebraic representation and numerical computational object."
        )

        st.markdown(
            "#### 11.5 Hierarchia összefoglaló" if hu else "#### 11.5 Hierarchy summary"
        )
        st.code(
            """
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
""",
            language="text",
        )

    # ------------------------------------------------------------------
    # 12-13. Summary table & rules
    # ------------------------------------------------------------------
    with st.expander(
        "12-13. Összefoglaló jelölési táblázat es jegyzékszabályok" if hu
        else "12-13. Summary notation table & registry rules",
        expanded=False,
    ):
        st.markdown(
            "#### Összefoglaló táblázat" if hu else "#### Summary table"
        )
        if hu:
            st.markdown(
                """
| Fizikai mennyiség | FORRÁS | REKONSTRUÁLT / EGYSÉGES | Streamlit / code |
|-------------------|--------|--------------------------|------------------|
| **A** (vektorpotenciáll) | (f, g, h) | (f_A, g_A, h_A) | `A_x, A_y, A_z` |
| **D** (elektromos elmozdulás) | (f, g, h) | (f_D, g_D, h_D) | `D_x, D_y, D_z` |
| **J_conduction** (vezetési áram) | (u, v, w) | (u, v, w) | `J_cond_x, ...` |
| **J_total** (teljes áram) | (p, q, r) | (p, q, r) | `J_total_x, ...` |
| **E** (elektromos térerősség) | (P, Q, R) | (P, Q, R) | `E_x, E_y, E_z` |
| **H** (mágneses térerősség) | (alpha, beta, gamma) | (alpha, beta, gamma) | `H_x, H_y, H_z` |
| **Psi** (skalárpotenciál) | Psi | Psi | `Psi` |
| **rho_e** (szabad töltéssűrűség) | rho_e | rho_e | `rho_e` |
| **rho** (fajlagos ellenállás) | rho | rho | `rho` |
"""
            )
            st.markdown("#### Fő jegyzékszabályok")
            st.markdown(
                """
1. A szimbólum jelentése fejezeteről fejezetre nem változik.
2. A forrásütközéseket rétegezett ábrázolás kezeli, nem csendes átnevezés.
3. FORRÁS / REKONSTRUÁLT / FiRSTT ÉRTELMEZÉS szigorúan elkülönül.
4. A standard matematika es a FiRSTT-specifikus konstrukciók egyértelműen elválnak.
5. A `quaternion_v2` négy rétege nem keverhető.
6. A szimulációs helyfoglalók csak matematikai illusztrációk.
7. A `torsion_product` fizikai értelmezése nyitott / hipotézis.
"""
            )
        else:
            st.markdown(
                """
| Physical quantity | SOURCE | RECONSTRUCTED / UNIFIED | Streamlit / code |
|-------------------|--------|--------------------------|------------------|
| **A** (vector potential) | (f, g, h) | (f_A, g_A, h_A) | `A_x, A_y, A_z` |
| **D** (electric displacement) | (f, g, h) | (f_D, g_D, h_D) | `D_x, D_y, D_z` |
| **J_conduction** (conduction current) | (u, v, w) | (u, v, w) | `J_cond_x, ...` |
| **J_total** (total current) | (p, q, r) | (p, q, r) | `J_total_x, ...` |
| **E** (electric field) | (P, Q, R) | (P, Q, R) | `E_x, E_y, E_z` |
| **H** (magnetic field) | (alpha, beta, gamma) | (alpha, beta, gamma) | `H_x, H_y, H_z` |
| **Psi** (scalar potential) | Psi | Psi | `Psi` |
| **rho_e** (free charge density) | rho_e | rho_e | `rho_e` |
| **rho** (resistivity) | rho | rho | `rho` |
"""
            )
            st.markdown("#### Key registry rules")
            st.markdown(
                """
1. Symbol meaning is not changed from chapter to chapter.
2. Source collisions are handled by layered representation, not silent renaming.
3. SOURCE / RECONSTRUCTED / FiRSTT INTERPRETATION remain strictly separate.
4. Standard mathematics and FiRSTT-specific constructions are clearly distinguished.
5. The four layers of `quaternion_v2` must not be mixed.
6. Simulation placeholders are mathematical illustration only.
7. `torsion_product` physical interpretation remains open / hypothesis.
"""
            )

    st.divider()
    with st.expander(
        "Teljes markdown forrás (Szimbólum jegyzék)" if hu
        else "Full markdown source (Symbol Registry)",
        expanded=False,
    ):
        content = load_markdown(SYMBOL_REGISTRY_PATH)
        st.markdown(content)
    # ------------------------------------------------------------------
    # Structured equation data (keeps layers explicit and easy to edit)
    # ------------------------------------------------------------------
    groups = [
        {
            "id": "A",
            "title": "A — Total current",
            "sim": "SIM-A-01",
            "components": [
                (r"p = u + \frac{\partial f}{\partial t}", "x-component of total current"),
                (r"q = v + \frac{\partial g}{\partial t}", "y-component of total current"),
                (r"r = w + \frac{\partial h}{\partial t}", "z-component of total current"),
            ],
            "reconstructed": r"\mathbf{J}_{\mathrm{total}} = \mathbf{J}_{\mathrm{conduction}} + \frac{\partial\mathbf{D}}{\partial t}",
            "firstt": "Total current is the sum of conduction current and displacement current. Any emphasis on the temporal change of the fields as primary is a hypothesis-level reading.",
        },
        {
            "id": "B",
            "title": "B — Magnetic force",
            "sim": "SIM-B-01",
            "components": [
                (r"\mu\alpha = \frac{\partial h}{\partial y} - \frac{\partial g}{\partial z}", ""),
                (r"\mu\beta = \frac{\partial f}{\partial z} - \frac{\partial h}{\partial x}", ""),
                (r"\mu\gamma = \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}", ""),
            ],
            "reconstructed": r"\mu\mathbf{H} = \nabla\times\mathbf{A}",
            "firstt": "Magnetic field strength is obtained from the curl of the vector potential. Possible links to torsion remain at hypothesis level.",
        },
        {
            "id": "C",
            "title": "C — Ampère–Maxwell law",
            "sim": "SIM-C-01",
            "components": [
                (r"\frac{\partial\gamma}{\partial y} - \frac{\partial\beta}{\partial z} = 4\pi p", ""),
                (r"\frac{\partial\alpha}{\partial z} - \frac{\partial\gamma}{\partial x} = 4\pi q", ""),
                (r"\frac{\partial\beta}{\partial x} - \frac{\partial\alpha}{\partial y} = 4\pi r", ""),
            ],
            "reconstructed": r"\nabla\times\mathbf{H} = 4\pi\mathbf{J}_{\mathrm{total}}",
            "firstt": "The C-source notation \( \\mathbf{J}=(p,q,r) \) already meant total current. In the reconstructed layer the meaning is made explicit as \( \\mathbf{J}_{\\mathrm{total}} \). Original source notation is left unchanged.",
            "status": "RESOLVED_BY_REPRESENTATION_LAYER",
        },
        {
            "id": "D",
            "title": "D — Electromotive force",
            "sim": "SIM-D-01",
            "components": [
                (r"P = \mu\Bigl(\gamma\frac{\partial y}{\partial t} - \beta\frac{\partial z}{\partial t}\Bigr) - \frac{\partial f}{\partial t} - \frac{\partial\Psi}{\partial x}", ""),
                (r"Q = \mu\Bigl(\alpha\frac{\partial z}{\partial t} - \gamma\frac{\partial x}{\partial t}\Bigr) - \frac{\partial g}{\partial t} - \frac{\partial\Psi}{\partial y}", ""),
                (r"R = \mu\Bigl(\beta\frac{\partial x}{\partial t} - \alpha\frac{\partial y}{\partial t}\Bigr) - \frac{\partial h}{\partial t} - \frac{\partial\Psi}{\partial z}", ""),
            ],
            "reconstructed": r"\mathbf{E} = \mu(\mathbf{v}\times\mathbf{H}) - \frac{\partial\mathbf{A}}{\partial t} - \nabla\Psi",
            "firstt": "\( -\\nabla\\Psi \) is treated as a highlighted longitudinal component. This reading is hypothesis-level, not a mathematical consequence of the source.",
        },
        {
            "id": "E",
            "title": "E — Electric displacement",
            "sim": "SIM-E-01",
            "components": [
                (r"f = \frac{1}{4\pi k}P", ""),
                (r"g = \frac{1}{4\pi k}Q", ""),
                (r"h = \frac{1}{4\pi k}R", ""),
            ],
            "reconstructed": r"\mathbf{D} = \frac{1}{4\pi k}\mathbf{E}",
            "firstt": "Source E assigns \( (f,g,h) \) to \( \\mathbf{D} \), while sources A/B/D assign the same letters to \( \\mathbf{A} \). Layered representation resolves the collision. It does **not** claim the original identical lettering was intentional.",
            "status": "RESOLVED_BY_REPRESENTATION_LAYER",
        },
        {
            "id": "F",
            "title": "F — Conduction current / local Ohm’s law",
            "sim": "SIM-F-01",
            "components": [
                (r"P = \rho u", ""),
                (r"Q = \rho v", ""),
                (r"R = \rho w", ""),
            ],
            "reconstructed": r"\mathbf{E} = \rho\,\mathbf{J}_{\mathrm{conduction}}",
            "firstt": "Local Ohm’s law. Any deeper reading of material parameters remains at hypothesis level.",
        },
        {
            "id": "G",
            "title": "G — Gauss’s law",
            "sim": "SIM-G-01",
            "components": [
                (r"\frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z} = \rho_e", ""),
            ],
            "reconstructed": r"\nabla\cdot\mathbf{D} = \rho_e",
            "firstt": "Divergence law. Possible links between charge density and the temporal origin of the fields remain hypothesis-level.",
        },
        {
            "id": "H",
            "title": "H — Continuity equation",
            "sim": "SIM-H-01",
            "components": [
                (r"\frac{\partial\rho_e}{\partial t} + \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0", ""),
            ],
            "reconstructed": r"\frac{\partial\rho_e}{\partial t} + \nabla\cdot\mathbf{J}_{\mathrm{conduction}} = 0",
            "firstt": "Expresses charge conservation. Any reading that privileges the primacy of time over spatial divergence is hypothesis-level.",
        },
    ]

    for g in groups:
        with st.expander(f"**{g['title']}**  ·  `{g['sim']}`", expanded=False):
            # SOURCE layer
            st.markdown(f"#### {t('layer_source')}")
            for latex, role in g["components"]:
                st.latex(latex)
                if role:
                    st.caption(role)

            st.divider()

def page_equations() -> None:
    st.header(t("nav_equations"))
    lang = st.session_state.get("lang", "en")

    if lang == "hu":
        st.caption(
            "Minden egyenletcsoport három szigorúan elválasztott réteget mutat: "
            "**FORRÁS** → **REKONSTRUÁLT / EGYSÉGES** → **FiRSTT ÉRTELMEZÉS**."
        )
    else:
        st.caption(
            "Each equation group shows three strictly separated layers: "
            "**SOURCE** → **RECONSTRUCTED / UNIFIED** → **FiRSTT INTERPRETATION**."
        )

    # ------------------------------------------------------------------
    # Structured equation data (bilingual titles & interpretations)
    # ------------------------------------------------------------------
    groups = [
        {
            "id": "A",
            "title_en": "A — Total current",
            "title_hu": "A — Teljes áram",
            "sim": "SIM-A-01",
            "components": [
                (r"p = u + \frac{\partial f}{\partial t}",
                 "x-component of total current",
                 "a teljes áram x-komponense"),
                (r"q = v + \frac{\partial g}{\partial t}",
                 "y-component of total current",
                 "a teljes áram y-komponense"),
                (r"r = w + \frac{\partial h}{\partial t}",
                 "z-component of total current",
                 "a teljes áram z-komponense"),
            ],
            "reconstructed": r"\mathbf{J}_{\mathrm{total}} = \mathbf{J}_{\mathrm{conduction}} + \frac{\partial\mathbf{D}}{\partial t}",
            "firstt_en": "Total current is the sum of conduction current and displacement current. Any emphasis on the temporal change of the fields as primary is a hypothesis-level reading.",
            "firstt_hu": "A teljes áram a vezetési áram és az elmozdulási áram összege. A mezők időbeli változásának elsődlegességére vonatkozó hangsúly hipotézis szintű olvasat.",
        },
        {
            "id": "B",
            "title_en": "B — Magnetic force",
            "title_hu": "B — Mágneses erő",
            "sim": "SIM-B-01",
            "components": [
                (r"\mu\alpha = \frac{\partial h}{\partial y} - \frac{\partial g}{\partial z}", "", ""),
                (r"\mu\beta = \frac{\partial f}{\partial z} - \frac{\partial h}{\partial x}", "", ""),
                (r"\mu\gamma = \frac{\partial g}{\partial x} - \frac{\partial f}{\partial y}", "", ""),
            ],
            "reconstructed": r"\mu\mathbf{H} = \nabla\times\mathbf{A}",
            "firstt_en": "Magnetic field strength is obtained from the curl of the vector potential. Possible links to torsion remain at hypothesis level.",
            "firstt_hu": "A mágneses térerősség a vektorpotenciál rotációjából adódik. A torzióval való lehetséges kapcsolat hipotézis szinten marad.",
        },
        {
            "id": "C",
            "title_en": "C — Ampère–Maxwell law",
            "title_hu": "C — Ampère–Maxwell törvény",
            "sim": "SIM-C-01",
            "components": [
                (r"\frac{\partial\gamma}{\partial y} - \frac{\partial\beta}{\partial z} = 4\pi p", "", ""),
                (r"\frac{\partial\alpha}{\partial z} - \frac{\partial\gamma}{\partial x} = 4\pi q", "", ""),
                (r"\frac{\partial\beta}{\partial x} - \frac{\partial\alpha}{\partial y} = 4\pi r", "", ""),
            ],
            "reconstructed": r"\nabla\times\mathbf{H} = 4\pi\mathbf{J}_{\mathrm{total}}",
            "firstt_en": "The C-source notation already meant total current. In the reconstructed layer the meaning is made explicit as \( \\mathbf{J}_{\\mathrm{total}} \). Original source notation is left unchanged.",
            "firstt_hu": "A C-forrás jelölése már a teljes áramot jelentette. A rekonstruált rétegben a jelentés explicitté válik: \( \\mathbf{J}_{\\mathrm{total}} \). Az eredeti forrásjelölés változatlan.",
            "status": "RESOLVED_BY_REPRESENTATION_LAYER",
        },
        {
            "id": "D",
            "title_en": "D — Electromotive force",
            "title_hu": "D — Elektromotoros erő",
            "sim": "SIM-D-01",
            "components": [
                (r"P = \mu\Bigl(\gamma\frac{\partial y}{\partial t} - \beta\frac{\partial z}{\partial t}\Bigr) - \frac{\partial f}{\partial t} - \frac{\partial\Psi}{\partial x}", "", ""),
                (r"Q = \mu\Bigl(\alpha\frac{\partial z}{\partial t} - \gamma\frac{\partial x}{\partial t}\Bigr) - \frac{\partial g}{\partial t} - \frac{\partial\Psi}{\partial y}", "", ""),
                (r"R = \mu\Bigl(\beta\frac{\partial x}{\partial t} - \alpha\frac{\partial y}{\partial t}\Bigr) - \frac{\partial h}{\partial t} - \frac{\partial\Psi}{\partial z}", "", ""),
            ],
            "reconstructed": r"\mathbf{E} = \mu(\mathbf{v}\times\mathbf{H}) - \frac{\partial\mathbf{A}}{\partial t} - \nabla\Psi",
            "firstt_en": "\( -\\nabla\\Psi \) is treated as a highlighted longitudinal component. This reading is hypothesis-level, not a mathematical consequence of the source.",
            "firstt_hu": "A \( -\\nabla\\Psi \) kiemelt longitudinális komponensként jelenik meg. Ez hipotézis szintű olvasat, nem a forrás matematikai következménye.",
        },
        {
            "id": "E",
            "title_en": "E — Electric displacement",
            "title_hu": "E — Elektromos elmozdulás",
            "sim": "SIM-E-01",
            "components": [
                (r"f = \frac{1}{4\pi k}P", "", ""),
                (r"g = \frac{1}{4\pi k}Q", "", ""),
                (r"h = \frac{1}{4\pi k}R", "", ""),
            ],
            "reconstructed": r"\mathbf{D} = \frac{1}{4\pi k}\mathbf{E}",
            "firstt_en": "Source E assigns \( (f,g,h) \) to \( \\mathbf{D} \), while sources A/B/D assign the same letters to \( \\mathbf{A} \). Layered representation resolves the collision. It does **not** claim the original identical lettering was intentional.",
            "firstt_hu": "Az E forrás a \( (f,g,h) \) betűket a \( \\mathbf{D} \)-hez rendeli, míg az A/B/D források ugyanezeket az \( \\mathbf{A} \)-hoz. A rétegezett ábrázolás feloldja az ütközést. **Nem** állítja, hogy az eredeti azonos betűhasználat szándékos volt.",
            "status": "RESOLVED_BY_REPRESENTATION_LAYER",
        },
        {
            "id": "F",
            "title_en": "F — Conduction current / local Ohm’s law",
            "title_hu": "F — Vezetési áram / lokális Ohm-törvény",
            "sim": "SIM-F-01",
            "components": [
                (r"P = \rho u", "", ""),
                (r"Q = \rho v", "", ""),
                (r"R = \rho w", "", ""),
            ],
            "reconstructed": r"\mathbf{E} = \rho\,\mathbf{J}_{\mathrm{conduction}}",
            "firstt_en": "Local Ohm’s law. Any deeper reading of material parameters remains at hypothesis level.",
            "firstt_hu": "Lokális Ohm-törvény. Az anyagi paraméterek mélyebb olvasata hipotézis szinten marad.",
        },
        {
            "id": "G",
            "title_en": "G — Gauss’s law",
            "title_hu": "G — Gauss-törvény",
            "sim": "SIM-G-01",
            "components": [
                (r"\frac{\partial f}{\partial x} + \frac{\partial g}{\partial y} + \frac{\partial h}{\partial z} = \rho_e", "", ""),
            ],
            "reconstructed": r"\nabla\cdot\mathbf{D} = \rho_e",
            "firstt_en": "Divergence law. Possible links between charge density and the temporal origin of the fields remain hypothesis-level.",
            "firstt_hu": "Divergencia-törvény. A töltéssűrűség és a mezők időbeli eredete közötti lehetséges kapcsolat hipotézis szinten marad.",
        },
        {
            "id": "H",
            "title_en": "H — Continuity equation",
            "title_hu": "H — Folytonossági egyenlet",
            "sim": "SIM-H-01",
            "components": [
                (r"\frac{\partial\rho_e}{\partial t} + \frac{\partial u}{\partial x} + \frac{\partial v}{\partial y} + \frac{\partial w}{\partial z} = 0", "", ""),
            ],
            "reconstructed": r"\frac{\partial\rho_e}{\partial t} + \nabla\cdot\mathbf{J}_{\mathrm{conduction}} = 0",
            "firstt_en": "Expresses charge conservation. Any reading that privileges the primacy of time over spatial divergence is hypothesis-level.",
            "firstt_hu": "A töltésmegmaradást fejezi ki. Az idő elsődlegességét a térbeli divergenciával szemben hangsúlyozó olvasat hipotézis szintű.",
        },
    ]

    for g in groups:
        title = g["title_hu"] if lang == "hu" else g["title_en"]
        with st.expander(f"**{title}**  ·  `{g['sim']}`", expanded=False):
            st.markdown(f"#### {t('layer_source')}")
            for item in g["components"]:
                latex, role_en, role_hu = item
                st.latex(latex)
                role = role_hu if lang == "hu" else role_en
                if role:
                    st.caption(role)

            st.divider()

            st.markdown(f"#### {t('layer_reconstructed')}")
            st.latex(g["reconstructed"])

            st.divider()

            st.markdown(f"#### {t('layer_firstt')}")
            st.markdown(g["firstt_hu"] if lang == "hu" else g["firstt_en"])

            if g.get("status"):
                status_label = "Állapot" if lang == "hu" else "Status"
                st.info(f"**{status_label}:** {g['status']}")

    st.divider()
    full_label = (
        "Teljes markdown forrás (Egyenlet jegyzék)"
        if lang == "hu"
        else "Full markdown source (Equation Registry)"
    )
    with st.expander(full_label, expanded=False):
        content = load_markdown(EQUATION_REGISTRY_PATH)
        st.markdown(content)

def page_simulations() -> None:
    st.header(t("nav_simulations"))
    st.warning(t("placeholder_sim"))
    st.markdown(t("placeholder_sim_note"))

    st.markdown("### Reserved simulation identifiers")
    st.code(
        "\n".join(
            [
                "SIM-A-01  · Total current",
                "SIM-B-01  · Magnetic force",
                "SIM-C-01  · Ampère–Maxwell",
                "SIM-D-01  · Electromotive force",
                "SIM-E-01  · Electric displacement",
                "SIM-F-01  · Conduction current / Ohm",
                "SIM-G-01  · Gauss’s law",
                "SIM-H-01  · Continuity equation",
            ]
        ),
        language="text",
    )
    st.caption(
        "These identifiers correspond to the Equation Registry. "
        "They are placeholders for future mathematical visualisations only."
    )


def page_firstt() -> None:
    st.header(t("nav_firstt"))

    lang = st.session_state.get("lang", "en")
    path = DATA_DIR / f"firstt_project_{lang}.md"
    content = load_markdown(path)
    st.markdown(content)


def page_sources() -> None:
    st.header(t("sources_title"))
    st.markdown(t("sources_intro"))

    st.subheader(t("sources_thanks"))

    lang = st.session_state.get("lang", "en")

    if lang == "hu":
        st.markdown(
            """
A jelen rekonstrukció és a tágabb FiRSTT keret inspirációt meritett a következő személyek 
munkásságából és gondolataiból:

- **Nyikolaj Kozirev**
- **Anatolij Akimov**
- **Gennagyij Sipov**
- **Albert Vejnyik**
- **Kisfaludy György** (Univerzum Egyháza)
- **Tóth Roland** (LIF Academy)

Munkájuk segitett formálni a projektben vizsgált kérdéseket és irányokat.

Az idő es a geometria kérdéseit formáló tágabb történeti és fogalmi hatások között 
**Albert Einstein** munkássága (a newtoni abszolút idő meghaladása) és az
**Einstein-Cartan-elmélet** (a spinhez kapcsolódó térido-torzió) szintén említést érdemel.
Ezek a tágabb tudományos kontextus részeként szerepelnek, nem a jelenlegi rekonstrukció 
kísérleti vagy elméleti igazolásaként.

A Maxwell-egyenletek rétegezett rekonstrukciója 
(FORRÁS -> REKONSTRUÁLT -> FiRSTT ÉRTELMEZÉS) önálló matematikai és fogalmi munka;
nem állítja a fenti szerzők támogatását, és nem kísérleti igazolasként jelenik meg.
"""
        )
        st.markdown(
            """
Tovabbi köszönet illeti azokat, akik a jelölési rétegek (FORRÁS / REKONSTRUÁLT / FiRSTT)
szigorú elválasztásában és a kvaternió-algebrai határok tisztázásában segitettek
(köztük Arcsi és a projekt beszélgetései).
"""
        )
    else:
        st.markdown(
            """
This reconstruction and the broader FiRSTT framework draw inspiration from the work
and ideas of:

- **Nikolai Kozyrev**
- **Anatoly Akimov**
- **Gennady Shipov**
- **Albert Veinik**
- **Gyorgy Kisfaludy** (Univerzum Egyhaza)
- **Roland Toth** (LIF Academy)

Their contributions helped shape questions and directions explored in this project.

Among the broader historical and conceptual influences that shaped questions about
time and geometry, the work of **Albert Einstein** (the move beyond Newtonian absolute time)
and the **Einstein-Cartan theory** (spacetime torsion linked to spin) are also acknowledged.
These are recorded as part of the wider scientific context, not as experimental or
theoretical validation of the present reconstruction.

The present layered reconstruction of Maxwell`s equations
(SOURCE -> RECONSTRUCTED -> FiRSTT INTERPRETATION) remains an independent mathematical
and conceptual effort; it does not claim endorsement by the above authors,
nor does it present experimental validation.
"""
        )
        st.markdown(
            """
Additional thanks go to those who helped keep the notation layers
(SOURCE / RECONSTRUCTED / FiRSTT) strictly separate and who clarified the boundaries
of the quaternion algebra (including Arcsi and project discussions).
"""
        )

    st.subheader(t("sources_links"))
    if lang == "hu":
        st.markdown(
            """
*Hivatkozási lista - később bővíthető:*

- Maxwell eredeti dolgozatai / értekezései
- Történeti szakirodalom az elektromágneses téregyenletek fejlődéséről 
- Kvaternio-algebra (Hamilton)
- Projekt-belső A-H forrásfájlok (nem nyilvánosak)
- A FiRSTT keret későbbi publikációi / preprintjei
"""
        )
    else:
        st.markdown(
            """
*Reference list - to be expanded later:*

- Maxwell`s original papers / treatises
- Historical secondary literature on the development of the field equations
- Quaternion algebra (Hamilton)
- Project-internal A-H source files (not public)
- Future publications or preprints of the FiRSTT framework
"""
        )

    st.subheader(t("sources_links"))
    if lang == "hu":
        st.markdown(
            """
*Hivatkozási lista - később bővíthető:*

- Maxwell eredeti dolgozatai / értekezései  
- Történeti szakirodalom az elektromágneses téregyenletek fejlődéséről  
- Kvaternió-algebra (Hamilton)  
- Projekt-belső A-H forrásfájlok (nem nyilvánosak)  
- A FiRSTT keret későbbi publikációi / preprintjei  
"""
        )
    else:
        st.markdown(
            """
*Reference list - to be expanded later:*

- Maxwell`s original papers / treatises  
- Historical secondary literature on the development of the field equations  
- Quaternion algebra (Hamilton)  
- Project-internal A-H source files (not public)  
- Future publications or preprints of the FiRSTT framework  
"""
        )


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------
def main() -> None:
    st.set_page_config(
        page_title="FiRSTT · Maxwell Reconstruction",
        page_icon="∇",
        layout="wide",
        initial_sidebar_state="expanded",
    )

    # Session defaults
    if "lang" not in st.session_state:
        st.session_state.lang = "en"
    if "theme" not in st.session_state:
        st.session_state.theme = "light"

    # Sidebar
    with st.sidebar:
        st.title("FiRSTT")
        st.caption("Maxwell reconstruction base")

        # Language
        lang = st.radio(
            t("lang_label"),
            options=["en", "hu"],
            format_func=lambda x: "English" if x == "en" else "Magyar",
            index=0 if st.session_state.lang == "en" else 1,
            key="lang_radio",
        )
        st.session_state.lang = lang

        # Theme
        theme = st.radio(
            t("theme_label"),
            options=["light", "dark"],
            format_func=lambda x: t("theme_light") if x == "light" else t("theme_dark"),
            index=0 if st.session_state.theme == "light" else 1,
            key="theme_radio",
        )
        st.session_state.theme = theme

        st.divider()

        # Navigation
        page = st.radio(
            "Navigation",
            options=[
                "home",
                "symbols",
                "equations",
                "simulations",
                "firstt",
                "sources",
            ],
            format_func=lambda x: {
                "home": t("nav_home"),
                "symbols": t("nav_symbols"),
                "equations": t("nav_equations"),
                "simulations": t("nav_simulations"),
                "firstt": t("nav_firstt"),
                "sources": t("nav_sources"),
            }[x],
            label_visibility="collapsed",
        )

    inject_theme_css(st.session_state.theme)

    # Title
    st.title(t("app_title"))
    st.caption(t("app_subtitle"))

    # Route
    if page == "home":
        page_home()
    elif page == "symbols":
        page_symbols()
    elif page == "equations":
        page_equations()
    elif page == "simulations":
        page_simulations()
    elif page == "firstt":
        page_firstt()
    elif page == "sources":
        page_sources()

    st.divider()
    st.caption(t("footer"))


if __name__ == "__main__":
    main()


            
                        
    
