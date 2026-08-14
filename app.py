import streamlit as st
from pathlib import Path


# ============================================================
# Alapútvonalak
# ============================================================

BASE = Path(__file__).parent
DATA = BASE / "data"


# ============================================================
# Streamlit konfiguráció
# ============================================================

st.set_page_config(
    page_title="FiRSTT — Maxwell rekonstrukció",
    page_icon="∿",
    layout="wide",
)


# ============================================================
# Dokumentumkezelés
# ============================================================

def load(name):
    """Markdown dokumentum betöltése UTF-8 kódolással."""
    return (DATA / name).read_text(encoding="utf-8")


def render_math_markdown(text):
    """
    A registry Markdown fájljaiban használt LaTeX jelölést
    Streamlit-kompatibilis formára alakítja.

    Forrás:
        \\[ ... \\]     ->     $$ ... $$
        \\( ... \\)     ->     $ ... $

    A matematikai tartalmat nem módosítja.
    Csak a megjelenítési delimitereket alakítja át.
    """

    text = text.replace(r"\[", "$$")
    text = text.replace(r"\]", "$$")
    text = text.replace(r"\(", "$")
    text = text.replace(r"\)", "$")

    return text


def render_document(name):
    """
    Markdown dokumentum betöltése és Streamlit-kompatibilis
    matematikai renderelése.
    """
    text = load(name)
    text = render_math_markdown(text)
    st.markdown(text)


# ============================================================
# Fejléc
# ============================================================

st.title("FiRSTT — Maxwell–kvaternió rekonstrukció")

st.caption(
    "Kiindulási dokumentáció • történeti háttér • "
    "jelölési és egyenlet-regiszter"
)


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


# ============================================================
# Navigáció
# ============================================================

tabs = st.tabs(
    [
        "Áttekintés",
        "Maxwell — történeti háttér",
        "Egyenletek",
        "Jelölések",
        "Kvaternió-alap",
        "Szimulációk",
    ]
)


# ============================================================
# 1. Áttekintés
# ============================================================

with tabs[0]:

    st.header("A kiindulási pont")

    st.markdown(
        """
A projekt jelen dokumentációs rétege nem a teljes FiRSTT-elmélet
publikálása. A cél a **kiindulási matematikai rendszer dokumentálása**
Maxwell munkájának tiszteletben tartásával, valamint annak megmutatása,
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


# ============================================================
# 2. Maxwell történeti háttér
# ============================================================

with tabs[1]:

    st.header("Maxwell — történeti háttér")

    render_document("maxwell_history.md")


# ============================================================
# 3. Egyenlet-regiszter
# ============================================================

with tabs[2]:

    st.header("FiRSTT Equation Registry v2")

    render_document("equation_registry_v2.md")


# ============================================================
# 4. Jelölési regiszter
# ============================================================

with tabs[3]:

    st.header("FiRSTT Symbol Registry v2.0")

    render_document("symbol_registry_v2.md")


# ============================================================
# 5. Kvaternió-alap
# ============================================================

with tabs[4]:

    st.header("Kvaternió-alap")

    st.markdown(
        r"""
A dokumentációs alap a Hamilton-féle kvaternió:

$$
q = w + xi + yj + zk
$$

A kvaternió itt **algebrai reprezentáció és számítási eszköz**,
nem automatikusan fizikai négydimenziós koordinátarendszer.

A teljes, fejlesztés alatt álló `quaternion_v2.py` külön marad;
ez az oldal csak az alapfogalmakat dokumentálja.
"""
    )


# ============================================================
# 6. Szimulációs labor
# ============================================================

with tabs[5]:

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
- a rekonstruált egyenletrendszer numerikus tesztjei.

**Egy numerikus demonstráció önmagában nem fizikai bizonyítás.**
"""
    )


# ============================================================
# Oldalsáv
# ============================================================

st.sidebar.header("FiRSTT Streamlit Base v2")

st.sidebar.markdown(
    """
Maxwell történeti háttér • Equation Registry •
Symbol Registry • kvaternió-alap •
fenntartott szimulációs labor
"""
)
