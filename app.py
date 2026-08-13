import streamlit as st
from pathlib import Path
BASE = Path(__file__).parent
DATA = BASE / 'data'
st.set_page_config(page_title='FiRSTT — Maxwell rekonstrukció', page_icon='∿', layout='wide')
def load(name): return (DATA/name).read_text(encoding='utf-8')
st.title('FiRSTT — Maxwell–kvaternió rekonstrukció')
st.caption('Kiindulási dokumentáció • történeti háttér • jelölési és egyenlet-regiszter')
st.markdown('''> **Cél:** egyetlen, áttekinthető helyen megmutatni azt a matematikai kiindulási rendszert, amelyből a FiRSTT gondolkodási kerete elindul.\n>\n> Ez az oldal **nem állítja, hogy a FiRSTT hipotézisei bizonyítottak**. A történeti Maxwell-anyag, a rekonstruált matematikai alak és a FiRSTT értelmezési lehetősége külön rétegben jelenik meg.''')
tabs=st.tabs(['Áttekintés','Maxwell — történeti háttér','Egyenletek','Jelölések','Kvaternió-alap','Szimulációk'])
with tabs[0]:
    st.header('A kiindulási pont')
    st.markdown('''A projekt jelen dokumentációs rétege nem a teljes FiRSTT-elmélet publikálása. A cél a **kiindulási matematikai rendszer dokumentálása** Maxwell munkájának tiszteletben tartásával, valamint annak megmutatása, hogy a kvaterniós formalizmus milyen további vizsgálati lehetőségeket kínálhat.\n\n### Rétegek\n1. **Történeti / forrásréteg** — mit ír és milyen jelöléseket használ a forrás.\n2. **Rekonstruált matematikai réteg** — egységesített, számítható jelölés.\n3. **FiRSTT-értelmezési réteg** — lehetséges értelmezési irányok, nem bizonyítás.\n4. **Numerikus / szimulációs réteg** — későbbi vizsgálatok helye.\n\nA mostani Streamlit-verzió szándékosan dokumentációs alap. A szimulációk helye fenn van tartva, de nincs kész fizikai modellként bemutatva.''')
with tabs[1]:
    st.header('Maxwell — történeti háttér'); st.markdown(load('maxwell_history.md'))
with tabs[2]:
    st.header('FiRSTT Equation Registry v2'); st.markdown(load('equation_registry_v2.md'))
with tabs[3]:
    st.header('FiRSTT Symbol Registry v2.0'); st.markdown(load('symbol_registry_v2.md'))
with tabs[4]:
    st.header('Kvaternió-alap')
    st.markdown(r'''A dokumentációs alap a Hamilton-féle kvaternió:\n\n$$q=w+xi+yj+zk.$$\n\nA kvaternió itt **algebrai reprezentáció és számítási eszköz**, nem automatikusan fizikai négydimenziós koordinátarendszer.\n\nA teljes, fejlesztés alatt álló `quaternion_v2.py` külön marad; ez az oldal csak az alapfogalmakat dokumentálja.''')
with tabs[5]:
    st.header('Szimulációs labor — fenntartott hely')
    st.info('A szimulációs modul ebben a verzióban szándékosan nincs implementálva.')
    st.markdown('''Ide kerülhetnek később: kvaterniómezők, komponensvizsgálatok, nemkommutatív műveletek, torziós konstrukciók, 3D vektor- és mezőábrázolás, valamint a rekonstruált egyenletrendszer numerikus tesztjei.\n\n**Egy numerikus demonstráció önmagában nem fizikai bizonyítás.**''')
st.sidebar.header('FiRSTT Streamlit Base v2')
st.sidebar.markdown('Maxwell történeti háttér • Equation Registry • Symbol Registry • kvaternió-alap • fenntartott szimulációs labor')
