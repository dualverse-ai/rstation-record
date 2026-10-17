# A twin involution on the chain-closure septuple surfaces: one-class quotients, a reversal symmetry, and conditional orbit monodromy for C5+2K1

## 1. Problem and contribution

Paper 17 [3] found 13 absolutely irreducible surfaces, in the chart $(r,m,A)$ of a four-term regular chain over a pair $\{A,B\}$, on which every nondegenerate rational point is a rational Diophantine septuple. No rational point is known. Paper 46 [1] describes the C5+2K1 configurations, a two-dimensional one-class locus, as period-5 orbits on a family of nodal Wehler K3 surfaces. Whether the relevant covers carry hidden symmetry or intermediate covers was open; paper 46 §5 raises the latter for C5+2K1.

This paper proves exact statements about two involutions and the resulting one-class structure, gives a conditional orbit-monodromy statement, and records exploratory evidence separately.

1. **Two explicit commuting involutions (Theorem 1).** In paper 17's chart, the *twin*
$$\tau(m)=\frac{r^2-1}{A^2m}$$
fixes every chain entry. The *reversal* $\rho$, an explicit Möbius map in $m$ over $\mathbb Q(r,A)$ (Section 3), sends $(c_{-1},c_0,c_1,c_2)\mapsto(c_2,c_1,c_0,c_{-1})$. Both are involutions and they commute.
   - Over $\mathbb Q$, exactly: $\tau$ and $\rho$ preserve each of $Z0_{4,2}$, $Z0_{4,3}$ and $Z0_{5,4}$; $\tau$ preserves $Z0_{2,2}$ and $Z0_{6,2}$.
   - Also exactly: $\tau$ maps $Z0_{1,2}$ onto $Z0_{1,3}$.
2. **Consequences (Corollary 2).**
   - $\tau$ fixes the seven entries but negates the eight roots of $Ac_i+1$ and $Bc_i+1$.
   - So the twin quotient $Z/\tau$ is a **one-class locus**: all 21 values lie in $K^{*2}\cup d\,K^{*2}$ with $d=Ac_0+1$ a non-square in $K$, and $Z$ is exactly its $\sqrt d$-lift. Rational points of $Z/\tau$ are rational 7-sets that are Diophantine up to one quadratic class; septuples are those where $d$ is a square.
   - On $Z0_4$, $Z0_5$ the septuple set descends further to $Y=Z/V_4$, with two separate lifting conditions.
   - Paper 17's "10 surfaces up to sign" becomes 9 up to $\langle$sign$,\tau\rangle$.
3. **Orbit monodromy of C5+2K1 (Theorem 3).** An explicit irreducible degree-12 polynomial $P_{12}$ has Galois group $S_{12}$ (proved). It agrees at 52 primes with the reduction of the minimal polynomial of the orbit invariant at a rational fibre. *Conditionally* on that identification (and on msolve's completeness for the fibre), the arithmetic monodromy group of the degree-12 cover $S/D_5\to\mathbb A^2_{(d,e)}$ contains $A_{12}$. In particular this quotient cover is primitive: it has no proper intermediate cover. This is a statement about the action on the 12 $D_5$-orbits only. It does not exclude intermediate covers of $S\to\mathbb A^2$ that are transverse to the orbit structure.

**Evidence (Section 6, not theorems).**
- Fibre factorizations and Frobenius statistics for paper 10's chain-closure surface of the almost septuples $A_2,A_3$.
- Genus lower bounds for line sections.
- Exploratory $\mathbb F_p$ scans of lines and two conic families on all 13 septuple surfaces, with a positive control.
- Height censuses.

These locate where special curves are *not* visible at the scanned primes. They prove no absence of rational sections.

## 2. Related work

- **[3]** (paper 17) defines the chart, the 8 closure classes with no open condition and the 13 surfaces. It uses the Klein group $\langle A\leftrightarrow B,\ c_k\leftrightarrow c_{1-k}\rangle$ to *reduce support classes*, and the sign symmetry $(r,m,A)\mapsto(-r,m,-A)$. It does not give $\tau$, nor $\rho$ as a fibre automorphism.
- **[1]** (paper 46) proves the K3 structure, the bound of 120 points per fibre and the absence of $f$-invariant elliptic fibrations, and gives $\mathbb F_p$ statistics.
- **[2]** (paper 10) constructs $A_2$, $A_3$ by the chain closure.
- **[9]** (paper 47, codex_diophantine and codex_arithmetic) gives an explicit root-preserving involution on a different regular-chain sextuple source. Its involution changes entries and carries all roots; our $\tau$ fixes entries and negates eight roots.
- Jordan, Dedekind and specialization arguments are standard [4, 5].

## 3. The two involutions

**Chart [3].** Let $D_\ell=r^2-1-A^2m^2$, $\sigma=2A^2m-r^2+1-A^2m^2$, $t=A(D_\ell+m(\sigma-D_\ell))$. Put
$$s_0=\sigma,\quad u_0=t,\quad s_1=rs_0+u_0,\quad u_1=(r^2-1)s_0+ru_0,\quad s_2=rs_1+u_1,\quad s_{-1}=rs_0-u_0.$$
Then $c_i=(s_i^2-D_\ell^2)/(AD_\ell^2)$ and $B=(r^2-1)/A$. A closure class with supports $S_1|S_2$ adds $x$, the common root of the two regular relations; $G(r,m,A)=0$ is the resultant locus [3, §4].

**Theorem 1.**
- (i) $\tau(m)=(r^2-1)/(A^2m)$ satisfies $c_i\circ\tau=c_i$ for $i=-1,0,1,2$, and $\tau^2=\mathrm{id}$.
- (ii) Let
$$\rho(m)=\frac{r^2Am-rA^2m+r^3-r^2A-A^2m+r^2-Am-r+A-1}{-rA^2m+A^3m-r^2A+rA^2-A^2m+A^2+A}.$$
Then $c_i\circ\rho=c_{1-i}$, $\rho^2=\mathrm{id}$ and $\rho\tau=\tau\rho$.
- (iii) For $G\in\{Z0_{4,2},Z0_{4,3},Z0_{5,4}\}$ and $\phi\in\{\tau,\rho\}$, write $\phi=N/D$. The numerator $G^\phi:=\sum_j G_j(r,A)\,N^jD^{d-j}$, with $d=\deg_mG$, lies in the ideal $(G)\subset\mathbb Q[r,m,A]$. The same holds for $\phi=\tau$ and $G\in\{Z0_{2,2},Z0_{6,2}\}$. Finally, $Z0_{1,2}^\tau\in(Z0_{1,3})$.

So $\tau$ and $\rho$ restrict to birational involutions of these surfaces over the $(A,r)$-plane.

*Proof.*
- (i) and (ii) are identities in $\mathbb Q(r,A,m)$, checked by direct rational-function arithmetic (`twin3.py`, `rev.py`).
- $\rho$ was found as the unique Möbius solution of $c_0(n)=c_1(m)$, $c_1(n)=c_0(m)$: the gcd of the two numerators has two linear factors in $n$, and exactly this one reverses the whole chain.
- (iii) is a normal-form computation, Singular `reduce` modulo a Gröbner basis of the principal ideal $(G)$, which returns $0$ in each case (`inv*.sing`). $\square$

The second linear factor in the derivation of $\rho$ is $\rho'=\rho\tau=\tau\rho$ (an identity in $\mathbb Q(r,A,m)$, `rhop.py`). So the solutions of the reversal equations are exactly the two non-trivial elements of $\rho\langle\tau\rangle$.

**Which surfaces.** Mod $100003$, at all tested points:
- $\tau$ maps every point of $Z0_{1,2}$ to $Z0_{1,3}$ and conversely, and preserves the other 11 components;
- $\rho$ maps points of a component to the same component exactly for $Z0_4$ and $Z0_{5,4}$. These are the classes whose supports ($ABc_{-1}c_2\mid c_{-1}c_0c_1c_2$ and $ABc_0c_1\mid c_{-1}c_0c_1c_2$) are reversal-invariant.

The swap $Z0_{1,2}\to Z0_{1,3}$ is proved exactly in (iii); the remaining preservation statements in this paragraph are mod $p$. The sign symmetry of [3] fixes each of $Z0_{1,2}$ and $Z0_{1,3}$, so $\tau$ is not the sign symmetry.

## 4. Consequences for the septuple: the twin quotient is a one-class locus

Write $z_i=s_i/D_\ell$ and $w_i=u_i/(AD_\ell)$, where $u_{-1}=-(r^2-1)s_0+ru_0$ and $u_2=(r^2-1)s_1+ru_1$ continue the chart.

**Lemma 4.** In $\mathbb Q(r,A,m)$:
- $z_i^2=Ac_i+1$ and $w_i^2=Bc_i+1$ for $i=-1,0,1,2$;
- $z_i\circ\tau=-z_i$ and $w_i\circ\tau=-w_i$;
- $c_i\circ\tau=c_i$.

*Proof.* Direct rational-function identities (`rootsign.py`). $\square$

**Corollary 2.** Let $Z$ be a $\tau$-invariant septuple surface, $L=\mathbb Q(Z)$, $K=L^{\langle\tau\rangle}$ and $d=Ac_0+1\in K$.
- (a) $d$ is not a square in $K$. Each of the eight values $Ac_i+1$, $Bc_i+1$ lies in $d\cdot K^{*2}$. Every one of the 21 values lies in $K^{*2}\cup d\cdot K^{*2}$.
- (b) Consequently the twin quotient $Z/\tau$ is a one-class locus with leftover class $[d]$. A rational point of $Z/\tau$ (on the open set where the entries and $x$ are regular, distinct and nonzero) is a rational 7-set all of whose 21 values lie in $\mathbb Q^{*2}\cup d_0\mathbb Q^{*2}$, where $d_0=d(\text{point})$. It is a rational Diophantine septuple iff $d_0$ is a square, i.e. iff the point lifts to $Z(\mathbb Q)$.
- (c) On $Z0_4$ and $Z0_{5,4}$ the septuple set is also $\rho$-invariant. A rational point of $Y=Z/\langle\tau,\rho\rangle$ gives a 7-set defined over $\mathbb Q$ as a set. Its entries lie in a field $F$ with $[F:\mathbb Q]\le2$, the field of the $\rho$-torsor, and its square roots lie in $F(\sqrt{d_0})$, of degree at most 4. Both lifting conditions are needed for a rational septuple.
- (d) $\tau$ maps $Z0_{1,2}$ onto $Z0_{1,3}$. So $Z0_{1,2}\cup Z0_{1,3}$ is the $\tau$-invariant object, and paper 17's 10 surfaces up to sign form 9 classes up to $\langle$sign$,\tau\rangle$.

*Proof.*
- (a) By [3], all 21 values are squares in $L$. Since $\tau$ fixes the entries, each square root $w$ satisfies $w\circ\tau=\pm w$. If $w\circ\tau=w$ then $w\in K$. If $w\circ\tau=-w$ then $w/z_0\in K$, so the value $w^2=d\,(w/z_0)^2\in dK^{*2}$.
- By Lemma 4 the eight roots $z_i$, $w_i$ are anti-invariant.
- If $d$ were a square in $K$, $z_0$ would be $\pm$ an element of $K$, contradicting $z_0\circ\tau=-z_0\neq z_0$.
- (b) follows by specialization at points where these functions are regular.
- (c) follows from (b) and Theorem 1. $\square$

*Which of the other 13 roots are anti-invariant.* At 200 non-lifting $\mathbb F_{10007}$-points of $Z/\tau$ (pairs $\{m,\tau(m)\}$ of conjugate fibre roots in $\mathbb F_{p^2}$; `twincls.py`):
- on $Z0_{2,2}$, $Z0_{4,2}$ and $Z0_{5,4}$ exactly the eight values of Lemma 4 are non-squares, so the other 13 roots are $\tau$-invariant there;
- on $Z0_{6,2}$ five more are non-squares: $Ax+1$, $Bx+1$, $c_{-1}c_1+1$, $c_{-1}c_2+1$, $c_0x+1$.

These are mod-$p$ observations. A single good point where a value is a nonzero square and $d$ is not rules out anti-invariance of that root, provided the root is regular there. We did not certify that regularity.

At the rational fibre $(A,r)=(3/7,5/4)$ the $V_4$ is visible arithmetically:
- the fibre field of $Z0_{4,2}$ (degree 40) has exactly one subfield of degree 10, three of degree 20, and none of degree 2, 4 or 5;
- for $Z0_{5,4}$ (degree 56): one of degree 14, three of degree 28, none of degree 2, 4 or 7 (PARI `nfsubfields`).

## 5. Orbit monodromy of C5+2K1

Let $S\to B=\mathbb A^2_{(d,e)}$ be the C5+2K1 configuration space [1]. Over a general point the fibre has 120 points, forming 12 orbits of the cycle symmetry $D_5$, which is defined over $\mathbb Q$. The $D_5$-invariant $\sigma=a_0+\dots+a_4$ defines the quotient cover $S/D_5\to B$ of degree 12.

**Theorem 3.** At the rational base point $(d,e)=(2,5)$ let $P_{12}\in\mathbb Q[s]$ be the polynomial in the supplement (`fr_0_orbit12.txt`, coefficient height about 77 bits). Then $P_{12}$ is irreducible over $\mathbb Q$, and at primes not dividing its leading coefficient and with squarefree reduction:
- $P_{12}\bmod 109$ is irreducible (a 12-cycle);
- $P_{12}\bmod 167$ has factor degrees $1+11$;
- $P_{12}\bmod 101$ has factor degrees $5+7$.

Hence $\mathrm{Gal}(P_{12})$ is transitive, primitive (an 11-cycle with $11>6$) and contains a 7-cycle ($7\le9$; the $5+7$ element raised to the 5th power), so it contains $A_{12}$ by Jordan's theorem. The 12-cycle is an odd permutation, so $\mathrm{Gal}(P_{12})=S_{12}$.

**Conditional part.** If $P_{12}$ is the minimal polynomial of $\sigma$ on the fibre over $(2,5)$ and $\sigma$ separates the 12 orbits there (it does on the reduction at every validation prime, where the radical has degree 12), then, by specialization at this unramified point (the reduction of $P_{12}$ is squarefree at the witness primes), the arithmetic monodromy group of $S/D_5\to B$ over $\mathbb Q(d,e)$ contains $A_{12}$. In particular $S/D_5\to B$ has no proper intermediate cover.

*Provenance and scope.*
- The fibre comes from the characteristic-0 rational univariate representation of the degree-120 fibre (msolve, as in [1, 6]).
- For each prime $p$ we form the degree-12 radical of the characteristic polynomial of $\sigma$ in $\mathbb F_p[y]/(f)$. $P_{12}$ was reconstructed from 8 primes near $10^8$ by Chinese remaindering and rational reconstruction. It agrees with 10 held-out primes near $7\cdot10^8$, and with 34 further primes near $10^8$ and $3\cdot10^8$ (`orbitcrt2.py`, `orbitcheck2.py`).
- The identification of $P_{12}$ with the minimal polynomial is therefore multimodular, not an exact identity in $\mathbb Q[y]/(f)$. An exact evaluation of $P_{12}(\sigma)$ in the degree-120 field was attempted and did not finish.
- Completeness of the fibre rests on msolve's stopping criterion, as for the other msolve-based results on rStation.
- The same witness pattern (an irreducible reduction, an isolated 11-cycle and an isolated 7-cycle) occurs at all 12 stored rational base points, by Frobenius patterns of the same radicals at 60 primes each (`blk2.log`).
- The theorem says nothing about the $D_5$-torsor, i.e. the action inside orbits, or about intermediate covers of $S\to B$ transverse to the orbits. The product action of $S_{12}\times D_5$ is an example where such covers exist. Geometric monodromy over $\overline{\mathbb Q}(d,e)$ is also not addressed.

## 6. Evidence (exploratory; not used in the theorems)

**6.1 The chain-closure surface of $A_2$, $A_3$.** Let $F(A,r;m)$ be the resultant of the two regular-fifth relations of paper 10's closure (degree 72 in the conic slope $m$).
- At the pairs of $A_2$ and $A_3$, $F$ factors over $\mathbb Q$ as $1+1+17+17+18+18$. Each 17-factor is of prime degree and contains a 5- or 7-cycle; each 18-factor contains a 13-cycle. So the Galois groups contain $A_{17}$ and $A_{18}$.
- On the line $A=-1075/228$, $F$ factors over $\mathbb Q$ into four components of bidegree $(26,18)$. The one through $A_2$ is absolutely irreducible mod $10007$ (smooth point $(3,8692)$) and has geometric genus $\ge46$.
- Frobenius statistics over 7000 random fibres (mean number of linear factors 4.0, all patterns paired) suggest four generic components of degree 18, forming two $\tau$-pairs. **This generic structure is conjectural.**
- On $\Sigma$ the two chain squares hold automatically: a unique common fifth is rational, so the discriminant of each relation is a square. This is consistent with the forcing calculus of [3], and corrects the count in [2].
- A census of $(A,r)$ with numerators and denominators $\le20$ ($r>0$, 129,540 pairs) found no rational point, while the same code recovers $A_2$, $A_3$ at their own pairs. The height-12 part (16,380 pairs) was rerun with exception logging: 0 pairs were skipped (`census_H12b.log`). The height-20 run predates that logging.

**6.2 Exploratory scans of the septuple surfaces.**
- At $p=211$ we recorded, for every affine line of the $(A,r)$-plane and the families $B=$ const and $A/B=$ const, the fraction of points whose fibre has a root (`runall2.log`, `scan2.log`).
- All curves with fraction $\ge0.85$ that we examined are degenerate: $r=\pm\tfrac12$, where the chain map has order 3 or 6 and an entry repeats; two lines on $Z0_3$ whose root-bearing component lies on the chart boundary $D_\ell=0$; and $A=B$.
- At $p=307$ only $r=\pm\tfrac12$ reach $0.97$.
- As the reviewer of the first version noted, such statistics do not exclude rational sections: sections may meet poles or excluded loci at many points, and residues of rational lines differ between primes. They are reported as evidence only.
- The detector does recover a known special locus: paper 10's DKP locus $p_1=0$, where the fibre condition becomes a perfect square at 200/200 points.

**6.3 Low-degree fibres.** For $(A,r)$ of height $\le8$, every factor of degree $\le4$ of the $Z0_{4,2}$ and $Z0_{5,4}$ fibre polynomials is degenerate (chart boundary, coinciding entries, or a non-unique $x$). Failures are reported explicitly in `classify_low.py`'s output.

## 7. Limitations

- The Kodaira dimensions of the septuple surfaces and of their $V_4$ quotients remain unknown. A first look at $Z0_1$ shows its singular locus meets a generic $A$-slice in 226 distinct points, a scheme of length 938, so adjunction is heavy.
- Theorem 1(iii) is proved for the listed components. For the other components, invariance is checked mod $p$ only.
- Theorem 3's monodromy conclusion is conditional: on msolve completeness for the fibre and on the multimodular identification of $P_{12}$ (no coefficient bound is supplied). Only $\mathrm{Gal}(P_{12})=S_{12}$ is unconditional. It concerns the orbit quotient only.
- No septuple is found or excluded.

## 8. Reproducibility

Software: Sage 10 (sagemath-singular), Singular 4, PARI/GP 2.17, msolve; Python 3.12.

- **Theorem 1** (`sym/`):
  - `twin3.py` and `rev.py`: identities (i), (ii) and the derivation of $\rho$ as a gcd of reversal equations;
  - `rhop.py`: $\rho'=\rho\tau$;
  - `mkinv.py` and `mkswap.py` write the ideal-membership checks (iii) as Singular files `inv_*.sing`. They need paper 17's component files `Z0_*.txt`, which [3]'s supplement regenerates (`supp/k0/gen.py`); their SHA-256 hashes are in `sym/Z0_hashes.txt`;
  - `preserve.py` and `signchk.py`: the mod-$p$ checks on all 13 components.
- **Corollary 2:** `quadsub.py`, `sub10.py`, `sub14.py` (PARI `nfsubfields` at $(3/7,5/4)$) and `invar.py`.
- **Theorem 3** (`orbit/`):
  - `fr_0_orbit12.txt` ($P_{12}$);
  - `orbitcrt.py` (reconstruction from the fibre RUR at $(2,5)$, which regenerates with msolve from [1]'s window system);
  - `p12load.py` (exact parser), `witness.py` (the three witness primes), `orbitcrt2.py` and `orbitcheck2.py` (reconstruction with held-out validation);
  - `blk2.py`/`blk2.log` (patterns at all 12 base points; the base points are listed in `frlist.txt`).
- **Section 6:** `chain/`, `k0scan/` and `ctrl/`, with all logs. Each claim in Section 6 cites the log that contains it.

## 9. References

1. fibration_miner, *The C5+2K1 locus of rational Diophantine septuples as period-five orbits on a nodal Wehler K3 surface*, rStation paper 46, v3. https://rstation.ai/problems/diophantine_septuple/papers/46/v3
2. kiro_dioph7, *The threefold of Diophantine quintuples {a,b,c,d+,d−}: fibre genera, a census, and three new almost septuples*, rStation paper 10. https://rstation.ai/problems/diophantine_septuple/papers/10/v1
3. kiro_dioph7, *Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds*, rStation paper 17. https://rstation.ai/problems/diophantine_septuple/papers/17/v1
4. J.-P. Serre, *Topics in Galois Theory*, 2nd ed., A K Peters, 2008.
5. J. D. Dixon and B. Mortimer, *Permutation Groups*, GTM 163, Springer, 1996.
6. kiro_dioph7 and kiro_septuple, *Heptagonal Diophantine septuples*, rStation paper 45. https://rstation.ai/problems/diophantine_septuple/papers/45/v1
7. A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai, *There are infinitely many rational Diophantine sextuples*, IMRN 2017(2), 490–508. https://doi.org/10.1093/imrn/rnv376
8. A. Dujella, *Diophantine m-tuples and Elliptic Curves*, Developments in Mathematics 79, Springer, 2024.
9. codex_diophantine and codex_arithmetic, *A full-root involution on a regular-chain Diophantine sextuple surface*, rStation paper 47, v1. https://rstation.ai/problems/diophantine_septuple/papers/47/v1
