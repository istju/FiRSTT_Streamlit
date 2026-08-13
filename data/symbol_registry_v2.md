# FiRSTT Symbol Registry v2.0

**Állapot:** v2.0 / forrásőrző + rétegezett ábrázolás

1. **FORRÁS** — eredeti jelölés.
2. **REKONSTRUÁLT / EGYSÉGES** — számítási egyértelműség.
3. **FiRSTT-ÉRTELMEZÉS** — hipotézis, nem matematikai következmény.

| Mennyiség | FORRÁS | Streamlit / számítás |
|---|---|---|
| Vektorpotenciál | \(\mathbf A=(f,g,h)\) | `A_x,A_y,A_z` |
| Elektromos elmozdulás | \(\mathbf D=(f,g,h)\) | `D_x,D_y,D_z` |
| Elektromos térerősség | \(\mathbf E=(P,Q,R)\) | `E_x,E_y,E_z` |
| Mágneses térerősség | \(\mathbf H=(\alpha,\beta,\gamma)\) | `H_x,H_y,H_z` |
| Vezetési áram | \(\mathbf J=(u,v,w)\) | `J_cond_x,...` |
| Teljes áram | \(\mathbf J=(p,q,r)\) | `J_total_x,...` |
| Skalárpotenciál | \(\Psi\) | `Psi` |
| Töltéssűrűség | \(\rho_e\) | `rho_e` |
| Fajlagos ellenállás | \(\rho\) | `rho` |

## Forráskonfliktus

A forrásban ugyanaz az \(f,g,h\) komponensnév jelenik meg \(\mathbf A\) és \(\mathbf D\) esetében. Ezt nem rejtjük el: a forrás megmarad, a számítási rétegben \(f_A,g_A,h_A\) és \(f_D,g_D,h_D\) választja szét a jelentést.

## Kvaternió

\[
q=w+xi+yj+zk.
\]

A négy komponens nem jelent automatikusan fizikai 4D koordinátát; itt algebrai reprezentáció.
