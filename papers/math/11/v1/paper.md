# Exact phase diagrams for a configuration-dependent optical tangent model

**Athanor lab (Aleksei Kudriashov with AI research agents)**

## 1. Definition and scope

Let \(n\ge2\), \(r=n-1\), and
\(B_n=\{(i/r,j/r):0\le i,j<n\}\). Every selected site has fixed weight
\(1/n^2\), regardless of the size of the selected set. Fix \(s=1/4\).
The motivating smooth optical index and metric are

\[
\Phi_S(x)=\frac1{n^2}\sum_{z\in S}(s^2+|x-z|^2)^{-1/2},\qquad
\eta_{S,\mu}=1+\mu\Phi_S,\qquad
g_{S,\mu}=\eta_{S,\mu}^2(dx^2+dy^2).
\tag{1}
\]

The finite problem studied here is defined directly as follows. Write a
flat-collinear triple in integer coordinates as \(e=(A,B,C)\), with
\(B\) strictly between \(A,C\). For an integer source site \(Z\), put

\[
D=C-A,\quad Q=D\cdot D,\quad H=\det(D,Z-A),\quad
t=\frac{(B-A)\cdot D}{Q},\quad m_P=r^2+16|P-Z|^2,
\]

and define

\[
a_{e,Z}=\frac{4H}{n^2(r^2Q+16H^2)}
\left[\sqrt{Qm_B}-(1-t)\sqrt{Qm_A}-t\sqrt{Qm_C}\right].
\tag{2}
\]

Set

\[
A_e(S)=\sum_{Z/r\in S}a_{e,Z},\qquad
M(S)=\min_{e/r\subseteq S}|A_e(S)|,\qquad \min\varnothing=+\infty.
\tag{3}
\]

For \(\lambda>0\), **tangent legality** means \(M(S)>\lambda\);
equality is forbidden. All three-element subsets of longer flat lines
are included. All occupied sources contribute. Non-collinear base triples
impose no tangent constraint. Reversing the endpoints changes only the
sign of (2).

The cardinality frontier and capacity are

\[
\Lambda_{n,k}=\max_{|S|=k}M(S),\qquad
C_n(\lambda)=\max\{k:\Lambda_{n,k}>\lambda\}.
\tag{4}
\]

The capacity identity follows by finite attainment; it assumes no
hereditary property. This is a separately defined finite model, not
an equivalent formulation of ordinary planar no-three-in-line. The kernel,
softening and normalization are modeling choices, not a claim about a
physical gravitational or particle theory. The softened radial kernel is
Plummer-type [1]. Optical metrics and lensing supply the geometric
background [2,3]. Geva and Steinberg [4] previously connected ordinary
geometric no-three sets with a rotating metamaterial/scatterer-array design;
their coupled-scatterer construction and near-collinearity discussion are
not the endpoint-fixed scalar-potential tangent predicate defined here.

The reductions and limit statements below are proved. The finite phase
diagrams are exactly checked by two code implementations written by one
author and by an external replay. A quantitative certificate at a specified
positive field strength is not claimed.

## 2. Endpoint-fixed variation

**Proposition 1.** Work in the sufficiently small-field simple-disk regime
established in Section 6. Let \(\gamma^S_\mu:[0,1]\to D\) be the unique
geodesic segment from physical sites \(a\) to \(c\), with fixed endpoints,
smoothly parameterized so that \(\gamma^S_0(u)=a+ud\), where
\(d=c-a\) and \(u\in[0,1]\). Put
\[
 V_S(u)=\left.\partial_\mu\gamma^S_\mu(u)\right|_{\mu=0},\qquad
 U_S(u)=\Pi V_S(u),
\]
where \(\Pi\) is orthogonal projection to \(d^\perp\). If
\(\nu=(-d_2,d_1)/|d|\) is the signed unit normal, then the signed normal
component \(\nu\cdot U_S(t)\), at a flat middle site \(b=a+td\), equals
\(A_e(S)\).

**Proof.** Write \(L=|d|\), and define

\[
w_z=\Pi(z-a),\qquad \rho_z^2=s^2+|w_z|^2,\qquad
R_z(u)=\sqrt{s^2+|a+ud-z|^2}.
\]

Linearizing the Euler–Lagrange equation of optical length
\(\int\eta_{S,\mu}(\gamma)|\gamma'|\,du\) gives the transverse
Dirichlet problem

\[
U_S''(u)=L^2\Pi\nabla\Phi_S(a+ud),\qquad U_S(0)=U_S(1)=0.
\]

Since \(R_z''=L^2\rho_z^2/R_z^3\) and
\(\Pi\nabla(R_z^{-1})=w_z/R_z^3\), its unique solution is

\[
U_S(u)=\frac1{n^2}\sum_{z\in S}\frac{w_z}{\rho_z^2}
\left[R_z(u)-(1-u)R_z(0)-uR_z(1)\right].
\tag{5}
\]

In integer coordinates, the signed normal component of \(w_z\) is
\(H/(r\sqrt Q)\), while
\(\rho_z^2=1/16+H^2/(r^2Q)\) and
\(R_z(P)=\sqrt{m_P}/(4r)\). Substitution at \(u=t\) gives (2).
Taking the scalar product with the signed unit normal \(\nu\) gives (2),
including its sign and normalization. ∎

Sources on the entire chord line have \(H=0\) and zero coefficient.
Sources reflected across that line have opposite coefficients. These
identities supply exact controls and explain why symmetry can preserve
forbidden triples even in a nonzero field.

## 3. Exact phase diagrams

Put \(\alpha_k=\Lambda_{3,k}\) and
\(\beta_k=\Lambda_{4,k}\). Site \((i,j)\) has id \(i+nj\);
bit id in a mask records occupancy. The finite frontiers are below.
Decimals are displays only; Appendix A gives exact values.

| Board | k | Frontier, approximately | Attaining masks | First mask | One limiting triple (ids) |
|---|---:|---:|---:|---:|---|
| 3×3 | 7 | 0.0575796798335884 | 4 | 239 | (0,1,2) |
| 3×3 | 8 | 0.0667629070524643 | 1 | 495 | (0,1,2) |
| 3×3 | 9 | 0 | 1 | 511 | (0,4,8) |
| 4×4 | 9 | 0.0417420067019457 | 8 | 7021 | (3,6,9) |
| 4×4 | 10 | 0.0398425656651011 | 8 | 46539 | (7,10,13) |
| 4×4 | 11 | 0.0285647351014218 | 8 | 8125 | (2,5,8) |
| 4×4 | 12 | 0.0285070584749398 | 1 | 63903 | (0,1,2) |
| 4×4 | 13 | 0.00885210669560640 | 8 | 28667 | (0,5,10) |
| 4×4 | 14 | 0.00960923986205918 | 4 | 28671 | (0,5,10) |
| 4×4 | 15 | 0.00448678801328113 | 8 | 49151 | (0,5,10) |
| 4×4 | 16 | 0 | 1 | 65535 | (0,5,10) |

The remaining frontiers are infinite: \(k\le6\) for \(n=3\), and
\(k\le8\) for \(n=4\). Infinite frontiers are witnessed precisely by
ordinary planar no-three sets. The census gives respectively 2 and 11
such sets at sizes 6 and 8; the row bound proves these planar maxima.

**Result 2 (exactly checked).** The complete capacity functions are

\[
C_3(\lambda)=
\begin{cases}8,&0<\lambda<\alpha_8,\\6,&\lambda\ge\alpha_8,\end{cases}
\]

and

| Interval for λ | C₄(λ) |
|---|---:|
| \((0,\beta_{15})\) | 15 |
| \([\beta_{15},\beta_{14})\) | 14 |
| \([\beta_{14},\beta_{12})\) | 12 |
| \([\beta_{12},\beta_{11})\) | 11 |
| \([\beta_{11},\beta_{10})\) | 10 |
| \([\beta_{10},\beta_9)\) | 9 |
| \([\beta_9,+\infty)\) | 8 |

The exact comparison order is
\(0<\beta_{15}<\beta_{13}<\beta_{14}<\beta_{12}<\beta_{11}
<\beta_{10}<\beta_9\). Thus sizes 7 and 13 never occur as capacities
on the respective boards. In particular,
\(\alpha_8>\alpha_7\) and \(\beta_{14}>\beta_{13}\): frontiers
need not decrease with cardinality. Capacity is nonincreasing in resolution,
directly from the predicate. The capacity-11 interval has positive width
\(\beta_{11}-\beta_{12}\approx0.00005767662648194\).

The unique \(\alpha_8\) attainer is the 3×3 perimeter; the unique
\(\beta_{12}\) attainer is the 4×4 perimeter. The eight
\(\beta_{15}\) attainers delete one site off both main diagonals. The
four \(\beta_{14}\) attainers delete the two corners of one side.
These descriptions follow from the saved masks, without symmetry reduction.

Frontier multiplicities differ from the number of legal sets attaining
capacity at a specified resolution. Complete histograms of \(M(S)\)
give the latter by summing counts at size \(C_n(\lambda)\) with
\(M>\lambda\). For example:

| λ | 3×3 capacity | Number attaining it | 4×4 capacity | Number attaining it |
|---|---:|---:|---:|---:|
| 1/100 | 8 | 9 | 12 | 202 |
| 1/20 | 8 | 1 | 8 | 31 |

There are 6 intervals of constant capacity and maximizing-set count for
\(n=3\), and 69 for \(n=4\). Reaching planar capacity therefore does
not necessarily mean that only planar configurations remain legal.

## 4. Exhaustion and exact comparisons

Each coefficient (2) is a rational linear combination of square roots of
squarefree positive integers. Combining identical radicals and clearing
denominators represents responses by integer vectors. The complete
coefficient matrices use 9 basis elements and denominator 13770 for
\(n=3\), and 15 elements and denominator 75283527600 for \(n=4\).

Equality is canonical vector equality. To compare unequal expressions,
enclose each \(\sqrt d\) by rational intervals obtained from
\(\lfloor\sqrt{dq^2}\rfloor/q\), using integer square roots; sign
changes swap interval endpoints. Refine intervals for the exact difference
until zero is excluded. This terminates: in a multiquadratic extension,
the independent sign changes of the prime square roots act on distinct
squarefree radicals by distinct characters. Averaging a rational relation
against each character proves their linear independence. A nonzero
canonical expression is nonzero, while its enclosure width tends to zero.
Floating-point tolerance is never used to certify equality or order.

The producer visits every mask in Gray order and evaluates every selected
triple, without pruning or symmetry quotient. The checker reconstructs
the projection formula (5) at rational physical sites, generates triples
by endpoints and interior sites, and visits all supersets of each triple
in binary order. It imports no producer code and uses decimal rather than
binary rational square-root enclosures. Both programs were written by Sol:
this is separate-code replay, not independent authorship or formal proof
assistant verification.

| Exactly checked item | n=3 | n=4 |
|---|---:|---:|
| Configurations | 512 | 65,536 |
| Flat triples | 8 | 44 |
| Single-source coefficients | 72 | 704 |
| Selected-triple evaluations | 512 | 360,448 |
| Distinct finite M(S), including zero | 29 | 1,986 |
| Chord-source zero checks | 24 | 172 |
| Reflection cancellation checks | 48 | 420 |
| Dihedral mask checks after enumeration | 4,096 | 524,288 |

Every cardinality count agrees with \(\binom{n^2}{k}\). The replay
checks all minima and limiting triples, frontier attainers, histograms and
strict interval boundaries. A separate Pell-identity test forces adaptive
comparison refinement; the production comparisons required no refinement
beyond their initial enclosures. The mathematical reduction plus exhaustive
evaluation establishes the finite results, subject to the usual executable
certificate audit.

## 5. Failure of heredity

**Proposition 3.** Legality is not hereditary, even on \(B_3\).

**Proof.** Take \(\lambda=1/100\), and put

\[
T=\{(0,1/2),(1/2,1/2),(1,1/2)\},\qquad S=T\cup\{(0,1)\}.
\]

The only selected flat triple in \(S\) is \(T\). Formula (2) gives

\[
M(T)=0,\qquad M(S)=\frac{\sqrt5+\sqrt{21}-6}{45}
>\frac7{450}>\frac1{100}.
\]

The strict bound uses \(\sqrt5>11/5\), \(\sqrt{21}>9/2\), each
verified by rational squaring. Thus deleting the upper source destroys
legality. Adding \((0,0)\) instead restores reflection symmetry about
the chord, making its response zero and again destroying legality. ∎

Consequently the legal sets cannot be the independent sets of a fixed
hypergraph on the board. Finite exhaustive optimization remains possible;
only pruning that assumes illegal sets have illegal supersets is invalid.

## 6. Two weak-field limits

For the smooth interpretation, restrict (1) to the closed Euclidean disk
\(D\) of radius 2 centered at \((1/2,1/2)\). For fixed \(n\), the potentials
are smooth and bounded in \(C^2\), uniformly over the finite family of
configurations. Simple metrics form a \(C^2\)-open set, and the Euclidean
disk is simple; see [5, §6] and [6]. Hence all these metrics are simple for
sufficiently small positive \(\mu\). Each endpoint pair then has a
unique geodesic segment in the disk, depending smoothly on \(\mu\).

In this regime, declare a smooth triple forbidden if the Euclidean distance
of one site to the segment joining the other two is at most
\(\varepsilon\), for any of the three endpoint choices. This specifies
segments and a resolution; it does not count arbitrary rays or extra
geodesics in a stronger-field lens.

**Proposition 4 (qualitative transfer).** Fix \(n\) and \(\lambda>0\)
unequal to every finite configuration margin \(M(S)\). With
\(\varepsilon=\mu\lambda\), the smooth and tangent legality predicates
agree for every \(S\subseteq B_n\), for all sufficiently small positive
\(\mu\).

**Proof.** Let \(D_\mu(S)\) be the minimum of all smooth triple tests,
with the empty minimum interpreted as infinity. For a flat triple with
its middle site \(b\), Proposition 1
and smooth dependence give

\[
\operatorname{dist}_E(b,\gamma^S_{ac})
=\mu|A_e(S)|+O(\mu^2).
\tag{6}
\]

Minimizing over the nearby closest point on the curve removes the tangential
variation; since \(b\) is strictly interior, no endpoint minimum intervenes.
The other endpoint choices have positive zeroth-order segment distance,
as do all choices for non-collinear triples. If \(S\) contains a flat
triple, we therefore have \(D_\mu(S)=\mu M(S)+O(\mu^2)\).
If it contains none, all its triple distances
stay bounded away from zero (or there are no tests). The sign of
\(M(S)-\lambda\) decides legality whenever finite. Finiteness of all
configurations makes the remainder control and the required small-field
range uniform at this fixed \(n\). ∎

The excluded levels are configuration margins, not merely capacity
boundaries. An individual response can equal \(\lambda\) without
causing ambiguity when another triple strictly violates the constraint.
At \(\lambda=M(S)\), the tangent predicate is still defined, but
first order alone does not decide the smooth predicate.

**Proposition 5 (fixed resolution).** At fixed \(n\), if
\(0<\varepsilon<\delta_n=1/(\sqrt2(n-1)^2)\), then for all
sufficiently small positive \(\mu\) the smooth legal sets are exactly
the ordinary planar no-three sets.

**Proof.** A nonzero integer determinant has absolute value at least one.
After normalization, every non-collinear point-to-line altitude is at
least \(\delta_n\); distance to a segment is no smaller. Uniform
convergence of segments to chords, with displacement below
\(\min(\varepsilon,\delta_n-\varepsilon)\), makes every flat middle
site forbidden and keeps every non-collinear triple allowed. ∎

These two limits explain why shrinking resolution with the field and
holding resolution fixed answer different questions. No numerical bound
on \(\mu\) is provided. Certification at a specified nonzero field
requires a quantitative uniqueness bound and rigorous geodesic enclosures
separated from the chosen resolution. Threshold equalities require
higher-order analysis. No joint \(n\to\infty\) limit is established.

## 7. Reproduction, prior work and open questions

The accompanying [supplement](supplement/README.md) contains the exact
predicate, the complete \(n=3,4\) masks and radical vectors, both programs,
the equality and comparison conventions, replay receipts, and commands for
reproducing all stated finite counts. The producer enumerates masks in Gray
order; the checker reconstructs the coefficient matrix from rational
geometry and visits triple supersets in a different order. Both were written
by Sol, so this is a separate-code replay rather than independent authorship.
An external pre-submission replay is recorded in the supplement.

The optical variational principle and simple-metric openness are prior
work [2,3,5,6]. We make no novelty claim for these tools or for the
Plummer-type softening. The contribution is the explicitly defined finite
predicate and its exactly checked phase diagrams. It does not certify the
earlier heuristic mass-world calculations, which used different conventions.

Three questions remain: Can one certify a phase at an explicit nonzero
\(\mu\)? Which phases survive changes of softening and normalization?
Can symmetry and cancellation predict the frontiers without enumerating
every configuration? Each has a concrete failure test: a smooth interval
certificate contradicting the proposed phase, a disappearing strict
frontier gap under parameter change, or a missed maximizing mask.

## Author and contributions

The submitting author is **Athanor lab** (account `athanor_lab`). Aleksei
Kudriashov initiated and directed the research programme and is the human
author responsible for this submission. Astra (gpt-6-astra) specified the
scalar model, derived the first variation and supplied the weak-field limit
arguments. Sol (gpt-6.1-sol) implemented the exact algebraic reduction,
producer, checker and phase analysis. The Guide (Claude Code; version not
recorded) coordinated the programme and maintained its research record. A
separate gpt-6.1-sol research core performed the external pre-submission
audit and replay reported in the supplement.

## References

1. H. C. Plummer, *On the Problem of Distribution in Globular Star
   Clusters*, *Monthly Notices of the Royal Astronomical Society* 71
   (1911), 460–470. [DOI](https://doi.org/10.1093/mnras/71.5.460).
2. G. W. Gibbons and M. C. Werner, *Applications of the Gauss–Bonnet
   theorem to gravitational lensing*, *Classical and Quantum Gravity* 25
   (2008), 235009. [arXiv:0807.0854](https://arxiv.org/abs/0807.0854).
3. Volker Perlick, *Gravitational Lensing from a Spacetime Perspective*,
   *Living Reviews in Relativity* 7 (2004), 9.
   [DOI](https://doi.org/10.12942/lrr-2004-9).
4. Tomer Geva and Ben Z. Steinberg, *Rest-frame analysis of rotating
   metamaterials, gyroscopes, and century-old problems in number theory*
   [Invited], *Optical Materials Express* 13(7) (2023), 1870–1882.
   [DOI](https://doi.org/10.1364/OME.489562).
5. Jan Bohr, François Monard and Gabriel P. Paternain,
   *Local and Global Blow Downs of Transport Twistor Space*, SIGMA 22
   (2026), 045. [Publisher PDF](https://sigma-journal.com/2026/045/sigma26-045.pdf),
   §6, p. 24, for \(C^2\)-openness of simple metrics.
6. Dmitri Burago and Sergei Ivanov, *Boundary distance, lens maps and
   entropy of geodesic flows of Finsler metrics*, Geometry & Topology 20
   (2016), 469–490.
   [Publisher PDF](https://msp.org/gt/2016/20-1/gt-v20-n1-p08-p.pdf).
   Their abstract records openness and the inclusion of flat metrics.

## Appendix A. Exact finite frontiers

The following expressions, together with the infinite frontiers in §3,
specify every capacity boundary exactly:

\[
\begin{aligned}
\alpha_7={}&-\frac4{15}+\frac{2\sqrt5}{45}-\frac{2\sqrt{17}}{153}
 +\frac{2\sqrt{21}}{45}+\frac{2\sqrt{33}}{153},\\
\alpha_8={}&\frac{-204+34\sqrt5+14\sqrt{21}+20\sqrt{33}}{765},\\
\alpha_9={}&0,\\
\beta_9={}&-\frac{5\sqrt2}{272}+\frac{\sqrt{34}}{144}
 +\frac{\sqrt{82}}{164}-\frac{\sqrt{146}}{164}
 -\frac{\sqrt{178}}{432}+\frac{\sqrt{434}}{272},\\
\beta_{10}={}&\frac{161127\sqrt2}{1527824}+\frac{\sqrt{34}}{144}
 +\frac{3\sqrt{82}}{328}-\frac{\sqrt{146}}{82}
 -\frac{49\sqrt{178}}{3672}-\frac{\sqrt{274}}{274}
 +\frac{\sqrt{434}}{136},\\
\beta_{11}={}&\frac{213\sqrt2}{2788}+\frac{\sqrt{34}}{144}
 +\frac{\sqrt{82}}{328}-\frac{\sqrt{146}}{164}
 -\frac{125\sqrt{178}}{7344}+\frac{\sqrt{434}}{136},\\
\beta_{12}={}&\frac{593}{10200}+\frac{\sqrt{33}}{136}
 -\frac{\sqrt{41}}{200}+\frac{\sqrt{73}}{292}
 -\frac{123\sqrt{89}}{14600}-\frac{\sqrt{137}}{292}
 +\frac{\sqrt{217}}{292},\\
\beta_{13}={}&-\frac{\sqrt{34}}{144}-\frac{\sqrt{82}}{164}
 +\frac{\sqrt{146}}{164}+\frac{\sqrt{178}}{432},\\
\beta_{14}={}&\frac{3\sqrt{34}-\sqrt{178}}{432},\\
\beta_{15}={}&\frac{5\sqrt2-2\sqrt{178}+\sqrt{434}}{272},\\
\beta_{16}={}&0.
\end{aligned}
\]
