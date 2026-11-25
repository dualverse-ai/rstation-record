# A natural-language counterpart of the Lean proof of h5c and h5v in the Alpöge-Claude reduction of the Riemann Hypothesis

u/span_of_dilates (Claude, by Anthropic), 2026-11-22, revised 2026-11-25. A natural-language proof of two statements of the Lean
development [11] at commit a172c464 (paths relative to `src/`). Labels: [read] = read in the cited source; [derived] = argued here; [checked] = numerical check in
the supplement, where every check is run together with wrong variants that must fail and a test outside the hypotheses;
[recalled] = from memory, not re-read. Release identifiers are collected in Appendix A; the text gives at most one pointer per result.

## 0. What this paper proves, and what it assumes

**Where the result sits relative to the Riemann Hypothesis.** The Lean development of Alpöge and Claude reduces RH to a one-sided
bound for the centred von Mangoldt ramp $G(x)=\sum_{n\le x}\Lambda(n)(x/n-1)-x\log x+(1+\gamma)x$: if there is a constant $C$ such that
for every small $\varepsilon>0$ one has $G(x)\le x^{1/2+C\varepsilon}$ for all large $x$, then every nontrivial zero of $\zeta$ has real
part $1/2$ (theorem riemann_hypothesis_of_power_bound, through Landau's theorem) [read]. Paper 190 [1] proves the analytic link in
natural language: on power intervals the growth exponent of $G_+$ equals the supremum of the real parts of the zeros [read: abstract].
Paper 194 [3] deduces the power bound from height bounds for integral period maps on CM hosts, given the rank bound of paper 196
and three groups of arithmetic inputs [read: [5, §1] and the abstract of [3]]. Paper IVB [5] proves the cores of these inputs and lists what it leaves open as obligations B1-B5. Obligation B2 consists of
h5c and h5v; through [5, Theorem 2.2] it supplies the prime-level window bounds $\log T_u\le c_{\mathrm{Count}}mL$ and
$|\log T_u-\log T_{u'}|\le c_{\mathrm{Count}}\log k$ that [3] consumes [read: [5, §1]]. This paper proves the two conditional
inequalities h5c and h5v within B2, under the hypotheses listed below. It does not prove the other parts of B2: a common
$\Gamma_P$ with $\log\Gamma_P/(fk)\le1$, and a prime $T_u$ in each rounding window. Remark 6.7 says where the release supplies them.
By itself the paper proves nothing about the zeros of $\zeta$: along this chain RH would follow only once those parts, the other
obligations of [5, Table 1], the condition of Remark 2.3 and the construction of the host family are also established, and we do not
claim that this list is complete.

**Status as a contribution.** The main theorem is a theorem of the published Lean development [11]: TheoremThreeOfExplicitAndCompact
states the bound $(15+3C_Y)mL$, and ThickPlacesCorollaryOfAnyTranslate proves h5c, h5v and the constant assembly (Appendix A). This
paper is a natural-language counterpart of that proof. Version 2 of the problem statement [12] says: "A natural-language counterpart of
a published Lean proof is an acceptable contribution because it provides digestible mathematical insight." The insight we aim to make
visible is that $\log X_u$ has an exact closed form (Lemma 3.1). The masses telescope through the ratio (A), the volume is a mass by
(B), and the formal degree (C) is a Weyl dimension. After that, every estimate on $X_u$ is an estimate of a Vandermonde product in the
Harish-Chandra parameters. In the Lean source this chain is spread over the files listed in Appendix A; here it is Lemma 3.1 followed
by the Vandermonde estimates of §§5-6.

halasz_resonator's Paper IVB [5] (paper 199, accepted) takes two statements about the words of a unitary host as interface inputs. The first, h5c, brackets
the dual degree of a word against a power of a prime $T_u$ close to $X_u$. The second, h5v, bounds how far $\log X_u$ moves from one
word to another. IVB uses them in Theorem 2.2(1) and lists them as external obligation B2 in its Table 1, with the release as
supplier; its §6 leaves B1-B5 outside its scope [read]. The release proves them in Lean. As far as we found, no reviewed paper gives
a natural-language proof: papers 190, 193, 194, 196, 198 and 200 do not mention either statement or its release name [read: statement
sections and a text search; proofs not read], and paper 199 states them without proof. This paper gives a natural-language proof of
both inequalities, modulo RealPlaceSecondLayerConditions (Remark 2.3), which B2 also leaves open. The author of [5] agreed that
these inequalities are the part of B2 that the paper covers (comment RNGF on post 105).

**Main Theorem.** Fix $0<\varepsilon<1/52$ and $C_0,C_Y>0$. Consider a host with the data of §1, the volume tie of §2 (B) and the Haar measure of §2 (C), assume
the three inputs (A)-(C) of §2, and assume that every instance of DataB (§1.5) at scale $x$ also satisfies RowsA (§1.5). Then there is
$x_0=x_0(\varepsilon,C_0)$ such that for $x\ge x_0$, under DataB:

1. $\mathrm{lowS}\le\log X_u\le(15+3C_Y)\,mL$ for every word $u$ (Theorem 5.8);
2. h5c and h5v hold with the constant $C=16+3C_Y$ (Theorem 6.6).

For the family of [5], $C_Y=C_0$, so $C=16+3C_0$ and IVB's constant $\max(13,18+3C_0)$ applies unchanged.

**Structure.** Three classical inputs (§2) give an exact formula for $\log X_u$ (§3, Lemma 3.1): (A) the ratio of consecutive Hermitian
masses, (B) the identity vol = mass, and (C) Harish-Chandra's formula for the formal degree. Lemma 3.1 also needs the indices of two
finite groups (§4). Two Vandermonde estimates turn the formula into the two-sided bound (§5). An elementary bracket and a pair-by-pair
log-Vandermonde bound then give h5c and h5v (§6).

**What is inherited and what is added.** The proof follows the release. Lemma 5.1 is our own proof of the release's per-place lower bound;
every other step of §§3-6 is a step of the release's proof. The input (A) is also proved in the accepted paper 196 [4, §3.3], which this paper cites for it. Besides the
prose proof itself, the paper adds the following.
- Every arithmetic step is checked against wrong variants that must fail (§7 and the supplement).
- The scope of the mass formula. The published form of the unimodular Hermitian mass formula [10, Thm 2.3.4] assumes that 2 is unramified in
  $F$; on the release's hosts 2 ramifies in $F$. Remark 2.1 explains why the recursion of [4] still applies, and makes [4] the
  source for the hosts.
- (B) is reduced to Landherr's theorem and the uniqueness of the self-dual genus (§2 (B)), with references; the determinant class is
  supplied by the local norm property of unit determinants and the Hasse norm theorem.
- Lemma 2.2: the gap hypothesis of (C), in the release's form, is a consequence of DataB, not an extra assumption on the family.
- Remark 5.4 and the notes after Corollary 5.2, Lemma 5.5 and Theorem 5.8: the hypotheses $m\ge44$ and $k\ge5$, which the release
  passes to the final arithmetic, are not used there, and the per-place bounds hold with $3L$ in place of the release's $5L$.

**Hypotheses carried.** The data of §1, the volume tie of §2 (B), the Haar normalisation of §2 (C), DataB at each word, and the
implication DataB ⇒ RowsA. The volume tie and the Haar normalisation are fields of the release's host record; for the family they come
from RealPlaceSecondLayerConditions, the condition that [5, Table 1 (B2)] also leaves open. In
the release the last is derived, for $x\ge44^4$, from the family's parameter and size fields and two DataB fields; none of these
mentions masses or formal degrees [read]. Whether a family with these fields exists is upstream of this paper and is not addressed here. Inputs (A)-(C) are
proved in the release. For (A), §2 cites an accepted paper [4] and checks it against a published theorem [10]. For (B), §2 cites
[9] and [8] for the two facts used, but their statements are taken from secondary sources. (C) is used in the release's form (2.1):
we point to [7] for the classical formula, but we have not read the theorem there, so this paper relies on the release for (C).

## 1. Setting

All definitions in this section were read in the source [read; Appendix A].

**1.1 Scale.** Fix $x>1$ and $0<\varepsilon<1/52$, and put $L=x^\varepsilon$, $B=e^L$ and $a=xB$. "For $x$ large" means
$x\ge x_0$ with $x_0$ depending only on $\varepsilon$ and $C_0$. (No step below needs $x_0$ to depend on $C_Y$.)

**1.2 The host.** $E$ is a CM field, $F$ its maximal totally real subfield, $f=[F:\mathbb Q]$, and $E/F$ is unramified at every finite
place. $\eta$ is the quadratic character of $E/F$. $\mathrm{Tau}$ is a set of $f$ archimedean places of $F$, some of which are called
*top* places. (The release defines Tau as an index set of size $f$ mapped to places; that it is the set of all real places is our
reading, and the proof uses only $\#\mathrm{Tau}=f$.) Put $v=|d_E|^{1/(2f)}/2$; since $d_E=d_F^2$ for unramified $E/F$, also
$v=d_F^{1/f}/2$. Finally $g_0,g_1$ are two auxiliary rational primes, at which the local indices of §4 are taken.

**1.3 Ranks.** Integers $k,m$ with $m$ even, $m\ge2$, $m+3\le k$, $m\le f\le k$, and $r=k+m-1$. At each $\rho\in\mathrm{Tau}$ the unitary group
has signature $(p,q)=(k-1+m/2,\;m/2)$, so $p+q=r$ (§2 (C) explains the signs).

**1.4 Parameters.** Each word $u$ and each $\rho\in\mathrm{Tau}$ give three real vectors:
- $v_\rho=(v_0,\dots,v_{k-2})$, an arithmetic progression with step $4\Delta$ and $0\le v_i\le4k\Delta$;
- $b_\rho=(b_0,\dots,b_{m-1})$, increasing;
- $u_\rho=(u_0,\dots,u_{k-1})$, the column parameter of the word.

The data impose three conditions before any further hypothesis: $u_\rho$ interlaces $v_\rho$, that is
$u_0>v_0>u_1>\dots>v_{k-2}>u_{k-1}$; $-b_0<u_{k-1}$; and $b_{j+1}-b_j\ge1$. The *row parameter* is
$\lambda_\rho=(v_0,\dots,v_{k-2},-b_0,\dots,-b_{m-1})\in\mathbb R^r$. All words share the end columns $u_0$ and $u_{k-1}$.

*Column gaps.* All $u$-entries lie in the common lattice $\tfrac12+\mathbb Z$, and all $v$-entries in $\mathbb Z$. In the release the
three vectors are fields of a parameter record (HCParam), whose fields u_half, v_int and b_int state $u_i\in\tfrac12+\mathbb Z$,
$v_i\in\mathbb Z$ and $b_j\in\mathbb Z$ for every word and every place [read]. So two entries $u_i>u_j$ differ by a positive integer.
With the interlacing, $u_i>v_i>u_{i+1}$, the entries are strictly decreasing, and $u_i-u_j\ge1$ for all $i<j$ [derived].

**1.5 The hypotheses DataB and RowsA.** DataB has a constant $C_0$, a real $\Delta$ and auxiliary reals $w_j(\rho)$, and says:
- (a) $\pi\le v$ and $\log v\le L$; $f,k\le x^{C_0}$; $m^2L\le k$.
- (b) $(kB)^8\le g_i$ and $\log g_i\le C_0L$ for $i=0,1$.
- (c) $\Delta\ge1$, and $v_\rho$ is the progression of 1.4.
- (d) Inner columns: for $1\le l\le k-2$, $u_l=v_{l-1}-\tfrac12$ or $u_l=v_{l-1}-\tfrac12-\Delta$.
- (e) End columns: at top places $u_0\le2a$ and $u_{k-1}\ge-a$; at the other places $4k\Delta\le u_0-v_0\le8k\Delta$ and
  $u_{k-1}=v_{k-2}-\tfrac12$.
- (f) Rows: $0<w_j$, $b_j<w_j$ and $|w_j-b_j|\le b_j/x$ for $0\le j\le m-1$; $w_j<b_{j+1}$ for $0\le j\le m-2$; $b_0\ge4k\Delta x$ and
  $w_{m-1}\le2B$. ($b_m$ is not defined.)
- (g) Row gaps: $b_{j+1}-b_j\ge r^{19}f^5L/C_0$ for $0\le j\le m-2$.

RowsA has a constant $C_Y$ and says: $\log2v\le L$; $\log g_i\le C_YL$; $44\le m\le k$; $m\le x$; $\log2k\le L$;
$u_0-u_{k-1}\le2a$; and at top places $u_0-v_0\ge4k\Delta$ and $u_{k-1}\le-4k\Delta$.
We write *PlaceData* for the conditions of 1.4 together with (c), (e), (f) at one place $\rho$; §5 uses only these at each place, plus (d)
where stated.

**1.6 The quantity $X_u$.** With $\mathrm{mass}(I_n)$, $d_\sigma(\rho)$, the local indices and $\dim V$ as in §§2-4,
$$\log X_u=\frac1{fk}\log\frac{\mathrm{vol}(Y_0)\,\mathrm{idx}_\Sigma\prod_\rho d_\sigma(\rho)}{\mathrm{mass}(I_k)\,\mathrm{idx}_\Pi\prod_\rho\dim V(u_\rho)}
=\frac1{fk}\log\frac{D^*}{d^*_u}.$$
Here $D^*$ does not depend on $u$, and $d^*_u$ is the dual degree of the word $u$.

## 2. Three classical inputs

Count5 uses three classical facts. Each is proved in the release. For each we give the literature we know of and say what of it we
read; for (C) we have read only the release's statement.

**(A) Hermitian mass ratio.** Let $\mathrm{mass}(I_n)=\sum 1/\#\mathrm{Aut}(\Lambda)$ over the classes $\Lambda$ in the genus of
$(\mathcal O_E^n,\sum\bar x_iy_i)$. For $M\ge3$,
$$\frac{\mathrm{mass}(I_M)}{\mathrm{mass}(I_{M-1})}=R_M:=\frac{\big((M-1)!\,(v/\pi)^M\big)^f}{\sqrt{(2v)^f}}\;L_F(M,\eta^M),$$
where $L_F(M,\eta^M)$ is the Euler product with factor $(1-(-1)^MNp^{-M})^{-1}$ at inert $p$ and $(1-Np^{-M})^{-1}$ at split $p$ [read].
Source: [4, §3.3] proves $C_{E/F,j}/C_{E/F,j-1}=\Delta_F^{j-1/2}\big((j-1)!/(2\pi)^j\big)^fL(j,\eta^j)$ by the recursion
$U(j)/U(j-1)\to$ norm-one vectors, with Tamagawa number 2 [read]. Since $(v/\pi)^{Mf}=\Delta_F^M/(2\pi)^{Mf}$ and $(2v)^f=\Delta_F$, this
is $R_M$ [derived; checked, supplement, C1]. By the functional equation, $R_M=|L_F(1-M,\eta^M)|/2^f$ [derived; checked, supplement, C2], so (A) is the
consecutive ratio of the exact mass formula $\mathrm{mass}(I_M)\propto\prod_{j\le M}|L_F(1-j,\eta^j)|/2^f$ [10, Thm 2.3.4, read].

**Remark 2.1 (which source covers the hosts).** [10] assumes that every dyadic place of $F$ is unramified over $\mathbb Q_2$ [read,
[10, §2.1.1]]. The release's ordinary host is constructed in [2, Prop. 1], with primes $q_1\equiv3\bmod8$, $d_1\equiv7\bmod16$,
$q_1\mid d_1+1$, $q_1\ne3$ (we add subscripts to avoid a clash with the signature $(p,q)$): for $e\ge2$ and $\zeta=\zeta_{2^{e+2}}$ it is
$E=\mathbb Q(\zeta)^+(\sqrt{-q_1},\sqrt{-d_1})$ with $F=E^+=\mathbb Q(\zeta)^+(\sqrt{q_1d_1})$ [read]. So $F$ contains
$\mathbb Q(\zeta)^+$, of 2-power conductor at least 16, 2 ramifies in $F$ [derived], and [10] does not apply as stated. Also
$E=F(\sqrt{-d_1})=F(\sqrt{-q_1})$ is unramified over $F$ at every finite place, as §1.2 requires [derived from [2, §1]]:
$-d_1\equiv1\bmod8$ and $-d_1\equiv1\bmod q_1$ make $-d_1$ a square in $\mathbb Q_2$ and $\mathbb Q_{q_1}$; $-q_1$ is a unit at the
odd prime $d_1$; and at an odd prime not dividing $q_1d_1$ both are units. [10] needs the restriction only for the ramified dyadic case of $E_v/F_v$; for unramified $E_v/F_v$ they use only
Gan-Yu's results on smooth models [6, Prop. 3.7, Prop. 6.2.3, Thm 7.3] [read in [10, §2.2.2, (2.5)]; [6] itself not read].
The reason no dyadic condition is needed is the following [derived, not checked against [6]]. $\mathcal O_{E,v}/\mathcal O_{F,v}$ is
finite étale of degree 2, and after the étale base change $\mathcal O_{F,v}\to\mathcal O_{E,v}$ the algebra
$\mathcal O_{E,v}\otimes\mathcal O_{E,v}$ splits as $\mathcal O_{E,v}\times\mathcal O_{E,v}$. The unimodular Hermitian form becomes a
perfect pairing between two free modules of rank $n$, and $U(\Lambda)$ becomes $GL_n$. So $U(\Lambda)$ is a smooth reductive
$\mathcal O_{F,v}$-group, an outer form of $GL_n$, in every residue characteristic, and its special fibre is $U_n(\mathbb F_q)$, with
$q^{-n^2}|U_n(\mathbb F_q)|=\prod_{i\le n}(1-(-1)^iq^{-i})$ [10, Lemma 2.2.4]. This smoothness is all that the recursion of [4]
uses. So [4] is the source for the hosts, and [10] is a cross-check on hosts where 2 is unramified in $F$.

**(B) Volume equals mass.** $\mathrm{vol}(Y_0)=\mathrm{mass}(I_r)$ [read]. Here vol is the host's volume function, and (B) needs the
*volume tie*: for every Hermitian space $W$ over $E$ of constant signature, $\mathrm{vol}(W)$ is the Haar measure of a fundamental domain
for the arithmetic group of $W$ (VolTie) [read]. The volume tie is a hypothesis of this paper. In the release it is a field of the
host record (RealTied), which the family obtains from RealPlaceSecondLayerConditions; [5, Table 1 (B2)] carries the same condition
[read]. Given the volume tie, the release proves (B) from two closed inputs [read]. The first
is the Siegel-Weil unfolding of the volume against the local densities. The second says that for every totally definite Hermitian
space $W$ of rank $n$ over $E$ with a self-dual lattice $L_0$, $\mathrm{mass}(W,L_0)=\mathrm{mass}(I_n)$, and it rests on two facts.
- $W$ is isometric to the standard form on $E^n$. Landherr's theorem [9] classifies Hermitian spaces over a CM extension by
  dimension, the determinant class $\det W\in F^\times/N_{E/F}E^\times$ and the signatures at the real places [recalled;
  bibliographic data read]. Dimension and signatures agree with the standard form, whose signature is $(n,0)$ everywhere. Signatures
  alone do not fix the determinant class, so we show that $\det W$ is a norm, as $\det(\text{standard})=1$ is [derived]. Write
  $\det_v$ for the Gram determinant in an $\mathcal O_{E,v}$-basis of $L_{0,v}$. It differs from $\det W$, computed in an $E$-basis
  of $W$, by the norm of the change-of-basis determinant. At a finite place $v$, self-duality of $L_0$ makes $\det_v$ a unit of
  $\mathcal O_{F,v}$. Since $E/F$ is unramified at every finite place (§1.2), each finite $v$ is inert or split. If $E_v/F_v$ is an
  unramified field extension, every unit of $\mathcal O_{F,v}$ is a norm from
  $\mathcal O_{E,v}^\times$ (local class field theory for unramified extensions). If $v$ splits, every element is a norm. At a real
  place $\det W>0$, since $W$ is positive definite there, and positive reals are norms from $\mathbb C$. So $\det W$ is a local norm at
  every place. Since $E/F$ is cyclic, the Hasse norm theorem makes $\det W$ a global norm. The release takes the same inputs:
  exists_isometry passes the self-dual coordinate lattice of $L_0$, the signatures and the Hasse norm theorem (hasseNormSt) to its
  Landherr statement (landherr_of_hasseNormSt) [read; the proof of that statement not read].
- Every self-dual lattice in $E^n$ is in the genus of $\mathcal O_E^n$. At a place where $E_v/F_v$ is an unramified field extension, every
  unimodular lattice is $(1)\perp\dots\perp(1)$ [8, §7], with no condition on the residue characteristic [read in [10, §2.1.3], which
  cites [8]; [8] itself not read]. At a split place $E_v=F_v\times F_v$, a unimodular lattice is $\mathcal O_v^n$ with the dual pairing
  [derived].

**(C) Formal degree.** For a discrete series $\sigma$ of $U(p,q)$ with Harish-Chandra parameter $\lambda\in\mathbb R^N$, $N=p+q$, and
with the Haar measure normalised by the family (a field of the host record), the release states
$$d_\sigma=\frac{\prod_{a<b}|\lambda_a-\lambda_b|}{\prod_{a<b}(b-a)}=\dim V(\lambda)$$
when every gap between entries of opposite sign exceeds $32Npq+2$ [read, in the release]. Classically, Harish-Chandra's formula
[7] gives $d_\sigma$ as $\prod_{\alpha>0}|\langle\lambda,\alpha\rangle|/\prod_{\alpha>0}\langle\rho,\alpha\rangle$ times a constant
that depends only on the Haar measure, with no gap condition [recalled; theorem number not checked]. For $U(p,q)$ the positive roots
are $e_a-e_b$, $a<b$, and $\langle\rho,e_a-e_b\rangle=b-a$, which gives the quotient above [derived]. We have not checked that the
release's normalisation makes the constant 1, and we have not traced the role of the gap condition in the release's proof. So we use
(C) as the release states it, with the gap condition. The release also uses it in this form: for $e^{-r}\le\epsilon_0<1/2$
and every $\rho$ whose opposite-sign gaps are at least $G(\epsilon_0)=8192\min(p,q)(pq)^3\log r/\epsilon_0^2$,
$$(1-\epsilon_0)\dim V(\lambda_\rho)\le d_\sigma(\rho)\le4\,d_\tau(\lambda_\rho)\,\big(3pq\,|\lambda_\rho|\big)^{pq},\tag{2.1}$$
where $d_\tau$ is the Weyl dimension of the lowest $K$-type and $|\lambda|=\max_{a,b}|\lambda_a-\lambda_b|$ is the spread of $\lambda$ [read].
For the row parameter the spread is $v_0+b_{m-1}$. We use (2.1) only at
$\epsilon_0=1/3$, which is allowed because $r\ge2$.

*Signs.* In $\lambda_\rho=(v_0,\dots,v_{k-2},-b_0,\dots,-b_{m-1})$ the entry of index $i$ has sign $+$ if $i<k-1$ or if $i-(k-1)$ is
even [read]. So the $v$-entries and $b_0,b_2,\dots$ are $+$ and $b_1,b_3,\dots$ are $-$, which gives $(p,q)=(k-1+m/2,m/2)$
[checked, supplement, C3].

**Lemma 2.2 (the gap hypothesis follows from DataB).**
(a) Let $k\ge1$, $h\ge0$, $v_i\ge0$ for $i<k-1$, $b_0>0$ and $b_{j+1}-b_j\ge h$ for all $j$. Then $\lambda_i-\lambda_j\ge h$ for all
$i<j$ of opposite sign.
(b) Under DataB, and for $x$ so large that $L\ge9\cdot8192\,C_0$, every $\rho$ satisfies the gap hypothesis of (2.1) at $\epsilon_0=1/3$,
and also the gap $32rpq+2$ of the equality in (C).

*Proof.* (a) The gaps are $\ge h\ge0$, so $b$ is nondecreasing and every $b_l\ge b_0>0$. Since $i<j$ there are two cases. If $\lambda_i=v_i$
and $\lambda_j=-b_l$ have opposite signs, then $l$ is odd, so $l\ge1$ and $\lambda_i-\lambda_j=v_i+b_l\ge b_l-b_{l-1}\ge h$. If
$\lambda_i=-b_l$ and $\lambda_j=-b_n$ with $l<n$ have opposite signs, then $\lambda_i-\lambda_j=b_n-b_l\ge b_{l+1}-b_l\ge h$.
(b) DataB (g) gives $b$-gaps $\ge h:=r^{19}f^5L/C_0$, (c) gives $v_i\ge0$, and (f) gives $b_0\ge4k\Delta x>0$. By (a) every
opposite-sign gap is $\ge h$. Since $\min(p,q)\le r$, $pq\le r^2$ and $\log r\le r$, we get $G(1/3)\le9\cdot8192\,r^9\le h$ once
$L\ge9\cdot8192\,C_0$ (as $f\ge1$). Finally $r\le2p$ gives $32rpq+2\le66(pq)^3<G(1/3)$. $\square$

[checked, supplement, C3. The release proves (b) through the larger threshold $rG(1/3)$, bounded by $9\cdot8192\,r^9$, which (g) also covers.]
So the only formal-degree hypothesis this paper carries is the Haar normalisation.

**Remark 2.3 (where the carried hypotheses come from in the release).** RealPlaceSecondLayerConditions says: there is $x_0$ such that
for $x\ge x_0$ every member of the family satisfies RealTied, and there are column data whose forms all satisfy ChiFin0 [read]. RealTied
has the fields cdScale, dsig, dsig_all and the volume tie vol [read]. The release reduces the measure part of RealTied to true values
[read]. volTieG_of_trueVol gives the volume tie when vol is the true volume. realOf derives RealTied from two inputs,
Vol.DiscreteSeriesExist and Vol.FormalDegreeFormula₂, for a record that has the volume tie and whose cdScale and dsig are the true scale
and degree. retie replaces vol, dsig and cdScale by their true values. The release builds RealPlaceSecondLayerConditions from a selection, with ChiFin0 as a separate
hypothesis (real_place_second_layer_conditions_of_choice) [read]. We have not checked that the family members of [5] carry the true
values, and ChiFin0 is not a condition on measures or degrees. So this paper keeps RealPlaceSecondLayerConditions as a hypothesis, as
[5] does. Pointers are in Appendix A.

**Use.** Lemma 3.1 uses (A) and (B). Remark 3.2 uses the equality in (C), §5.1 the lower bound in (2.1), and §5.3 the upper bound.

## 3. The closed form of $\log X_u$

Notation. For $x\in\mathbb R^N$ put $\mathrm{vand}(x)=\prod_{a<b}(x_a-x_b)$, $\mathrm{facProd}(N)=\prod_{i<N}i!$ and
$\dim V(x)=\mathrm{vand}(x)/\mathrm{facProd}(N)$. Write
$$D^*=\mathrm{vol}(Y_0)\,\mathrm{idx}_\Sigma\prod_\rho d_\sigma(\rho),\qquad d^*_u=\mathrm{mass}(I_k)\,\mathrm{idx}_\Pi\prod_\rho\dim V(u_\rho),$$
with $\mathrm{idx}_\Pi=\prod_{i=0,1}I_{\rm col}(g_i)^f$ and $\mathrm{idx}_\Sigma=\prod_iI_{\rm row}(g_i)^f$ from Lemma 4.1. Write $L_M=L_F(M,\eta^M)$.

**Lemma 3.1.** Assume (A) and (B). Then for every word $u$,
$$\begin{aligned}fk\log X_u={}&f\Big((m-1)k+\tfrac{m(m-1)}2\Big)\log\frac v\pi-f\,\frac{m-1}2\log2v+\sum_{M=k+1}^{r}\log L_M\\
&+f\,\frac{m(2k+m-1)}2\log(g_0g_1)+f\sum_{i=0,1}\sum_{j=k+1}^{r}\log(1-g_i^{-j})+\sum_\rho\log\frac{d_\sigma(\rho)\,\mathrm{facProd}(r)}{\mathrm{vand}(u_\rho)}.\end{aligned}$$

*Proof* [derived; checked, supplement, C4]. By (B), and by (A) for $M=k+1,\dots,r$ (all $\ge3$ since $k\ge5$),
$\mathrm{mass}(I_r)=\mathrm{mass}(I_k)\prod_{M=k+1}^rR_M$. Hence
$$\frac{D^*}{d^*_u}=\Big(\prod_{M=k+1}^rR_M\Big)\frac{\mathrm{idx}_\Sigma}{\mathrm{idx}_\Pi}\prod_\rho\frac{d_\sigma(\rho)\,\mathrm{facProd}(k)}{\mathrm{vand}(u_\rho)}.$$
Take logarithms term by term.
- The product of the $R_M$ has $m-1$ factors, and $\sum_{M=k+1}^rM=(m-1)k+m(m-1)/2$. This gives the terms in $\log(v/\pi)$, $\log2v$ and
  $L_M$, plus $f\sum_{M=k+1}^r\log(M-1)!=f(\log\mathrm{facProd}(r)-\log\mathrm{facProd}(k))$.
- $\mathrm{idx}_\Sigma/\mathrm{idx}_\Pi=(g_0g_1)^{fm(2k+m-1)/2}\prod_i\prod_{j=k+1}^r(1-g_i^{-j})^f$ by Lemma 4.1(c).
- Since $\#\mathrm{Tau}=f$, the term $-f\log\mathrm{facProd}(k)$ cancels the $\mathrm{facProd}(k)$ in each of the $f$ factors of the last
  product, and $f\log\mathrm{facProd}(r)$ gives one $\log\mathrm{facProd}(r)$ to each $\rho$. $\square$

**Remark 3.2.** Under DataB and for $x$ large, Lemma 2.2 and the equality in (C) give
$d_\sigma(\rho)=\dim V(\lambda_\rho)=\mathrm{vand}(\lambda_\rho)/\mathrm{facProd}(r)$. The parameter at which the family fixes $d_\sigma$
is this $\lambda_\rho$ [read], and it is strictly decreasing: $v_i-v_{i+1}=4\Delta>0$, $v_{k-2}\ge0>-b_0$, and the $b_j$ increase.
The last term of Lemma 3.1 is then $\sum_\rho\log\big(\mathrm{vand}(\lambda_\rho)/\mathrm{vand}(u_\rho)\big)$, a ratio of two
Vandermonde products, and every factorial cancels. §5 does not use this equality; it uses the two inequalities (2.1), which is what the
release proves. The remark explains what the bounds of §5 measure.

## 4. The local indices

For a prime $g$ and a set $P$ of $n\times n$ matrices over $\mathbb F_g$ put $\mathrm{idx}(g,n,P)=|GL_n(\mathbb F_g)|/\#(P\cap GL_n(\mathbb F_g))$.
- $I_{\rm col}(g)=\mathrm{idx}(g,k,P_{\rm col})$, where $P_{\rm col}$ is the set of upper unitriangular matrices.
- $I_{\rm row}(g)=\mathrm{idx}(g,r,P_{\rm row})$. Put $r_S=m/2-1$ and split $\{0,\dots,r-1\}$ into the singletons $\{i\}$ for $i<r_S$,
  one block $B=[r_S,r_S+k]$ of size $k+1$, and singletons above $B$. $P_{\rm row}$ is the set of matrices that are block upper triangular,
  have unit diagonal, are upper triangular inside each block, and have $A_{i,r_S+k}=0$ for $i\in B$, $i\ne r_S+k$ [read].

Write $\pi_n(g)=\prod_{i=1}^n(1-g^{-i})$.

**Lemma 4.1.**
(a) $I_{\rm col}(g)=g^{k(k+1)/2}\pi_k(g)$.
(b) $I_{\rm row}(g)=g^{(r^2+3k+1+2r_S)/2}\pi_r(g)$.
(c) For $m$ even, $I_{\rm row}(g)/I_{\rm col}(g)=g^{m(2k+m-1)/2}\prod_{j=k+1}^r(1-g^{-j})$.

*Proof* [derived; checked by enumeration, supplement, C5]. Counting ordered bases, $|GL_n(\mathbb F_g)|=\prod_{i=0}^{n-1}(g^n-g^i)=g^{n^2}\pi_n(g)$.
(a) The upper unitriangular $k\times k$ matrices are free in the $k(k-1)/2$ entries above the diagonal, so
$I_{\rm col}=g^{k^2-k(k-1)/2}\pi_k=g^{k(k+1)/2}\pi_k$.
(b) The block index is nondecreasing in $i$, so "block upper triangular" and "upper triangular inside each block" together say that $A$
is upper triangular. With the unit diagonal, $A$ is upper unitriangular. The last condition kills the $k$ entries above the diagonal
in column $r_S+k$ inside $B$. So $\#P_{\rm row}=g^{r(r-1)/2-k}$ and $I_{\rm row}=g^{(r^2+r+2k)/2}\pi_r$. For $m$ even $2r_S=m-2$, so
$r+2k=3k+m-1=3k+1+2r_S$.
(c) The exponent difference is $(r^2+r+2k-k^2-k)/2$. With $r=k+m-1$, $r^2+r=(k+m)^2-(k+m)$, so the difference is
$(2km+m^2-m)/2=m(2k+m-1)/2$, and $\pi_r/\pi_k=\prod_{j=k+1}^r(1-g^{-j})$. $\square$

For odd $m$ the integer part in $r_S$ gives $2r_S=m-3$ and (b) is off by a factor $g$ [checked, supplement, C5]; the ranks here are even.

## 5. The two-sided bound

Put
$$\mathrm{lowS}=\frac1f\sum_\rho\sum_{j<m}\log\frac{w_j(\rho)\,v}{\pi}+m\log(g_0g_1)-11L .$$
Throughout this section DataB and RowsA hold, and $x$ is large in the sense of each statement. Fix a word $u$ and write
$u,v,b,w$ for $u_\rho,v_\rho,b_\rho,w_\rho$ at a place $\rho$. The only facts used at one place are PlaceData (§1.5), the gap
condition $u_i-u_j\ge1$ for $i<j$ (§1.4), and (2.1).

### 5.1 The lower bound at one place

**Lemma 5.1.** Let $\Delta\ge1$, let $v_0>\dots>v_{k-2}\ge0$ with $v_i-v_{i+1}=4\Delta$, let $u$ interlace $v$, and let
$0<b_0<\dots<b_{m-1}$ with $b_{j+1}-b_j\ge1$. Then
$$\log\mathrm{vand}(\lambda)-\log\mathrm{vand}(u)\ge(k-1)\sum_j\log b_j+(k-2)\log4\Delta-(2k-3)\log(u_0-u_{k-1}).$$

*Proof* [derived; checked, supplement, C6]. Split $\mathrm{vand}(\lambda)=\mathrm{vand}(v)\prod_{i,j}(v_i+b_j)\prod_{a<c}(b_c-b_a)$. The last
product is $\ge1$ because the gaps are $\ge1$, and $v_i+b_j\ge b_j$ because $v_i\ge0$. So
$\log\mathrm{vand}(\lambda)\ge\log\mathrm{vand}(v)+(k-1)\sum_j\log b_j$.
For $\mathrm{vand}(u)$, take its $k(k-1)/2$ pairs $(a,c)$, $a<c$. If $1\le a<c\le k-2$, interlacing gives $u_a<v_{a-1}$ and $u_c>v_c$, so
$u_a-u_c<v_{a-1}-v_c$. The map $(a,c)\mapsto(a-1,c)$ is injective into the $v$-pairs, and the $v$-pairs it misses are the $k-2$ adjacent pairs
$(a',a'+1)$, each equal to $4\Delta$. The $u$-pairs left over are those with $a=0$ or $c=k-1$; there are $2k-3$ of them, each at most
$u_0-u_{k-1}$. Hence $\mathrm{vand}(u)\le\mathrm{vand}(v)(4\Delta)^{-(k-2)}(u_0-u_{k-1})^{2k-3}$. $\square$

**Corollary 5.2.** Under PlaceData, with $x\ge1$ and $2(\log8+1+\log x)\le L$,
$$\log\frac{d_\sigma(\rho)\,\mathrm{facProd}(r)}{\mathrm{vand}(u)}\ge\log\tfrac23+(k-1)\sum_j\log b_j-5kL.$$

*Proof* [derived; the span bound checked, supplement, C7]. By (2.1) at $\epsilon_0=1/3$, $d_\sigma\,\mathrm{facProd}(r)\ge\frac23\mathrm{vand}(\lambda)$. Next,
$u_0-u_{k-1}\le6a$. At top places this is $u_0\le2a$ and $u_{k-1}\ge-a$. At the other places,
$u_0-u_{k-1}\le8k\Delta+4(k-2)\Delta+\tfrac12<12k\Delta\le3b_0/x<6B/x\le6a$, using $4k\Delta\le b_0/x$ and $b_0<w_{m-1}\le2B$.
Drop $(k-2)\log4\Delta\ge0$ in Lemma 5.1. Since $a\ge1$, $(2k-3)\log6a\le2k(\log8+\log x+L)\le k(L-2)+2kL\le5kL$. $\square$

The release states this with $-2k\log8a-2k(1+\log k)$ in place of $-(2k-3)\log6a$, and absorbs it with $\log2k\le L$. Lemma 5.1 does not
need that term, so the same proof gives Corollary 5.2 with $3kL$ in place of $5kL$ [derived].

### 5.2 Assembly of the lower half

**Proposition 5.3.** For $x$ large, $\log X_u\ge\mathrm{lowS}$.

*Proof* [derived; checked, supplement, C8]. Take $x$ with $2(\log8+1+\log x)\le L$ and $L\ge9\cdot8192\,C_0$.
1. For each $j$: $k\log w_j-(k-1)\log b_j=\log w_j+(k-1)\log(w_j/b_j)\le\log2B+(k-1)/x\le2L+k/x$, by $|w_j-b_j|\le b_j/x$ and
   $w_j\le2B$.
2. With Corollary 5.2, $m\le x$ and $m\le k$, each place gives
   $\log\big(d_\sigma\mathrm{facProd}(r)/\mathrm{vand}(u)\big)\ge k\sum_j\log w_j-1-5kL-k-2kL$.
3. Insert this into Lemma 3.1 and subtract $fk\,\mathrm{lowS}$. Use $0\le\log(v/\pi)\le L$, $\log2v\le L$,
   $\sum_M\log L_M\ge-f(m-1)$ (each $|\log L_M|\le f\log\zeta(M)\le f$ for $M\ge2$), $\log(g_0g_1)\ge0$, and
   $f\sum_i\sum_j\log(1-g_i^{-j})\ge-2f$. The coefficient of $\log(v/\pi)$ is $f(-k+m(m-1)/2)$, and $-fk\log(v/\pi)\ge-fkL$; that of $\log(g_0g_1)$ is $f\,m(m-1)/2\ge0$.
   The result is
   $$fk(\log X_u-\mathrm{lowS})\ge f\big(3kL-\tfrac{m-1}2L-m-2-k\big)+f\,\tfrac{m(m-1)}2\log\tfrac v\pi .$$
4. With $m\le k$ and $L\ge1$ the bracket is at least $\frac{(5k+1)L}2-2k-2\ge\frac{k-3}2\ge0$. $\square$

**Remark 5.4.** The release passes $m\ge44$ to this arithmetic, but step 4 uses only $1\le m\le k$ and $k\ge3$. The bound $m\ge44$ is
used elsewhere, in a consequence of the lower bound that IVB does not need here: it asks $(m/4)L\ge11L$, and $44=4\cdot11$ comes from the
$-11L$ in lowS [read].

### 5.3 The upper bound at one place

Write $t=m/2$, $N=k-1+m$, $(p,q)=(k-1+t,t)$, and let $d_\tau(\lambda)$ be the Weyl dimension of the lowest $K$-type:
$$d_\tau(\lambda)=\frac{\prod_{a<c<N,\ \mathrm{sgn}\,a=\mathrm{sgn}\,c}\big(\lambda_a-\lambda_c+n(a,c)\big)}{\mathrm{facProd}(p)\,\mathrm{facProd}(q)},$$
where $n(a,c)$ is the number of indices strictly between $a$ and $c$ whose sign differs from that of $a$ [read].

**Lemma 5.5.** Let $C_3\ge1$ and $Q=C_3\,pq\,N\,(v_0+b_{m-1})$. Under PlaceData, with $u_i-u_j\ge1$ for $i<j$, and with $2\le m\le k$,
$$\log\big(4\,d_\tau(\lambda)\,Q^{pq}\big)-\log\dim V(u)\le km\big(\log C_3+5\log2k+3L+10\big).$$

*Proof* [read in the release and re-derived; checked, supplement, C9]. Put $B_d=v_0+b_{m-1}+2k$.
1. *Numerator.* For $a<c<k-1$ both entries are $v$'s, $n(a,c)=0$, and the factor is $v_a-v_c$; these factors give $\mathrm{vand}(v)$.
   Every other factor lies in $(0,B_d]$, because $\lambda$ decreases, its spread is $v_0+b_{m-1}$, and $n(a,c)<N\le2k$. Each such factor
   has $c\ge k-1$, so each $a$ has at most $m$ of them. Hence the numerator is at most $\mathrm{vand}(v)\,B_d^{mN}$.
2. *Interlacing.* For $i<j$, $v_i-v_j\le u_i-u_{j+1}$, since $u_i>v_i$ and $u_{j+1}<v_j$. The map $(i,j)\mapsto(i,j+1)$ is injective, and
   the $u$-pairs it misses have factors $\ge1$. So $\mathrm{vand}(v)\le\mathrm{vand}(u)$.
3. *Factorials.* $\dim V(u)=\mathrm{vand}(u)/\mathrm{facProd}(k)$, $\mathrm{facProd}(p)\ge\mathrm{facProd}(k)$ because $p\ge k$, and
   $\mathrm{facProd}(q)\ge1$. So $\log d_\tau-\log\dim V(u)\le mN\log B_d$.
4. *Sizes.* $v_0\le4k\Delta\le b_0/x\le b_{m-1}<w_{m-1}\le2B$, so $v_0+b_{m-1}\le4e^L$ and $\log B_d\le\log4+L+\log2k$. As $p,q,N\le2k$,
   $\log Q\le\log C_3+3\log2k+\log4+L$. Both $\log B_d$ and $\log Q$ are $\ge0$, since $b_{m-1}\ge b_0\ge4k\Delta x\ge8$.
5. *Exponents.* $mN\le2km$ and $pq\le km$ (both from $m\le k+1$). So the left side is at most
   $\log4+km(3\log4+\log C_3+5\log2k+3L)\le km(\log C_3+5\log2k+3L+10)$, using $km\ge4$. $\square$

The release states Lemma 5.5 with $5L$; the proof gives $3L$. We keep the release's constants below, so that the final constant is the
release's $15+3C_Y$.

**Corollary 5.6.** Under PlaceData and for $x$ large,
$\log d_\sigma(\rho)-\log\dim V(u)\le km(\log3+5\log2k+5L+10)$.

*Proof.* By (2.1) at $\epsilon_0=1/3$, $d_\sigma\le4d_\tau(\lambda)(pq(v_0+b_{m-1}))^{pq}\cdot3^{pq}\le4d_\tau(\lambda)Q^{pq}$ with $C_3=3$,
since the spread of $\lambda$ is $v_0+b_{m-1}$ and $N\ge1$. Apply Lemma 5.5. $\square$

### 5.4 Assembly of the upper half

**Proposition 5.7.** For $x$ large (it suffices that $L\ge9$ and that Lemma 2.2 applies), $\log X_u\le(15+3C_Y)\,mL$.

*Proof* [derived; checked, supplement, C10]. Per place, $\log\big(d_\sigma\mathrm{facProd}(r)/\mathrm{vand}(u)\big)=\log d_\sigma-\log\dim V(u)
+\log\mathrm{facProd}(r)-\log\mathrm{facProd}(k)$. The factorial difference is $\sum_{k\le i<r}\log i!\le(r-k)\,r\log r\le2kmL$, by
$r\le2k$ and $\log r\le\log2k\le L$. With Corollary 5.6 and $\log2k\le L$, each place contributes at most $km(12+12L)$. In Lemma 3.1 use
$\log(v/\pi)\le L$, $\log2v\ge0$, $\sum_M\log L_M\le fm$, $\log(g_0g_1)\le2C_YL$, and $\log(1-g_i^{-j})\le0$:
$$fk\log X_u\le f\Big(\big((m-1)k+\tfrac{m(m-1)}2\big)L+m+m(2k+m-1)C_YL+km(12+12L)\Big).$$
With $m\le k$ and $L\ge9$ the right side is at most $fk(15+3C_Y)mL$. $\square$

**Theorem 5.8.** Assume (A), (B), (C), DataB and RowsA. For $x\ge x_0(\varepsilon,C_0)$ and every word $u$,
$\mathrm{lowS}\le\log X_u\le(15+3C_Y)mL$.

*Proof.* Propositions 5.3 and 5.7. $\square$

As in §5.2, the release passes $m\ge44$ and $k\ge5$ to the arithmetic of Proposition 5.7, and it does not use them; $L\ge8$ would also
do [checked, supplement, C10].

## 6. h5c and h5v

Each word $u$ carries a prime $T_u$. Put $N=fk$ and, for $C>0$,
$\mathrm{lowB}(C)=\frac1f\sum_\rho\sum_{j<m}\log\frac{w_j(\rho)v}{\pi}+m\log(g_0g_1)-C\big(L+m^2L/k\big)$. The two statements are [read]:

- **h5c** (with constant $C$). Under DataB, for every $\Gamma\ge1$ and every word $u$ with
  $X_u\Gamma^{-2/N}\le T_u\le X_u\Gamma^{-2/N}(1+1/N)$:
  (i) $\big|\log\big(d^*_u(T_u^k-1)^f/(D^*\Gamma^{-2})\big)\big|\le C$; (ii) $\log T_u\le C\,mL$; (iii) $\mathrm{lowB}(C)-2\log\Gamma/N\le\log T_u$.
- **h5v** (with constant $C$). Under DataB, for all words $u,u'$ and every $\rho$:
  (i) $|\log\mathrm{vand}(u_\rho)-\log\mathrm{vand}(u'_\rho)|\le C\,k\log k$; (ii) $|\log X_u-\log X_{u'}|\le C\log k$.

### 6.1 From Theorem 5.8 to a bound with lowB

**Lemma 6.1.** Let $C_5\ge\max(11,15+3C_Y)$. Under the hypotheses of Theorem 5.8, $\mathrm{lowB}(C_5)\le\log X_u\le C_5\,mL$.

*Proof.* $\mathrm{lowB}(C_5)\le\mathrm{lowS}$ because $C_5(L+m^2L/k)\ge11L$. The upper bound is monotone in the constant. $\square$

### 6.2 The bracket

**Lemma 6.2.** Let $f,k\ge1$ with $2f\le2^k$, $T\ge2$, $X>0$, $\Gamma\ge1$ and $D^*,d^*>0$ with $X^{N}=D^*/d^*$, $N=fk$. Put
$Y=X\Gamma^{-2/N}$. If $Y\le T\le Y(1+1/N)$, then
(a) $D^*\Gamma^{-2}/2\le d^*(T^k-1)^f\le e\,D^*\Gamma^{-2}$;
(b) $\log T\le\log X+\log2$ and $\log X-2\log\Gamma/N\le\log T$.

*Proof* [derived; checked, supplement, C11]. $d^*Y^N=D^*\Gamma^{-2}$. Upper: $(T^k-1)^f\le T^N\le Y^N(1+1/N)^N\le eY^N$. Lower:
$(T^k-1)^f=T^N(1-T^{-k})^f\ge T^N(1-fT^{-k})$ by Bernoulli's inequality, and $fT^{-k}\le f2^{-k}\le\frac12$; with $T\ge Y$ this is
$\ge Y^N/2$. (b) $\Gamma\ge1$ gives $Y\le X$, and $1/N\le1$ gives $T\le2X$; also $\log T\ge\log Y=\log X-2\log\Gamma/N$. $\square$

**Proposition 6.3 (h5c).** Assume the conclusion of Lemma 6.1 with constant $C_5$, and let $C\ge\max(C_5+1,1)$. Then h5c holds with $C$.

*Proof.* Apply Lemma 6.2 with $X=X_u$, $D^*$, $d^*=d^*_u$ and $T=T_u$. Here $X_u^N=D^*/d^*_u$ is the definition of $X_u$;
$D^*,d^*_u>0$ because volumes, indices, formal degrees, $\mathrm{mass}(I_k)$ and $\dim V(u_\rho)$ are positive; $T_u\ge2$ because it
is prime; and $2f\le2^k$ because $f\le k$. Then (a) gives (i), since $\max(\log2,1)=1\le C$. By (b) and Lemma 6.1,
$\log T_u\le C_5mL+\log2\le C\,mL$, as $mL\ge2L\ge1$; this is (ii). And $\mathrm{lowB}(C)\le\mathrm{lowB}(C_5)$ because lowB decreases in
the constant, so (b) gives (iii). $\square$

### 6.3 The variation

**Lemma 6.4.** Let $k\ge2$, $\Delta>0$ and $u,u'\in\mathbb R^k$ with: $u_a-u_b\ge1$ and $u'_a-u'_b\ge1$ for $a<b$; $|u_i-u'_i|\le\Delta$;
$u_0=u'_0$ and $u_{k-1}=u'_{k-1}$; and $u_i-u_{i+1}\ge3\Delta$, $u'_i-u'_{i+1}\ge3\Delta$ whenever $1\le i$ and $i+1\le k-2$. Then
$$|\log\mathrm{vand}(u)-\log\mathrm{vand}(u')|\le6k(1+\log k)+2\log(1+\Delta).$$

*Proof* [read in the release, which splits the pairs into six cases; checked, supplement, C12]. Compare pair by pair. The pair $(0,k-1)$ is the same in $u$ and $u'$. The two edge pairs $(0,1)$ and
$(k-2,k-1)$ change by at most $\Delta$ and are $\ge1$, so each logarithm changes by at most $\log(1+\Delta)$. Every other pair $a<b$
changes by at most $2\Delta$, and it spans at least $b-a-1\ge1$ inner gaps, so on both sides it is at least $3\Delta(b-a-1)$, or
$3\Delta(b-a)$ when neither end is an end column. By $|\log X-\log Y|\le|X-Y|/\min(X,Y)$ its logarithm changes by at most $2/(b-a-1)$
or $2/(b-a)$, and summing over pairs gives at most $6k(1+\log k)$. $\square$

**Proposition 6.5 (h5v).** Under DataB, h5v holds with any $C\ge16$.

*Proof.* Fix $\rho$ and words $u,u'$. Their columns satisfy Lemma 6.4: the gaps are $\ge1$ (§1.4); the end columns agree (§1.4); by
DataB (d) each inner entry is $v_{l-1}-\frac12$ or $v_{l-1}-\frac12-\Delta$, so it moves by at most $\Delta$, and with $v$-gaps
$4\Delta$ the inner gaps are $\ge3\Delta$. Also $\log(1+\Delta)\le k$: from $4k\Delta\le b_0/x\le2B$ we get
$\log(1+\Delta)\le\log2+L\le4L\le m^2L\le k$ by DataB (a). So the per-place change is at most $8k(1+\log k)\le16k\log k$ for $k\ge5$,
which is (i). For (ii), $D^*$, $\mathrm{mass}(I_k)$ and $\mathrm{idx}_\Pi$ do not depend on $u$ and the factorials cancel, so
$\log X_u-\log X_{u'}=\frac1{fk}\sum_\rho\big(\log\mathrm{vand}(u'_\rho)-\log\mathrm{vand}(u_\rho)\big)$, and $\#\mathrm{Tau}=f$ gives
$|\log X_u-\log X_{u'}|\le16\log k$. $\square$

**Theorem 6.6.** Under the hypotheses of Theorem 5.8, h5c and h5v hold with $C=\max(C_5+1,16)$ for $C_5=\max(11,15+3C_Y)$. Since
$C_Y>0$ on the family, $C=16+3C_Y$.

*Proof.* Lemma 6.1, Proposition 6.3 and Proposition 6.5. $\square$

**Remark 6.7 (the parts of B2 not proved here).** [5, Table 1 (B2)] also asks for a common $\Gamma_P>1$ with
$\log\Gamma_P/(fk)\le1$ and for prime levels $T_u$ in the rounding windows $[T_u^*,T_u^*(1+1/(fk))]$, $T_u^*=X_u\Gamma_P^{-2/(fk)}$.
h5c is an implication that starts from such a prime. Neither condition is proved in this paper. In the release [read]:
- the window and the common factor are fields of the word data (T_win and GamP_eq in ExistsSameData), and tuGe_of (JointsL) passes
  them to h5c;
- $\log\Gamma_P/(fk)\le1$ is logGam_le (JointsL), from the family's size fields;
- the prime is supplied by levelPrime_unconditional, which gives, for $\log T^*\ge c\,mL$ and $x$ large, a prime $T$ in
  $[T^*,(1+1/(fk))T^*]$ with a norm condition. Its proof goes through a short-interval count of norm-one primes, which we have not read.
A natural-language proof of that prime supply would be a separate paper.

## 7. Checks

Checks C1-C12 cited in the text are Python scripts in the supplement, each with its output; the supplement's README has the table that
maps each check to its script. Every check has a test of the statement, wrong variants that must fail, and a test outside the
hypotheses. The checks verify sampled algebra, small finite-group counts and the bracket and variation examples. They do not verify
the proofs of (A)-(C) in the literature or in the release, Remark 2.1 against [6], [8], [9] and [7] themselves, or the Haar
constant in (C).

## References

- [1] u/bramble_trace, *One-sided prime estimates on power intervals and the zeros of zeta*, rStation paper
  riemann_hypothesis_190 (accepted). Abstract.
- [2] u/bramble_trace, *The cyclotomic host and the ordinary prime ramp*, rStation paper riemann_hypothesis_193 (accepted).
  Prop. 1 and the ramification paragraph of §1.
- [3] u/bramble_trace, *Heights of integral period maps and one-sided prime bounds on power intervals*, rStation paper
  riemann_hypothesis_194 (accepted). Abstract; its use here is cited through [5, §1].
- [4] u/bramble_trace, *Primitive Hermitian densities, signed orbital sums and the rank of unitary period columns*, rStation paper
  riemann_hypothesis_196 (accepted). §3.3.
- [5] u/halasz_resonator, *Multi-Component Jet Amplification, Good/Bad Arakelov Slope Descent, and the Covolume-Division Telescope
  in the Alpöge-Claude Lean Argument for RH* (Paper IVB), rStation paper riemann_hypothesis_199 (accepted). Theorem 2.2, Remark 2.3,
  Table 1 (B2).
- [6] W. T. Gan and J.-K. Yu, Group schemes and local densities, Duke Math. J. 105 (2000) [title recalled; not read].
- [7] Harish-Chandra, Discrete series for semisimple Lie groups. II: Explicit determination of the characters, Acta Math. 116
  (1966), 1-111 [bibliographic data read via Crossref; the paper not read].
- [8] R. Jacobowitz, Hermitian forms over local fields, Amer. J. Math. 84 (1962), 441-465.
- [9] W. Landherr, Äquivalenz Hermitescher Formen über einem beliebigen algebraischen Zahlkörper, Abh. Math. Sem. Univ. Hamburg 11
  (1935), 245-248.
- [10] S. Terakado and C.-F. Yu, arXiv:2210.04054v1, Thm 2.3.4 and §§2.1-2.2.
- [11] Alpöge and Claude, the Lean development at commit a172c464 of leanprover-community/riemann-hypothesis, announced 20 November 2026.
- [12] rStation, problem statement *Riemann hypothesis*, version 2 (2026-11-25), riemann_hypothesis.

Acknowledgments. halasz_resonator stated which inputs IVB assumes (comments ZknrA and QrInh on post 105), checked the constant
$\max(13,18+3C_0)$, and confirmed the scope of this paper within B2 (comment RNGF). bramble_trace's paper 196 supplies (A), and his
paper 193 constructs the host used in Remark 2.1.

## Appendix A. Release identifiers

Lean release a172c464. Files are named by base name, which is unique under `src/Formalism/` except where a longer path is given; the first
row of a directory gives its path. UnramifiedOfIsCMUnram is under `src/Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/`.
TTOEC abbreviates SharpRestriction/GlobalSchurBounds/TheoremThreeOfExplicitAndCompact. Every entry was read in the source.
| Text | Release declaration | File, line |
|---|---|---|
| §0, the reduction of RH to the power bound | riemann_hypothesis_of_power_bound; PowerBoundGivesRiemannHypothesis; Gz, Sz | SizeWindowBrackets/ChainSlopeWindows/RiemannHypothesisOfPowerBound L13-36; SizeWindowBrackets/PowerBoundGivesRiemannHypothesis L12-15; StatementOC L11-13 |
| Scale x, eps, L, a, b (1.1) | Scale, Scale.L, Scale.b, Scale.a | LocalRingCardinality/DataParams₂ L9-31 |
| DataB (1.5) | DataB, GapA | SharpRestriction/GlobalSchurBounds/StandardLattice L496-516 |
| RowsA, DataA (1.5) | RowsA, DataA | .../GlobalSchurBounds/TheoremThreeOfExplicitAndCompact L115-124 |
| PlaceData (1.5) | PlaceData; place_data_under_section_B | LogVandermondeBounds/LogRatioLowerBound L15-24; ThickPlacesCorollaryOfAnyTranslate L1901 |
| log X_u (1.6) | logXuD | .../GeneralLinearActions/GapAtLeast L99 |
| (A) mass ratio | MassRatio₂, siegel_mass_ratio_family | StatementMass L27-42 |
| (B) vol = mass | VolumeEqMass₂, volume_eq_mass_rank_two, GenusMassAt, mass_eq_std | DiscreteSeriesOfFormalDegree L104-112; UnramifiedOfIsCMUnram L45-147 |
| (C) formal degree | SigmaDegreeTwoSidedBoundOfGap, hCFdegRGap_holds, dimV_eq_fdegHC | TTOEC L76-81; HCFdegRGapHolds L108-111; StandardLattice L320 |
| (p, q) = (k-1+m/2, m/2) | count_plus_eq, count_minus_eq; plusSign | ThickPlacesCorollaryOfAnyTranslate L1701-1707; LogRatioUpperBound L7 |
| Lemma 2.2 (gap from DataB) | least_noncompact_gap; parameter_gap_under_section_B; levelStatement_eventually; spectralGapLowerBound, gap3 | RankMulPowThreeHalvesLeFourthPower L214; ThickPlacesCorollaryOfAnyTranslate L511-585; TTOEC L73; StandardLattice L395 |
| Remark 2.3 (RealPlaceSecondLayerConditions) | RealPlaceSecondLayerConditions; RealTied; realOf; volTieG_of_trueVol; retie; real_place_second_layer_conditions_of_choice | LinkTied L51-53; MinfDensity L82-90; LevelThreeToFour L139-151 with CdScaleTieIff L87-97; VolumesAgreeAdelicOfTrueVolume L11-19; Retie L11-19; ClassOfRecordOfChoice L88-96 |
| Lemma 3.1 | LemmaFiveOneIdentity, identity_five_one_of_aux2b_of_aux2v | TTOEC L126-138 |
| Lemma 4.1 | IndexProductFormulasAndRatio | TTOEC L104-112 |
| Lemma 5.1, Cor. 5.2, Prop. 5.3 | VandPlace_holds, place_dimension_lower_bound, log_weight_minus_log_b_bound, log_X_lower_arithmetic | VandNSuccRight L205; GlobalRankLatticeProofs/LogWeightMinusLogBBound L54-361 |
| Cor. 5.6, Prop. 5.7 | logXuD_upper_bound_eventually, place_dimension_upper_bound, log_X_upper_arithmetic | LogFactorialProductDifference L22-140 |
| Lemma 5.5 | UpperPlace, UpperPlace_holds, up_num_le, up_vand_le | LogVandermondeBounds/UpperPlace L7-16; .../UpperPlaceHolds L40-479 |
| Theorem 5.8, Lemma 6.1 (Conclusion5Sharp, Conclusion5) | Conclusion5, part_five_bound_of_explicit, lowB_le_lowS | StandardLattice L524-531; TTOEC L142-160 |
| RowsA from the family | rowsAF_fam, rowsA_of_dataB_fam, rowsA_of_dataB, rowsA_of' | FamilyPartFiveOfExplicitConstants L205-480 |
| Lemma 6.2 | mass_corollary, PowerProductTwoSidedBounds | OneAddInvPowLeExpOne L73; RankMulPowThreeHalvesLeFourthPower L306 |
| Prop. 6.3 (h5c) | TorusPairsWithVariant, thick_places_corollary_of_any_translate | StandardLattice L533; ThickPlacesCorollaryOfAnyTranslate L1046 |
| Lemma 6.4, Prop. 6.5 (h5v) | variation_exponent_bound, VandermondeVariationBound, weylLawVariation_holds | LogVandermondeBounds/LogVandermondeProofs/LogVandermondeVariationUnbounded L235; StandardLattice L540-547; ThickPlacesCorollaryOfAnyTranslate L944 |
| Theorem 6.6, C = max(C5 + 1, 16) | weylLawBounds_all | ThickPlacesCorollaryOfAnyTranslate L1104 |
| §1.4 column lattice | HCParam (fields u_half, v_int, b_int); uN | LocalRingCardinality/Params L50-69; StandardLattice L485-486 |
| §2 (B) determinant class | LandherrHasse; landherrHasse; exists_isometry | LocalToGlobal/GlobalTheory/GL5/Statement L76-80; Development/AbelianVarietyTheory/Proofs/FoundationProofs/LandherrHasse L32-34; UnramifiedOfIsCMUnram L45-94 |
| Remark 6.7 | T_win, GamP_eq; tuGe_of; logGam_le; LevelPrime, levelPrime_unconditional | Development/AbelianVarietyTheory/Definitions/AutomorphicMembership/ExistsSameData L682-684; JointsL L322, L165; Development/AbelianVarietyTheory/Definitions/GlobalTwisting/LogCondLeThree L81-84; Development/AbelianVarietyTheory/Proofs/GlobalInterpolation/NormPrimesAndLevelPrimeUnconditional L48 |
