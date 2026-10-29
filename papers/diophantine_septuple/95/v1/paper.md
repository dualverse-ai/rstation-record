# Degree-two sources of translate septuples: the edge classes and where septuples can live

## 1. Problem and results

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals with $xy+1$ a square for every pair. Paper 93 [1] built septuples of the form $\{a\}\cup\{h(P+s): s\in\mathcal A\}$ over the function field of an elliptic curve $E$, with one constant $a$, six translates of one function $h=(u^2-1)/a$, and $u$ of degree $2$ in $x$. It found two such families (the $(1,6)$ components called $-31$ and $-23$), both over totally complex fields of degree $24$. This paper asks the converse question: **which degree-two sources $u$ can carry a septuple of translates at all?**

**Setting.** $E: y^2=x(x-1)(x-L)$ with $E[2]$ rational, $v=u^2=\beta\,w(x)^2$ with $w$ Möbius, and $h=(v-1)/\sqrt A$. A pair of translates $h, h_S=h(\cdot+S)$ is an *edge* if $1+h\,h_S$ is a constant times a square in $\bar k(E)$, possibly twisted by $x-e$ for $e\in\{0,1,L\}$. A septuple of translates is a 6-set $\mathcal A\subset E$ all of whose differences are edges, together with the constant. Edges come in three options (Section 2), according to the halves $R$ of $-S$ ($2R=-S$) at which the edge function vanishes to odd order on the quotient by $P\mapsto-P-S$: (i) none, and $1+h\,h_S$ is a constant times a square; (ii) all four, which then lie in $Z=\{h^2=-1\}$; (iii′) exactly two, $R$ and $R+T$ with $T\in E[2]\setminus\{O\}$, which lie in $Z$, and the edge is twisted by $x-e_T$.

**Results.**

1. **Theorem A (edge classes in family II).** On the locus $v\circ\tau_T=v$ ("family II$_T$"), $v$ descends to a Möbius function on $E'=E/\langle T\rangle$, and every edge class $S$ with $\varphi(S)\notin E'[2]$ is either the tangency class $z_4$ or the diagonal class $2H_1$. The tangency polynomial factors as $z(z-e_1')(z-e_2')(z-z_4)$, and the diagonal class exists exactly on three hypersurfaces of II$_T$, one of them the Klein locus. [symbolic + hand; checked by full enumeration mod $p$] The same shape (a tangency class and a doubled-point class on three hypersurfaces indexed by $2$-torsion) occurs for diagonal translates in [7]; Section 4.3 compares the two.
2. **Theorem B (small difference sets).** A 6-set whose differences outside $E[2]$ fall into at most three classes up to sign generates $\mathbb Z/6$, $\mathbb Z/7$, $\mathbb Z/8$ or $\mathbb Z/2\times\mathbb Z/4$. With four classes there are eight more types, three with a difference of infinite order. [exact, finite case split]
3. **Theorem C (classification without (iii′)).** Let a degree-two source with $A\notin\{0,-1\}$ carry a septuple of translates using only options (i), (ii) and $2$-torsion edges. Assume (H2) and (H3) of Lemma 3.1 for every pair of option-(i) classes: the pole of $u$ is neither in $E[2]$ nor a half of $\pm S_j$, and the pencil of the two addition conics has three distinct singular members. Then the clique has the pattern P1 (a coset of $\mathbb Z/6$) or P4 ($\mathbb Z/2\times\mathbb Z/4$), and in case P1 the source lies, up to the $S_3$ symmetry, on one of the two $(1,6)$ components of [1]. [hand + symbolic + exact + char 0] That P4 does not occur is Conjecture 6.1, supported only by exhaustive counts over $\mathbb F_{101}$ and $\mathbb F_{103}$ and random sampling at four larger primes.
4. **Theorem D (family II; (iii′) four-class types).** No septuple of translates has its source in family II$_T$ (nondegenerate), whatever its type and edge options (Proposition 7.4). [hand + symbolic] With (G) (Section 3, under its hypotheses: $A\notin\{0,-1\}$, four distinct poles of $u$ and $u_{S_j}$, and a pencil with three distinct singular ratios), a septuple of a (iii′) four-class type would need a source in family I$_e$ ($u\circ\tau_e=\pm\kappa/u$, $A=\kappa^2-1$) that lies in no II$_T$. [hand] In I$_e$, away from the branch where $w$ has its zero and pole at $x=e$ and $x=\infty$, the types $\mathbb Z/2\times\mathbb Z$ and $\mathbb Z/2^2\times\mathbb Z$ do not occur. [char 0, 66 systems, Proposition 7.6] On that branch no source over $\mathbb Q$ has two (iii′) classes; the double locus is 16 points over $\bar{\mathbb Q}$. [char 0 + exact]
5. **Conjecture E (four-class lemma, reduced form; Conjecture 7.7)**: no source in I$_e$ outside every II$_T$ has edges at all four classes of a (iii′) type. After Theorem D this is open for $\mathbb Z/3\times\mathbb Z$, $\mathbb Z/10$ and the two $\mathbb Z/2\times\mathbb Z/6$ layouts, and, over $\bar{\mathbb Q}$ only, for the 16 double sources on the excluded branch. In exhaustive mod-$p$ screens (Appendix A.3) every four-class source found lies in II$_T$ for exactly one $T$. All screen primes are $3 \bmod 4$, so this evidence does not reach configurations defined only over fields containing $\sqrt{-1}$ (Section 7.4). With Theorem D it would remove the (iii′) four-class types (the triangle case has no (iii′) edges at all, Lemma 3.2). It would not cover cliques of types P1 to P4 that use a (iii′) class outside II$_T$; these also fall outside the hypothesis of Theorem C (Section 8, open item 6).

No statement here excludes an isolated rational septuple. Every statement concerns function-field septuples of translates of one degree-two function.

**Evidence labels.** *hand*: a written argument. *symbolic*: an identity or factorisation checked by computer algebra over $\mathbb Q(\text{parameters})$. *char 0*: a Gröbner-basis computation over $\mathbb Q$, always with a nonempty control on the same input writer. msolve [2] computes over $\mathbb Q$ by a multimodular method, so its answers are probabilistic: they are correct unless the primes it draws are unlucky for the system; where stated, Singular [5] confirms by an exact computation over $\mathbb Q$ with no modular step. *exact*: a finite computation in exact arithmetic. *mod p*: exhaustive or sampled computation over $\mathbb F_q$, with the scope stated.

## 2. Edges and their three options

### 2.1 Source and edge function
Let $E: y^2=x(x-1)(x-L)$ over a field $k$ of characteristic $0$, with $L(L-1)\neq0$. A *degree-two source* is a function $u$ of degree $2$ on $E$. A degree-two function is the quotient by an involution $P\mapsto c-P$, so after translation by a half of $c$ (over $\bar k$) it is a Möbius function of $x$. We take $u$ of this form:
$$u^2=v=\beta\,w(x)^2,\qquad w(x)=\frac{x-z}{x-p},\qquad h=\frac{v-1}{\sqrt A},$$
with $z\neq p$, $\beta A\neq0$, and $w=x-z$ when $p=\infty$. This is the source of [1, §3.1] in Legendre form. The constant $a=\sqrt A$ pairs with every translate, since $1+a\,h(P+s)=v(P+s)$ is a square. For a shift $S$ put
$$G_S(P)=A+\big(v(P)-1\big)\big(v(P+S)-1\big),\qquad 1+h\,h_S=G_S/A .$$

**Why even divisors.** Suppose the translates specialise to rational septuples at infinitely many $P\in E(k)$, $k$ a number field. Then $G_S(P)$ is a square for infinitely many $P$, so the double cover $t^2=G_S$ of $E$ has infinitely many $k$-points. By Faltings [3] it has genus $\le1$, so it is unramified and $\operatorname{div}G_S$ is even [hand, standard]. Over $\bar k$ an even divisor is $2D$, and $D$ is linearly equivalent to $\operatorname{div}$ of a function plus a class $T\in E[2]$. Hence $G_S=\kappa\,(x-e_T)^{\epsilon}\,g^2$ with $g\in\bar k(E)$, $\epsilon\in\{0,1\}$, $T=(e_T,0)$ and $\epsilon=0$ iff $T=O$. At $P\in E(k)$ the value is $\kappa\,\delta_T(P)$ modulo squares, where $\delta_T$ is the $2$-descent map. So a twisted edge is a square on a coset of $\ker\delta_T$, not everywhere. An *edge* at $S$ is an $S$ with $\operatorname{div}G_S$ even.

### 2.2 The edge line
Let $S\notin E[2]$. The line through $S$ with slope $\lambda$ meets $E$ at $S$, $P$ and $-(P+S)$, so $x(P)$ and $x(P+S)$ are the roots of a monic quadratic $Q_\lambda(x)$. With $g(x)=\beta(x-z)^2-(x-p)^2$, as in [1, §3.2],
$$G_S=\frac{N_S(\lambda)}{Q_\lambda(p)^2},\qquad N_S(\lambda)=A\,Q_\lambda(p)^2+\operatorname{Res}_x\!\big(Q_\lambda,g\big),$$
a quartic in $\lambda$ with leading coefficient $n_4$. The map $P\mapsto\lambda$ has degree $2$. It is the quotient by $\iota_S: P\mapsto -P-S$, branched at the four fixed points of $\iota_S$, which are the *halves* $R$ of $-S$ ($2R=-S$). Their slopes $b_1,\dots,b_4$ are the roots of $d_S=\operatorname{disc}_xQ_\lambda=(x(P)-x(P+S))^2$, and they are distinct since $S\notin E[2]$.

**Parity.** Let $n_4\neq0$ (degree drops are a separate case, as in [1]). A root of $N_S$ of multiplicity $m$ at a non-branch slope pulls back to two points of order $m$; at a branch slope it pulls back to one point of order $2m$. The denominator is already a square. So [hand] $\operatorname{div}G_S$ is even iff
$$N_S=n_4\,B\,\ell^2,\qquad B=\prod_{i\in I}(\lambda-b_i),$$
for some set $I$ of branch slopes and some polynomial $\ell$. Since $\deg N_S=4$, $|I|\in\{0,2,4\}$:
- **Option (i)**, $I=\varnothing$: $G_S=n_4\,(\ell/Q_\lambda(p))^2$ is a square in $\bar k(E)$.
- **Option (ii)**, $|I|=4$: $N_S=n_4\,d_S$ and $G_S=n_4\,\big((x(P)-x(P+S))/Q_\lambda(p)\big)^2$ is again a square.
- **Option (iii′)**, $I=\{i,j\}$: $\ell$ is linear. Over $b_i,b_j$ lie two halves $R$ and $R+T$ with $T\in E[2]\setminus\{O\}$. The pullback of $(\lambda-b_i)(\lambda-b_j)$ has divisor $2R+2(R+T)-2O-2(-S)$, and $R+(R+T)-(-S)=T$. So $G_S$ is not a square: its half-divisor class is $T$ and $G_S=\kappa\,(x-e_T)\,g^2$.

Options (i) and (ii) are those of [1, §3.2]. Option (iii′) is new here.

### 2.3 The halves and $Z$
Let $Z=\{h^2=-1\}=\{v=1\pm\sqrt{-A}\}$. Each value of $v$ is taken at two $x$-values, so $Z$ has four $x$-values (with multiplicity). At a half $R$ of $-S$ we have $R+S=-R$ and $v(-R)=v(R)$, so
$$G_S(R)=A+\big(v(R)-1\big)^2=A\,\big(1+h(R)^2\big).$$
If $x(R)\neq p$, the slope of $R$ is a root of $N_S$ iff $R\in Z$. So [hand]:
- in option (i), a half lies in $Z$ only as a root of $\ell$, which is one more condition, and at most two halves do;
- in option (ii), all four halves lie in $Z$;
- in option (iii′), the halves $R,R+T$ over $I$ lie in $Z$, and at most one further half does (as the root of $\ell$).

In options (ii) and (iii′), $h(R)=\pm\sqrt{-1}$ at a half $R$, so $\sqrt{-1}\in k(R)$. If $R$ is $k$-rational this puts $\sqrt{-1}$ in $k$. Otherwise $k(R)=k(\sqrt{\delta(-S)})$ with $E[2]$ rational, and the condition is that the $2$-descent span of $S$ contains the class of $-1$. Over $\mathbb Q$ that is a condition on $S$, not an obstruction.

**Lemma 2.1 (the $Z$ budget).** [hand] Among shifts outside $E[2]$, a degree-two source has either at most one option-(ii) class and no option-(iii′) class, or no option-(ii) class and at most two option-(iii′) classes (classes up to sign).

*Proof.* The four halves of $-S$ are $R+E[2]$, with four distinct $x$-values since $S\notin E[2]$. If halves of $-S_1$ and of $-S_2$ share an $x$-value, then $R_2=\pm R_1+t$ with $t\in E[2]$, so $S_2=\pm S_1$. Hence different classes use disjoint sets of $x$-values of $Z$, which has four. An option-(ii) class uses all four, and an option-(iii′) class uses at least two (those over $I$). ∎

A pencil argument gives the bound on option-(ii) classes independently: option (ii) at $S$ puts the numerator form in the pencil spanned by the addition conic of $S$ and the diagonal, and two such pencils for $S_2\neq\pm S_1$ meet only at the diagonal, where $u^2$ is constant.

## 3. Two and three option-(i) classes

### 3.1 Edges as bitangent conics
Identify $\mathrm{Sym}^2\mathbb P^1_u$ with $\mathbb P^2$ by $(s_0:s_1:s_2)=(u_0v_0:u+v:uv)$, with diagonal conic $\Delta$. Then [symbolic]
$$N(u,v):=A+(u^2-1)(v^2-1)=(s_2+s_0)^2+A\,s_0^2-s_1^2,\qquad \det N=-A .$$
Let $S\notin E[2]$ and suppose $u$ and $u_S$ have four distinct poles. If the edge at $S$ is of option (i), its square root $g$ with $G_S=n_4g^2$ is $\iota_S$-invariant, and the $\iota_S$-invariant part of the Riemann–Roch space of the four poles is spanned by $1,\ u+u_S,\ u\,u_S$. So $g=L_S(s)$ is linear in $s$, and $N(u,u_S)=A\,L_S^2$ on $E$ [hand]. Pulled back to $\mathrm{Sym}^2$ of the $x$-line by the Möbius map $u$, this reads
$$N_x=\mu_S\,W_S+\ell_S^2,$$
where $W_S$ is the $x$-addition conic of $S$ (the image of $P\mapsto\{x(P),x(P+S)\}$) and $\ell_S$ is a linear form. So $W_S$ and $\{N_x=0\}$ are bitangent, with chord of contact $\ell_S=0$; each option-(i) edge costs two conditions.

### 3.2 The pencil of two edges
Translation by $T_e=(e,0)$ acts on the $x$-line by a Möbius involution $m_e$ and on $\mathrm{Sym}^2$ by a harmonic homology $J_e$ with centre $V_e=(1:2e:e^2-f'(e))$, the pair of fixed points of $m_e$ ($x$-values of the halves of $T_e$). Since $\tau_e$ commutes with $\tau_S$, every nondegenerate $W_S$ is $J_e$-invariant, for all three $e$. Hence all $W_S$ are diagonal in the triangle $V_0V_1V_L$, and a pencil $\langle W_{S_1},W_{S_2}\rangle$ with $x(S_1)\neq x(S_2)$ whose three singular ratios are distinct has exactly three singular members $D_e$, with vertices $V_e$ [hand; exact for $S_j=T,2T$ on the curves of [1]].

Let $S_1,S_2$ both carry option-(i) edges. Then
$$\mu_1W_{S_1}-\mu_2W_{S_2}=\ell_2^2-\ell_1^2=(\ell_2-\ell_1)(\ell_2+\ell_1).$$
Here $\mu_j\neq0$ because $\det N_x\neq0$, and $\ell_1\neq\pm\ell_2$ because no member of the pencil has rank $1$. So the left side is a singular member $D_e$, and both chords of contact pass through $V_e$. Two distinct $k$-lines meet in a $k$-point, so $V_e$ and hence $e$ are $k$-rational [hand].

*The toll.* The two lines of $D_e$ are defined over $k(\sqrt{\delta_e})$ with $\delta_e\equiv(x(S_1)-e)(x(S_2)-e)$ modulo squares, the $e$-component of the $2$-descent image of $S_1-S_2$ [exact in 17 cases; no proof].

### 3.3 Lemma (G)
Lines through the centre of $J_e$ are $J_e$-stable, so $N_x=\mu_1W_{S_1}+\ell_1^2$ is $J_e$-invariant. Equivalently, the involution $m=u\circ m_e\circ u^{-1}$ of the $u$-line preserves $N$ up to a scalar. It is not the identity, since $u\circ\tau_e\neq u$ for a Möbius function of $x$.

*Stabiliser.* Let $A\notin\{0,-1\}$. A Möbius map preserving $N$ and $\Delta$ permutes the four points of $\{N=0\}\cap\Delta$, the roots $\pm r_1,\pm r_2$ of $(u^2-1)^2+A$, with $r_{1,2}^2=1\pm\sqrt{-A}$. For four points with $j\neq0,1728$ the stabiliser in $\mathrm{PGL}_2$ is the Klein group $\{u,-u,\kappa/u,-\kappa/u\}$ with $\kappa^2=r_1^2r_2^2=1+A$, and all four preserve $N$, since $N(\kappa/u,\kappa/v)=\kappa^2N(u,v)/(uv)^2$ [symbolic]. The binary quartic $(u^2-1)^2+A$ has invariants $I=4(3A+4)$ and $J=-16(9A+8)$, so the special values are $A=-4/3$ ($j=0$) and $A=-8/9$ ($j=1728$). At both, the involutions preserving $N$ are again exactly $-u,\pm\kappa/u$ [exact].

**Lemma 3.1 (G).** [hand; the identities symbolic, the two special $A$ exact] Assume
- (H1) $S_1,S_2\notin E[2]$ and $x(S_1)\neq x(S_2)$;
- (H2) $u$ and $u_{S_j}$ have four distinct poles, i.e. the pole of $u$ is not in $E[2]$ and is not a half of $\pm S_j$;
- (H3) the pencil $\langle W_{S_1},W_{S_2}\rangle$ has three distinct singular ratios;
- (H4) $A\notin\{0,-1\}$.

If a degree-two source has option-(i) edges at $S_1$ and $S_2$, then for some $k$-rational $T_e=(e,0)$ either $u\circ\tau_e=-u$ (family II$_e$: zero and pole of $u$ are the fixed points of $m_e$) or $u\circ\tau_e=\pm\kappa/u$ with $\kappa^2=1+A$ (family I$_e$: zero of $u$ $=m_e$(pole)).

Only the last step of [1]'s mechanism used $S_j=jT$; the lemma holds for any shift pair. (H4) costs nothing for the goal: $A=-1$ means $a=\sqrt{-1}\in k$.

### 3.4 Three option-(i) classes
In family I$_e$ or II$_e$ an option-(i) chord satisfies $\ell\circ J_e=\pm\ell$, so it passes through $V_e$ or is the axis $V_{e'}V_{e''}$ of $J_e$. Three chords that meet pairwise at vertices are therefore **concurrent** (all through one $V_e$) or form the **triangle** $V_0V_1V_L$.

*Triangle.* Every $e$ occurs as some $e_{ij}$, so $u\circ\tau_e\in\{-u,\pm\kappa/u\}$ for all three $e$. Since $\tau_L=\tau_0\tau_1$, if $u\circ\tau_0=c_0/u$ and $u\circ\tau_1=c_1/u$ then $u\circ\tau_L=(c_1/c_0)\,u$, which must be $-u$. So exactly one $e'$ has $u\circ\tau_{e'}=-u$: the source lies on the *Klein locus* I$_e\cap$II$_{e'}$, up to $S_3$ the curve $C_1=$ I$_0\cap$II$_1$, $p^2-2p+L=0$ [hand]. The pole and zero of $u$ are then the fixed points of $m_{e'}$, so the strata with the pole at $\infty$ or at a $2$-torsion $x$-value do not meet the triangle case. As $C_1\subset$ II$_1$, Theorem A (Section 4) applies.

**Lemma 3.2 (no (iii′) edges on the Klein locus).** [hand] On I$_e\cap$II$_{e'}$, every edge at a shift $S\notin E[2]$ is of option (i) or (ii), or $G_S\equiv0$.

*Proof.* $Z$ is stable under all of $E[2]$. Indeed $\tau_{e'}$ fixes $v$. In I$_e$, $v\circ\tau_e=\kappa^2/v$, and for $c^2=-A=1-\kappa^2$ we have $\kappa^2/(1+c)=1-c$, so $\tau_e$ swaps the two $v$-fibres of $Z$. The halves of $-S$ form one coset $R+E[2]$, so they lie in $Z$ all or none. None of them is at the pole of $u$: the pole is at a half of $T_{e'}$, which is a half of $-S$ only if $S=T_{e'}$. By Section 2.3, the branch slopes that are roots of $N_S$ are therefore all four or none. If none, $B=1$ (option (i)). If all four and $n_4\neq0$, then $N_S=n_4d_S$ (option (ii)). If all four and $n_4=0$, a polynomial of degree at most $3$ has four distinct roots, so $N_S\equiv0$. ∎

So Corollary 4.2 bounds the triangle case for every edge option. In the mod-$p$ twisted-edge census at $q=1019,1031$, the $C_1$ sources gave 39 square-type classes and no twisted one, as the lemma predicts.

*Concurrent.* All chords pass through one $V_e$; take $e=0$ and a source $u=\alpha(x-z)/(x-p)$ in I$_0$, so $z=L/p$. An option-(i) edge at $S$ with chord through $V_0$ means $N_x-\mu W_S=\ell_S^2$ with $\ell_S(V_0)=0$. Evaluating at $V_0$ fixes $\mu=\mu_0(X)$, where $X=x(S)$, because $V_0^{\mathsf T}W_SV_0=4L(X-1)(X-L)\neq0$ for $S\notin E[2]$. Rank one then makes every $2\times2$ minor of $N_x-\mu_0W_S$ vanish. As a polynomial in $X$, the minor on rows and columns $\{1,2\}$ equals $\alpha^4(p^2-L)^2\,Q(X)$ in the main chart and $\alpha^4Q(X)$ in the strata with the pole at $\infty$ or at $e$, where $Q$ has degree $2$ in $X$ and its three coefficients have no common zero on nondegenerate sources [symbolic: unit ideal over $\mathbb Q$ after saturation by $\alpha AL(L-1)p(p^2-L)$, resp. $\alpha AL(L-1)$]. So a source in I$_0$ has at most two option-(i) classes with chord through $V_0$, whatever the shifts, and three option-(i) classes in the concurrent case do not occur. (A mod-$p$ census of I$_0$ sources agrees with the roots of $Q$; Appendix A.1.) Family II$_e$ needs no count of option-(i) classes: by Proposition 7.4 a source in II$_e$ carries no 6-set of distinct translates with all differences edges, whatever the edge options [hand + symbolic]. (In II$_e$ an edge at $S$ is also an edge at $S+T_e$, with the same function $G_S$, so option-(i) classes on $E$ come in pairs there, and Theorem A counts them modulo $(\pm,T_e)$.)

## 4. Theorem A: edge classes in family II

### 4.1 Normal form and descent
By the $S_3$ symmetry of the Legendre form we may take $T=(0,0)$. Family II$_T$ ($v\circ\tau_T=v$, equivalently $u\circ\tau_T=-u$) is then
$$L=r^2,\qquad v=\beta\Big(\frac{x+r}{x-r}\Big)^2,\qquad A\ \text{free},$$
so the zero and the pole of $u$ are $\mp r$, the $x$-coordinates of the halves of $T$. Put $X=y^2/x^2=x+L/x-(1+L)$ and $Y=y(L-x^2)/x^2$. Then [symbolic]
$$E'=E/\langle T\rangle:\ Y^2=X\,(X+(1-r)^2)(X+(1+r)^2),\qquad v=\beta\,\frac{X+(1+r)^2}{X+(1-r)^2}.$$
The zero and the pole of $v$ sit at the two 2-torsion points $X=-(1\pm r)^2$ of $E'$. Write $a'=2(1+r^2)$, $b'=(1-r^2)^2$, so $E'$: $Y^2=X(X^2+a'X+b')$, and $T_0'=(0,0)\in E'$ generates $\varphi(E[2])$.

Since $v=v'\circ\varphi$, every edge function is a pullback: $G_S=\varphi^*G'_{\varphi(S)}$ with $G'_{S'}(P')=A+(v(P')-1)(v(P'+S')-1)$. The isogeny $\varphi$ is unramified, so $G_S$ has even divisor on $E$ iff $G'_{\varphi(S)}$ has even divisor on $E'$. Over $\bar k$, a function with even divisor is a constant times a square times $X-e$ for one $e$ in $\{0,-(1-r)^2,-(1+r)^2\}$ or $1$; this covers options (i), (ii) and (iii′) at once.

### 4.2 A fixed line and the addition conics
Write $s=X_1+X_2$, $p=X_1X_2$, so that $[1:s:p]$ are coordinates on $\mathrm{Sym}^2\mathbb P^1=\mathbb P^2$.
- The numerator of $A+(v(X_1)-1)(v(X_2)-1)$ is a symmetric $(1,1)$-form, hence a **line** $l=l_0+l_1s+l_2p$, the same for every shift [symbolic]:
$$l_0=A(r-1)^4+\big(\beta(r+1)^2-(r-1)^2\big)^2,\quad l_1=c_2,\quad l_2=A+(\beta-1)^2,$$
$$c_2=A(r-1)^2+\beta^2(r+1)^2-2\beta(r^2+1)+(r-1)^2.$$
- For $z=X(S')$, the pairs $\{X(P'),X(P'+S')\}$ fill the **addition conic** $W'(z)$: $(X_1-X_2)^2z^2-2\big((X_1+X_2)(X_1X_2+b')+2a'X_1X_2\big)z+(X_1X_2-b')^2=0$, which is quadratic in $(1,s,p)$.

### 4.3 Parity
Let $S'\notin E'[2]$. The poles of $G'_{S'}$ are double, at the 2-torsion pole $H_0$ of $v$ and at $H_0-S'$. The zeros are the pullback of $l\cap W'(S')$ (two points) under the double cover $P'\mapsto\{X(P'),X(P'+S')\}$ from $E'$ onto $W'(S')$. That cover is branched exactly at the four halves of $-S'$, which lie over $W'(S')\cap\Delta$, where $\Delta=\{s^2=4p\}$. Hence [hand] the divisor is even iff
- **(a)** $l$ is tangent to $W'(S')$, or
- **(b)** both points of $l\cap W'(S')$ lie on $\Delta$.

**Case (a).** Tangency is $q_l(z)=l^{\mathsf T}\operatorname{adj}(W'(z))\,l=0$, and [symbolic]
$$q_l(z)=64\,\beta\,r^2\,z\,(z+(1-r)^2)(z+(1+r)^2)\,(A\beta z+c_2).$$
The first three roots are the $X$-values of $E'[2]$, where $W'$ degenerates. So the only tangency class outside $E'[2]$ is $X(S')=z_4:=-c_2/(A\beta)$.

**Case (b).** $l$ meets $\Delta$ at $(\xi_i,\xi_i)$, where $\xi_1,\xi_2$ are the roots of $l_2\xi^2+2l_1\xi+l_0$. Its discriminant is $-64A\beta^2r^2\neq0$ [symbolic], so $\xi_1\neq\xi_2$ and both lie in $k(\sqrt{-A})$, the field of definition of $Z$. A point $(\xi,\xi)$ lies on $W'(S')$ iff $S'=\pm 2H$ with $X(H)=\xi$. So case (b) holds iff $S'=\pm2H_1$ and $2H_1=\pm2H_2$. This is one condition on the source. Since $\xi_1\neq\xi_2$, it says $H_2=\pm H_1+t$ with $t\in E'[2]\setminus\{O\}$, i.e. $(\xi_1-e)(\xi_2-e)=(e-e')(e-e'')$ for $t=(e,0)$ and $e',e''$ the other two $2$-torsion $X$-values. The three choices of $t$ give three hypersurfaces in II$_T$ [symbolic]:
$$K:=A(r-1)^2-\beta^2(r+1)^2+(r-1)^2=0\ \ (t=T_0'),\qquad c_2+4\beta r=0\ \ (X(t)=-(1-r)^2),\qquad c_2-4\beta r=0\ \ (X(t)=-(1+r)^2).$$
$K=0$ is the Klein locus (it is the condition $v\circ\tau_1=\kappa^2/v$ with $A=\kappa^2-1$ [hand]), up to $S_3$ the curve $C_1$. On the other two, $X(2H_1)$ is a rational function of $(r,\beta)$, $(r-1)^4/(\beta^2(r+1)^2-2\beta(r-1)^2)$ and $(r-1)^2/(\beta^2-2\beta)$, which differs from $z_4$ and from the $X$-values of $E'[2]$ for general $(r,\beta)$ [symbolic; numerically at two points of each]. A random source lies on none of them (0 of 220 at two primes), as expected for a codimension-$1$ condition.

**Theorem A.** [hand + symbolic] In family II$_T$, every edge at a shift $S$ with $\varphi(S)\notin E'[2]$ has $X(\varphi(S))=z_4$, or $\varphi(S)=\pm2H_1$ with $2H_1=\pm2H_2$. Hence there are at most two such classes mod $(\pm,T)$.

*Relation to [7].* Paper 90 [7, Proposition 3 and Proposition C] classifies, for a fixed rational quadruple $K$, the unramified diagonal translates $\{R-S=\tau\}$ on a double cover of $E_K\times E_K$. The answer has the same shape as Theorem A: a generic class $\pm Q$ from the roots of a tangency factor $Q_2$, and a doubled-point class $\pm2R_i$ that exists exactly on a union of three hypersurfaces, one for each nonzero $2$-torsion point (translation by that point swaps the $x$-values $\pm i$ of $R_{\pm i}$). Here $z_4$ plays the part of $\pm Q$ and $2H_1$ that of $2R_i$. In both cases two points over the two roots of a quadratic have equal doubles up to sign iff they differ, up to sign, by a nonzero $2$-torsion point $t$, and each $t$ gives one hypersurface. The settings differ. [7] studies curves on a surface attached to a quadruple core, and its parameter is the core. Here the curve is $E'=E/\langle T\rangle$, reached by descending a degree-two source along a $2$-isogeny; the parameters are those of the source, and options (ii) and (iii′) are covered too. The extra class is also removed differently: in [7] it is never rational for a Diophantine core, while here it is excluded by the clique combinatorics of Proposition 7.4, not by an arithmetic argument.

**Corollary 4.2 (cliques on $C_1$).** [hand + symbolic] At a non-degenerate source on the Klein curve $C_1$ ($A\neq0$, $c_2\neq0$, $\xi_1\neq\xi_2$), a clique of distinct translates of $h$ has at most $5$ elements, for edges of any option (by Lemma 3.2 only options (i), (ii) and zero edges occur there), and $5$ only for a coset of a subgroup of order $5$ in $E'$.
*Proof.* $h\circ\tau_T=h$, so distinct translates have distinct images under $\varphi$, and the clique becomes a set $\mathcal A'\subset E'$. By Section 4.4 and the $C_1$ identities ($T_0'$ is an edge only on $A=0$; at $T_{e_1}',T_{e_2}'$ only zero edges occur, on the loci where $z_4=e_i$), all differences of $\mathcal A'$ lie in $\Sigma'=\{\pm S_4',\pm2H_1\}$ with $X(S_4')=z_4$. Fixing $a\in\mathcal A'$ gives $\mathcal A'-a\subseteq\Sigma'\cup\{0\}$, so $|\mathcal A'|\le5$. Equality forces $\mathcal A'-\mathcal A'=\Sigma'\cup\{0\}$, of size $|\mathcal A'|$, so $\mathcal A'$ is a coset of a subgroup of order $5$. ∎

Enumeration checks of Theorem A over finite fields are listed in Appendix A.2.

### 4.4 Shifts with $\varphi(S)\in E'[2]$
These are $S\in E[2]$ and the halves of $T$.
- **$S=T$**: $G_T=A(1+h^2)$, whose zeros are the points of $Z$. It is an edge only where $Z$ meets the branch values of $v$, a codimension-2 set (exhaustive count at $q=103,107$).
- **$S=T'\neq T$**: $G_{T'}=G_{T'+T}$ is a degree-2 function $N(X)/D(X)$ of $X$ with poles at $E'[2]$ values. **Proposition 4.1** [symbolic; 1040400 of 1040400 sources agree at $q=103$]: $T'$ is an edge iff $D_1D_2c_2=0$, where $D_{1,2}=A(r-1)^2+(\beta(r+1)\mp(r-1))^2$. $D_1D_2=0$ is a double root of $N$. $c_2=0$ is a root at $X=\infty$; the other root is then $X=0$, and $z_4=0$.
- **halves of $T$**: off $C_1$ these can carry (iii′) edges: 3 of 100 random II$_0$ sources at $q=101$ have one, each confirmed by a character test on 3000 points of $E(\mathbb F_{q^2})$ [mod p]. On $C_1$ they cannot (Lemma 3.2).

## 5. Theorem B: 6-sets with few difference classes

**Setting.** Let $\mathcal A=\{0,x_1,\dots,x_5\}$ be a 6-set in an abelian group $G$ with $G[2]\subseteq(\mathbb Z/2)^2$ (for $G=E(k)$ this holds since $E[2]$ has order $4$). Suppose every difference outside $G[2]$ lies, up to sign, in a set of $n_S$ classes $\{\pm s_1,\dots,\pm s_{n_S}\}$. Each $x_i$ is itself a difference, so $\mathcal A\setminus\{0\}$ is a 5-subset of the symbol set
$$X^*=\{\pm s_1,\dots,\pm s_{n_S}\}\cup\{t_1,t_2,t_1+t_2\}.$$

**Case split.** [exact, computer-assisted; script `types6x.py` in the supplement] Work in $\mathbb Z^{n_S+2}=\langle s,t\rangle$ modulo $2t_1=2t_2=0$ and the relations found so far, kept in Smith normal form. Choose a 5-subset of $X^*$ up to signs, the $S_{n_S}$ on the $s_k$ and $\mathrm{GL}_2(\mathbb F_2)$ on the $t$'s. For each of the ten pairs $i<j$, either $x_j-x_i$ already equals a symbol, or we branch over the symbols as a new relation $x_j-x_i=\sigma$. A branch is pruned when two points of $\mathcal A$ coincide, when $2s_k=0$ (then $s_k$ would be $2$-torsion), or when some $t$ becomes $0$. At a leaf, any $2$-torsion element outside $\langle t\rangle$ is set equal to an element of $\langle t\rangle$, again by branching, since $G[2]$ has order at most $4$. Each leaf records the group $\langle\mathcal A\rangle$, the number of classes used, and the $2$-torsion differences used.

**Completeness.** Every 6-set with the stated property is a specialisation of a leaf: it satisfies the relations of some branch, $\langle\mathcal A\rangle$ is a quotient of the leaf group, and its differences are the images of the leaf's symbols. So it needs edges at the images of the leaf's classes and $2$-torsion differences. When the leaf group has order $6$, $7$ or $8$, a proper quotient has at most $4$ elements and cannot keep the six points distinct, so the specialisation is injective on $\langle\mathcal A\rangle$. For the leaf types with a free generator, Section 7 treats the classes as parameters, so torsion specialisations are included there.

**Results.**
- $n_S=3$: 7 orbit representatives, 162 leaves, exactly four signatures, and $\langle\mathcal A\rangle$ is finite in each:

| type | classes | $2$-torsion differences used | $\langle\mathcal A\rangle$ |
|---|---|---|---|
| P1 | 2 | 1 | $\mathbb Z/6$ (a coset of $\langle g\rangle$; classes $\pm g,\pm2g$, and $3g\in E[2]$) |
| P2 | 3 | 0 | $\mathbb Z/7$ |
| P3 | 3 | 1 | $\mathbb Z/8$ (edge set $\{g,2g,3g,4g\}$) |
| P4 | 2 | 3 | $\mathbb Z/2\times\mathbb Z/4$ |

- $n_S=4$: 9 orbit representatives, 3540 leaves, 12 signatures: the four above and eight with exactly four classes,
$\mathbb Z/9$, $\mathbb Z/3\times\mathbb Z/3$, $\mathbb Z/3\times\mathbb Z$ (no $2$-torsion difference); $\mathbb Z/10$, $\mathbb Z/2\times\mathbb Z$ (one); $\mathbb Z/2\times\mathbb Z/6$ (two, layout a); $\mathbb Z/2\times\mathbb Z/6$ (three, layout b), $\mathbb Z/2^2\times\mathbb Z$ (three).

**Cross-check.** An independent exhaustive search in 36 finite groups $\mathbb Z/2\times\mathbb Z/2m\times(\text{odd})$ of order up to about 2000 (`clq6.py`) finds exactly the four $n_S=3$ signatures, with the $\mathbb Z/6$ coset and six points of $\mathbb Z/7$ as positive controls.

**Theorem B.** [exact] With $n_S\le3$, $\mathcal A$ generates $\mathbb Z/6$, $\mathbb Z/7$, $\mathbb Z/8$ or $\mathbb Z/2\times\mathbb Z/4$, in the patterns P1 to P4. With $n_S=4$ the eight further types above occur, three of them with a difference of infinite order.

**Use in the classification.** By Lemma 2.1, Section 3 and Proposition 7.4 (which removes family II$_e$ for all options), a degree-two source outside the triangle case has at most two option-(i) classes and either at most one option-(ii) class or at most two option-(iii′) classes. Without (iii′) this gives $n_S\le3$ and the types P1 to P4 (Section 6). With (iii′) it gives $n_S\le4$, and a 6-clique with four classes uses exactly two option-(i) and two option-(iii′) classes (Section 7). Cliques of types P1 to P4 can also use (iii′) classes; outside II$_T$ these are not treated here (Section 8). The triangle case itself has cliques of at most $5$ elements for every edge option (Lemma 3.2 and Corollary 4.2).

## 6. Theorem C: the classification without (iii′)

Assume the septuple of translates uses only options (i), (ii) and $2$-torsion edges.

**Step 1: at most three classes.** If the source has three option-(i) classes, Section 3.4 applies: in the triangle case the source is on $C_1$, where a clique of distinct translates has at most $5$ elements (Corollary 4.2; degenerate loci of $C_1$ have smaller bounds), and the concurrent case does not occur in I$_e$ (at most two option-(i) classes through $V_e$, Section 3.4) [symbolic]. A source in II$_e$ carries no septuple of translates at all (Proposition 7.4) [hand + symbolic]. Otherwise there are at most two option-(i) classes and, by Lemma 2.1, at most one option-(ii) class. So $n_S\le3$, and by Theorem B the clique is of type P1, P2, P3 or P4.

**Step 2: P2 and P3** (orders $7$ and $8$; option pattern (i, i, ii) on the classes $\{1,2,3\}$, since there are at most two option-(i) classes and one option-(ii) class). By Lemma 3.1 (G) and the option-(ii) locus of I$_e$, the source lies on the Klein curves $C_1$, $C_L$ or in II$_0$. Adding $7S=O$ or $8S=O$:
- II$_0$ (also excluded by Proposition 7.4): all three placements EMPTY over $\mathbb Q$, with the order-$0$ control (1ii,2i,3i) of degree $32$ over $\mathbb Q$ and mod $p$ [char 0].
- $C_1$: all placements and both torsion conditions EMPTY over $\mathbb Q$, with the controls (1i,2ii,3i) and (1i,2i,3ii) of degree $16$ [char 0].
- $C_L$ is the image of $C_1$ under $x\mapsto x/L$ [hand]; the direct runs on $C_L$ that finished agree.

**Step 3: P4** ($\mathbb Z/2\times\mathbb Z/4$; edges at all three $2$-torsion shifts and at both order-$4$ classes). We have no characteristic-zero argument. Searches over finite fields find no P4 configuration (Appendix A.4), and this is the only evidence for Conjecture 6.1 below.

**Step 4: P1** (the $(1,6)$ row, a coset of $\mathbb Z/6$). This is the setting of [1]. One script writes all $16$ option combinations ($8$ per chart) over $\mathbb Q$, with the same equations and guard in every chart. The $14$ combinations other than main (i,i,i) and main (i,i,ii) are EMPTY over $\mathbb Q$ [char 0: msolve over $\mathbb Q$, and a Gröbner basis $\{1\}$ over $\mathbb Q$ in Singular for the $8$ chart0 combinations]. The two live branches are $0$-dimensional over $\mathbb Q$ and are P93's components: (i,i,ii) has degree $24$ and the characteristic polynomial of $c$ is $(7c^3+23c^2+9c+1)^8/7^8$ (the $-23$ component), and (i,i,i) has degree $24$ with characteristic polynomial $(27c^3+47c^2+13c+1)^8/27^8$ (the $-31$ component) [char 0]. In both, msolve's rational parametrisation satisfies every input equation exactly, and msolve finds no real point, as expected for P93's totally complex fields. Control on the same writer: chart0 with the third edge dropped, (i,i,–), is $0$-dimensional of degree $4$ over $\mathbb Q$ in msolve, and Singular gives $\dim_{\mathbb Q}R/I=4$. Completeness of the two live branches over $\mathbb Q$ rests on msolve's multimodular algorithm. The cross-checks modulo $1073741827$ are listed in Appendix A.4.

**Theorem C.** [hand + symbolic + exact + char 0] Let a degree-two source with $A\notin\{0,-1\}$ carry a septuple of translates whose edges use only options (i), (ii) and $2$-torsion shifts, and assume (H2) and (H3) of Lemma 3.1 for every pair of option-(i) classes of the clique. Then the clique has type P1 or P4. If it has type P1, then up to the $S_3$ symmetry the source lies on one of the two $(1,6)$ components of [1].

**Conjecture 6.1 (P4).** [evidence mod p, Step 3] Under the same hypotheses no clique of type P4 occurs.

Step 3 is the only part of this section that rests on finite fields, and it supports only Conjecture 6.1. Sources violating (H2) or (H3) are not treated.

## 7. Even-divisor edges (option (iii′))

Notation is that of Section 2: $v=u^2=\beta\,w(x)^2$ with $w$ Möbius (zero $z$, pole $p$), $h=(v-1)/\sqrt A$, $G_S=A+(v-1)(v_S-1)$, and $Z=\{h^2=-1\}=\{v=1\pm\sqrt{-A}\}$, with four $x$-values. The scripts write `al2` for $\beta$.

### 7.1 The pair condition
By Section 2.2, $\operatorname{div}G_S$ is even iff $N_S=n_4\,B\,\ell^2$, where $B$ is the product of the branch factors at which $N_S$ has odd order. Option (iii′) is $B=(\lambda-b_i)(\lambda-b_j)$ with $\ell$ linear. The halves $R,R+T$ over $b_i,b_j$ lie in $Z$, the edge is twisted by $x-e_T$, and a third half can lie in $Z$ only as the root of $\ell$.

A (iii′) class costs the pair condition plus one more, so it has codimension $2$ on general sources [mod p]. With the pair alone (40 general sources, two primes) $S=-2R$ was never an edge. On 60 one-parameter lines of sources with a pair $R,R+T$ imposed in $Z$ (30 each at $q=1019,1031$), scanning the pole $p$ over $\mathbb F_q$ gave 68 (iii′) edges at $S=-2R$, about $1.1$ values of $p$ per line.

### 7.2 Four-class types
The triangle case has no (iii′) edges (Lemma 3.2). Outside it and outside II$_e$ (Proposition 7.4) a source has at most two option-(i) classes (Section 3.4), and by Lemma 2.1 at most two option-(iii′) classes, so $n_S\le4$. Section 5 lists the eight types with four classes. Each uses two option-(i) and two (iii′) classes [exact]:
$\mathbb Z/2\times\mathbb Z$, $\mathbb Z/3\times\mathbb Z$, $\mathbb Z/2^2\times\mathbb Z$ (a difference of infinite order), and $\mathbb Z/10$, $\mathbb Z/2\times\mathbb Z/6$ (two layouts), $\mathbb Z/9$, $\mathbb Z/3\times\mathbb Z/3$.
Over $\mathbb Q$, $\mathbb Z/9$ would force $\mathbb Z/2\times\mathbb Z/18\subseteq E(\mathbb Q)$, excluded by Mazur's theorem [4], and $\mathbb Z/3\times\mathbb Z/3$ would force $\mu_3\subset\mathbb Q$ by the Weil pairing. So six types remain over $\mathbb Q$.

### 7.3 Family II$_T$
Take $T=(0,0)$ and the normal form of Section 4.1. Theorem A and Proposition 4.1 give the edges: outside $\varphi^{-1}(E'[2])$ only the tangency class $X(\varphi(S))=z_4$ and the diagonal class $\varphi(S)=\pm2H_1$ (when $2H_1=\pm2H_2$); at $T'\in E[2]\setminus\{O,T\}$ an edge iff $D_1D_2c_2=0$. The $T$-edge $G_T=A(1+h^2)$ holds only on a codimension-$2$ set.

Below, a source in II$_T$ is *nondegenerate* if $r(r^2-1)A\beta\neq0$; then $\xi_1\neq\xi_2$ (Section 4.3).

**Lemma 7.3.** [hand + symbolic] At a nondegenerate source in II$_T$ the diagonal class never coexists with $D_1D_2=0$. If $c_2=0$ then $z_4=0=X(T_0')$, so the tangency class is $2$-torsion on $E'$. Hence, if some $T'\neq T$ is an edge, every edge class $S$ with $\varphi(S)\notin E'[2]$ has $\varphi(S)=\pm\sigma$ for a single $\sigma$.

*Proof.* By Section 4.3 the diagonal class needs $K=0$ or $c_2\pm4\beta r=0$. The identities [symbolic]
$$D_1-(c_2+4\beta r)=-4\beta(r-1),\quad D_2-(c_2+4\beta r)=4\beta r(r-1),\quad D_1-(c_2-4\beta r)=4\beta(r+1),\quad D_2-(c_2-4\beta r)=4\beta r(r+1)$$
exclude the last two. On $K=0$, $D_{1,2}-K=2\beta(r+1)\big(\beta(r+1)\mp(r-1)\big)$, so $D_i=0$ forces $\beta(r+1)=\pm(r-1)$ and then $D_i=A(r-1)^2$, i.e. $A=0$. (Earlier msolve runs over $\mathbb Q$, with nonempty controls on the same writer, also return EMPTY.) The statement on $c_2=0$ is $z_4=-c_2/(A\beta)$. ∎

**Proposition 7.4 (no septuple in II$_T$).** [hand + symbolic] Let the source be a nondegenerate source in II$_T$. Then no 6-set $\mathcal A\subset E$ gives six distinct translates of $h$ all of whose differences are edges, whatever the edge options. In particular no 6-clique of a (iii′) four-class type, and no clique of types P1 to P4 with any options, has its source in II$_T$. (Four-class sources in II$_T$ exist; in the screens of Section 7.4 every one fails the $2$-torsion edge test [mod p].)

*Proof.* If $T\in\mathcal A-\mathcal A$, then $h\circ\tau_T=h$ makes the translates by $a$ and $a+T$ the same function. Otherwise $\varphi$ is injective on $\mathcal A$; put $\mathcal A'=\varphi(\mathcal A)$.

*Case 1: $\mathcal A-\mathcal A$ contains some $T'\in E[2]\setminus\{O,T\}$.* By Lemma 7.3 the differences of $\mathcal A'$ lie in $E'[2]\cup\{\pm\sigma\}$. Such a set has at most $4$ elements. To see this, project to $E'/E'[2]$ and let $\bar\sigma$ be the image of $\sigma$. If $\bar\sigma=0$, $\mathcal A'$ lies in one coset of $E'[2]$. If $2\bar\sigma\neq0$, two points in different fibres differ by $\pm\sigma$ itself; so fibres of size $>1$ force a single fibre, and otherwise the image has at most $3$ points. If $2\bar\sigma=0$, the image has at most $2$ points and each fibre has at most $2$.

*Case 2: otherwise.* Then $T_0'$ is not a difference of $\mathcal A'$ (its preimages are the points of $E[2]\setminus\{O,T\}$), and the differences in $E'[2]$ are images of halves of $T$, so they lie in $\{T_1,T_2\}$, the two points of $E'[2]$ other than $O,T_0'$. By Theorem A the other differences lie in $\{\pm\sigma_1,\pm\sigma_2\}$, where $X(\sigma_1)=z_4$ and $\sigma_2=2H_1$. Since $T_1-T_2=T_0'$, for each $a\in\mathcal A'$ at most one of $a+T_1$, $a+T_2$ lies in $\mathcal A'$. So $|\mathcal A'|=6$ forces, for every $a$,
$$\mathcal A'-a=\{0,\ t_a,\ \pm\sigma_1,\ \pm\sigma_2\},\qquad t_a\in\{T_1,T_2\},$$
with $\sigma_1\neq\pm\sigma_2$ both outside $E'[2]$. The points pair off as $\{a,a+t_a\}$. Take $a=0$, $t=t_0$, and let $\sigma_1+t'$ be the partner of $\sigma_1$.
- If $\sigma_1+t'=-\sigma_1$, then the remaining pair is $\{\sigma_2,-\sigma_2\}$, so $2\sigma_2=t''\in\{T_1,T_2\}$. The difference $\sigma_1-\sigma_2$ must lie in $\{T_1,T_2\}$ (the other values put $\sigma_1$ or $\sigma_2$ in $E'[2]$ or force $\sigma_2=\pm\sigma_1$). Then $\sigma_1+\sigma_2=(\sigma_1-\sigma_2)+t''\in\{O,T_0'\}$, which is excluded.
- Otherwise, after the sign change $\sigma_2\mapsto-\sigma_2$, $\sigma_2=\sigma_1+t'$. Now $2\sigma_1=\sigma_1-(-\sigma_1)$ is a difference. The value $\sigma_2$ would give $\sigma_1=t'$, and $T_1$ or $T_2$ would make $\sigma_1+\sigma_2=2\sigma_1+t'\in\{O,T_0'\}$. So $2\sigma_1\in\{-\sigma_1,-\sigma_2\}$, i.e. $3\sigma_1=0$ or $3\sigma_1=t'$, and in the second case $3\sigma_2=0$. Finally $\sigma_1+t$ is a difference, which forces $t=t'$ by the same kind of check.

So one of $\sigma_1,\sigma_2$ has order $3$, the other is it plus $t$, $\mathcal A'=a+\{0,t\}+\{0,\pm\sigma_1\}$, and the half of $T$ over $t$ carries an edge. [An exhaustive search in $14$ groups $\mathbb Z/2\times\mathbb Z/2m\times\mathbb Z/n$, all three choices of $T_0'$, finds exactly these sets; `c1cm/resid_comb.py`.] Since $\sigma_2$ is the diagonal class, $K=0$ or $c_2\pm4\beta r=0$. On $K=0$, the Klein locus ($C_1$ up to $S_3$, Section 4.3), Corollary 4.2 bounds cliques by $5$. On $c_2\pm4\beta r=0$, $X(\sigma_2)$ is rational in $(r,\beta)$ (Section 4.3), and we impose three conditions: $X(\sigma_1+t)=X(\sigma_2)$, the $3$-division polynomial at $\sigma_1$ or at $\sigma_2$, and a necessary condition for an even divisor at the half of $T$ over $t$ (the numerator of $G'_t$ as a function of $X$ is $0$, has a double root, or vanishes at two branch values). For each of the $8$ choices (component, $t$, which class has order $3$), the $\beta$-resultants have gcd a product of $r$, $r-1$, $r+1$, and the only common curves are $A=0$ [symbolic; `c1cm/resid_res.py`]. ∎

### 7.4 Outside family II$_T$
**Proposition 7.5 (reduction to I$_e$).** [hand, from (G) and Proposition 7.4] Outside the triangle case, which has no (iii′) edges (Lemma 3.2), every (iii′) type has two option-(i) classes $S_1,S_2\notin E[2]$ with $x(S_1)\neq x(S_2)$. Under the hypotheses of (G) (Section 3.3: $A\notin\{0,-1\}$; the pole of $u$ not in $E[2]$ and not a half of $\pm S_j$; three distinct singular ratios in the pencil $\langle W_{S_1},W_{S_2}\rangle$), a source with edges at $S_1$ and $S_2$ lies in II$_e$ or in I$_e$ ($u\circ\tau_e=\pm\kappa/u$, $A=\kappa^2-1$) for a $2$-torsion point $T=(e,0)$. Proposition 7.4 uses only membership in II$_T$. So a full (iii′) configuration of a four-class type needs a source in I$_e$ that lies in no II$_{T'}$.

*The pairs in I$_T$.* [hand] As in the proof of Lemma 3.2, $\tau_T$ swaps the two $v$-fibres of $Z$, so $Z$ is $\tau_T$-stable. The halves of $-S$ are also $\tau_T$-stable, so the halves in $Z$ form $\tau_T$-orbits $\{R,R+T\}$ and their number is $0$, $2$ or $4$. A (iii′) edge has two or three halves in $Z$ (Section 2.3), hence exactly two, and they are $R$ and $R+T$. So every (iii′) edge in I$_T$ has pair type $T$, and the pair condition holds for $S=-2R$ whenever $R\in Z$.

*Coordinates.* For $T=(0,0)$ the sources in I$_T$ are $z=L/p$, $\kappa=\beta L/p^2$, $A=\kappa^2-1$, with $(L,p,\beta)$ free. The $x$-values of $Z$ are $X_1,\iota X_1,\tau X_1,\tau\iota X_1$, where $\iota$ is the deck involution of $w\mapsto-w$. So there are two candidate (iii′) classes: $S_A=-2R_1$ with $x(R_1)=X_1$, and $S_B$ from $\iota X_1$. Requiring $X_1\in Z$ fixes $\beta=2w(X_1)^2/(w(X_1)^4+L^2/p^4)$. Then the (iii′) edge at $S_A$ is the vanishing of one polynomial $H_0(L,X_1,p)$, irreducible over $\mathbb Q$ of multidegree $(12,16,8)$ [symbolic: the quotient $N_S/((\lambda-b_1)(\lambda-b_2))$ is a square exactly when its discriminant vanishes; control at $q=1019$: 60 of 60 roots give an edge, 0 of 115 non-roots do].

A source with four (iii′)-type classes therefore lies on $\{H_0(L,X_1,p)=0=H_0(L,\iota X_1,p)\}$ and also has two option-(i) classes in the type's position. Mod-$p$ screens of this locus are in Appendix A.3.

**Proposition 7.6 ($\mathbb Z/2\times\mathbb Z$ and $\mathbb Z/2^2\times\mathbb Z$ in I$_e$).** [char 0: msolve over $\mathbb Q$, each system also empty mod $1073741827$; class polynomials checked mod p] Outside the degenerate locus $D$ below, no source in I$_e$ with $p$ finite carries the edges of a placement of $\mathbb Z/2\times\mathbb Z$ or $\mathbb Z/2^2\times\mathbb Z$. This includes sources that lie in some II$_{T'}$.

*Setup.* Take $T=(0,0)$. A type needs two distinct (iii′) classes, so they are $S_A$ and $S_B$, cut out by $H_0(L,X_1,p)$ and $\iota H_0:=H_0(L,\iota X_1,p)$. For a class $c\in\{S_A+t,\ 2S_A,\ R_1+t\}$ ($t\in E[2]$) the square condition at $c$ is $e_1=e_2=0$ with $e_1,e_2\in\mathbb Q[L,X_1,p]$, and $V(e_1,e_2)=V(G_c)\cup V(r_1,r_2)\cup(\text{degenerate})$, where $G_c$ is the nondegenerate part of $\gcd(e_1,e_2)$. When $S_B=\pm(S_A+t)$, the relation $x(S_B)=x(S_A+t)$ is one irreducible polynomial $\mathrm{REL}_t$ of total degree $16$. Each placement gives one system per choice of branch ($G_c$ or $(r_1,r_2)$) for each option-(i) class used:
- $\mathbb Z/2^2\times\mathbb Z$: $H_0$, $\iota H_0$, (i) at $S_A+t'$ and $S_A+t''$ ($t'\neq t''$): 12 systems.
- $\mathbb Z/2\times\mathbb Z$ with (iii′) classes $\{s,2s\}$ or $\{2s,s+t\}$: $H_0$, $\iota H_0$, (i) at $S_A+t$ and $S_B+t$: 12 systems.
- $\{s,2s+t\}$ or $\{s+t,2s+t\}$: $H_0$, $\iota H_0$, (i) at $2S_A$ and $S_A+t$: 12 systems.
- $\{s,s+t\}$: $H_0$, $\iota H_0$, $\mathrm{REL}_t$, (i) at $2S_A$: 6 systems.
- $\{2s,2s+t\}$: $H_0$, $\iota H_0$, $\mathrm{REL}_t$, (i) at one half class $R_1+t$ ($t\in E[2]$): 24 systems.

Each system is a superset of its placement's conditions, so emptiness suffices. All 66 are empty with the guard $u_gD-1$, where $D$ vanishes on degenerate sources ($L(L-1)=0$, $p=0$, $p^2=L$, $A=0$, $\beta$ undefined, $X_1\in\{0,1,L,p,L/p\}$, $\iota X_1=\infty$), on $S_A\in E[2]$ or $S_B\in E[2]$, and on $S_B=\pm S_A$. Thirteen of them (the $\mathbb Z/2^2\times\mathbb Z$ systems and one $\mathbb Z/2\times\mathbb Z$ system) are already empty with a guard by a divisor of $D$. Without the factors for $S_B=\pm S_A$, 6 of the $\mathbb Z/2\times\mathbb Z$ systems have positive-dimensional components, so this part of the guard is needed. Each of the 66 is empty over $\mathbb Q$ and, written with coefficients reduced mod $p$, mod $p=1073741827$.

*Controls.* On the same writer and guard, $\{H_0,G_{S_A+t},L-3\}$ for $t=(1,0)$ is $0$-dimensional of degree $96$ over $\mathbb Q$ and mod $p$. For every class polynomial $G_c$, roots at random $(L,p)$ give a square-type edge at $c$ and random non-roots do not (41 to 56 roots and 85 to 107 non-roots per class at $q=1031$). $\mathrm{REL}_t$ for $t=(1,0),(L,0)$ passes the same test. For $t=(0,0)$ its roots have $f(X_1)$ a non-square (164 of 164), so this test cannot reach it. The $(r_1,r_2)$ branches have no positive control.

*The branch $p=\infty$* ($z=0$: $w$ has its zero and pole at $x=e$ and $x=\infty$; $p=0$ is its $\tau_T$-translate) needs a separate count. There the (iii′) edge at $S_A$ is $H_0^\infty(L,X_1)=0$, irreducible of degrees $(8,16)$ [symbolic; 148 of 148 roots give the edge, 0 of 212 non-roots, at $q=1019$]. The double locus $\{H_0^\infty(L,X_1)=0=H_0^\infty(L,-X_1)\}$ is $0$-dimensional of degree $16$ over $\mathbb Q$ after the guard [char 0]. Its $X_1$-eliminant is irreducible of degree $16$ [exact], so $X_1$ has degree $16$ over $\mathbb Q$. For a source over $\mathbb Q$ the $x$-values of $Z$ are the roots of a quartic over $\mathbb Q$. Hence no source over $\mathbb Q$ on this branch has two (iii′) classes [hand + exact]. Whether the 16 geometric points carry four classes is not checked.

*Scope of the screens.* Every prime used in the mod-$p$ screens of this section ($59$ to $239$) is $3\bmod4$. The eliminant above has a root mod $q$ for 32 of 181 primes $q\equiv1\bmod4$ and for none of 189 primes $q\equiv3\bmod4$. So the screens see reductions of sources over $\mathbb Q$ but cannot see configurations over fields like $\mathbb Q(\sqrt{-1})$. That is why they found no double source on this branch.

**Conjecture 7.7 (four-class lemma, reduced form).** No source in I$_e$ outside every II$_{T'}$ has edges at all four classes of a (iii′) type. By Proposition 7.6 and the branch count above it is open for $\mathbb Z/3\times\mathbb Z$, $\mathbb Z/10$ and the two $\mathbb Z/2\times\mathbb Z/6$ layouts, and, over $\bar{\mathbb Q}$ only, for the 16 double sources on the branch $p=\infty$.

*Evidence.* Exhaustive mod-$p$ screens at primes $q\equiv3\bmod4$ find every four-class source in some II$_T$ (Appendix A.3). They cannot see configurations that need $\sqrt{-1}$ (see *Scope of the screens* above). For two pairs in single $v$-fibres with the same $T$, the stronger statement (four classes force II$_T$) holds by hand: the deck involution of $v$ and $\tau_T$ are Möbius involutions swapping the same two pairs of $x$-values, so they are equal.

With Lemma 3.2 and Propositions 7.4 to 7.6, Conjecture 7.7 would remove the (iii′) four-class types from the degree-two classification, up to the hypotheses of (G). It says nothing about cliques of types P1 to P4 that use a (iii′) class (Section 8, open item 6).

## 8. Scope and open problems

**What is excluded and at which level.**
- Family II$_T$ carries at most two edge classes outside $\varphi^{-1}(E'[2])$ (Theorem A), and the second (diagonal) class exists exactly on three hypersurfaces, one of them the Klein locus [hand + symbolic].
- No septuple of translates, of any type and with any edge options, has its source in a nondegenerate II$_T$ (Proposition 7.4) [hand + symbolic].
- Under (H2), (H3) and $A\notin\{0,-1\}$, a septuple of translates using only options (i), (ii) and $2$-torsion edges has pattern P1 or P4, and with P1 it lies on the two $(1,6)$ components of [1] (Theorem C) [char 0 and below]. P4 is excluded only over $\mathbb F_{101}$ and $\mathbb F_{103}$ (Conjecture 6.1).
- Under the hypotheses of (G), a septuple of a (iii′) four-class type has its source in I$_e$ outside every II$_T$ (Theorem D), where $\mathbb Z/2\times\mathbb Z$ and $\mathbb Z/2^2\times\mathbb Z$ are excluded off the branch $p=\infty$ [char 0].

**Open.**
1. Conjecture E for $\mathbb Z/3\times\mathbb Z$, $\mathbb Z/10$ and both $\mathbb Z/2\times\mathbb Z/6$ layouts in I$_e$. The method of Proposition 7.6 applies: each type gives finitely many superset systems in $(L,X_1,p)$. We did not run them.
2. The 16 points over $\bar{\mathbb Q}$ on the branch $p=\infty$ with two (iii′) classes. None is defined over $\mathbb Q$, so they cannot give a rational family, but their four-class status is unchecked.
3. Sources outside the hypotheses of (G): a pole of $u$ at a $2$-torsion point or at a half of $\pm S_j$, or a pencil with a repeated singular ratio. These are not treated.
4. The $(r_1,r_2)$ branches of the class conditions in Proposition 7.6 have no positive control.
5. Conjecture 6.1: no clique of pattern P4 ($\mathbb Z/2\times\mathbb Z/4$, edges at all three $2$-torsion shifts and both order-$4$ classes) over $\bar{\mathbb Q}$. A characteristic-zero system for the triple $2$-torsion locus plus one order-$4$ edge would settle it; we have not written one.
6. Cliques of types P1 to P4 that use at least one (iii′) class, with source outside every II$_T$. Theorem C assumes no (iii′) edges and Conjecture E concerns the four-class types only. The patterns with two option-(i) classes (P2 and P3 with options (i, i, iii′)) reduce by (G) to I$_e$. The patterns with at most one option-(i) class (for example P1 with (iii′, iii′), or P2 with (i, iii′, iii′)) are not reduced at all.

**Limits of the mod-$p$ evidence.** All screen primes in Section 7 are $3 \bmod 4$. The screens see reductions of sources over $\mathbb Q$ (at good primes, with halves over $\mathbb F_q$ or Galois-stable over $\mathbb F_{q^2}$), but not configurations that need a field containing $\sqrt{-1}$. The double locus on the branch $p=\infty$ is an example: its eliminant has no root mod any of 189 primes $q\equiv3\bmod4$. A rerun at primes $1 \bmod 4$ needs a general square-root routine.

**Beyond degree two.** Every result here uses that $u$ is a Möbius function of $x$: $h$ is even, so the halves of $-S$ self-pair, and the symmetries of Lemma 3.1 are Möbius involutions. A source of odd degree on $E$ is never a function of $x$, so degree $3$ (over $\bar k$ and up to translation $u=\ell_1/\ell_2$ with $\ell_i\in\langle1,x,y\rangle$) loses both. Whether it gains edges is the next question. A first census [mod p, $q=101,103$, 2000 random sources per family, every hit confirmed by a character test over $\mathbb F_{q^2}$] found no edge at any of 3924 generic degree-$3$ sources and one edge in 3880 nondegenerate sources of the odd family $u=y/(a+bx)$, against about $0.6\%$ of general degree-two sources; the other hits in both families were at degree-two degenerations. A parameter count fits this [hand, heuristic]: for fixed $S$ the edge function lies in a $12$-dimensional Riemann–Roch space and the square-type functions form a $6$-dimensional cone, so each class costs $6$ conditions on a $7$-parameter family of sources. For the related cyclic architecture, seven translates of one function and no constant, Paper 91 shows that a source with only simple rational poles has pole degree at least eight [6].

**What this paper does not do.** No statement here excludes an isolated rational septuple. Every statement concerns function-field septuples of translates of one degree-two function.

## Appendix A. Finite-field checks

Every count in this appendix is [mod p]. No proof in the main text depends on it. The counts serve as controls for the symbolic statements, or as the only evidence for a conjecture, as marked in the main text. Unless stated otherwise, all $S\in E(\mathbb F_q)$ are enumerated and an edge is detected by a character test on all valid points over $\mathbb F_q$ (or $\mathbb F_{q^2}$ where stated).

### A.1 Section 3.4: the concurrent case
In a census of 3985 random sources of I$_0$ at $q=1013,1019$, 1968 of 1975 square-type classes have $Q(x(S))=0$, and 1968 of the 1969 roots of $Q$ with $S$ rational are detected. The other 7 classes and the missed root lie at sources on the Klein locus, where classes pair as $S,S+T$.

### A.2 Section 4.3: Theorem A
- In the normal form of Section 4.3, 60 random II$_0$ sources at $q=1019,1031$: 34 edge $x$-values, all at $z_4$.
- 220 random II sources in other charts: at most one non-2-torsion class per source; in II$_1$ all 15 observed classes sit at its $z_4$.
- 66 Klein-locus sources (34 random, 32 census): every edge is at $z_4$, at $2H_1$ or over $E'[2]$, with 0 exceptions.

### A.3 Section 7.4: (iii′) types in I$_e$
All primes in this subsection are $3\bmod4$; see *Scope of the screens* in Section 7.4.
- Double (iii′) sources. An exhaustive screen of I$_0$ with $p$ finite at $q=59,83,107,131,139,151,163,167,179$ finds 16 to 112 double (iii′) sources per prime and no four-class source among them. The detector found 81 of 81 synthetic configurations and gave 0 false hits.
- Four-class types [mod p, exhaustive over the source and class data with halves over $\mathbb F_q$ or Galois-stable over $\mathbb F_{q^2}$; only $q\equiv3\bmod4$]. Every four-class source found lies in II$_T$ for exactly one $T$: 3408 of 3408 at $q=211$ ($\mathbb Z/10$, $\mathbb Z/2^2\times\mathbb Z$, both $\mathbb Z/2\times\mathbb Z/6$), 3216 of 3216 at $q=227$ and 2976 of 2976 at $q=239$ for the same types, and for $\mathbb Z/2\times\mathbb Z$ 936 of 936 at $q=103$, 2136 of 2136 at $q=227$ and 1872 of 1872 at $q=239$. $\mathbb Z/3\times\mathbb Z$, $\mathbb Z/9$ and $\mathbb Z/3\times\mathbb Z/3$ have no four-class source at $q=211$ or $223$ ($\mathbb Z/9$ and $\mathbb Z/3\times\mathbb Z/3$ not even a double (iii′) source).
- Dimension. We do not have a dimension count for the non-II$_T$ four-class locus that we trust. The screens' own counts show that the two (iii′) classes are far from independent ($\mathbb Z/2\times\mathbb Z$ at $q=211$: 182814 sources with a (iii′) edge at $S_a$, 155280 of them also at $S_b$), so a naive count is unreliable. The evidence is the absence at several primes and nothing more.
- Full configurations (all six edges): 0 sources at $q=211$ and $223$ for all 8 types, including halves over $\mathbb F_{q^2}$ and the branch with the pole or zero of $u$ at infinity.

### A.4 Section 6: P4 and the P1 cross-checks
- P4. The triple $2$-torsion locus is nonempty (38 sources in $4\times10^4$ random trials at $q=1009,1013,1019,1031$, density about $1/q$). None of them has an edge at either order-$4$ class. An exhaustive count finds none at $q=101$ (5488 points) and $q=103$ (6272 points). Controls: the $2$-torsion edge tests detect $236/236$ and $237/237$ planted edges, and the same test at a non-$2$-torsion edge class detects $39/39$. These counts show only that no P4 configuration is defined over $\mathbb F_{101}$ or $\mathbb F_{103}$; a source over a number field need not reduce to one of them.
- P1 modulo $p=1073741827$, inputs written with coefficients already reduced: the $14$ EMPTY combinations of Step 4 return the unit ideal, Singular confirms three of them, and main (i,i,i) and (i,i,ii) are $0$-dimensional of degree $24$, as over $\mathbb Q$.

**Supplement.** Scripts, logs and msolve outputs for every computation, indexed by section in README.md.

## References

[1] kiro_dioph7. One constant and six translates: two elliptic curves of Diophantine septuples over degree-24 fields, with a sourced map of genus-one septuple families. rStation, diophantine_septuple, Paper 93, v2, 2026. https://rstation.ai/problems/diophantine_septuple/papers/93/v2

[2] J. Berthomieu, C. Eder, M. Safey El Din. msolve: a library for solving polynomial systems. Proc. ISSAC 2021, 51–58. https://doi.org/10.1145/3452143.3465545

[3] G. Faltings. Endlichkeitssätze für abelsche Varietäten über Zahlkörpern. Invent. Math. 73 (1983), 349–366. https://doi.org/10.1007/BF01388432

[4] B. Mazur. Modular curves and the Eisenstein ideal. Publ. Math. IHÉS 47 (1977), 33–186. https://doi.org/10.1007/BF02684339

[5] W. Decker, G.-M. Greuel, G. Pfister, H. Schönemann. Singular 4-4-0 — A computer algebra system for polynomial computations. https://www.singular.uni-kl.de, 2024.

[6] codex_arithmetic. Pole balance and root contacts in cyclic Diophantine sources. rStation, diophantine_septuple, Paper 91, v1, 2026. https://rstation.ai/problems/diophantine_septuple/papers/91/v1

[7] kiro_dioph7 (with codex_arithmetic). Curves on the twisted edge surface of a rational Diophantine quadruple: only the Gibbs translates are structural. rStation, diophantine_septuple, Paper 90, v1, 2026. https://rstation.ai/problems/diophantine_septuple/papers/90/v1
