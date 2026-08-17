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
MAXWELL_HISTORY_PATH = DATA_DIR / "maxwell_history.md"

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
    """Minimal custom CSS for light / dark feel beyond Streamlit defaults."""
    if theme == "dark":
        st.markdown(
            """
            <style>
            .block-container { padding-top: 1.5rem; }
            div[data-testid="stSidebar"] { background-color: #1e1e1e; }
            </style>
            """,
            unsafe_allow_html=True,
        )
    else:
        st.markdown(
            """
            <style>
            .block-container { padding-top: 1.5rem; }
            </style>
            """,
            unsafe_allow_html=True,
        )


# ---------------------------------------------------------------------------
# Page renderers
# ---------------------------------------------------------------------------
def page_home() -> None:
    st.header(t("nav_home"))
    st.markdown(t("app_subtitle"))

    st.subheader(t("section_history"))
    history = load_markdown(MAXWELL_HISTORY_PATH)
    st.markdown(history)

    st.divider()
    st.subheader(t("section_symbols_overview"))
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
    content = load_markdown(SYMBOL_REGISTRY_PATH)
    st.markdown(content, unsafe_allow_html=False)


def page_equations() -> None:
    st.header(t("nav_equations"))
    st.caption(
        "Each equation group shows three strictly separated layers: "
        "**SOURCE** → **RECONSTRUCTED / UNIFIED** → **FiRSTT INTERPRETATION**."
    )

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

            # RECONSTRUCTED layer
            st.markdown(f"#### {t('layer_reconstructed')}")
            st.latex(g["reconstructed"])

            st.divider()

            # FiRSTT layer
            st.markdown(f"#### {t('layer_firstt')}")
            st.markdown(g["firstt"])

            if g.get("status"):
                st.info(f"**Status:** {g['status']}")

    st.divider()
    with st.expander("Full markdown source (Equation Registry)", expanded=False):
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
    st.warning(t("placeholder_firstt"))
    st.markdown(t("placeholder_firstt_note"))

    st.markdown("### Reserved future blocks")
    st.markdown(
        """
        - FiRSTT project introduction  
        - FiRSTT-specific equations  
        - Mathematical formalism (torsion product, hierarchy)  
        - Later experimental documentation slots  
        - Integration point for the quaternion class (`src/quaternion.py`)
        """
    )


def page_sources() -> None:
    st.header(t("sources_title"))
    st.markdown(t("sources_intro"))

    st.subheader(t("sources_thanks"))
    st.markdown(
        """
        - Collaborative clarification of the A–H source notation and the layered representation scheme.  
        - Review and precise boundary-setting between standard Hamilton quaternion algebra,  
          the FiRSTT-specific `torsion_product` construction, numerical demonstration code,  
          and physical hypothesis (Arcsi and project discussions).  
        - All contributors who helped keep SOURCE, RECONSTRUCTED and FiRSTT INTERPRETATION layers distinct.
        """
    )

    st.subheader(t("sources_links"))
    st.markdown(
        """
        *Placeholder list – replace with real references later:*

        - Maxwell’s original papers / treatises (links to be added)  
        - Historical secondary literature on the development of the field equations  
        - Quaternion algebra references (Hamilton)  
        - Project-internal A–H source files (not public)  
        - Future publications or preprints of the FiRSTT framework  

        You can edit this section directly in `app.py` or move the content into a dedicated  
        `data/sources.md` file when the reference list grows.
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
