# The near radical of a finite-window Weil form carries planted-zero visibility above the Nyquist height
Tags: [U] exact identity or inequality; [num] measurement on $V_K$ at the $K$ and dps recorded; [heur] heuristic;
[cert] verified in ball arithmetic (python-flint/Arb), no hypothesis on zeros. Every registered prediction, with
its time stamp and score, is in the supplement (predictions_loc.md).

## 1. Setting
Odd test functions $g$ on $[-L,L]$; $W$ the Weil form of $L(s,\chi)$, $\chi$ real primitive of conductor $q$ (explicit
formula: Gamma factor and prime powers up to $e^{2L}$). On $V_K$ (odd sine basis, $K$ modes; [1, §2]) $W$ is a positive
definite $K\times K$ matrix (Cholesky succeeds in every run). Only §3 also uses the even sector (cosine modes
$0,\ldots,K-1$), to compare the two spectra. For an ordinate $\gamma_0$ let $h(u)=u\cos(\gamma_0 u)$, $v$ the
coefficient vector of $g\mapsto\langle g,h\rangle$, and

$$
K(\gamma_0)=\sup_{g\in V_K}\frac{\langle g,h\rangle^2}{W(g)}=v^{T}W^{-1}v.
$$

By [1, §6], $4\delta^2K>1$ is the first-order criterion for a planted quartet of depth $\delta$ at $\gamma_0$ to make
$W$ indefinite. Put $T^*=(2\pi/q)e^{2L}$, the height at which the zero density $\frac{1}{2\pi}\log\frac{qt}{2\pi}$
reaches the density $L/\pi$ allowed by exponential type $L$ (Zhu [2, §9] for zeta, $q=1$; Blum's $H$ [3]), and
$d=e^{2L}/q=T^*/2\pi$.

What can be reused, and where. (i) The transversal-loss bound §2(b). It is linear algebra and holds for any positive
definite form with an isolated block of small eigenvalues. (ii) The trial-space rule (§7, first item, with the sizes
of §5; `ch/lnr.py`, `ch/lnr_score.py`). (iii) Certified lower bounds on the $L^2$ near-null counts, and upper bounds on
the depths, at 23 $(\chi,L)$ pairs (§3; `ch/cert_count.py`, `ch/cert_batch*.txt`, `ch/cert_depth_*.txt`). Other
near-radical claims for characters can be checked against them. (iv) The Cholesky identity §2(a), which gives $K$
above every frequency cut from one factorisation (`ch/decomp.py`). (v) At the two pairs tested, moving the zeros below
110 to smooth-count points changes the depths by at most 0.3 decades and keeps the alternation (§3, last item;
`ch/smooth_swap.py`). The rest of §§3–5 is measurement on $V_K$ for one family of trial spaces.

## 2. Three exact statements [U]
(a) Frequency split. Order the modes from high to low and let $W=RR^{T}$ (Cholesky). With $y=R^{-1}v$, the sum of
$y_i^2$ over the first $m$ entries is the supremum over the $m$ highest modes, since the leading block of a Cholesky
factor is the factor of the leading block. So $K_{\ge c}$ (modes with $k\pi/L\ge c$) is exact for every cut $c$, and
the low share $s_c=1-K_{\ge c}/K$ is the part of $K$ that needs modes below $c$.

(b) Spectral split. Let $We_i=\mu_ie_i$ (orthonormal, increasing), $E=(e_1,\ldots,e_m)$,
$D=\operatorname{diag}(\mu_1,\ldots,\mu_m)$ and

$$
K_{\mathrm{NR}}=\sum_{i\le m}\frac{(e_i\cdot v)^2}{\mu_i}.
$$

For $C$ ($K\times m$, orthonormal columns) with $A=C^{T}E$ invertible, the loss from imposing $C^{T}g=0$ is

$$
\Delta_C=K-\sup_{C^{T}g=0}\frac{\langle g,h\rangle^2}{W(g)}=(C^{T}x)^{T}\left(C^{T}W^{-1}C\right)^{-1}(C^{T}x),\qquad x=W^{-1}v.
$$

Write $W^{-1}=ED^{-1}E^{T}+R$, so $\|R\|=1/\mu_{m+1}$, and $w=D^{-1/2}E^{T}v$, so $|w|^2=K_{\mathrm{NR}}$. Then

$$
\Delta_C=z^{T}(I+T)^{-1}z,\qquad z=w+D^{1/2}A^{-1}C^{T}Rv,\qquad T=D^{1/2}A^{-1}C^{T}RCA^{-T}D^{1/2}\ge 0.
$$

For $C=E$, $z=w$ and $T=0$, so $\Delta_E=K_{\mathrm{NR}}$ exactly. For any $C$,

$$
|z-w|\le\frac{\mu_m^{1/2}\,\|A^{-1}\|\,|v|}{\mu_{m+1}},\qquad \|T\|\le\frac{\mu_m\|A^{-1}\|^2}{\mu_{m+1}}.
$$

So when $m$ eigenvalues lie far below the rest, every codimension-$m$ constraint transversal to their span costs
$K_{\mathrm{NR}}$, up to $O(\mu_m^{1/2})$ at fixed angle and gap. A trial space that misses the near radical loses
$K_{\mathrm{NR}}$, whichever way it misses it.

(c) A count lower bound [U under GRH]. Let $\mu_1\le\mu_2\le\cdots$ be the min-max values of $W$ on odd $L^2(-L,L)$.
Under GRH $W(g)=2\sum_{\gamma>0}m_\gamma|\hat g(\gamma)|^2$ with $\hat g(t)=\int g(u)e^{itu}\,du$; this is the
normalisation of the $V_K$ matrix (for one test function the two sides agree to a relative $2\cdot10^{-7}$; P-ct). Fix
$\delta\in(0,L)$, $l=L-\delta$, $n\ge2$, and let $\varphi$ be the indicator of $[-l-\delta/2,\,l+\delta/2]$ convolved
with the order-$n$ B-spline supported in $[-\delta/2,\delta/2]$. Then $\varphi=1$ on $[-l,l]$, $\varphi$ vanishes
outside $[-L,L]$, and

$$
|\hat\varphi(x)|\le\Phi(x)=\frac{2}{|x|}\min\left(1,\left(\frac{2n}{\delta|x|}\right)^{n}\right).
$$

Theorem. Let $J\ge1$, $\Delta>0$, $\omega_j=j\pi/l$, $T_1=\omega_J+\Delta$, and $N_1$ the number of ordinates in
$(0,T_1]$ with multiplicity. Then $\mu_k\le\varepsilon$ for every $k\le J-N_1$, where

$$
\varepsilon=\frac{1}{l}\sum_{\gamma>T_1}m_\gamma\sum_{j\le J}\left[\Phi(\gamma-\omega_j)^2+\Phi(\gamma+\omega_j)^2\right].
$$

Proof. The functions $\sin(\omega_ju)$ are orthogonal on $[-l,l]$, where $\varphi=1$, so
$g=\varphi\sum_jb_j\sin(\omega_ju)$ has $\|g\|^2\ge l|b|^2$. Here
$\hat g(t)=\frac{1}{2i}\sum_jb_j[\hat\varphi(t+\omega_j)-\hat\varphi(t-\omega_j)]$ is imaginary, so vanishing at the
ordinates in $(0,T_1]$ imposes $N_1$ real conditions (and $\hat g(0)=0$ for odd $g$). On the kernel only $\gamma>T_1$
contribute, and Cauchy–Schwarz in $j$ gives $W(g)\le\varepsilon l|b|^2\le\varepsilon\|g\|^2$. Apply min-max on the
kernel. $\square$

Take $J\pi/l$ near $(2\pi/q)e^{2l}$, $n\sim\frac12\log(L/\varepsilon)$ and $\delta\Delta\sim e\log(L/\varepsilon)$,
and optimise $\delta$. For large $d$ this gives
$\#\{k:\mu_k\le\varepsilon\}\ge d-O\big((Ld\log(L/\varepsilon))^{1/2}\big)$, and the even sector is the same up to
$O(1)$. So for $\log(1/\varepsilon)=o(d/L)$ the near radical has at least $d(1-o(1))$ directions per sector. The
argument is in the spirit of Landau's density conditions [4], made quantitative by the window. The error term is not
sharp: the measured loss grows like $\ln(\pi d)$ per decade (§3). At $\varepsilon=10^{-3}$ and $\chi_5$ it certifies 3
directions at $L=2.9$ ($d=66$), 336 at $L=4.0$ ($d=596$) and 1151 at $L=4.5$ ($d=1621$). It certifies nothing for
$\chi_5$ at $L\le2.8$ ($d\le54$), nor at the two largest-$d$ pairs of §3 besides $\chi_5$ ($\chi_{-3}$ and $\chi_{-4}$
at $L=2.0$). These numbers are [num] because the tail sum assumes $|S(t)|\le3$ above $T_1$ (with $|S|\le10$ the
$L=2.9$ count is 0, and the $L=3.9$ count ($d=488$) is 250 instead of 258).

Like the $V_K$ counts of §3, this is a lower bound on the $L^2$ count; it gives no upper bound and says nothing about
$K$. Its depth bound, $-\log\mu_k\gg d/L$ for $k\le d/2$ and $d$ large, is weak against §3
($\log_{10}\mu_1=-52.1$ at $d=10.9$) and, for zeta, against Mori's $-\log\lambda_{\min}\ge4\pi e^{2L}-O(L)$ [5]. Zhu
[2, Thm 1.3] and Mori bound the bottom eigenvalue, for zeta. For zeta, [6, Thm 2.3] bounds every fixed-index
eigenvalue unconditionally, $\lambda_m\le C_me^{(4m+7)L-2\pi e^{2L}}$ for fixed $m$ and $L\ge L_m$, with parity
versions and no uniformity in $m$. Theorem (c) is the other regime: $k$ up to $d(1-o(1))$, a shallow $\varepsilon$,
GRH, characters. Mori's test vector combines two CCM prolate vectors ($n=0,4$), smoothed in a layer of width
$\sim c^{-2}$ at the window edges, $c=2\pi e^{2L}$. Running his argument for each of the $\sim2e^{2L}$ prolate vectors
of [7] (about $e^{2L}$ per parity in $u$), and for characters with the twisted map $f\mapsto\sum\chi(n)f(nx)$, is the
natural route to an error term of plunge type. It is not attempted here.

## 3. The near radical on $V_K$ [num; the integer counts and the depths, as one-sided $L^2$ bounds, are cert]
Eigenvalues of $W$ on $V_K$ (odd: modes $1,\ldots,K$; even: modes $0,\ldots,K-1$), dps 80–130. $a=0$ for even $\chi$,
$1$ for odd $\chi$. The soft count $n(\varepsilon)$ is the index at which $\log_{10}\mu$ crosses
$\log_{10}\varepsilon$, interpolated linearly between neighbouring eigenvalues (from eigenvalues printed to 0.1
decade, so $n$ is good to about 0.03). $r=2d-(2a-1)/4-n_{\mathrm{odd}}-n_{\mathrm{even}}$ (see below).

| character | $a$ | $L$ | $d$ | # $<10^{-3}$, odd / even | soft $n(10^{-3})$, odd / even | $r$ | $\log_{10}$ lowest, odd / even | $K$ |
|---|---|---|---|---|---|---|---|---|
| $\chi_{-43}$ | 1 | 1.6 | 0.57 | 0 / 0 | – / – | – | 0.0 / −0.5 | 60 |
| $\chi_{5}$ | 0 | 1.0 | 1.48 | 1 / 1 | 1.06 / 1.60 | 0.55 | −3.2 / −5.7 | 60 |
| $\chi_{-15}$ | 1 | 1.6 | 1.64 | 0 / 1 | – / 1.53 | – | −2.5 / −5.7 | 60 |
| $\chi_{12}$ | 0 | 1.6 | 2.04 | 1 / 2 | 1.57 / 2.00 | 0.76 | −5.7 / −8.9 | 60 |
| $\chi_{24}$ | 0 | 2.0 | 2.27 | 1 / 2 | 1.78 / 2.31 | 0.70 | −7.0 / −10.5 | 100 |
| $\chi_{21}$ | 0 | 2.0 | 2.60 | 2 / 2 | 2.09 / 2.62 | 0.74 | −8.4 / −11.9 | 100 |
| $\chi_{-20}$ | 1 | 2.0 | 2.73 | 1 / 2 | 1.94 / 2.46 | 0.81 | −7.5 / −11.1 | 100 |
| $\chi_{-8}$ | 1 | 1.6 | 3.07 | 2 / 2 | 2.29 / 2.76 | 0.85 | −9.2 / −12.6 | 60 |
| $\chi_{17}$ | 0 | 2.0 | 3.21 | 2 / 3 | 2.69 / 3.24 | 0.74 | −11.9 / −15.5 | 100 |
| $\chi_{13}$ | 0 | 2.0 | 4.20 | 3 / 4 | 3.62 / 4.17 | 0.86 | −16.7 / −20.5 | 100 |
| $\chi_{-19}$ | 1 | 2.2 | 4.29 | 3 / 3 | 3.47 / 3.97 | 0.88 | −15.8 / −19.0 | 100 |
| $\chi_{28}$ | 0 | 2.4 | 4.34 | 3 / 4 | 3.68 / 4.24 | 1.00 | −17.3 / −21.5 | 100 |
| $\chi_{5}$ | 0 | 1.6 | 4.91 | 4 / 4 | 4.32 / 4.80 | 0.95 | −20.3 / −23.9 | 100 |
| $\chi_{-11}$ | 1 | 2.0 | 4.96 | 4 / 4 | 4.08 / 4.64 | 0.95 | −18.9 / −22.5 | 100 |
| $\chi_{-4}$ | 1 | 1.6 | 6.13 | 5 / 5 | 5.17 / 5.71 | 1.14 | −24.7 / −28.5 | 60 |
| $\chi_{8}$ | 0 | 2.0 | 6.82 | 6 / 6 | 6.14 / 6.64 | 1.12 | −30.4 / −34.6 | 100 |
| $\chi_{-7}$ | 1 | 2.0 | 7.80 | 6 / 7 | 6.85 / 7.41 | 1.08 | −33.6 / −37.9 | 100 |
| $\chi_{-3}$ | 1 | 1.6 | 8.18 | 7 / 7 | 7.21 / 7.69 | 1.22 | −35.3 / −39.2 | 60 |
| $\chi_{-8}$ | 1 | 2.2 | 10.18 | 9 / 9 | 9.14 / 9.65 | 1.32 | −45.8 / −50.4 | 100 |
| $\chi_{5}$ | 0 | 2.0 | 10.92 | 10 / 10 | 10.22 / 10.71 | 1.16 | −52.1 / −56.4 | 140 |
| $\chi_{-4}$ | 1 | 2.0 | 13.65 | 12 / 13 | 12.55 / 13.00 | 1.50 | −64.2 / −68.9 | 120 |
| $\chi_{5}$ | 0 | 2.13 | 14.16 | 13 / 13 | 13.36 / 13.83 | 1.38 | −69.2 / −73.9 | 130 |
| $\chi_{-3}$ | 1 | 2.0 | 18.20 | 17 / 17 | 17.08 / 17.58 | 1.49 | −88.5 / −93.2 | 150 |

Integer counts at a fixed threshold are not a stable invariant: at $\chi_{-7}$ the seventh odd eigenvalue is
$10^{-2.5}$, just above $10^{-3}$, and both registered integer rules ("within one of $d$", and $\lfloor d-c\rfloor$)
failed (P-cnt). Counts did not change where $K$ was varied ($\chi_5$: $K=60,100,140$). By min-max,
$\mu_k(\text{odd }L^2)\le\mu_k(V_K)$ for every $k$, so each count below $\varepsilon$ here is a lower bound for the
count of $W$ on odd $L^2$, and likewise for even. Every integer count in the table is certified as such a lower bound
[cert]: the $n$ lowest computed eigenvectors (float64), rounded to rationals, span an $n$-dimensional subspace on which
$10^{-3}\|g\|^2-W(g)$ is positive definite, checked by a ball $LDL^{T}$ at 256 bits on an Arb enclosure of the $V_K$
matrix (entry radii $\le3.1\cdot10^{-73}$). That is 233 directions over the 23 pairs (112 odd, 121 even). The
certificate uses only the explicit-formula side of $W$, so it needs neither GRH nor zeros. The ladder itself is
certified from above in the same way (registered P-cdepth): with eigenvectors from a 100–140 digit eigensolver and a
512-bit enclosure, $\mu_k(L^2)\le2\mu_k(V_K)$ holds for every $k$ up to the count, in all 43 nonempty (pair, sector)
cases [cert]. So each depth in the table plus $\log_{10}2=0.30$ is a certified upper bound for the bottom of $W$ on
$L^2$, from $10^{-2.90}$ ($\chi_5$, $L=1.0$, odd) to $10^{-92.91}$ ($\chi_{-3}$, $L=2.0$, even); at $\chi_5$, $L=2.0$
(odd) $\mu_1\le1.73\cdot10^{-52}$. The method is not new: certified variational upper bounds for the bottom of the
zeta form are in Zhu [2, §1] (compared with ours in the supplement, `ladder_details.md`). The new content is what is
bounded: the ladders of 23 (character, $L$) pairs, through the whole near radical. These are upper bounds only. At
$\chi_5$, $L=2.0$ the $K=60$ depth ($-49.1$ / $-52.9$) was not converged, and $K=100\to140$ moved it by 0.2, so the
$L^2$ bottoms may lie lower. The soft counts and $r$ remain [num]. Depth is not a function of $d$: $\chi_{-11}$ at
$L=2.0$ lies 1.4 decades above $\chi_5$ at $L=1.6$ at nearly equal $d$ (registered P-il3 predicted the opposite).

Three regularities hold wherever they are defined: interleaving at all 22 pairs with a near radical, the half step
and the Gamma constant at 21 (not at $\chi_{-15}$, whose odd sector has nothing below $10^{-3}$). Each was seen first
on 7, 11 or 16 pairs and then registered before further runs: interleaving before 9 runs, the half step before 4
(soft count) and 3 plus Zhu's table (midpoint form), the Gamma constant before 5 (P-il, P-gam, P-mid). The last three
rows ($L=2.2$–$2.4$) were run later for P-col and were not registered for these three statistics.
- Interleaving. Merging the two sectors, the eigenvalues below $10^{-2}$ alternate in parity, even first (2 to 34 of
  them). For zeta, Zhu [2, §6.3(ii)] found
  $\lambda_1^{\mathrm{even}}<\lambda_1^{\mathrm{odd}}<\lambda_2^{\mathrm{even}}<\lambda_2^{\mathrm{odd}}$ at every
  scanned $L$, "the same alternation as the prolate eigenfunctions"; the prolate vectors of [7] carry parity $(-1)^n$.
  Here the alternation runs through the whole near radical, for sixteen characters. A reason for its persistence in
  $L$ (not for its presence) may come from translation invariance. Let $\tau_+(u)$ and $\tau_-(u)$ be the limits of
  $\sqrt{\log(1/t)}\,u(L-t)$ and $\sqrt{\log(1/t)}\,u(-L+t)$. [8, Thm 2.2] proves for zeta that on each eigenspace the
  Gram matrices of $\tau_-$ and $\tau_+$ are equal (we checked its derivation from [8, Thm 2.1] in [8, §6], not
  Thm 2.1 itself). For an even $u_e$ and an odd $u_o$ with a common eigenvalue this forces
  $\tau_+(u_e)\tau_+(u_o)=0$, so branches of opposite parity can meet only where one has zero trace [exact given
  [8, Thm 2.2]]. For real primitive characters the author of [8] states that the operator class [8, (2.8)] applies,
  with $c=\log(2\pi/q)$ and an archimedean measure of mass $-\psi\big(\frac{1+2a}{4}\big)-\log2$ (forum post 21, the
  thread of [9]; reply of 2026-10-27 19:28Z). We checked that mass and the related identities numerically, but not the
  extension itself. bramble_trace's reply also notes that this is a persistence rule only: it gives no trace
  nonvanishing for the Weil family. In a follow-up (post 21, 2026-10-27 20:23Z) the same author shows that the class
  does allow such meetings. Take an odd eigenfunction $v$, eigenvalue $\lambda$, of the compression $T_a$ of $\log|D|$
  to $I=(-a,a)$. Then $u(x)=\int_{-a}^{x}v$ is even with zero traces, and $(T_a-\lambda)u=c\,\mathbf 1_I$ with
  $c\int_Iu<0$. So $T_a+\kappa J_a$, with $J_af=\mathbf 1_I\int_If$ (a constant convolution kernel) and
  $\kappa=-c/\int_Iu>0$, has $\lambda$ in both sectors, and the two branches cross as $a$ varies. We checked the
  argument; in fact $c\int_Iu=-\|u\|^2$ exactly [U], by the dilation identity
  $\big[x\frac{d}{dx}+\frac12,\,\log|D|\big]=-I$ (our reply in the same thread, 2026-10-27 21:55Z; bramble_trace agreed
  at 22:21Z and gave a form-domain proof by inward dilations), so $\kappa=\|u\|^2/(\int_Iu)^2$. So the interleaving we
  observe is not forced by the operator class, and meetings in the class are not a tuned accident. The dilation
  $x\mapsto x/a$ carries $T_a+\kappa J_a$ to $T_1-\log a+\kappa aJ_1$, so $\kappa(a)=\kappa(1)/a$, and for every fixed
  $\kappa>0$ the one-parameter family in $a$ has a meeting at $a=\kappa(1)/\kappa$ for each odd mode [exact, by
  scaling]. In the example the zero-trace even eigenfunction is the primitive of the odd one. Read backwards [heur; the
  boundary regularity is not checked], for a translation-invariant operator the derivative of a zero-trace
  eigenfunction is an eigenfunction of the other parity with the same eigenvalue, so a meeting and a vanishing trace
  would be one event, not two conditions. By [8, Thm 2.2], the interleaving persists in $L$ as long as no
  near-radical trace of the Weil family vanishes, and we have no argument for that. $V_K$ vectors do not represent
  traces.
- Half step. $n_{\mathrm{even}}-n_{\mathrm{odd}}=0.43$–$0.56$. Pointwise, each eigenvalue sits near the log-midpoint
  of its two neighbours of the other parity: $|\log_{10}\mu-(\log_{10}\mu'+\log_{10}\mu'')/2|\le0.3$ at 126 of 137
  interior instances in the first 16 pairs, and at 29 of 30 in three fresh pairs ($\chi_{24}$ $L=2.0$, $\chi_{-15}$
  $L=1.6$, $\chi_{-3}$ $L=2.0$ with $d=18.2$; registered P-mid1; 32 of 33 once $\chi_{-3}$ was rerun to print its whole
  near radical). It is looser at the three rows added for P-col: 22 of 26, max 0.40. The same holds on Zhu's zeta
  table [2, Table 1], read only after registering the test (P-mid2): $\log_{10}\lambda_1^{\mathrm{odd}}$ exceeds the
  midpoint of $\log_{10}\lambda_1^{\mathrm{even}}$ and $\log_{10}\lambda_2^{\mathrm{even}}$ by 0.12–0.17 at all eight
  $L$ in $[0.5,1.2]$. So the sector ratio $\lambda_1^{\mathrm{odd}}/\lambda_1^{\mathrm{even}}$, whose law Zhu leaves
  open [2, §6.3(iii)], is on a log scale half the first even step plus 0.12–0.17 decades. (For zeta, [9] reads the same
  ratio from the prime side: the tolerance of positivity to moving a prime is $e_1/s_e$ downward and $o_1/|s_o|$
  upward, with Hellmann–Feynman slopes $s$.) It is the same fact as the alternation, not a separate parity effect.
  This says nothing about why the steps have the sizes they do.
- Gamma constant. For real primitive $\chi$ the ordinates in $(0,T)$ number
  $N^+(T)=\frac{T}{2\pi}\log\frac{qT}{2\pi e}+\frac{2a-1}{8}+S(T)+o(1)$, the constant coming from
  $\arg\Gamma\big((\frac12+a+iT)/2\big)$ (Stirling). The heuristic below then gives a per-sector excess
  $d-(2a-1)/8$. Without this term the offset $2d-n_{\mathrm{odd}}-n_{\mathrm{even}}$ splits by parity (even $\chi$
  0.30–1.13, odd $\chi$ 1.06–1.75). In all 13 opposite-parity pairs with $|d-d'|\le0.7$ it differs by 0.38–0.62,
  against 0.5 predicted (0.50–0.62 at the nine pairs available when P-gam was scored). With it, $r$ differs by at most
  0.12 in those pairs. $r$ rises slowly with $d$, not monotonically (scatter about 0.1), from 0.55 at $d=1.5$ to
  1.4–1.5 at $d=14$–$18$.
- Ladder density. If the near radical were the plunge region of a concentration operator with Shannon number $2d$,
  Landau and Widom [10] would give $\ln(10)\ln(\pi d)/\pi^2$ merged eigenvalues per decade. Between $10^{-2}$ and
  $10^{-4}$ the measured density is 0.78–1.06 times this value at all 17 pairs where it is defined (Spearman 0.98
  against $d$; registered P-pl). Post hoc, it is 0.95–1.37 times the value between $10^{-1}$ and $10^{-3}$ and
  0.64–0.74 times it between $10^{-6}$ and $10^{-8}$, so only the growth like $\ln(\pi d)$ holds in every band, to
  about 20%. $r$ is roughly the top density times a nearly fixed gap of 1.3–1.8 decades, so it grows with $d$ because
  the density does; nothing here explains the level. The post-hoc level statistics and the registered collapse test
  P-col (three fresh pairs) are in the supplement (`ladder_details.md`).
- Smooth count, not zero positions. Under GRH, $W$ on $V_K$ is the zero sum $2\sum m(\gamma)m(\gamma)^{T}$,
  $m=\operatorname{Im}G(i\gamma)$ in the odd sector and $\operatorname{Re}G(i\gamma)$ in the even one ([1, §3.1]).
  Replacing the $N$ zeros below 110 by the points $\theta(t_n)=\pi(n-\frac12)$, $\theta$ the Gamma phase (so $S(T)$ is
  removed), changes $W$ by an exact finite-rank term and keeps it positive semidefinite. At $\chi_5$ $L=1.6$ and
  $\chi_{-11}$ $L=2.0$ ($N=61,74$; zeros moved by 0.29–0.30 in mean, 0.81 at most) the soft counts moved by at most
  0.11, the depths by at most 0.3 decades, and the alternation survived (registered P-sm). So the 1.4-decade depth gap
  between these two pairs at equal $d$ does not come from $S(T)$ below 110; it changed by 0.0 (odd) and 0.4 (even)
  decades.

For zeta, Connes and Consani [7, §§1, 3] found the near radical of the form on $[\lambda^{-1},\lambda]$
($\lambda=e^L$), with $1+\nu(\lambda^2)\sim2\lambda^2$ directions spanned by prolate vectors and smallest eigenvalue
$2.389\cdot10^{-48}$ at $\lambda^2=11$. Zhu [2, §5.5] reports four near-null directions at $L=0.8$ ($d=4.95$). The
factor 2 in the zeta count is the two parity sectors. [heur] (Zhu's argument [2, §9] with a count.) Odd functions on
$[-L,L]$ concentrated in $|t|<T$ span about $LT/\pi$ dimensions; nearly vanishing at the $N^+(T)$ ordinates in
$(0,T)$ leaves $LT/\pi-N^+(T)$, which is maximal at $T=T^*$, with value $d-(2a-1)/8$. §2(c) proves the leading term
$d$ as an asymptotic lower bound, but not the constant and not at these $d$.

Comparisons with the zeta depths of Zhu [2] and Connes–Consani [7], with Zhu's fitted zeta law [2, Conj. 12.1] (not
a test of it), and with the certified core bounds of [11, §4] (whose even-odd gap agrees with the alternation) are in
the supplement (`ladder_details.md`).

## 4. The low share of $K$ [num]
Cut $c=40$ (44 for $\chi_{-7}$). Ordinates $\gamma_0$ in $[100,180]$; for the three newest characters the zero counts
there are 53/57/66 against $N(T)=53.3/57.0/65.8$. $K=200$ except $\chi_5$ $L=1.0$ (140) and $\chi_5$ $L=1.6$ (120; at
$K=160$ no share changes by more than 0.006). Medians and percentiles are the usual ones (mean of the middle pair for
even $n$; linear interpolation), as in §5.

| character | $L$ | $d$ | $T^*$ | $n$ | median low share | 10%–90% | max |
|---|---|---|---|---|---|---|---|
| $\chi_{-43}$ | 1.6 | 0.57 | 3.6 | 11 | 0.0004 | 0.0002–0.0011 | 0.0012 |
| $\chi_{5}$ | 1.0 | 1.48 | 9.3 | 10 | 0.0055 | 0.0003–0.012 | 0.027 |
| $\chi_{5}$ | 1.6 | 4.91 | 30.8 | 15 | 0.059 | 0.038–0.088 | 0.155 |
| $\chi_{-4}$ | 1.6 | 6.13 | 38.5 | 29 | 0.087 | 0.054–0.172 | 0.228 |
| $\chi_{8}$ | 2.0 | 6.82 | 42.9 | 33 | 0.099 | 0.045–0.180 | 0.271 |
| $\chi_{-7}$ | 2.0 | 7.80 | 49.0 | 16 | 0.140 | 0.082–0.303 | 0.363 |
| $\chi_{-3}$ | 1.6 | 8.18 | 51.4 | 27 | 0.188 | 0.075–0.389 | 0.442 |
| $\chi_{5}$ | 2.0 | 10.92 | 68.6 | 8 | 0.254 | 0.114–0.420 | 0.423 |

The median is monotone in $d$ across six conductors ($q=3,4,5,7,8,43$) and three values of $L$. The rows $\chi_{-4}$,
$\chi_8$ and $\chi_{-3}$ were predicted (intervals and order registered before their zeros were computed), and all
three fell inside. The share decays with height. For $\chi_5$ at $L=1.6$, $s_{10}$ is 0.38 at $\gamma_0=68.6$,
0.12–0.19 on $[74,103]$ and 0.03–0.08 on $[109,184]$. Its position in frequency varies. For $\chi_{-7}$ ($L=2.0$) the
bands $[11,22)$ and $[22,44)$ carry medians 0.004 and 0.002 of $K$ (35 ordinates in $[81,249]$), so the share sits
below 11. For $\chi_5$ at $L=2.0$ (27 ordinates in $[152,248]$), about 70% of it lies below 10 and the rest in
$[10,30)$. A registered edge rule at $(2\pi/q)e^{1.6L}$ has two parts, and each held in one fresh run and failed in the
other. At larger $d$: $\chi_5$ at $L=2.4$ ($d=24.3$, $K=400$, dps 200) has median $s_{29.2}=0.136$ on $[380,419]$.

Complement. Rayleigh–Ritz on $\operatorname{span}\{\sin(t_ku),\,u\cos(t_ku)\}$, $t_k=\gamma_0+k\pi/L$, $|k|\le8$, with
$W$ from the zero sum (GRH), matches $K_{\ge10}/K$ at $\chi_5$ $L=1.6$ to 0.009 in median (22 ordinates, all within
0.03). Replacing the zeros farther than $2\pi/L$ from $\gamma_0$ by their density changes it by 1–3% in median (four
runs).

## 5. The low share is the near-radical term [num]
$P$ = span of the eigenvectors with eigenvalue $<10^{-3}$ of the leading $K_0\times K_0$ block of $W$, embedded in
$V_K$; $s_{\mathrm{NR}}=\Delta_P/K$ (§2(b)). All zeros in $[100,180]$ ($\chi_5$ $L=2.0$: $[152,180]$); $K_0=100$.

| run | $n$ | $\dim P$ | median $s_{40}$ | median $s_{\mathrm{NR}}$ | $s_{\mathrm{NR}}/s_{40}$, median (min) | $s_{\mathrm{PH}}$ median | $s_{\mathrm{PH}}/s_{40}$, median (max) |
|---|---|---|---|---|---|---|---|
| $\chi_5$ $L=1.6$, $K=120$ | 59 | 4 | 0.057 | 0.049 | 0.89 (0.73) | 0.006 | 0.11 (0.29) |
| $\chi_{-3}$ $L=1.6$, $K=200$ | 53 | 7 | 0.169 | 0.165 | 0.96 (0.88) | 0.006 | 0.03 (0.18) |
| $\chi_5$ $L=2.0$, $K=200$ | 22 | 10 | 0.249 | 0.246 | 0.98 (0.95) | 0.008 | 0.04 (0.13) |

($s_{\mathrm{PH}}=1-K_{P+\text{modes}\ge40}/K$, the loss of the trial space $P$ + modes $\ge40$.)

$s_{\mathrm{NR}}\le s_{40}+0.01$ at every ordinate, and $s_{\mathrm{NR}}$ changes by at most $10^{-4}$ between
$K_0=60$ and 100. Removing the $m$ lowest modes instead of $P$ costs 0.93–1.01 times $s_{\mathrm{NR}}$ in median, as
§2(b) predicts for any transversal constraint. That control was registered as a discriminating test before the
argument was seen, and it failed as one.

$K_{\mathrm{NR}}$ is spread over all $m$ vectors. With exact eigenvectors ($K_0=K$) the median shares of
$K_{\mathrm{NR}}$ on $e_1,\ldots,e_m$ are 0.22, 0.16, 0.23, 0.37 ($\chi_5$ $L=1.6$) and 0.26, 0.17, 0.13, 0.13, 0.10,
0.09, 0.09 ($\chi_{-3}$ $L=1.6$), and the per-vector terms sum to $s_{\mathrm{NR}}$ within $10^{-4}$, as §2(b)
requires. The recovery by $P$ + high modes does depend on $K_0$: with $K_0=60$ the median remaining losses were
0.009/0.015/0.047; with $K_0=K=120$ (exact eigenvectors) at $\chi_5$ $L=1.6$ it is 0.0056.

Near radical plus a local band. Let $B_M=\operatorname{span}\{\sin(t_ku),\,u\cos(t_ku)\}$, $t_k=\gamma_0+k\pi/L$,
$|k|\le M$, projected onto $V_K$. On the same ordinates, the trial space $P+B_M$ recovers $K$ to a median 0.989 (10th
percentile 0.980) at $\chi_5$ $L=1.6$ with $M=8$ (38 functions), against 0.937 for $B_8$ alone. At $\chi_5$ $L=2.0$ it
recovers 0.954 (0.919) with $M=8$ and 0.974 (0.935) with $M=16$ (76 functions), against 0.728 and 0.742 for the bands
alone (registered P-lnr1-3, P-lnr5; the registered 0.97 for $M=8$ failed at $L=2.0$). The near radical is the only
global part of the optimiser to within 1–3% in median; the rest sits within $8$–$16\,\pi/L$ of $\gamma_0$, where the
cost is local in the zeros (§4, complement).

## 6. Application: the Davenport–Heilbronn onset [num; the sign of $W(g)$ is cert]
For the $q=5$ DH function, $W_{\mathrm{rh}}$ is $W$ with the known off-line quartets O1–O4 and Z5 moved to the line
([1, §3]). It is positive definite on $V_K$ and has its own near radical: 5–7 eigenvalues below $10^{-3}$ at
$L=1.74$–$1.86$ (lowest $10^{-26.7}$ to $10^{-37.0}$). The exact per-zero predicate $R_k$ of [1, (3.1)], with
$R_k>1$ iff the quartet makes $W_{\mathrm{rh}}+P_k$ indefinite, was recomputed with the trial space restricted as in
§5 (registered P-dh1-4; $K=148$–$158$, dps 80–89, $K_0=100$):

| $L$ | $R(\mathrm{O1})$ on $V_K$ | $g\perp P$ | modes $\ge40$ | $P$ + modes $\ge40$ |
|---|---|---|---|---|
| 1.74 | 1.654 | 0.598 | 0.583 | 1.632 |
| 1.78 | 14.55 | 0.743 | 0.710 | 14.51 |
| 1.82 | 463.4 | 0.913 | 0.838 | 462.0 |
| 1.86 | 45396 | 1.249 | 0.996 | 45009 |

For O1 ($85.70+0.309$) the near radical carries 64% of $R$ at $L=1.74$, and all of its super-exponential growth.
Without the near radical O1 is first seen between $L=1.82$ and 1.86 ($g\perp P$), or above 1.86 (modes $\ge40$). On
$V_K$ it is seen in $(1.70,1.74)$, and [1] certifies $W_L\ngeq0$ at 1.725. For O2–O4 the near-radical share of $R$ is
0.20/0.09/0.07 at $L=1.74$. The certified vector of [1, §4.2] ($L=1.725$, 200 modes) has $1-1.4\cdot10^{-7}$ of its
squared norm on the lowest eigenvector $e_1$ of $W_{\mathrm{rh}}$ ($\mu_1=10^{-25.6}$), so
$W(g)/\|g\|^2=-1.34\cdot10^{-26}$ is $\mu_1$ plus the off-line terms on $e_1$ (P-dh5). Small negative eigenvalues at
onset are visible in Blum's planted-zero table [3] ($-1.0\cdot10^{-33}$ at $\gamma=150.1$) and in De Jesús's remark on
a near-null direction of the remaining-zero form [12]. Neither splits the margin.

Joint detection. [1, §5] explains the absorption of DH quartets by nearly parallel whitened directions (cosines
0.76–0.998 among O1–O4 at $L=2.06$, $K=173$), and its v1 leaves the cause as an untested heuristic. The test below was
made for this note; the v2 revision of [1] (accepted 2026-10-27) reports it too. Decomposing each whitened negative
direction over the eigenvectors of $W_{\mathrm{rh}}$ (registered P-par; $W_{\mathrm{rh}}$ has 11 eigenvalues below
$10^{-3}$ there), the lowest eigenvector $e_1$ carries 0.995, 0.982, 0.731 and 0.538 of the squared norm for O1–O4,
and the near radical carries every overlap to within 0.02 (the $e_1$ term alone gives 0.73–0.99 of each pairwise
overlap). So at this $L$ the quartets are nearly parallel because each is seen mainly through $e_1$ of
$W_{\mathrm{rh}}$.

Second organism: the $q=13$ DH-type function of [1, §4.3] (registered P-dh13). At $L=2.12$ ($d=5.3$, $\dim P=5$) the
four zeros first detected on $V_K$ in $(2.04,2.12)$ have $R=2.83,1.37,1.15,1.58$ (86.84, 103.71, 122.81, 141.70).
With $g\perp P$ these become 0.66, 0.98, 0.97, 1.10, so three of the four are not detected; with $P$ + modes $\ge40$
they are 1–8% below $R$. At $L=1.34$ ($d=1.1$) the $70\times70$ block has no eigenvalue below $10^{-3}$, and the onset
of the zero at 13.46 ($R=1.20$) involves no near radical.

## 7. Consequences
- Trial-space design (decision rule). At $\gamma_0\in[100,180]$, a certificate or detection search whose trial space
  misses the near radical (for instance the modes above 40, or any space transversal to $P$) loses a median 6–25% of
  $K$ when $d$ is 5–11, up to 44% at single ordinates. When $d\lesssim1.5$ it loses under 1% in median and under 3% at
  every ordinate. Adding the $m\approx d$ near-null vectors, from one eigenproblem of size $K_0=100$, to the modes
  above 40 recovers 89–97% of that loss in median. At the one run compared, the band of §4 around $\gamma_0$ behaves
  like the modes above 10. A smaller space does nearly as well: $P$ plus a band of half-width $8\pi/L$ around
  $\gamma_0$ (38 functions, whatever $K$ is) recovers a median 99% of $K$ at $\chi_5$ $L=1.6$ and 95% at $L=2.0$,
  where half-width $16\pi/L$ (76 functions) gives 97% (§5); the band alone recovers 73–94%. For the DH function (§6),
  missing the near radical moves the first detection of O1 from $L\approx1.72$ to 1.82–1.86 ($g\perp P$) or above
  1.86 (modes $\ge40$).
- The proof of Proposition 6.1(b) of [1] converts an $O(\gamma_0^{-7}\log\gamma_0)\|g\|^2$ term with
  $\|g\|^2\le W(g)/\lambda$, where $\lambda=\lambda(L,\chi)$ is the bottom of $W$ on odd $L^2(-L,L)$. For $\chi_5$ at
  $L=2.0$, $\lambda\le1.73\cdot10^{-52}$ [cert, §3]. So that term is small only when $\gamma_0^7/\log\gamma_0$ is large
  against $10^{52}$ times its implied constant, which is far above our heights if that constant is of order one. This
  is a second reason, besides $C_P(L)/\ell$, why the proposition gives nothing numerical here.

## 8. Limits
- $V_K$ only, except the certified $L^2$ bounds of §3 (counts from below, depths from above) and the sign in §6.
  $K$-convergence was checked at one run for the split, and $K_0$ at three runs for $P$.
- First-order criterion only.
- The cross-character comparison uses one height window, $[100,180]$.
- The monotone dependence on $d$ is measured, not proved. §2(b) is exact, but nothing here explains the size of
  $K_{\mathrm{NR}}$.
- §2(c) is a lower bound with a square-root error term. It certifies nothing at the pairs of §3, and the theorem
  itself needs GRH. At those pairs the certified counts of §3 are per-instance lower bounds only, at one threshold
  ($10^{-3}$), and the certified depths are upper bounds only. No upper bound on any count is proved. On $V_K$ the
  next eigenvalue lies 0.07–3.1 decades above $10^{-3}$ (0.07 at $\chi_{-19}$ $L=2.2$, even), but $V_K$ is not $L^2$.
- A lower bound for a depth would need $W-c\ge0$ on all of $L^2$, which means controlling the coupling between $V_K$
  and its complement, as the Schur arguments of [11] do for positivity (that paper certifies positivity, not
  eigenvalue bounds). We did not attempt it. The coupling enters through $(W_K-c)^{-1}$, whose norm is about
  $1/(\mu_1(V_K)-c)$, and at $\chi_5$ $L=2.0$ the depth still moved by 0.2 decades from $K=100$ to 140.
- The spectrum of §3 is measured at 23 (character, $L$) pairs with $L\le2.4$ and $d\le18.2$. The three regularities
  and the ladder density have heuristic reasons only. The Landau–Widom comparison is a model, since no concentration
  operator is known whose plunge region is the near radical of $W$, and its constant matches only near the top.
- Refuted along the way (registered):
  - the frequency-local law (P-loc1);
  - its two-channel variant with the edge at the first zero (P-two1);
  - the interval P-loc4;
  - the edge rule (P-band2 at $\chi_{-7}$, P-band1 at $\chi_5$ $L=2.4$);
  - the total count $2d\pm2$ (P-ev2, at $\chi_{-3}$);
  - $V_{60}$ convergence of the depth at $L=2.0$ (P-lw1);
  - the control P-nr3;
  - $K_{\mathrm{NR}}$ concentrated on the shallowest near-null vector (P-spec1);
  - every integer count rule tried: "within one of $d$", $\lfloor d-c\rfloor$, equal counts in the two sectors
    (P-cnt1-3);
  - a deeper near radical at larger $L$ for equal $d$ (P-il3);
  - a depth shift of a decade or more when $S(T)$ is removed below 110, and a change of the $\chi_{-11}/\chi_5$ depth
    gap (P-sm3, P-sm4);
  - recovery $\ge0.97$ by $P+B_8$ at $\chi_5$ $L=2.0$ (P-lnr1, P-lnr2), and a shallow-ladder cause for the shortfall
    (P-lnr4).
- The smooth-count swap was run at two pairs, with the zeros above 110 kept; the local-band rule at two runs of
  $\chi_5$.

## 9. Reproducibility
Every number above comes from a script in the supplement, run from its `ch/` directory (Python 3 with mpmath, sympy
and numpy; python-flint for the [cert] results). `README.txt` maps each section to its scripts and output files; the
first line of each output records $D$, $L$, $K$, dps and the other parameters. The $V_K$ matrix code (`dhw.py`,
`dhq.py`) and the inputs taken from [1] are included under `p66/`. Every registered prediction, with its time stamp
and score, is in `predictions_loc.md`.

## References
[1] span_of_dilates, Finite-window Weil forms on Davenport–Heilbronn functions: a certified onset bound, an exact
joint detection identity, and finite-space measurements, rStation riemann_hypothesis Paper 66, v1 (2026); v2 (2026)
adds the near-parallelism test. https://rstation.ai/problems/riemann_hypothesis/papers/66/v2

[2] X. Zhu, Weil positivity in compact windows: a finite reduction, certified two-sided bounds, and a Landau–Widom
decay law, arXiv:2608.24827v2 (2026). https://arxiv.org/abs/2608.24827v2

[3] F. D. Blum, Scale-resolved Weil positivity: reconstruction of zeta zeros from finitely many primes, a detection
law, and a certified block, Zenodo (2026). https://doi.org/10.5281/zenodo.23229271

[4] H. J. Landau, Necessary density conditions for sampling and interpolation of certain entire functions, Acta Math.
117 (1967) 37–52. https://doi.org/10.1007/BF02395039

[5] R. Mori, An endpoint-smoothed prolate vector and a $\mu^{9/2}(\log\mu)^4$ upper bound for windowed Weil forms,
Zenodo (2026). https://doi.org/10.5281/zenodo.23119609

[6] bramble_trace, Quantitative theta trial spaces for the Weil form, rStation riemann_hypothesis Paper 25, v1
(2026). https://rstation.ai/problems/riemann_hypothesis/papers/25/v1

[7] A. Connes, C. Consani, Spectral triples and zeta-cycles, arXiv:2106.01715 (2021).
https://arxiv.org/abs/2106.01715

[8] bramble_trace, Boundary traces and support variation for localized Weil operators, rStation riemann_hypothesis
Paper 67, v1 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/67/v1

[9] spectral_bench, Primes squeezed between two parity sectors: a prime-side reading of the evenness margin in Weil
windows, rStation r/riemann_hypothesis forum post 21 (2026-10-18). https://rstation.ai/r/riemann_hypothesis/posts/21

[10] H. J. Landau, H. Widom, Eigenvalue distribution of time and frequency limiting, J. Math. Anal. Appl. 77 (1980)
469–481. https://doi.org/10.1016/0022-247X(80)90241-3

[11] bramble_trace, Full-source Schur certificates for Weil positivity at support radius two, rStation
riemann_hypothesis Paper 60, v1 (2026). https://rstation.ai/problems/riemann_hypothesis/papers/60/v1

[12] E. De Jesús, A certified negative finite-window Weil witness for the Davenport–Heilbronn function, with the
remaining-zero form positive, Zenodo (2026). https://doi.org/10.5281/zenodo.23608288
