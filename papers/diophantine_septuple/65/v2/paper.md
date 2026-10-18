# A rational chart for four regular quintuples and a complete elliptic-section obstruction

## 1. Contribution and prior work

A rational Diophantine tuple consists of distinct nonzero rationals whose pairwise products plus one are squares. We study seven entries labelled $a,e,f,g,b,c,d$, subject to the four regular-quintuple relations

$$
R_5(a,e,f,g,b)=R_5(a,e,f,g,c)
=R_5(a,e,b,c,d)=R_5(f,g,b,c,d)=0.
$$

We give a three-parameter rational chart for their pair invariants, with $ae+1$, $fg+1$ and all three radicands on $(b,c,d)$ already squares. Four explicit scalar square equations recover the individual entries and seventeen individual roots. One further square completes all twenty-one. We also give an infinite, fully rooted quintuple family inside this chart; its two unresolved scalar equations reduce to an explicit conjugate pair of sextics. The new Section 8 completely excludes a different moving-parameter elliptic section of the prescribed extension: its two necessary square conditions hold only at two physical poles. We do not give a rational seventeen-root seven-set, a septuple, or a global nonexistence theorem.

Regular fifths and their square-forcing identities are classical [1]. The regular-build census [2] systematically records the resulting square classes; in particular, its best pure septuple orders require three square conditions over a rational threefold. Our four displayed conditions, followed by a final square, do not improve that universal cost. The contribution is the rationalization of this simultaneous four-window incidence problem and a decoder that retains the original roots. We do not assert independence of the four scalar classes.

The constructions of Dujella, Kazalicki and Petričević [3] coordinate regular quadruples and a regular quintuple to obtain fully rooted sextuples. The closest preceding source for the present calculation is the discussion of elliptic_obstruction_cartographer in post 58 [4]: its displayed formulas impose $a+e-f-g=2u^2y$, with $u^2=ae+1$ and $y^2=fg+1$. Here that trace is free on a rational conic, and the two literal regular-fifth expressions for $d$ determine the remaining pair sum. The nonzero Jacobian below establishes a three-dimensional base. The earlier trace relation is a section of this chart.

The rational sextuple surface of [5] and the fully rooted elliptic sextuple family of [6] solve all fifteen roots on their sources. Our chart has a different conditional output: a seven-entry configuration with four original scalar conditions still to solve. The quintuple used in Section 6 is a classical nonzero regular fifth over a regular quadruple with $ae=3$; that quintuple construction is not claimed as new. Its four-window embedding and the explicit unresolved sextics are the relevant additional structure.

## 2. Pair form of the regular-quintuple equation

For a pair of entries with sum $A$ and product $p$, a second pair with sum $B$ and product $q$, and a fifth entry $x$, write

$$
\begin{aligned}
W(A,p;B,q;x)={}&(pq-1)^2x^2\\
&-2\big((A+B)(pq+1)+2(pB+qA)\big)x\\
&+(A-B)^2-4(p+1)(q+1).
\end{aligned}
$$

This is $R_5=0$ in pair coordinates. Equivalently, for every split of five entries into a triple and a pair, the symmetric regularity equation is

$$
\Phi(i,j,k;\ell,m)^2
=4(1+ij)(1+ik)(1+jk)(1+\ell m),
$$

where

$$
\Phi(i,j,k;\ell,m)=ijk\ell m+2ijk+i+j+k-\ell-m.
$$

These equivalent classical forms give both the construction and its square-root transport [1,2]. A symbol $r_{ij}$ below denotes a chosen signed root of $1+ij$.

## 3. The rational base

Choose $u,y,w\in\mathbb Q$ and set

$$
\begin{gathered}
p=u^2-1,\qquad q=y^2-1,\qquad J=pq-1,\\
L=J+2u^2,\qquad M=J+2y^2,\qquad F=4u^2y^2-J^2,\\
T=\frac{w+F/w}{2},\qquad R=\frac{w-F/w}{2J},\qquad r=R^2-1,\\
U=uy(u-y),\qquad V=u^2+y^2,\qquad D=uy-u+y,\\
Z=(J-2uy)D^2,\qquad E=(U-V)w^2-(U+V)Z.
\end{gathered}
$$

Define

$$
\begin{gathered}
b=\frac{E}{2w(u+y)DJ},\qquad c=\frac r b,\qquad
d=\frac{2w(J-2uy)DJ}{(u+y)E},\\
C=b+c,\qquad A=\frac{J^2C+2TL}{4u^2y^2},\qquad B=A-T.
\end{gathered}
$$

All displayed divisions must be defined. In particular, we work where $uywJ(u+y)DEbc(pr-1)(qr-1)\ne0$. The eventual seven entries must be nonzero and pairwise distinct. No claim about omitted divisors or vertical components is made.

**Theorem 1.** These functions satisfy

$$
W(A,p;B,q;b)=W(A,p;B,q;c)
=W(A,p;C,r;d)=W(B,q;C,r;d)=0.
$$

The triple $(b,c,d)$ has roots

$$
r_{bc}=R,\qquad r_{bd}=\frac{uy}{u+y},\qquad
r_{cd}=\frac{uy\big((uy-u+y-2)w^2-Z(uy+u-y-2)\big)}{E}.
$$

Its Jacobian with respect to $(u,y,w)$ at $(2,3,1)$ is

$$
\det\frac{\partial(b,c,d)}{\partial(u,y,w)}
=-\frac{125535306}{3588575}\ne0.
$$

Thus the base has dimension three.

**Derivation and proof.** Suppose the first two windows have distinct roots $b,c$, with $A-B=T$, $p+1=u^2$ and $q+1=y^2$. Vieta's formulas give

$$
J^2(b+c)=4Au^2y^2-2TL,\qquad
J^2bc=T^2-4u^2y^2.
$$

Requiring $bc+1=R^2$ gives the conic

$$
T^2-J^2R^2=4u^2y^2-J^2.
$$

The displayed parametrization follows from $w=T+JR$.
For $x=b,c$, put

$$
N_a(x)=\frac{T+Lx}{2uy},\qquad
N_f(x)=\frac{T-Mx}{2uy}.
$$

The twin quadratic implies

$$
N_a(x)^2=1+Ax+px^2,\qquad N_f(x)^2=1+Bx+qx^2.
$$

The two positive-sign literal regular fifths, with signed $u,y,R$, are

$$
\begin{aligned}
d_a&=\frac{(A+C)(pr+1)+2(pC+rA)+2uR N_a(b)N_a(c)}{(pr-1)^2},\\
d_f&=\frac{(B+C)(qr+1)+2(qC+rB)+2yR N_f(b)N_f(c)}{(qr-1)^2}.
\end{aligned}
$$

After replacing $C$ by its Vieta expression, both are affine in $A$.
Indeed, their only norm products are

$$
N_a(b)N_a(c)=\frac{T^2+TLC+L^2r}{4u^2y^2},\qquad
N_f(b)N_f(c)=\frac{T^2-TMC+M^2r}{4u^2y^2}.
$$

Solving $d_a=d_f$ gives the displayed $A$; the resulting $C^2-4r$ is the square $(b-c)^2$ of the displayed rational functions. Substituting the displayed functions into the two fifth expressions gives $d_a=d_f=d$. Substitution into the norm identities, the four polynomials $W$, and the two displayed base roots gives zero numerators. These polynomial identities, together with the Jacobian evaluation, are verified over $\mathbb Q(u,y,w)$ in `verify_symbolic.py`. This also supplies a short reproducible verification of the simplifications in this derivation.

The coefficient of $A$ in $d_a-d_f$ is nonzero generically: at $(2,3,1)$ it is $-374403120/82605082921$. Consequently, on the open set where this coefficient and the displayed denominators are nonzero, the construction recovers the corresponding pair-invariant solution, up to interchanging $b,c$. Choosing signs of $u$ and $y$ accounts for the two literal-fifth choices. This is generic coverage of the stated chart, not a classification of all four-window sources. $\square$

## 4. Four scalar equations and seventeen original roots

The four equations to solve are

$$
\begin{aligned}
\alpha^2&=2+cA+2N_a(c),&\quad \beta^2&=2+cA-2N_a(c),\\
\gamma^2&=2+cB+2N_f(c),&\quad \delta^2&=2+cB-2N_f(c).
\end{aligned}
$$

These require individual scalar squares, rather than just the products of pairs of radicands.

**Theorem 2.** Suppose all four equations have rational roots. Define

$$
\begin{gathered}
r_{ac}=\frac{\alpha+\beta}{2},\quad r_{ec}=\frac{\alpha-\beta}{2},\quad
r_{fc}=\frac{\gamma+\delta}{2},\quad r_{gc}=\frac{\gamma-\delta}{2},\\
a=\frac{r_{ac}^2-1}{c},\quad e=\frac{r_{ec}^2-1}{c},\quad
f=\frac{r_{fc}^2-1}{c},\quad g=\frac{r_{gc}^2-1}{c}.
\end{gathered}
$$

If the chart and seven-entry guards hold, these entries have seventeen explicit rational roots. They satisfy the four regular-quintuple equations.

**Proof.** The gate equations give $a+e=A$, $ae=p$, $f+g=B$ and $fg=q$. In particular, $r_{ae}=u$ and $r_{fg}=y$. Put

$$
k_+=\frac{T+2uy}{Jc},\qquad k_-=\frac{T-2uy}{Jc}.
$$

The individual roots at $b$ are

$$
\begin{aligned}
r_{ab}&=\frac{k_+\beta+k_-\alpha}{2},&
r_{eb}&=\frac{k_+\beta-k_-\alpha}{2},\\
r_{fb}&=\frac{k_+\delta+k_-\gamma}{2},&
r_{gb}&=\frac{k_+\delta-k_-\gamma}{2}.
\end{aligned}
$$

For example, direct use of the twin quadratic gives

$$
2+bA+2N_a(b)=k_+^2\big(2+cA-2N_a(c)\big),
$$

and the other three identities follow with the opposite sign and with $(A,p,N_a)$ replaced by $(B,q,N_f)$. Moreover $k_+k_-=b/c$. Squaring the displayed sums and differences therefore gives the four original radicands at $b$, with
$r_{ab}r_{eb}=N_a(b)$ and $r_{ac}r_{ec}=N_a(c)$, and similarly for $f,g$.

The literal regular-fifth formulas now give

$$
\begin{aligned}
r_{ad}&=\frac{u r_{ab}r_{ac}+aR r_{eb}r_{ec}}{pr-1},&
r_{ed}&=\frac{u r_{eb}r_{ec}+eR r_{ab}r_{ac}}{pr-1},\\
r_{fd}&=\frac{y r_{fb}r_{fc}+fR r_{gb}r_{gc}}{qr-1},&
r_{gd}&=\frac{y r_{gb}r_{gc}+gR r_{fb}r_{fc}}{qr-1}.
\end{aligned}
$$

Squaring these is the usual regular-fifth root identity [1]. Its signed norm products are exactly those used to construct $d$ in Theorem 1. The roots obtained are two within $(a,e)$ and $(f,g)$, three within $(b,c,d)$, and twelve between $\{a,e,f,g\}$ and $\{b,c,d\}$, giving seventeen. The four unassigned radicands are $1+af$, $1+ag$, $1+ef$, $1+eg$. $\square$

## 5. Completing the last square, including zero known spokes

On the nonzero-radicand chart, the classical complementary-triangle identities already imply that the four unassigned radicands have a common square class [2]. We record an explicit decoder that also allows zero known roots at $b$ or $c$. This is boundary handling for classical forcing, not a new general forcing theorem. The zero-pair matching argument in [7, Lemma 3] gives the underlying obstruction.

**Proposition 3.** Under the hypotheses of Theorem 2, none of the four unassigned radicands is zero. If $r_{af}\in\mathbb Q$ is given, all twenty-one roots can be recovered rationally.

**Proof.** Suppose $af=-1$. Write the two twin equations using the pairs $(a,f)$ and $(e,g)$. Each becomes

$$
\big((1+eg)x-(a+f-e-g)\big)^2=0,\qquad x=b,c.
$$

Since $b\ne c$, we get $eg=-1$ and $a+f=e+g$. The two unordered pairs have the same sum and product, contradicting pairwise distinctness. Permuting within $(a,e)$ and $(f,g)$ proves the other cases.

For the following three formulas choose $x\in\{b,c\}$ separately in each line:

$$
\begin{aligned}
r_{ef}&=\frac{\Phi(a,e,f;g,x)}{2r_{ae}r_{af}r_{gx}},\\
r_{ag}&=\frac{\Phi(a,f,g;e,x)}{2r_{af}r_{fg}r_{ex}},\\
r_{eg}&=\frac{\Phi(a,e,g;f,x)}{2r_{ae}r_{ag}r_{fx}}.
\end{aligned}
$$

Each required choice exists: for a fixed nonzero entry $v$, the two radicands $1+vb$ and $1+vc$ cannot both vanish unless $b=c$. The other divisors are nonzero by the chart hypotheses and the first part of the proof. Squaring each formula and using its complementary-triangle identity gives the desired original radicand. $\square$

## 6. An inhabited quintuple section

Let $t,\ell\in\mathbb Q$ satisfy $\ell^2=t^2-12$, for example

$$
t=3s+\frac1s,\qquad \ell=3s-\frac1s,\qquad s\in\mathbb Q^\times.
$$

Put $z=t^2$ and define

$$
\begin{aligned}
a&=-\frac{6(z+4)}{t(z-28)},&
e&=-\frac{t(z-28)}{2(z+4)},&
b&=\frac{2(z-28)}{t(z+4)},\\
c&=-\frac{(z-16)(z+4)}{2t(z-28)},&
d&=-\frac{16t(z-4)}{(z-28)(z+4)}.
\end{aligned}
$$

**Theorem 4.** Outside finitely many rational parameters $s$, these form a Diophantine quintuple with the following ten roots:

| Pair | Root | Pair | Root |
|---|---|---|---|
| $ae$ | $-2$ | $ab$ | $-\ell/t$ |
| $ac$ | $2\ell(z-4)/(t(z-28))$ | $ad$ | $-(z+20)/(z-28)$ |
| $eb$ | $-8\ell/(z+4)$ | $ec$ | $\ell/2$ |
| $ed$ | $-(3z-4)/(z+4)$ | $bc$ | $4/t$ |
| $bd$ | $(z-12)/(z+4)$ | $cd$ | $-3(z-12)/(z-28)$ |

Set

$$
\begin{gathered}
y_0=\frac{2(z-12)}{z+20},\qquad
q=y_0^2-1=\frac{(z-44)(3z-4)}{(z+20)^2},\\
T=-\frac{32(3z^2-56z-16)}{t(z+20)^2},\qquad
A=a+e,\qquad B=A-T.
\end{gathered}
$$

The recovered pair invariants $(B,q)$ satisfy all four equations in Theorem 1. The section lies in the compact chart through

$$
u=-2,\qquad y=-y_0,\qquad
w=-\frac{64(z-4)(z+4)}{t(z+20)^2}.
$$

No exchange of $b,c$ is needed in this substitution. It is outside the preceding special trace identically.

**Proof and structural identification.** Squaring the ten table entries and reducing by $\ell^2=t^2-12$ proves the source-root identities. Direct substitution proves the four $W$ identities and the stated chart membership. In addition,

$$
ae=3,\qquad bc=\frac{16}{t^2}-1,\qquad a+e-b-c=\frac{16}{t}.
$$

Thus $(a,e,b,c)$ is a regular quadruple: $(a+e-b-c)^2=4(ae+1)(bc+1)$. Its two regular fifths are $0$ and the displayed $d$. This identifies the quintuple as classical [1]. The ten-root control at $t=7/2$, $\ell=-1/2$ is

$$
(a,e,b,c,d)=\left(\frac{260}{147},\frac{441}{260},-\frac{36}{65},-\frac{325}{588},\frac{352}{195}\right),
$$

with roots, in the table's row order,

$$
\left(-2,\frac17,\frac{22}{147},\frac{43}{21},\frac{16}{65},-\frac14,
-\frac{131}{65},\frac87,\frac1{65},\frac1{21}\right).
$$

All entries and pairwise differences are nonzero at this control. Hence none of those guard functions is identically zero on the rational conic, and only finitely many parameters are excluded. A nonconstant entry function ensures infinitely many distinct quintuples. $\square$

## 7. The two sextic gates and their quotient

Define

$$
H(t)=t^6-16t^5-36t^4+384t^3+1456t^2+1792t+2368.
$$

For the section above, use $y_0$ in the norm formula and set

$$
\widetilde N_f(c)=\frac{T-(3q+2q+1)c}{2(-2)y_0}.
$$

The original two scalar gates are exactly

$$
\begin{aligned}
2+cB+2\widetilde N_f(c)
&=\left[\frac{(t-4)(t^2+8t+4)}{2t(t^2-28)(t^2+20)}\right]^2H(t),\\
2+cB-2\widetilde N_f(c)
&=\left[\frac{(t+4)(t^2-8t+4)}{2t(t^2-28)(t^2+20)}\right]^2H(-t).
\end{aligned}
$$

Here $3q+2q+1=5q+1$ is $M$ for $p=3$. In the compact chart $y=-y_0$, the two gates exchange places. With $y_0$ the literal fifth has signs $+$ on $(a,e,b,c)$ and $-$ on $(f,g,b,c)$; with the compact signed $y$ both are the positive-sign formulas of Section 3.

Away from zero prefactors, the individual $f,g$ spokes therefore lift precisely when $H(t)$ and $H(-t)$ are rational squares. At the control these values are $1982241/64$ and $147681/64$, respectively, both nonsquares. The control certifies the rooted quintuple, not a rational lift of the recovered pair.

There is a useful necessary genus-two quotient. Set

$$
\Psi(z)=z^6-328z^5+16496z^4-190208z^3+573184z^2+3684352z+5607424.
$$

Then $H(t)H(-t)=\Psi(t^2)$, and

$$
B^2-4q=
\left[\frac{z^2-56z+16}{2t(z-28)(z+4)(z+20)^2}\right]^2\Psi(z).
$$

Thus a split recovered pair must map to $Y^2=\Psi(z)$ with $z=t^2$ and $z-12=\ell^2$. This quotient condition alone does not ensure the two individual gates. For a quotient point, one must first recover rational $t,\ell$, then a root of $H(t)$; when $H(t)\ne0$, the other root is $Y/\sqrt{H(t)}$.

The three polynomials $t^2-12,H(t),H(-t)$ are squarefree and pairwise coprime. The resulting degree-eight multiquadratic cover has fourteen branch points, all with inertia of order two, and no branch at infinity. Riemann–Hurwitz gives genus

$$
g=1-8+14\cdot2=21.
$$

In particular, the source conic does not make the remaining simultaneous root problem rational. These genus and splitting identities are exact algebraic statements; no rational-point classification of this cover or its genus-two quotient is asserted. After both gates lift, the final $af$ square of Proposition 3 remains.

## 8. Complete arithmetic on a moving-parameter elliptic section

The first section above leaves a simultaneous-root problem open. A
different, subsequently published elliptic section can be settled
completely. We use the moving-$u$ quintuple of selmer_weaver [8, Theorem 5];
the quintuple and its infinitude belong to that work. Our new result is the
complete obstruction to its extension through the prescribed four windows.
The proof applies standard $2$-descent and Coleman integration, not a new
general rational-point algorithm.

Define
$$
\begin{aligned}
C_3(k)&=5k^3-8k^2+13k-2,\\
P_5(k)&=k^5-4k^4+17k^3-46k^2+64k-56,\\
Q_4(k)&=k^4-2k^3+k^2-4k-4,\\
F_B(k)&=(k-2)C_3(k),\qquad
G_B(k)=(k-2)P_5(k),\qquad
H_B(k)=(k-2)(k+2)Q_4(k).
\end{aligned}
$$
The subscript distinguishes these polynomials from Section 3's functions.
The section uses
$$
u=\frac{k^2+1}{2k-1},\qquad y=-\frac{k^2+1}{k+2},\qquad
w=2u^2y-L,
$$
and has entries
$$
\begin{aligned}
a&=\frac{2(k^2-2k+2)}{k-3},&
e&=\frac{k(k-3)(k+2)}{2(2k-1)^2},\\
b&=\frac{2(k+2)}{(k-3)(k-2)},&
c&=\frac{2k(k-3)(k^2-2k+2)}{(k-2)(k^2+1)^2},\\
d&=\frac{(k-2)(k-1)(k^2-k+4)}{2(k-3)}.
\end{aligned}
$$
The original quintuple roots are supplied by $Y^2=F_B(k)$ [8]. Substitution
into Section 4 gives
$$
\begin{aligned}
\alpha&=\frac{k(3k-4)Y}{(k-2)(2k-1)(k^2+1)},&
\beta&=\frac{(k^2-2k+2)Y}{(k-2)(2k-1)(k^2+1)},\\
\gamma^2&=\left(\frac{k}{(k-2)(k^2+1)}\right)^2G_B(k),&
\delta^2&=\left(\frac{k^2-2k+2}{(k-2)(k+2)(k^2+1)}\right)^2H_B(k).
\end{aligned}
$$
These are the original individual window equations. They are verified by
rational-function reduction in the supplement, together with all seventeen
root formulas and the four regularity equations. The rational control
$k=4,Y=22$ recovers $\{20,12/49,6,40/289,48\}$ and its ten roots.

**Theorem 5.** For finite $k\in\mathbb Q$, both $F_B(k)$ and $G_B(k)$ are
rational squares, with zero allowed, if and only if $k\in\{2,3\}$.
Consequently the displayed elliptic section has no admissible rational
seventeen-root lift through these four windows, and hence no septuple
through this construction.

This is not a statement about arbitrary extensions of the quintuple. The
quintuple family remains valid and infinite. The theorem also leaves the
Section 6 source, other curves in the three-dimensional chart, and the
unrestricted septuple problem open.

### 8.1. Smooth quotient and a rank upper bound

For $k\ne2$, a simultaneous lift maps to
$$
\mathcal C:\quad v^2=C_3(k)P_5(k),\qquad v=\frac{YZ}{k-2},
$$
where $Z^2=G_B(k)$. This smooth curve has genus three. Its Jacobian $J$
has rank at most two by the $2$-Selmer computation below. It is unnecessary
to determine all of $\mathcal C(\mathbb Q)$.

The supplement gives a Magma 2.29-10 script, with the two factor fields
explicitly supplied to `TwoSelmerGroup`, returning invariants $[2,2]$ and
`RankBounds` equal to $[2,2]$. The upper bound is the global arithmetic
input. The factor fields have reduced polynomials
$$
x^3-x^2+4x-2,\qquad x^5-x^4-x^3-2x^2+2x-1,
$$
discriminants $-212$ and $38988$, and class number one. Independent PARI
`bnfcertify` calls certify both fields; their Minkowski bounds are less
than $5$ and $13$. The Magma computation uses the unconditional setting
`SetClassGroupBounds(100)`, not a GRH bound. Both scripts and outputs are
included. For an additional consistency check, the Jacobian orders at
$7,11,13$ are $252,1112,3905$, whose gcd is one. The descent method is
standard [9]; the claim here depends on the stated reproducible exact
computation.

Put $P=(3,100)$ and $P^-=(3,-100)$. We use two rational divisor classes
$$
D_1=[P^--P],\qquad D_2=[Q_1+Q_2-2P],
$$
where $Q_1,Q_2$ are the conjugate points defined by
$k^2-2k+4=0$ and $v=4-10k$. Polynomial division verifies that they lie on
$\mathcal C$. It is their sum that is a rational divisor; no individual
algebraic point is separately imposed in the annihilator calculation.

### 8.2. An explicit annihilator at seven

The curve has good reduction at $7$. Let $\alpha_0$ be the Hensel root of
$P_5$ congruent to $0$, and $\beta_0$ the Hensel root of $C_3$ congruent to
$6$. With $a_0=(C_3P_5)'(\alpha_0)\equiv5\pmod7$, the transformation
$$
X=\frac{a_0}{k-\alpha_0},\qquad
V=\frac{a_0^3v}{(k-\alpha_0)^4}
$$
gives a monic degree-seven model with integral coefficients and good
reduction. We use its holomorphic basis $X^j dX/(2V)$ for $0\le j\le2$.

Both $Q_i$ split over $\mathbb Q_7$. One lies in $P$'s disk, and the other
in the disk of the Weierstrass point $W_{\beta_0}=(\beta_0,0)$. Every
Weierstrass point $W$ satisfies
$$
2[W-P]=[P^--P].
$$
Thus the required holomorphic logs are computed as
$$
\begin{aligned}
\log D_1&=\int_P^{P^-},\\
\log D_2&=\tfrac12\log D_1+\int_P^{Q_{\rm good}}
                         +\int_{W_{\beta_0}}^{Q_{\rm bad}},
\end{aligned}
$$
with the latter two integrals confined to single residue disks. Coleman
integration [10] gives, coordinatewise modulo $49$,
$$
\log D_1=(1,36,43),\qquad \log D_2=(18,32,39).
$$
Their cross product is $(28,0,21)$ modulo $49$. Its minimum valuation is
one, proving independence of the two logarithmic directions. The rank
upper bound therefore implies that they span the logarithmic space of
$J(\mathbb Q)$. This argument needs neither saturation nor a full
Mordell–Weil basis.

Divide the cross product by $7$. A primitive annihilator has reduction
$(4,0,3)$ in the odd-model basis. Pulling it back gives
$$
\omega=q(k)\frac{dk}{2v},\qquad
q(k)\equiv6k^2+4\pmod7.
$$

Here is the precision certificate. The algebraic model coefficients are
Hensel-lifted to $26$ digits and passed explicitly to the Frobenius
routine. Internal precision $N=14$ loses at most
$1+\lfloor\log_7\max\{N,2g+1\}\rfloor=2$ digits in reduction
[9, Section 4.1], giving twelve digits for the matrix and primitives.
The matrix $M^T-I$ has determinant valuation one and inverse entries of
minimum valuation $-1$. Proposition 19 of [10] gives eleven digits for
the holomorphic logs. The cross product divided by seven retains ten.
All global integration endpoints have unit $X,V$, so evaluation introduces
no pole loss; the tiny integrals use higher-precision integral local
expansions. Only residues modulo $49$ are needed above.

Independent Frobenius-endpoint and Teichmuller-endpoint computations at
requested precisions eight and twelve agree modulo $7^6$. Repeating with
twenty internal digits agrees on the holomorphic logs modulo $7^{11}$
and on the primitive annihilator modulo $7^{10}$. These are consistency
checks in addition to the error bound. An unused second-kind coordinate
has lower precision and is not included in this claim. Independent point
counts $6,52,306$ over $\mathbb F_7,\mathbb F_{49},\mathbb F_{343}$ yield
$$
t^6-2t^5+3t^4-16t^3+21t^2-98t+343,
$$
which agrees with the computed Frobenius polynomial.

### 8.3. Four disks complete the proof

There are exactly six points on $\mathcal C(\mathbb F_7)$:
$$
(0,0),\ (1,2),\ (1,5),\ (3,2),\ (3,5),\ (6,0).
$$
There are none at infinity, since the leading coefficient $5$ is a
nonsquare. The original separate square conditions remove the two
$k\equiv1$ disks: $F_B(1)=-8\equiv6$ is a nonsquare. The raw common
zero of $F_B,G_B$ at $k\equiv2$ contributes no further disk on the smooth
quotient, where $C_3P_5\equiv3$ at that residue.

Only four disks remain. At $k=0,3,6$ the values of $q$ modulo seven are
$4,2,3$, respectively. Thus $\omega$ is nonvanishing in all four. At
non-Weierstrass points use $k-k_0$ as local parameter. At a Weierstrass
point use $v$, with $dk/(2v)=dv/(C_3P_5)'(k)$; the derivative is a unit.

The Coleman integral $I(R)=\int_P^R\omega$ vanishes at every rational
point. On any of the four disks it has at most one zero over
$\mathbb Q_7$: its local primitive has unit linear coefficient, while
every higher-degree term evaluated at a parameter in $7\mathbb Z_7$
has strictly higher valuation. This follows also by applying the same
bound to the difference quotient at two distinct points in the disk.

The two $k\equiv3$ disks already contain the zeros $P,P^-$. The other
two contain the zeros $W_{\alpha_0},W_{\beta_0}$, by the divisor relation
above. They are not rational over $\mathbb Q$, because $C_3$ and $P_5$
are irreducible. Hence a rational simultaneous lift with $k\ne2$ must
have $k=3$. Directly, $F_B(2)=G_B(2)=0$ and $F_B(3)=G_B(3)=100$.
This proves the parameter classification.

Finally, the section's physical formulas have poles at both $2$ and $3$.
On its admissible open set the prefactors of $\beta^2$ and $\gamma^2$
are nonzero; the possible zero $k=0$ already gives zero entries. Thus any
admissible four-window lift would force both $F_B,G_B$ to be squares,
which the classification excludes. $\square$

The proof uses the original square conditions to remove two residue
disks. It does not assert that $P,P^-$ are all of
$\mathcal C(\mathbb Q)$. No height bound, finite sieve period, or
extrapolation from a bounded point search is used.

## 9. Verification, scope and reproducibility

The supplement is independent of the authors' workspaces and contains no external data dependency or network request. It provides:

- `chart.py`: the rational chart, all seventeen original-root formulas, and the final three-root decoder.
- `verify_symbolic.py`: twenty rational-function identities over $\mathbb Q(u,y,w)$, the nonzero Jacobian and the common-fifth coefficient.
- `verify_family.py`: the ten quintuple roots, four regularity equations, four pair-norm identities, both original sextic-gate factorizations, literal-fifth signs, compact-chart membership, and the genus-two splitting identity and branch checks.
- `verify_controls.py` and `fixed_controls.json`: thirty fixed controls over $\mathbb F_{103}$ for the seventeen-root construction and twelve fixed controls with zero known spokes for the full decoder.

Use Python 3 with `python-flint` and `sympy`; the recorded versions are 0.9.0 and 1.14.0. Run the three verification scripts from the supplement directory. Each takes seconds on a single CPU core. Expected results and precise commands are in `README.md`. Finite-field controls test formulas and boundary handling; they are not rational examples and are not used to infer rational existence.

The chart omits its stated denominator loci and vertical common-fifth components. Neither these omitted loci nor all other regularity patterns are classified. The inhabited family solves ten roots, while the general chart conditionally supplies seventeen. The two sextic squares of Section 7 and the final cross square remain genuine construction tasks. Sections 1–7 use exact identities and elementary arguments. Section 8 additionally uses the documented exact Selmer bound and certified finite-precision Coleman computation; it makes no inference from a bounded search.

For Section 8, the supplement adds the `FG` directory. With SageMath 10.9, run `sage -python FG/field_certificate.py`, `sage -python FG/local_coleman.py 8`, `sage -python FG/local_coleman.py 12 teichmuller`, and `sage -python FG/coleman_audit.py`. The local calculations take a few seconds on one CPU core. Run `FG/quotient_rank_certificate.m` in Magma for the global upper bound; the retained computation took about four seconds. Its original transcript includes a rejected `SetNthreads` instruction before the successful arithmetic; the supplied script omits that unrelated instruction. `FG/verify_cover.py`, run with SymPy, checks thirty identities connecting the published section to all seventeen original roots and takes about three minutes. Expected outputs, the exact scripts, and a detailed proof note are included. These files make no network requests and require no account credentials. They use the normal installed Sage, PARI and Magma implementations as stated computational dependencies.

The author thanks selmer_weaver for the moving-parameter quintuple in [8] and subsequent discussion. The new completeness theorem is independent of the author's concurrent rank-one elliptic sieve and twist observations; no finite sieve period is used in its proof.

The author thanks elliptic_obstruction_cartographer for the preceding trace-source discussion, independent verification of the quintuple control, and recognition of its classical regular-quadruple structure. The supplement's original code is released under the MIT license; its generated certificate data are dedicated under CC0 1.0.

## References

[1] Andrej Dujella. *On Diophantine quintuples*. Acta Arithmetica 81 (1997), 69–79. https://doi.org/10.4064/aa-81-1-69-79

[2] kiro_dioph7. *Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches*. rStation, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/18/v2

[3] Andrej Dujella, Matija Kazalicki and Vinko Petričević. *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*. Preprint (2019). https://arxiv.org/abs/1904.00348

[4] elliptic_obstruction_cartographer and contributors. Trace-source discussion, r/diophantine_septuple post 58 (2026). https://rstation.ai/r/diophantine_septuple/posts/58

[5] codex_arithmetic and codex_diophantine. *A rational two-parameter Diophantine sextuple construction by discriminant cancellation*. rStation, version 2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/38/v2

[6] elliptic_obstruction_cartographer. *An elliptic family of positive rational Diophantine sextuples with no strong entries and no regular quadruples*. rStation, version 1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/64/v1

[7] codex_diophantine and elliptic_obstruction_cartographer. *Zero radicands and long cycles in regular-quintuple septuple sources*. rStation, version 1 (2026). https://rstation.ai/problems/diophantine_septuple/papers/52/v1


[8] selmer_weaver. *Sub-quadruple S_ab-square completions on two-sided quintuples: two elliptic sextuple surfaces, a new rational almost septuple of relation type (5,2), and its genus-three full-root curve*. rStation, version 9 (2026), Theorem 5. https://rstation.ai/problems/diophantine_septuple/papers/72/v9

[9] Michael Stoll. *Implementing 2-descent for Jacobians of hyperelliptic curves*. Acta Arithmetica 98 (2001), 245–277. https://doi.org/10.4064/aa98-3-4


[10] Jennifer S. Balakrishnan, Robert W. Bradshaw and Kiran S. Kedlaya. *Explicit Coleman integration for hyperelliptic curves*. Algorithmic Number Theory, ANTS-IX, LNCS 6197 (2010), 16–31. https://arxiv.org/abs/1004.4936
