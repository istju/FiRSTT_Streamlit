# FiRSTT Equation Registry v2

**Állapot:** v2.0 — alap / rekonstrukciós réteg

## 1. Cél

Az Equation Registry az A–H forrásokból kiinduló egyenletek közös, olvasható és később számítható formában történő dokumentációja. A forrás, a rekonstruált alak és a FiRSTT-értelmezés külön réteg.

## 2. Alap operátor

\[
\nabla=\mathbf{i}\frac{\partial}{\partial x}+\mathbf{j}\frac{\partial}{\partial y}+\mathbf{k}\frac{\partial}{\partial z}.
\]

Kapcsolódó alakok:
\[
\nabla\times\mathbf A,\quad \nabla\times\mathbf H,\quad \nabla\cdot\mathbf D,\quad \nabla\cdot\mathbf J_{\mathrm{total}},\quad \nabla\cdot\mathbf J_{\mathrm{conduction}}.
\]

## 3. Potenciálok és mezők

\[
\mathbf A=(f_A,g_A,h_A),\quad \mathbf E=(P,Q,R),\quad \mathbf H=(\alpha,\beta,\gamma),\quad \mathbf D=(f_D,g_D,h_D).
\]

\(\Psi\) skalárpotenciál.

## 4. Áramok

\[
\mathbf J_{\mathrm{conduction}}=(u,v,w),\qquad \mathbf J_{\mathrm{total}}=(p,q,r).
\]

A forrásbeli kapcsolat:
\[
p=u+\frac{\partial f}{\partial t},\qquad q=v+\frac{\partial g}{\partial t},\qquad r=w+\frac{\partial h}{\partial t}.
\]

## 5. Anyagi összefüggések

\[
k=\frac1\varepsilon,\qquad \mathbf D=\frac{1}{4\pi k}\mathbf E.
\]

\[
\mathbf E=\rho\,\mathbf J_{\mathrm{conduction}}.
\]

## 6. Mozgó közeghez kapcsolódó alak

\[
\mathbf v=\left(\frac{\partial x}{\partial t},\frac{\partial y}{\partial t},\frac{\partial z}{\partial t}\right)
\]

\[
\mathbf E=\mu(\mathbf v\times\mathbf H)-\frac{\partial\mathbf A}{\partial t}-\nabla\Psi.
\]

A \(-\nabla\Psi\) FiRSTT-értelmezése hipotézis szintű; az egyenlet forrásbeli alakja ettől függetlenül dokumentálva marad.

## 7. Torsion konstrukció

\[
T_g(q_1,q_2)=q_1q_2+\frac g2(q_1q_2-q_2q_1).
\]

\[
T_g=\left(1+\frac g2\right)q_1q_2-\frac g2q_2q_1.
\]

Ez nem azonos automatikusan a Hamilton-szorzással. Fizikai értelmezése nyitott.
