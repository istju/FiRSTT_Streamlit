import streamlit as st
from pathlib import Path

# ============================================================
# FiRSTT Streamlit Base
# ============================================================

BASE = Path(__file__).parent
DATA = BASE / "data"

st.set_page_config(
    page_title="FiRSTT — Maxwell rekonstrukció",
    page_icon="∿",
    layout="wide"
)


# ============================================================
# Nyelvválasztás
# ============================================================

st.sidebar.header("FiRSTT Streamlit Base v2")

language = st.sidebar.radio(
    "Nyelv / Language",
    ["🇭🇺 Magyar", "🇬🇧 English"],
    index=0
)

if language == "🇭🇺 Magyar":
    lang = "hu"
else:
    lang = "en"


# ============================================================
# Dokumentumbetöltés
# ============================================================

DOCUMENTS = {
    "maxwell_history": {
        "hu": "maxwell_history.md",
        "en": "maxwell_history_en.md",
    },
    "equation_registry": {
        "hu": "equation_registry_v2.md",
        "en": "equation_registry_v2_en.md",
    },
    "symbol_registry": {
        "hu": "symbol_registry_v2.md",
        "en": "symbol_registry_v2_en.md",
    },
}


def load_document(name):
    """
    Dokumentum betöltése a kiválasztott nyelven.

    Ha az angol változat még nincs fenn, az alkalmazás
    nem omlik össze, hanem jelzi a hiányzó dokumentumot.
    """
    filename = DOCUMENTS[name][lang]
    path = DATA / filename

    if not path.exists():
        if lang == "en":
            st.warning(
                f"English version is not available yet:\n\n`{filename}`"
            )
        else:
            st.warning(
                f"A dokumentum nem található:\n\n`{filename}`"
            )
        return ""

    return path.read_text(encoding="utf-8")


# ============================================================
# Cím és bevezetés
# ============================================================

if lang == "hu":

    st.title("FiRSTT — Maxwell–kvaternió rekonstrukció")

    st.caption(
        "Kiindulási dokumentáció • történeti háttér • "
        "jelölési és egyenlet-regiszter"
    )

    st.markdown(
        """
        > **Cél:** egyetlen, áttekinthető helyen megmutatni azt a
        > matematikai kiindulási rendszert, amelyből a FiRSTT
        > gondolkodási kerete elindul.
        >
        > Ez az oldal **nem állítja, hogy a FiRSTT hipotézisei
        > bizonyítottak**. A történeti Maxwell-anyag, a rekonstruált
        > matematikai alak és a FiRSTT értelmezési lehetősége külön
        > rétegben jelenik meg.
        """
    )

else:

    st.title("FiRSTT — Maxwell–Quaternion Reconstruction")

    st.caption(
        "Foundational documentation • historical background • "
        "symbol and equation registries"
    )

    st.markdown(
        """
        > **Purpose:** to present, in one accessible place, the
        > mathematical starting system from which the FiRSTT
        > conceptual framework emerged.
        >
        > This page **does not claim that the FiRSTT hypotheses
        > are proven**. The historical Maxwell material, the
        > reconstructed mathematical form, and the possible FiRSTT
        > interpretations are presented as separate layers.
        """
    )


# ============================================================
# Fülek
# ============================================================

if lang == "hu":

    tabs = st.tabs([
        "Áttekintés",
        "Maxwell — történeti háttér",
        "Egyenletek",
        "Jelölések",
        "Kvaternió-alap",
        "Szimulációk"
    ])

else:

    tabs = st.tabs([
        "Overview",
        "Maxwell — Historical Background",
        "Equations",
        "Symbols",
        "Quaternion Foundation",
        "Simulations"
    ])


# ============================================================
# 1. Áttekintés
# ============================================================

with tabs[0]:

    if lang == "hu":

        st.header("A kiindulási pont")

        st.markdown(
            """
            A projekt jelen dokumentációs rétege nem a teljes
            FiRSTT-elmélet publikálása. A cél a
            **kiindulási matematikai rendszer dokumentálása**
            Maxwell munkájának tiszteletben tartásával, valamint
            annak megmutatása, hogy a kvaterniós formalizmus
            milyen további vizsgálati lehetőségeket kínálhat.

            ### Rétegek

            1. **Történeti / forrásréteg** — mit ír és milyen
               jelöléseket használ a forrás.
            2. **Rekonstruált matematikai réteg** —
               egységesített, számítható jelölés.
            3. **FiRSTT-értelmezési réteg** — lehetséges
               értelmezési irányok, nem bizonyítás.
            4. **Numerikus / szimulációs réteg** — későbbi
               vizsgálatok helye.

            A mostani Streamlit-verzió szándékosan dokumentációs
            alap. A szimulációk helye fenn van tartva, de nincs
            kész fizikai modellként bemutatva.
            """
        )

    else:

        st.header("The Starting Point")

        st.markdown(
            """
            The present documentation layer of the project is
            **not a publication of the complete FiRSTT theory**.
            Its purpose is to document the **mathematical starting
            system**, with respect for Maxwell's work, and to show
            what further investigative possibilities the quaternion
            formalism may offer.

            ### Layers

            1. **Historical / source layer** — what the source
               states and which notation it uses.
            2. **Reconstructed mathematical layer** — unified,
               computationally usable notation.
            3. **FiRSTT interpretation layer** — possible
               interpretive directions, not proofs.
            4. **Numerical / simulation layer** — reserved for
               future investigations.

            This Streamlit version is intentionally a documentation
            foundation. The simulation area is reserved, but is not
            presented as a completed physical model.
            """
        )


# ============================================================
# 2. Maxwell történeti háttér
# ============================================================

with tabs[1]:

    if lang == "hu":
        st.header("Maxwell — történeti háttér")
    else:
        st.header("Maxwell — Historical Background")

    content = load_document("maxwell_history")

    if content:
        st.markdown(content)


# ============================================================
# 3. Equation Registry
# ============================================================

with tabs[2]:

    if lang == "hu":
        st.header("FiRSTT Equation Registry v2")
    else:
        st.header("FiRSTT Equation Registry v2")

    content = load_document("equation_registry")

    if content:
        st.markdown(content)


# ============================================================
# 4. Symbol Registry
# ============================================================

with tabs[3]:

    if lang == "hu":
        st.header("FiRSTT Symbol Registry v2.0")
    else:
        st.header("FiRSTT Symbol Registry v2.0")

    content = load_document("symbol_registry")

    if content:
        st.markdown(content)


# ============================================================
# 5. Kvaternió-alap
# ============================================================

with tabs[4]:

    if lang == "hu":

        st.header("Kvaternió-alap")

        st.markdown(
            r"""
            A dokumentációs alap a Hamilton-féle kvaternió:

            $$q = w + xi + yj + zk.$$

            A kvaternió itt **algebrai reprezentáció és
            számítási eszköz**, nem automatikusan fizikai
            négydimenziós koordinátarendszer.

            A teljes, fejlesztés alatt álló `quaternion_v2.py`
            külön marad; ez az oldal csak az alapfogalmakat
            dokumentálja.
            """
        )

    else:

        st.header("Quaternion Foundation")

        st.markdown(
            r"""
            The mathematical foundation uses the Hamilton quaternion:

            $$q = w + xi + yj + zk.$$

            Here the quaternion is treated as an **algebraic
            representation and computational tool**, not
            automatically as a physical four-dimensional
            coordinate system.

            The complete `quaternion_v2.py` implementation under
            development remains separate; this page documents only
            the foundational concepts.
            """
        )


# ============================================================
# 6. Szimulációs labor
# ============================================================

with tabs[5]:

    if lang == "hu":

        st.header("Szimulációs labor — fenntartott hely")

        st.info(
            "A szimulációs modul ebben a verzióban szándékosan "
            "nincs implementálva."
        )

        st.markdown(
            """
            Ide kerülhetnek később:

            - kvaterniómezők,
            - komponensvizsgálatok,
            - nemkommutatív műveletek,
            - torziós konstrukciók,
            - 3D vektor- és mezőábrázolás,
            - a rekonstruált egyenletrendszer numerikus tesztjei.

            **Egy numerikus demonstráció önmagában nem fizikai
            bizonyítás.**
            """
        )

    else:

        st.header("Simulation Laboratory — Reserved")

        st.info(
            "The simulation module is intentionally not implemented "
            "in this version."
        )

        st.markdown(
            """
            Future modules may include:

            - quaternion fields,
            - component analysis,
            - non-commutative operations,
            - torsion constructions,
            - 3D vector and field visualization,
            - numerical tests of the reconstructed equation system.

            **A numerical demonstration is not, by itself, a physical proof.**
            """
        )


# ============================================================
# Sidebar
# ============================================================

st.sidebar.markdown("---")

if lang == "hu":

    st.sidebar.markdown(
        """
        **FiRSTT Streamlit Base v2**

        Maxwell történeti háttér  
        • Equation Registry  
        • Symbol Registry  
        • kvaternió-alap  
        • fenntartott szimulációs labor
        """
    )

else:

    st.sidebar.markdown(
        """
        **FiRSTT Streamlit Base v2**

        Maxwell historical background  
        • Equation Registry  
        • Symbol Registry  
        • quaternion foundation  
        • reserved simulation laboratory
        """
    )
