## 1. Problem and contribution

A rational Diophantine $m$-tuple is a set of $m$ distinct nonzero rationals such that $a_ia_j+1$ is a square for every $i\neq j$. No rational septuple is known [1, Problem 3.2], although there are infinitely many sextuples [7]. An *almost septuple* satisfies 20 of the 21 conditions [1, Problem 3.3]. In [13] two almost septuples, $A_2$ and $A_3$, came from one construction: a four-term regular *chain* over a fixed pair, closed by a seventh element that is a regular fifth element of two sub-quadruples. This paper classifies every closure of a four-chain by two regular relations through the seventh element, with complete square-class forcing.

1. **Complete forcing (Section 3).** Each regular relation gives $\mathbb F_2$-linear relations among the square classes of the $21$ values $uv+1$: one for each of the matchings of $R_4$ or $3|2$ splits of $R_5$, and one for the discriminant in each variable. We take the full linear closure. Of the $191$ classes of support pairs, $8$ leave **no** condition open ($k=0$), $28$ leave one class open, and the rest leave $2$–$5$. Version 1 of this paper used a weaker rule and reported no $k=0$ class; the referee's counterexample is one of the new $k=1$ classes.
2. **Reconstruction (Section 4).** On each component of the elimination locus, the seventh element is the rational function $x=-(a_1e_2-a_2e_1)/(a_1b_2-a_2b_1)$ from the first subresultant. We certify at an $\mathbb F_p$-point of each component that this denominator, the leading coefficients, and every factor divided by in the forcing are generically nonzero. Some components fail a non-degeneracy condition at every one of $8$–$12$ sampled $\mathbb F_p$-points: the two quadratics are proportional, or $x$ is $0$ or an element of the six-set. We set these aside as degenerate. That classification is by sampling, not proof, so all results below are stated for the retained components, and the set-aside ones remain unresolved loci.
3. **Septuple surfaces (Theorem 2, Section 5).** The $8$ classes with $k=0$ give $13$ non-degenerate absolutely irreducible surfaces ($10$ up to the sign symmetry), of degree $84$–$154$ in $(r,m,A)$. On a dense open subset of each, every rational point is a rational Diophantine septuple. All 21 values $uv+1$ are squares in the function field. Conversely, a non-degenerate septuple of these closure types lies on one of these surfaces or on one of the two $k=0$ components set aside as degenerate.
4. **Almost-septuple surfaces (Theorem 3).** The $k=1$ classes give $54$ retained components of $25$ classes that fail exactly one condition, and $3$ components of two tied classes where four conditions fail together. On each, the failing value is proved not to be a square in $\bar{\mathbb Q}(H)$. The proof uses smooth $\mathbb F_p$-points where it is a nonsquare and others where it is a square (Lemma 5b, `nonsqw_z1.out`).
5. **Genus (Section 6).** Each septuple surface is absolutely irreducible. In $29$ of the $30$ coordinate pencils, all but finitely many rational fibres are absolutely irreducible with geometric genus $\ge$ 55. (The computation for the $A$-pencil of Z0$_{7,2}$ did not finish.) The certificate is an irreducible $\mathbb F_p$-fibre with the generic bidegree and a smooth $\mathbb F_p$-point, plus a count of odd branch points. So no certified pencil is rational or elliptic, and each such fibre carries finitely many septuples (Faltings [12]). The almost-septuple surfaces have bounds of the same kind (Tables 5–6). Fibre-genus bounds do not bound the Kodaira dimension: a blown-up $\mathbb P^2$ carries pencils of plane curves of every genus. Whether a septuple surface is rational, K3 or elliptic, and so could carry infinitely many septuples, is left open.
6. **Searches (Section 7).** On the septuple surfaces we searched the Lasić chart to height 100–150 on five sign-orbit representatives, and the $(r,m)$ chart to height 60 on all ten (Table 7). No septuple appeared. The $27$ new $k=1$ components were searched in the $(r,m)$ chart to height 60 (Table 7b). They give no almost septuple, but a degenerate point yields a new rational Diophantine sextuple. The A2-type search to height $450$ and the CL/M searches of version 1 are retained. They find only $A_2,A_3,A_4$ and Dujella's $AS_{11}$.
7. **A new almost septuple** (Section 8):
$$
A_4=\left\{-\tfrac{3492}{39325},\ \tfrac{13975}{1936},\ \tfrac{5043968}{4758325},\ \tfrac{723}{208},\ \tfrac{58443}{5200},\ \tfrac{6992}{1573},\ \tfrac{50700}{212521}\right\}.
$$
It fails only $\tfrac{5043968}{4758325}\cdot\tfrac{6992}{1573}+1=\tfrac{42752269481}{86515^2}$. It is not on Dujella's list [5] or in [3,4,6,13].

`verify3.py` checks all identities, both closure computations, the four almost septuples, and polynomial vanishing exactly. It needs only the standard library.

## 2. Chains and regular relations

Let $A\neq0$ and $AB+1=r^2$, $A\ne B$. If $Ac+1=s^2$ and $Bc+1=t^2$, then $(s,t)$ lies on the conic $Bs^2-At^2=B-A$. The map $\sigma(s,t)=(rs+At,Bs+rt)$ preserves this conic and has determinant $1$. Put $(s_{k+1},t_{k+1})=\sigma(s_k,t_k)$ and $c_k=(s_k^2-1)/A$. Then $Bc_k+1=t_k^2$ and $c_kc_{k+1}+1=(rc_k+s_kt_k)^2$; $c_{k\pm1}$ are the two regular fourth elements of $\{A,B,c_k\}$ [11]. We parametrise the conic by the line of slope $m$ through $(1,1)$:
$$
s_0=\frac{2Am-B-Am^2}{B-Am^2},\qquad t_0=1+m(s_0-1).
$$
So $(r,m,A)$ are coordinates on four-chains $E=\{A,B,c_{-1},c_0,c_1,c_2\}$. All six elements are rational functions with common denominator $A\Delta^2$, $\Delta=r^2-1-A^2m^2$ (`base.lib`).

**Lemma 1 (chain).** In $E$ the $12$ values $AB+1$, $Ac_k+1$, $Bc_k+1$ $(k=-1,\dots,2)$, $c_{-1}c_0+1$, $c_0c_1+1$, $c_1c_2+1$ are squares of rational functions in $(r,m,A)$. The three values for $c_{-1}c_1$, $c_0c_2$, $c_{-1}c_2$ are not.

**Lemma 2 (symmetric regular relations).** Let
$$
R_4(a,b,c,d)=(a+b-c-d)^2-4(ab+1)(cd+1),\qquad R_5(a,b,c,d,e)=(abcde+2abc+a+b+c-d-e)^2-4(ab+1)(ac+1)(bc+1)(de+1).
$$
(i) $R_4$ is symmetric in its four arguments: the three matchings $\{ab|cd\},\{ac|bd\},\{ad|bc\}$ give the same polynomial. (ii) $R_5$ is symmetric in its five arguments: all ten $3|2$ splits give the same polynomial. (iii) As a polynomial in any one argument, $R_4$ is monic of degree $2$ with discriminant $16\prod(uv+1)$ over the three pairs of the other arguments. $R_5$ has leading coefficient $(\prod\text{others}-1)^2$ and discriminant $16\prod(uv+1)$ over the six pairs of the other four.

Both identities are checked symbolically (`sym.py`, SymPy) and at random rationals (`verify3.py`).

## 3. Complete square-class forcing

A *closure* adds a seventh element $x$ through two regular relations with supports $S_1,S_2\subset E$. If $|S|=3$ the relation is $R_4(S,x)=0$; if $|S|=4$ it is $R_5(S,x)=0$. There are $20+15=35$ supports and $595$ unordered pairs. The Klein group generated by $A\leftrightarrow B$ and the reversal $c_k\leftrightarrow c_{1-k}$ preserves the chain structure, which leaves $191$ classes.

**Square classes.** Let $\Omega$ be the set of $21$ pairs of $E\cup\{x\}$. At a rational point where all $21$ values $uv+1$ are nonzero, write $[uv]\in\mathbb Q^\*/\mathbb Q^{\*2}$, an $\mathbb F_2$-vector. Lemma 1 gives $[uv]=0$ on $12$ pairs. Each relation through $x$ gives the following equations.

- *Matchings and splits.* $R_4(a,b,c,d)=0$ reads $(a+b-c-d)^2=4(ab+1)(cd+1)$ for each matching. So $[ab]+[cd]=0$ for all three matchings. $R_5=0$ gives $[ab]+[ac]+[bc]+[de]=0$ for all ten splits. This uses only that the factors are nonzero. If the left side vanishes, the product is $0$, which is excluded.
- *Discriminants.* If a quadratic with rational coefficients has a rational root, its discriminant is a square. This holds whatever the leading coefficient is, since $\mathrm{disc}=(2\alpha u+\beta)^2$ at a root $u$. By Lemma 2(iii), each variable $v$ of the relation gives $\sum[uw]=0$ over the pairs of the other arguments.

Let $k$ be the dimension of the solution space of these equations in the $9$ unknown classes (the $3$ open chain pairs and the $6$ pairs $xe$). A pair is *forced* if its class vanishes on that whole space (`clos2.py`).

**Proposition 3.** Over the $191$ classes the distribution of $k$ is $\{0{:}8,\ 1{:}28,\ 2{:}48,\ 3{:}59,\ 4{:}33,\ 5{:}15\}$. Every class with $k=0$ forces all $21$ pairs. Of the $28$ classes with $k=1$, $25$ leave exactly one pair unforced. In the other three ($\{AB\,c_{-1}\}|\{c_{-1}c_0c_1c_2\}$, $\{ABc_0\}|\{c_{-1}c_0c_1c_2\}$, $\{ABc_{-1}c_0\}|\{c_{-1}c_0c_1c_2\}$), the four pairs $c_{-1}c_1,c_{-1}c_2,c_1x,c_2x$ all share one free class, so they hold or fail together.

Compared with the rule of version 1 (discriminants only, applied to the three open chain pairs), the transitions old $k\to$ new $k$ are: $(1\to1)\,11$, $(2\to0)\,6$, $(3\to0)\,2$, $(3\to1)\,14$, $(4\to1)\,3$; $k$ never increases (full list in `clos2.out`). The referee's example $\{A c_{-1}c_1\}|\{c_{-1}c_0c_2\}$ is one of the new $k=1$ classes (free pair $Bx$).

| name | $S_1\,|\,S_2$ | name | $S_1\,|\,S_2$ |
|---|---|---|---|
| Z0$_1$ | $ABc_{-1}c_1\,|\,Ac_{-1}c_0c_2$ | Z0$_5$ | $ABc_0c_1\,|\,c_{-1}c_0c_1c_2$ |
| Z0$_2$ | $ABc_{-1}c_1\,|\,c_{-1}c_0c_1c_2$ | Z0$_6$ | $Ac_{-1}c_0c_1\,|\,Bc_{-1}c_0c_2$ |
| Z0$_3$ | $ABc_{-1}c_1\,|\,c_{-1}c_0c_2$ | Z0$_7$ | $Ac_{-1}c_0c_2\,|\,Bc_{-1}c_1$ |
| Z0$_4$ | $ABc_{-1}c_2\,|\,c_{-1}c_0c_1c_2$ | Z0$_8$ | $Ac_{-1}c_0c_2\,|\,Bc_{-1}c_1c_2$ |

Table 1. The eight closure classes with $k=0$ (one representative each).

The $28$ classes with $k=1$ are listed in `index.txt` with their free pairs. Eleven of them are the eleven types of version 1. Table 2 gives the translation.

| version 1 | A2-type | CL1 | CL3 | CL4 | CL7 | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|---|---|---|---|---|
| class | Z1$_{15}$ | Z1$_{13}$ | Z1$_7$ | Z1$_4$ | Z1$_3$ | Z1$_{24}$ | Z1$_5$ | Z1$_{16}$ | Z1$_{14}$ | Z1$_6$ | Z1$_8$ |

Table 2. The eleven types of version 1 among the new $k=1$ classes. The $14$ further single-failure classes are Z1$_{10,11,12,17,\dots,23,25,\dots,28}$.

The proposition says what the equations force. That the free class really is nonzero, so the remaining condition really fails, is proved per component in Theorem 3, from smooth $\mathbb F_p$-points where the free value is a nonsquare (Lemma 5b).

## 4. Elimination and reconstruction of the seventh element

For a class $\tau=(S_1,S_2)$, write the relations as $Q_i=a_ix^2+b_ix+e_i$ with $a_i,b_i,e_i\in\mathbb Z[r,m,A]$, after clearing the denominator $A\Delta^2$ (`base.lib`, procedures `R4x`, `R5x`). The Sylvester resultant is
$$
G_\tau=(a_1e_2-a_2e_1)^2-(a_1b_2-a_2b_1)(b_1e_2-b_2e_1).
$$
It vanishes whenever $Q_1,Q_2$ have a common root, including the cases where a leading coefficient vanishes. We factor $G_\tau$ over $\mathbb Q$ (Singular). The factors of degree $\le4$ are constants, $A$, $\Delta=r^2-1-A^2m^2$ (where $c_0$ or the conic degenerates) and, for CL7 and M5, $2r\pm1$ (where $\sigma^3=-I$, so $c_2=c_{-1}$). They are discarded. Each remaining irreducible factor $H$ is a *component*.

**Lemma 4 (subresultant).** Let $P$ be a rational point of $H$ with $a_1a_2\ne0$ and $S_1:=a_1b_2-a_2b_1\ne0$ at $P$. Then $Q_1,Q_2$ have exactly one common root, and it is
$$
x_P=-\frac{a_1e_2-a_2e_1}{a_1b_2-a_2b_1}\in\mathbb Q .
$$
*Proof.* $G(P)=0$ with $a_1a_2\ne0$ gives a common root $\xi\in\bar{\mathbb Q}$. Then $\xi$ is a root of $a_2Q_1-a_1Q_2=-S_1x-(a_1e_2-a_2e_1)$, which is linear because $S_1\ne0$. So $\xi=x_P$. If there were two common roots, $Q_1$ and $Q_2$ would be proportional, which forces $S_1=0$. $\square$

This replaces the incorrect argument of version 1, which inferred rationality from discriminants. Those discriminants are squares only once a rational common root is known.

**Lemma 5 (certificate).** Let $H\in\mathbb Z[r,m,A]$ be primitive and irreducible over $\mathbb Q$, and let $F\in\mathbb Z[r,m,A]$. Suppose there is a prime $p$ and $P\in\mathbb F_p^3$ with $\bar H(P)=0$ and $\bar F(P)\ne0$. Then $F$ does not vanish identically on $V(H)$.

*Proof.* Otherwise, by the Nullstellensatz $H\mid F^n$ in $\mathbb Q[r,m,A]$. By Gauss' lemma ($H$ primitive) this also holds in $\mathbb Z[r,m,A]$. Reducing mod $p$ gives $\bar F(P)^n=0$. $\square$

To pass from a value at an $\mathbb F_p$-point to the function field, the point must be smooth. At a singular point the inference fails: on $u^2=v^2w$ the function $w=(u/v)^2$ is a square, yet it takes the nonsquare value $2$ at the point $(0,0,2)$ mod $5$.

**Lemma 5b (smooth specialisation).** Let $H\in\mathbb Z[r,m,A]$ be primitive and irreducible over $\mathbb Q$, and let $f=N/D$ with $N,D\in\mathbb Z[r,m,A]$. Let $p$ be a prime and $P\in\mathbb F_p^3$ a point with $\bar H(P)=0$, $\partial\bar H/\partial v\,(P)\ne0$ for some variable $v$, and $\bar N(P)\bar D(P)\ne0$.

- (a) If $\bar f(P)$ is a nonsquare in $\mathbb F_p$, then $f$ is not a square in $\mathbb Q(H)$.
- (b) If in addition $P'$ is a second such point for the same $p$ with $\bar f(P')$ a nonzero square, then $f\notin c\,\mathbb Q(H)^{\times2}$ for every $c\in\mathbb Q^\times$. If $H$ is absolutely irreducible, then $f$ is not a square in $\bar{\mathbb Q}(H)$.

*Proof.* Since $H$ is primitive and irreducible over $\mathbb Q$, it is prime in $\mathbb Z[r,m,A]$. So $X=\operatorname{Spec}\mathbb Z[r,m,A]/(H)$ is integral with function field $\mathbb Q(H)$, and flat over $\mathbb Z$. By the Jacobian criterion, $X\to\operatorname{Spec}\mathbb Z$ is smooth at $P$, so $R=\mathcal O_{X,P}$ is a regular local ring, hence a UFD and normal. The element $p$ is prime in $R$, because $R/pR$ is the local ring of $\bar H$ at its smooth point $P$. Since $\bar N(P)\bar D(P)\ne0$, $f$ is a unit of $R$.

(a) If $f=g^2$ with $g\in\mathbb Q(H)$, then $g$ is integral over $R$, so $g\in R$ and $\bar f(P)=\bar g(P)^2$ in the residue field $\mathbb F_p$.

(b) Suppose $f=cg^2$, and write $c=p^kc'$ with $c'$ prime to $p$. Since $f$ is a unit, comparing the valuations at the prime $p$ of $R$ gives $k=2j$. Then $(p^jg)^2=f/c'$ is a unit of $R$, so $p^jg\in R$ by (a)'s argument and $\bar f(P)=\bar c'\cdot\overline{p^jg}(P)^2$. Thus $\bar f(P)$ has the Legendre symbol of $\bar c'$, and so does $\bar f(P')$, a contradiction. If $H$ is absolutely irreducible and $f=g^2$ with $g\in\bar{\mathbb Q}(H)$, then $\operatorname{Gal}(\bar{\mathbb Q}/\mathbb Q)$ acts on $g$ through a character of order $\le2$. If it is trivial, $g\in\mathbb Q(H)$. Otherwise it cuts out some $\mathbb Q(\sqrt c)$, so $g\sqrt c\in\mathbb Q(H)$ and $f\in c\,\mathbb Q(H)^{\times2}$. $\square$

**Non-degeneracy.** A point of $H$ is *non-degenerate* if it satisfies all of the following:

- $A\Delta\ne0$;
- $a_1a_2S_1\ne0$;
- the seven elements $E\cup\{x_P\}$ are distinct and nonzero;
- all $21$ values $uv+1$ are nonzero;
- $\prod_{w\in T}w\ne1$ for every $4$-subset $T$ of an $R_5$ relation's five arguments, so that no $R_5$ drops degree in any variable.

Each condition is $F\ne0$ for an explicit polynomial (numerator of a rational function), so the non-degenerate points form a Zariski-open subset $U_H$. `nondeg0.py` samples $\mathbb F_{100003}$-points of $\bar H$. At each one it computes $\gcd(\bar Q_1,\bar Q_2)$ and $x$, and records which of these conditions fail. It also records the Legendre symbol of each of the $21$ values. A component is *non-degenerate* if some sampled point satisfies all conditions. By Lemma 5, $U_H\neq\emptyset$ for such a component, applied to the product of the condition polynomials. A component is *degenerate* if a condition fails at every sampled point.

Of the $15$ components for the $8$ classes with $k=0$:

- $13$ are non-degenerate. All $134$ sampled points satisfy all conditions (`nondeg0_z0.out`).
- Z0$_{5,2}$ and Z0$_{5,3}$ (degree $20$) have $x=0$ at every sampled point.

Of the $83$ components for the $28$ classes with $k=1$:

- $57$ are non-degenerate.
- $26$ are degenerate. At every sampled point of these, one of the following holds: $x=0$ (8), $x\in E$ (10), or $Q_1\propto Q_2$ with a repeated element of $E$ (8). See `degen_z1.out` and `degen2_prop.out`.

Degeneracy of these components is inferred from $8$–$12$ random samples, not proved. They are excluded from Theorems 2–3, so any non-degenerate rational points on them are not covered by this paper.

## 5. Septuple surfaces and almost-septuple surfaces

**Theorem 2.** Let $H$ be one of the $13$ non-degenerate components of the $k=0$ classes (Table 3). Every rational point $P\in U_H(\mathbb Q)$ gives a rational Diophantine septuple $E(P)\cup\{x_P\}$. Conversely, every rational Diophantine septuple containing a four-chain over a pair whose seventh element satisfies the two relations of a $k=0$ class $\tau$, with all non-degeneracy conditions, arises this way from a component of $G_\tau$. That component is one of those in Table 3 unless it is Z0$_{5,2}$ or Z0$_{5,3}$.

*Proof.* By Lemma 4, $x_P$ is a rational common root. The six-set is non-degenerate and all $21$ values are nonzero. So the square classes are defined and satisfy every equation of Section 3, in particular the discriminant equations, because $x_P$ is rational. Since $k=0$, all $21$ classes vanish, so every value is a nonzero rational square. The elements are distinct and nonzero by non-degeneracy. Conversely, such a septuple gives a rational point of $G_\tau=0$ off $A\Delta(2r\pm1)=0$, so it lies on some component. $\square$

The same argument works over any field of characteristic $0$. In particular all $21$ values are squares in the function field $\mathbb Q(H)$. A real point of $U_H$ has all $21$ values positive, and `realtest.py` confirms this numerically on every component. This is a consistency check, not evidence for rational points.

| comp. | sign partner | $(\deg,\deg_r,\deg_m,\deg_A)$ | terms |
|---|---|---|---|
| Z0$_{1,2}$ | self | $(84,52,32,44)$ | $7858$ |
| Z0$_{1,3}$ | self | $(84,52,32,44)$ | $7858$ |
| Z0$_{2,2}$ | self | $(96,56,40,48)$ | $10380$ |
| Z0$_{2,3}$ | self | $(104,64,40,56)$ | $18091$ |
| Z0$_{3,2}$ | self | $(136,88,48,72)$ | $32769$ |
| Z0$_{4,2}$ | Z0$_{4,3}$ | $(104,64,40,52)$ | $29117$ |
| Z0$_{5,4}$ | self | $(130,76,56,68)$ | $31829$ |
| Z0$_{6,2}$ | Z0$_{6,3}$ | $(85,50,36,46)$ | $19227$ |
| Z0$_{7,2}$ | self | $(154,92,64,80)$ | $48188$ |
| Z0$_{8,2}$ | Z0$_{8,3}$ | $(100,64,36,52)$ | $26311$ |

Table 3. The ten septuple surfaces up to sign ($13$ components). The map $(r,m,A)\mapsto(-r,m,-A)$ sends $E$ to $-E$ and $x$ to $-x$. Sign partners were found by comparing $\bar H(-r,m,-A)$ with every component mod $p$ (`signpair.py`). Six of the eight $k=0$ classes were already in version 1, as $k=2$ types K2$_{5,6,8,9,10,11}$. Exactly these six had "no usable chart polynomial" there, so the old $k=2$ search never covered them. Z0$_5$ and Z0$_8$ were $k=3$ types, which were not searched.

**Theorem 3.** Let $H$ be one of the $54$ non-degenerate components of the $25$ single-failure classes with $k=1$, and let $w$ be the value $uv+1$ of the free pair of the class. Every $P\in U_H(\mathbb Q)$ gives seven distinct nonzero rationals with $20$ of the $21$ values $uv+1$ squares, and $P$ is a septuple iff $w(P)$ is a square. Moreover $w$ is not a square in $\bar{\mathbb Q}(H)$. The same holds for the three non-degenerate tied components Z1$_{1,3}$, Z1$_{2,4}$, Z1$_{2,5}$, with $17$ squares and a block of four values whose square classes agree; none of the four is a square in $\bar{\mathbb Q}(H)$.

*Proof.* The first part is Proposition 3 at the points of $U_H$, as in the proof of Theorem 2. For the second, `nonsqw.py` records, for each of the $57$ components, a point $P\in\bar H(\mathbb F_{100003})$ with $\partial\bar H/\partial A\,(P)\ne0$ at which $A\Delta$, $a_1a_2S_1$ and all non-degeneracy polynomials of Section 4 are nonzero and every free value is a nonsquare. For each free value it also records a second such point where that value is a nonzero square (`nonsqw_z1.out`, $123$ lines, none missing). All values $uv+1$ are regular at these points, with denominators dividing a power of $A\Delta S_1$. Lemma 5b applies, using the absolute irreducibility from Section 6. `chkw.py` re-verifies every line from the component files with the standard library only. $\square$

So the locus where the free value is a square is a double cover of $H$, and it is geometrically irreducible. Its rational points over $U_H$ are septuples. Theorem 3 does not decide whether it has any.

The $26$ degenerate $k=1$ components, among them all three components of Z1$_9$, are excluded from Theorem 3 on the sampling evidence of Section 4.

The $54$ components comprise the $30$ of version 1 (Table 2, under the new names) and $24$ new ones in the $14$ new classes.

## 6. Genus of the coordinate fibres

Fix one coordinate $v\in\{A,r,m\}$ of a component $H$; the other two are $(w_1,w_2)$. For $v_0$ in a field, the *fibre* $H_{v_0}$ is the plane curve $H(v_0;w_1,w_2)=0$. Let $n=\deg_{w_2}H_{v_0}$, and let $n_o$ be the total degree of the factors of $\operatorname{disc}_{w_2}H_{v_0}$ that occur to odd order and are coprime to the leading coefficient. If $H_{v_0}$ is absolutely irreducible, Riemann–Hurwitz for the projection to $w_1$ gives $g\ge\lceil(n_o-2n+2)/2\rceil$. A root of odd order is a branch point, because singularities contribute even amounts. We use both projections and take the larger bound.

**Lemma 6 (generic fibre).** Let $H\in\mathbb Z[r,m,A]$ be irreducible over $\mathbb Q$. Suppose that for a prime $p$ and $\bar v_0\in\mathbb F_p$ the fibre $\bar H_{\bar v_0}$:

(i) has the same degrees in $w_1$ and $w_2$ as $H$;
(ii) is irreducible over $\mathbb F_p$ with multiplicity one;
(iii) has a smooth $\mathbb F_p$-point;
(iv) gives the Riemann–Hurwitz bound $g_p$.

Then $H$ is absolutely irreducible. For all but finitely many $v_0\in\mathbb Q$, the fibre $H_{v_0}$ is absolutely irreducible of geometric genus $\ge g_p$.

*Proof.* A curve over $\mathbb F_p$ that is irreducible but not absolutely irreducible has all its $\mathbb F_p$-points on the intersection of its conjugate components, and so has no smooth $\mathbb F_p$-point. By (ii) and (iii), $\bar H_{\bar v_0}$ is therefore absolutely irreducible.

Let $v_0\in\mathbb Z$ reduce to $\bar v_0$. By (i), a factorisation of $H_{v_0}$ over $\bar{\mathbb Q}$ would reduce to a factorisation of $\bar H_{\bar v_0}$ over $\bar{\mathbb F}_p$ with the same bidegrees. So $H_{v_0}$ is absolutely irreducible. Also by (i), the leading coefficient does not drop, so the discriminant commutes with reduction. An odd-order root of $\overline{\operatorname{disc}}$ has an odd-order root of $\operatorname{disc}$ above it, so $n_o(\mathbb Q)\ge n_o(\mathbb F_p)$ while $n$ is unchanged (the reduction lemma of version 1). Hence $g(H_{v_0})\ge g_p$ for every $v_0\equiv\bar v_0\pmod p$.

These $v_0$ are Zariski-dense in the $v$-line. The geometric generic fibre is therefore irreducible, and so is $H$ over $\bar{\mathbb Q}$. On a dense open subset of the $v$-line the fibres are geometrically integral with constant geometric genus, equal to that of the generic fibre. This genus is $\ge g_p$, because the open set meets the dense set above. $\square$

The finite exceptional set is not computed. Version 1 instead bounded fibres explicitly over all residues mod $101,103$ off an exceptional set $U_p$; that statement is retained for the old components (`genus_v1.txt`).

*Quotients.* The tied component Z1$_{1,3}$ involves $r$ and $A$ only through $r^2$ and $A^2$, so every discriminant factor has even order and the bound above is vacuous. Write $H(r,m,A)=H_q(r^2,m,A^2)$. The fibre of $H$ over $A=a_0$ maps onto the fibre of $H_q$ over $U=a_0^2$ by $r\mapsto r^2$, so its genus is at least that of the quotient fibre (and similarly for the $r$-pencil). Irreducibility is certified on $H$ itself and the genus bound on $H_q$ (`halve.py`). No other component has a variable occurring only to even powers.

`fgz2.py` takes one random $\bar v_0\in\mathbb F_{32003}$ per pencil. It checks (i), factors the fibre over $\mathbb F_p$ (PARI), searches for a smooth point, and computes $g_p$ for both projections. `fgzagg.py` prints the tables. A bound is *certified* if (i)–(iii) hold.

| surface | fix $A$ | fix $r$ | fix $m$ |
|---|---|---|---|
| Z0$_{1,2}$ | 137 | 55 | 125 |
| Z0$_{1,3}$ | 137 | 55 | 137 |
| Z0$_{2,2}$ | 167 | 73 | 139 |
| Z0$_{2,3}$ | 167 | 73 | 151 |
| Z0$_{3,2}$ | 309 | 97 | 317 |
| Z0$_{4,2}$ (and Z0$_{4,3}$) | 163 | 70 | 157 |
| Z0$_{5,4}$ | 229 | 119 | 177 |
| Z0$_{6,2}$ (and Z0$_{6,3}$) | 142 | 72 | 120 |
| Z0$_{7,2}$ | ? | 120 | 284 |
| Z0$_{8,2}$ (and Z0$_{8,3}$) | 157 | 76 | 150 |

Table 5. Certified genus lower bounds for the generic coordinate fibres of the septuple surfaces, one per sign pair. "?": the computation did not finish within its time limit, so no bound is claimed for that pencil.

| comp. | fix $A$ | fix $r$ | fix $m$ | comp. | fix $A$ | fix $r$ | fix $m$ |
|---|---|---|---|---|---|---|---|
| Z1$_{10,6}$ (Z1$_{10,7}$) | 81 | 37 | 64 | Z1$_{23,2}$ | 131 | 47 | 127 |
| Z1$_{11,4}$ | 186 | 73 | ? | Z1$_{23,3}$ | 131 | 47 | 133 |
| Z1$_{12,2}$ (Z1$_{12,3}$) | 95 | 42 | 90 | Z1$_{25,2}$ (Z1$_{25,3}$) | 163 | 75 | 128 |
| Z1$_{17,3}$ (Z1$_{17,2}$) | 137 | 72 | 106 | Z1$_{26,2}$ | 132 | 54 | 133 |
| Z1$_{18,2}$ (Z1$_{18,3}$) | 127 | 55 | 117 | Z1$_{27,2}$ | 161 | 67 | ? |
| Z1$_{19,2}$ (Z1$_{19,3}$) | 123 | 47 | 114 | Z1$_{27,3}$ | 169 | 72 | 149 |
| Z1$_{20,2}$ (Z1$_{20,3}$) | 129 | 40 | 143 | Z1$_{28,6}$ | ? | 97 | 143 |
| Z1$_{21,4}$ | 165 | 70 | ? | Z1$_{1,3}$$^q$ | 105 | 50 | 32 |
| Z1$_{22,2}$ | 115 | 47 | 111 | Z1$_{2,4}$ (Z1$_{2,5}$) | 125 | 56 | 110 |
| Z1$_{22,3}$ | 115 | 47 | 110 |  |  |  |  |

Table 6. The same for the $24$ new single-failure components and the $3$ tied components, one row per orbit of the sign map $(r,m,A)\mapsto(-r,m,-A)$ (partner in parentheses; `signpair_z1.out`). The sign map preserves each coordinate pencil, so partners have the same bounds. $^q$: bound computed on the quotient described above. "?": as in Table 5.

The $30$ components of version 1 keep the bounds of its Table 3, reproduced in the supplement as `genus_v1.txt`. Under good reduction they are $\ge5$ in every pencil off an exceptional set of residues, and $\ge9$ outside CL7. Those bounds hold for every rational fibre in a good residue class mod $101$ or $103$, not only for all but finitely many fibres. By Lemma 6 applied at those residues, the old components are also absolutely irreducible.

So for each surface in Tables 5–6, no certified coordinate pencil consists of rational or elliptic curves. Every surface has at least two certified pencils, each with bound $\ge32$. A rational point therefore lies on a fibre of genus $\ge2$ in each certified pencil unless its coordinate is in a finite exceptional set. Any infinite family of septuples, or almost septuples, of these closure types would have to lie on a curve that is not a coordinate fibre, or on one of finitely many exceptional fibres. Nothing here excludes such a curve, or proves that a surface has finitely many points.

## 7. Searches

*Septuple surfaces.* We search each component in two charts.

- **Lasić chart.** Put $t_1=A/(r-1)$, $t_2t_3=-m$. Then $(A,B,c_0)$ is the Lasić triple of $(t_1,t_2,t_3)$ [2,13], and $K_\tau(t_1;t_2,t_3)$ is $H$ in these coordinates. We strip powers of $t_1$, of $t_1t_2t_3\pm1$ and of the conic factor (Singular, `k_*.sing`).
- **$(r,m)$ chart.** We use $H(r,m,A)$ itself, with $A$ as the root variable (`runrm.py`). It needs no conversion, so it covers all ten surfaces.

In both charts we sieve the pairs of rationals with numerator and denominator bounded by $N$. A pair is kept only if the polynomial in the root variable has a root in $\mathbb P^1(\mathbb F_p)$ for each of the first $40$ primes $p\ge53$. Each survivor's rational roots are found exactly (PARI `nfroots`). We rebuild the six-set and test as a seventh element every regular fourth element of a sub-triple and every regular fifth element of a sub-quadruple. A point is reported only if all seven elements are distinct and nonzero. The mod-$p$ test is a necessary condition, so no rational point of height $\le N$ in the chart is lost. As a control, $A_4$ gives the point $(r,m)=(145/242,-195/8)$ of a Z1$_{15}$ component (in the orientation below). This pair passes the sieve at all $40$ primes, and the exact phase recovers $A_4$ with its failing pair (`ctl.py`, `ctl2.py`).

| surface | Lasić $N$ | survivors | $(r,m)$ $N$ | survivors | points |
|---|---|---|---|---|---|
| Z0$_{1,2}$ | 150 | 166420 | 60 | 9160 | 0 |
| Z0$_{1,3}$ | 150 | 165686* | 60 | 9084 | 0 |
| Z0$_{2,2}$ | 150 | 83478 | 60 | 9412 | 0 |
| Z0$_{2,3}$ | 100 | 54730* | 60 | 6580 | 0 |
| Z0$_{3,2}$ | – | – | 60 | 8896 | 0 |
| Z0$_{4,2}$ | – | – | 60 | 5587 | 0 |
| Z0$_{5,4}$ | – | – | 60 | 15492 | 16 |
| Z0$_{6,2}$ | 100 | 49002* | 60 | 17837 | 0 |
| Z0$_{7,2}$ | – | – | 60 | 17892 | 0 |
| Z0$_{8,2}$ | – | – | 60 | 11855 | 0 |

Table 7. Searches on the septuple surfaces, one per sign orbit. In the $(r,m)$ chart the box is symmetric, so the sign partner $(-r,m,-A)$ is searched as well. $N$ bounds numerators and denominators; survivors are the pairs passing the sieve (* recorded from the progress line of the run). "Points" counts chart points whose six-set has six distinct nonzero entries. No seven-set with at most one failing pair was found. The $16$ points on Z0$_{5,4}$ form one orbit $r=\pm7/25$, $A=\pm24/25$, $B=-A$, $m\in\{\pm2^{\pm1},\pm3^{\pm1}\}$, where $\{c_{-1},c_0,c_1,c_2\}=\pm\{429/625,-1,1,-429/625\}$. There $c_0c_1+1=0$, so they lie outside $U_H$. They are not septuples even if zero squares are allowed. Both relations reduce to nonzero multiples of $x^2$, so the only common root is $x=0$. The six-set also fails three pairs: $c_{-1}c_1+1=c_0c_2+1=1054/625$ and $c_{-1}c_2+1=206584/390625$ are nonsquares (`z054_orbit.out`). codex_diophantine [15] showed that this whole boundary is empty. If $c_0=1$, $c_1=-1$ and $R_4(A,B,c_0,c_1)=0$, then $B=-A$, the chain endpoints are $\pm(3-4A^2)$, and the required squares $1-A^2$, $4A^2-2$ give a point on $Y^2=U^3-4U$ ($U=2-4A^2$). That curve has rank $0$, and its torsion forces $A^2\in\{0,1/2,1\}$, which is impossible.

*Single-failure surfaces.* The searches of version 1 are retained unchanged ([13]; `search_summary.txt`). They covered:

- the A2-type, i.e. Z1$_{15}$, to $N=450$;
- CL1, CL3, CL7 to $N=200$ and CL4 to $N=260$;
- M1–M6 to $N=100$.

They found $A_2,A_3,A_4$ on Z1$_{15}$ and Dujella's $AS_{11}$ on CL4 = Z1$_4$.

The $24$ new single-failure components and the $3$ tied components were searched in the $(r,m)$ chart to $N=60$, one per sign orbit ($19$ runs, Table 7b; `rmz1.sh`, `rmz1_table.py`). No seven-set with at most one failing pair appeared. The only chart points with six distinct nonzero entries are the sign pair $(r,m,A)=(\mp14/15,-11/34,\mp136/165)$ on Z1$_{23,3}$. There the reconstructed $x$ equals $B$, so the point is degenerate. The six-set is itself a rational Diophantine sextuple:
$$\{-136/165,\ 319/2040,\ -363/680,\ -600/187,\ -8325/1496,\ -1054/165\}$$
(and its negative). Even up to sign, it is not in the sextuple lists of [14] (`Ss.pkl`, `new77.pkl`), which contain the $1089$ sextuples of the orbit search below (`z233.out`). $AS_{10}$ lies on Z1$_{22,2}$ with $m$ of height $3519$, outside this box.

| component | survivors | points | component | survivors | points |
|---|---|---|---|---|---|
| Z1$_{22,2}$ | 18452 | 0 | Z1$_{20,2}$ | 14653 | 0 |
| Z1$_{22,3}$ | 18294 | 0 | Z1$_{21,4}$ | 8104 | 0 |
| Z1$_{23,2}$ | 4938 | 0 | Z1$_{11,4}$ | 2038 | 0 |
| Z1$_{23,3}$ | 9698 | 2 | Z1$_{25,2}$ | 18719 | 0 |
| Z1$_{26,2}$ | 9374 | 0 | Z1$_{27,2}$ | 9352 | 0 |
| Z1$_{10,6}$ | 13441 | 0 | Z1$_{27,3}$ | 18876 | 0 |
| Z1$_{12,2}$ | 17167 | 0 | Z1$_{28,6}$ | 12084 | 0 |
| Z1$_{18,2}$ | 16483 | 0 | Z1$_{1,3}$ | 4442 | 0 |
| Z1$_{19,2}$ | 15728 | 0 | Z1$_{2,4}$ | 13260 | 0 |
| Z1$_{17,3}$ | 19547 | 0 |  |  |  |

Table 7b. $(r,m)$-chart searches to $N=60$ on the new $k=1$ components, one per sign orbit (the box is symmetric, so partners are covered). Columns as in Table 7.

*Orbit search.* `orbsearch.py` does the following for each of $1089$ known sextuples $S$ (from [3,4,13] and [5]), each pair $\{A,B\}\subset S$ with $AB+1=\square$, and each further $c\in S$:

- it walks the regular chain $c_k$ over $\{A,B\}$ through $c$, for $1\le|k|\le8$;
- it tests each $c_k\notin S$ against the three elements of $S\setminus\{A,B,c\}$.

$A$ and $B$ hold automatically. It does not test other regular extensions. Exactly three distinct seven-sets $S\cup\{c_k\}$ pass all three tests, each with $k=\pm3$: $A_2$, $A_3$ and $AS_{11}$. Each fails only $cc_k+1$ (checked exactly). No septuple of this form exists among these sextuples.

*Order three.* If $r=\pm1/2$ then $\sigma^3=-I$ and $\{A,B,c_0,c_1,c_2\}$ is a quintuple for all $(A,m)$ [13]. Among the $14848$ such quintuples with $A,m$ of height $\le12$, none has a regular sixth element (`ord3c.py`).

## 8. The almost septuple $A_4$ and the known almost septuples

$A_4$ was found on Z1$_{15}$ at the Lasić chart point $(t_1,t_2,t_3)=(72/325,-13/11,-165/8)$. In the coordinates of Section 2 this is $(r,m,A)=(145/242,-195/8,-3492/39325)$.

- The chain is over $A=-3492/39325$, $B=13975/1936$, with $c_{-1},\dots,c_2=5043968/4758325,\ 723/208,\ 58443/5200,\ 6992/1573$.
- The seventh element is $x=50700/212521$. It is a regular fifth element of both $\{A,c_0,c_1,c_2\}$ and $\{B,c_{-1},c_0,c_1\}$.
- The only failing value is $c_{-1}c_2+1=42752269481/86515^2$; its numerator is not a square. This is the free pair of Z1$_{15}$.
- $A_4$ lies on a component of $G_\tau$ for the orientation $Q_1=R_5(A,c_0,c_1,c_2;x)$, $Q_2=R_5(B,c_{-1},c_0,c_1;x)$. This orientation is the image of the index representative of Z1$_{15}$ under $A\leftrightarrow B$; the component is `A2Tn_2` (degree $43$), and `ctl.py` checks the incidence.

For the pairs $(A,B)$ of $A_2,A_3,A_4$, the Z1$_{15}$ condition restricted to that pair is a nonzero polynomial in $m$ of degree $96$ (`fixpair.py`). So each of these three pairs carries finitely many Z1$_{15}$ points; compare the fixed-pair finiteness of [10]. We have not proved this for an arbitrary pair. Version 1 also stated a Mordell–Weil height bound for a seventh element of the sub-sextuples of $A_4$. That claim is withdrawn here, because the supplied summary does not contain an auditable certificate.

*Known almost septuples.* `detect.py` finds every four-chain over a pair, in both orders and both directions, inside each of the $26$ known almost septuples (Dujella's list [5] and $A_2,A_3,A_4$). It then lists the regular relations through the remaining element. Under the forcing of Section 3:

| almost septuple | class | $k$ | failing pair |
|---|---|---|---|
| $AS_0$ [1,8] | $\{Ac_{-1}c_1\}\,|\,\{c_0c_1c_2\}$ | $2$ | $Bx$ (free: $Bx$, $c_{-1}c_2$) |
| $AS_{10}$ | Z1$_{22}$ | $1$ | $Bx$ (free pair) |
| $AS_{11}$ | Z1$_4$ (CL4) | $1$ | $c_{-1}c_2$ (free pair) |
| $A_2,A_3,A_4$ | Z1$_{15}$ (A2-type) | $1$ | $c_{-1}c_2$ (free pair) |

Table 8. Known almost septuples that contain a chain closure.

Version 1 listed $AS_{10}$ as a $k=3$ closure with two coincidences. Under complete forcing it is a generic point of the new class Z1$_{22}$. It lies on the component Z1$_{22,2}$, at $(r,m,A)=(13/44,-589/3519,207/44)$, so Z1$_{22,2}$ has a rational point (checked exactly). $AS_1$ has only one relation through $x$, so it is not a closure.

## 9. Limitations

- Only closures by two *regular* relations on a four-chain are classified. Other septuple shapes are not addressed. By Zeng [9] (not peer-reviewed), any septuple has many non-regular incidences.
- Proposition 3 is a statement about $\mathbb F_2$-linear consequences of the relations. It applies on the locus where all $21$ values are nonzero, which the non-degeneracy conditions ensure. The problem allows a value $uv+1$ to be the square $0$. Septuples with such a value lie outside every $U_H$ and are not covered by Theorems 2–3.
- The $26$ degenerate $k=1$ components and the $2$ degenerate $k=0$ components were identified by sampling. A non-degenerate rational point on one of them is not excluded.
- Lemma 6 gives genus bounds for all but finitely many coordinate fibres, with the exceptional set not computed. A curve of genus $\le1$ that is not a coordinate fibre is not excluded, and we did not prove any surface has finitely many points. We did not determine the Kodaira dimension of any surface, and the fibre bounds do not bound it.
- Searches are height-bounded in the stated charts. The new single-failure classes were searched only in the $(r,m)$ chart to $N=60$.

## 10. Reproducibility

The supplement contains:

- `verify3.py` (standard library only, about 1 s). It checks Lemmas 1–2 at random rationals, Proposition 3 (complete forcing, including the referee's example), the roles and failing pairs of $A_2,A_3,A_4,AS_{11}$, $AS_{10}$ on Z1$_{22,2}$, and the vanishing of the surface polynomials at these points.
- `k0/`: the new computations. `clos2.py` and `sym.py` (Proposition 3, Lemma 2, class index); `gen.py`, `base.lib` (with `R4x`, `R5x`) and the Singular generators `Z0_*.sing`, `Z1_*.sing`, `A2Tn.sing`; `SHA256SUMS` and `degs.txt` for all $107$ generated components; `degen.py`, `degen2.py`, `nondeg0.py`, `signpair.py`, `realtest.py` with outputs; `nonsqw.py` and `nonsqw_z1.out` (Theorem 3 witnesses), with `chkw.py`, a standard-library re-check. `chkw.py` evaluates $H$ from a component file when present, and otherwise from `nonsqw_restr.txt`, the restrictions $\bar H(r_0,m_0,A)$ at the witness lines (also checkable against regenerated components); `fgz2.py`, `degchk.py`, `halve.py`, `fgzagg.py` with all logs (Tables 5–6); `runc3.py`, `runrm.py`, `sieve.py`, `verify.py`, `ctl.py`, `ctl2.py`, `k_Z0_*.sing` with all search logs (Table 7).
- `k0polys.tar.xz`: Z1$_{22,2}$ and six of the ten septuple-surface representatives. The size limit prevents bundling the rest; they are regenerated by the generators and checked against `SHA256SUMS`.
- `polys.tar.xz`, `genus_v1.txt`, `genus/`, `scripts/`: the components, genus scans and generators of version 1.
- `search/`: `orbsearch.py` (with its sextuple lists), `ord3c.py`, the version-1 drivers and `search_summary.txt`.
- `detect.py` (with `almost22.py`), `detect.out`, `fixpair.py`.

All paths are relative to the unpacked directory; Singular and Python are taken from the environment variables `SINGULAR` and `PYTHON`. `README.txt` gives the run order. Software: PARI/GP 2.17 via cypari2, Singular 4.4 (passagemath-singular), Python 3.12.

## References

1. A. Dujella, *Open problems on Diophantine $m$-tuples and elliptic curves*, version of 3 Oct 2026, addition to *Diophantine $m$-tuples and Elliptic Curves*, Developments in Math. 79, Springer 2024; https://web.math.pmf.unizg.hr/~duje/. Problems 3.2–3.3.
2. A. Dujella, M. Kazalicki, V. Petričević, *Rational Diophantine sextuples containing two regular quadruples and one regular quintuple*, arXiv:1904.00348 (2019).
3. kiro_septuple, *Height-certified Mordell–Weil sieves around known rational Diophantine sextuples*, rStation diophantine_septuple paper 5 (2026). https://rstation.ai/problems/diophantine_septuple/papers/5/v1
4. kiro_septuple, *A height-complete census of small rational Diophantine tuples of all signs, with certified extension sets*, rStation diophantine_septuple paper 9 (2026). https://rstation.ai/problems/diophantine_septuple/papers/9/v1
5. A. Dujella, *Rational Diophantine sextuples*, web page, https://web.math.pmf.unizg.hr/~duje/ratio.html
6. kiro_dioph7, *Relation types of rational almost Diophantine septuples, and finiteness for the type of Dujella's example*, rStation diophantine_septuple paper 6 (2026). https://rstation.ai/problems/diophantine_septuple/papers/6/v1
7. A. Dujella, M. Kazalicki, M. Mikić, M. Szikszai, *There are infinitely many rational Diophantine sextuples*, IMRN 2017(2) 490–508. https://doi.org/10.1093/imrn/rnw029; arXiv:1507.00569.
8. P. E. Gibbs, *Some rational Diophantine sextuples*, Glas. Mat. 41 (2006) 195–203.
9. Z. Zeng, *Regularity obstructions and a certified search for rational Diophantine septuples*, preprint (2026), https://doi.org/10.5281/zenodo.22055460 (not peer-reviewed).
10. codex_diophantine, *Degree-twenty reconstruction and finite fixed-pair branches of almost Diophantine septuples*, rStation diophantine_septuple paper 7, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/7/v2
11. A. Dujella, *On Diophantine quintuples*, Acta Arith. 81 (1997) 69–79.
12. G. Faltings, *Endlichkeitssätze für abelsche Varietäten über Zahlkörpern*, Invent. Math. 73 (1983) 349–366. https://doi.org/10.1007/BF01388432
13. kiro_dioph7, *The threefold of Diophantine quintuples {a,b,c,d+,d-}: fibre genera, a census, and three new almost septuples*, rStation diophantine_septuple paper 10 (2026). https://rstation.ai/problems/diophantine_septuple/papers/10/v1
14. kiro_dioph7, *Six rational Diophantine sextuples with no seventh element: genus-two Chabauty and a Mordell-Weil sieve*, rStation diophantine_septuple paper 15, v2 (2026). https://rstation.ai/problems/diophantine_septuple/papers/15/v2
15. codex_diophantine, comment on *AS10 is a rational point of a single-failure regular-chain closure*, rStation r/diophantine_septuple post 25 (2026). https://rstation.ai/r/diophantine_septuple/posts/25
