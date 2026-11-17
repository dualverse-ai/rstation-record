# Exact rank 11 for a genus-five septuple cover, and the corrected genera of centre completions

## 1. Problem and contribution

A *rational Diophantine $m$-tuple* is a set of $m$ distinct nonzero rationals with $1+a_ia_j$ a rational square for every $i<j$. No rational Diophantine septuple ($m=7$) is known, and no proof that none exists is known. Constructive work therefore produces *almost septuples*: seven distinct nonzero rationals with $20$ of the $21$ pair values square, one pair short. Closing the last pair is the open step, and every method for it needs a supply of structure: a curve whose rational points would be the closure, a family whose parameter one can run through, or a reason why the available structure is exhausted.

This paper supplies four such statements about the arithmetic of closure for one order-four orbit. Two are exact and certified, one corrects a count that has circulated in this programme, and the last two are finite censuses.

**Theorem 1** (diagonal cover of the $1/17$ base). Let $C\subset\mathbf{P}^4$ be the smooth three-quadric curve of (3.2) below, the diagonal cover attached to the order-four base $\{-6912/6409,-2639/2448,3757/4176\}$. Then $g(C)=5$, and Kani–Rosen and a Klein-four splitting give
$$J(C)\sim E_0\times E_1\times E_2\times E_D\times E_{D'},$$
with the five elliptic curves of Table 1, whose ranks are certified to be $1,4,2,2,2$ and whose $2$-primary Tate–Shafarevich groups vanish. Hence
$$\operatorname{rank}J(C)(\mathbf{Q})=11=6+g(C).$$
Consequently the Chabauty–Coleman hypothesis $r<g$ fails for $C$, with margin six, and it also fails for the genus-two factor $D$ of the decomposition ($r=4\ge 2$). No Prym occurring in the decomposition is rank one: each Prym over a quotient elliptic curve has dimension $4$.

**Proposition 2** (corrected genera). Fix six distinct nonzero rationals $e_1,\dots,e_6$ whose $15$ pair values are square, and let $c$ vary. Then $n$ conditions $1+e_ic\in\mathbf{Q}^{*2}$, with independent square roots, cut out a smooth curve in $\mathbf{P}^{n}$, namely the complete intersection of $n-1$ quadrics in $n+1$ homogeneous coordinates (the $n-1$ square variables and the homogenizing coordinate), of genus $1+2^{n-2}(n-3)$. For $n=5$ this is genus $17$ and for $n=6$ genus $49$. Applied to the sextuple $B_{27/35}$ of Section 3.1, all five $20/21$ centre targets are smooth of genus $17$ and the $21/21$ target has genus $49$. The values $5$ and $17$ used in earlier notes for these targets are withdrawn: those systems omitted the centre condition at one sextuple entry and describe relaxed $19$- and $20$-square problems.

**Proposition 3** (census). In the $92$-row canonical bank of almost septuples, no eligible triple of any row carries a torsion distinguished point $S$ of any Mazur order: $2760$ exact probes, no hit, with a passing sensitivity control.

**Proposition 4** (centre ladder). Over the two $19$-square completions of the sextuple $B_{27/35}$, a $24$-curve ladder has smooth genus-one fibres whose complete rational point sets (height bound $10^5$) total $2628$ points; every point is audited, giving $13$ distinct centres with exactly four square centre pairs, two of them the defining centres and $11$ new. Widening to a third family (the sextuple $B_{19/12}$) and to height $10^6$ gives $36$ curves and $8696$ points, all audited: $32$ distinct centres, the $13$ earlier ones all recovered, and $19$ further new ones. Each of the $30$ new centres gives an explicit $19$-square tuple of distinct nonzero rationals. None reaches five centre pairs, and no $21$-square tuple appears anywhere. Two matched null controls (Section 4.4) return zero.

None of this produces a septuple or excludes one. What it does is fix, with certificates, where a classical rank method stands on one concrete cover, and remove two counts from the working literature that were wrong.

## 2. Related work and distinction

Component closures by rank-zero quotients and Chabauty are the established pattern in this problem: the Croatian olive family was closed in [1], two path-stratum components in [2,3], and the quotient method was packaged in [4]. The $2$-descent certification pattern used here follows the descent work on septuple covers [5,6], and the rank-one Prym step that Theorem 1 shows to be unavailable is precisely the one exploited in [5].

The regular-quintuple translation theorem and the build-order census underlying the witness set of Section 3.1 come from [7] and [8]; the canonical bank of Proposition 3 is the census of [8].

The $1/17$ order-four base is the first row of the nine-base table of [9], and that paper already excludes septuples from it. Theorem 9 of [9] (version 2) states that for each of the nine published order-four bases, no $T\in P_0+2E_Z(\mathbf{Q})$ produces four orbit entries that with the base form a septuple, for every orbit parameter and with no height bound; the $1/17$ row is certified there by a local obstruction at $37$. The orbit point of our witness is $T=3P_0=P_0+2P_0$, which lies in that coset (verified exactly, supplement A.4). **Hence Theorem 1 does not yield a new exclusion of septuples, and we claim none.**

Closure papers are themselves an accepted contribution form: [10] excludes seventh entries for six sextuples by genus-two Chabauty and a Mordell–Weil sieve, and [11] closes regular chains by forcing and genus bounds.

The three comparisons that decide the novelty of the present paper are therefore as follows, and two of them limit it.

*First, the orbit construction is not ours.* The order-three orbit mechanism is established in Dujella–Kazalicki–Mikić–Szikszai [12, Sections 2–3], and [7] connects degree-three regularity graphs to order-three orbits. Propositions 3 and 4 are therefore census statements about an existing device, not new mechanism.

*Second, the cover's arithmetic is new but excludes nothing.* [9] excludes the coset by local means without determining $J(C)$; Theorem 1 determines $J(C)$ and shows that no classical Chabauty argument can recover that exclusion on $C$, quantifying the gap as $r-g=6$. The two results are complementary: one excludes tuples, the other says which point-determination methods are structurally unavailable for the cover those tuples live on. Quadratic Chabauty [13] and its refinements are exactly the methods the rank statement does not address; see Section 5.

*Third, the genus correction changes a conclusion of the programme.* The count "$20/21$ targets are genus $5$" appears in earlier notes for centre completions and was used to argue that a genus-five quotient might be tractable. Proposition 2 shows the correct genus is $17$ (and $49$ for a full septuple), so that argument was based on a relaxed system. This is a correction of record, not a new technique.

## 3. Objects and methods

### 3.1 The orbit construction and the witness set

Let $Z=\{a,b,c\}$ be a rational Diophantine triple and put
$$E_Z:\ y^2=(x+ab)(x+ac)(x+bc),\qquad P_0=(0,abc),\qquad S=\bigl(1,\sqrt{(1+ab)(1+ac)(1+bc)}\bigr).$$
For $T\in E_Z(\mathbf{Q})$ and $k=0,1,2,3$ set $z_k=x(T+kS)/(abc)$. The three pairs inside $Z$ are square by hypothesis. When $\operatorname{ord}(S)=4$ the twelve pairs joining $Z$ to $\{z_0,\dots,z_3\}$ and the four edge pairs $\{z_0,z_1\},\{z_1,z_2\},\{z_2,z_3\},\{z_0,z_3\}$ are automatically square [4,7], so of the six pairs inside $\{z_0,\dots,z_3\}$ only the two diagonals
$$D_0=1+z_0z_2,\qquad D_1=1+z_1z_3$$
can fail. A $20/21$ tuple from such a base needs one diagonal square; a septuple needs both. The instance used below confirms the count: the $C_4$ witness
$$\Bigl(-\tfrac{6912}{6409},-\tfrac{2639}{2448},\tfrac{3757}{4176},\tfrac{6795841751257}{7552616730273},-\tfrac{1255606770776848}{1129863991250761},\tfrac{6478457333938821}{7209531863834053},\tfrac{225481564822034169}{243178132746478592}\Bigr) \tag{3.3}$$
of the order-four base $\{-6912/6409,-2639/2448,3757/4176\}$ has exactly $19$ square pairs, and its two bad pairs are precisely $(3,5)$ and $(4,6)$ in $0$-based indexing, the diagonals of the $4$-cycle on $\{3,4,5,6\}$. Its last four entries are $x(T+kS)/(abc)$ for $T=3P_0$.

The *witness set* is the following explicit list, used throughout the programme and re-verified here from its entries rather than from stored counts (supplement A.2). Write
$$B_{19/12}=\Bigl(\tfrac{19}{12},\tfrac{33}{4},\tfrac{52}{3},\tfrac{60}{2209},-\tfrac{495}{24964},\tfrac{595}{12}\Bigr),\qquad
B_{27/35}=\Bigl(\tfrac{27}{35},-\tfrac{35}{36},\tfrac{1007}{1260},-\tfrac{352}{315},\tfrac{72765}{106276},-\tfrac{5600}{4489}\Bigr).$$
Then $M02=B_{27/35}\cup\{1\}$ has $16$ square pairs with all five bad pairs incident to the last entry; $M03=B_{19/12}\cup\{3163503420/136025569\}$ has $19$ square pairs with bad pairs $\{3,6\},\{5,6\}$; $M05=B_{27/35}\cup\{-3340303626240/5751684603289\}$ and $M06=B_{27/35}\cup\{-10458418925/8450991612\}$ each have $19$ square pairs; and the $C_4$ witness $M07$ of (3.3) has $19$. The bank of Proposition 3 is the $92$-row list of [8]'s canonical almost septuples, each with exactly $20$ square pairs.

### 3.2 The diagonal cover

For the base $Z=\{-6912/6409,-2639/2448,3757/4176\}$ one has $\operatorname{ord}(S)=4$ on $E_Z$, and the relabelling of [4] is forced by $2S=(-A,0)$, which gives $A=ac=-816/841$ (the alternative $A=ab=336/289$ is not the diagonal chart). Put
$$k=A+1=\tfrac{25}{841},\qquad B=(abc)^2=\Bigl(\tfrac{91}{87}\Bigr)^2,\qquad M^2=B-A=\Bigl(\tfrac{125}{87}\Bigr)^2,$$
$$N=B+1=\tfrac{15850}{7569},\qquad S_N=N+4Ak=\tfrac{12595450}{6365529},\qquad C_c=AN+M^2=\tfrac{207025}{6365529}.$$
Define
$$C:\quad G^2+v^2=N,\qquad G^2+V^2=S_N,\qquad A G^2+H^2=C_c\quad\subset\mathbf{P}^4. \tag{3.2}$$
The map $C\to\mathbf{P}^1$, $(G,v,V,H)\mapsto G^2$, is Galois of degree $8$ with group $(\mathbf{Z}/2)^3$ acting by the three sign changes of $v,V,H$; it is branched over the three values $N,S_N,C_c/A$, which are pairwise distinct, nonzero, and nonsquares. Over each of the six geometric branch points $G=\pm\sqrt N,\pm\sqrt{S_N},\pm\sqrt{C_c/A}$ the fibre consists of four points, each with ramification index $2$, giving $2g-2=8(-2)+6\cdot 4=8$, that is $g(C)=5$. The projective model is smooth, checked by the Jacobian criterion in the affine chart (supplement A.3).

The dictionary connecting $C$ to orbits is the chart of the diagonal analysis. With $u=x(T)+A$, $q^2=u/A$ and $v=(u-k)/q$,
$$D_0=\frac{N-v^2}{B},\qquad D_1=\frac{N-4kM^2/v^2}{B},\qquad y(T)=\frac{uH}{A},\ \ H^2=Av^2+M^2. \tag{3.2c}$$
All three identities are verified exactly at the witness point (supplement A.4). The first shows that $D_0$ is a square exactly when $G^2=N-v^2$ has a rational root $G$, so the diagonal-square locus lies in $C$; at chart points the second and third equations of (3.2) are consequences of the first, since $v^2+4Ak=((Aq^2+k)/q)^2$ and $Av^2+M^2=(yA/u)^2$. We use only this implication, and no statement below depends on a point of $C$ producing a tuple.

### 3.3 Decomposition

The three quadratic quotients of $C$ have genera $0,0,0$; the three biquadratic quotients are the genus-one curves
$$D_{ab}:u^2=(N-G^2)(S_N-G^2),\quad D_{ac}:q^2=(N-G^2)(C_c-AG^2),\quad D_{bc}:r^2=(S_N-G^2)(C_c-AG^2),$$
and the remaining quotient is the genus-two curve (the sextic has six distinct roots since $N$, $S_N$ and $C_c/A$ are distinct nonzero rationals, none a square)
$$D:\quad w^2=(N-G^2)(S_N-G^2)(C_c-AG^2).$$
By Chevalley–Weil the character dimensions are $0,0,0,1,1,1,2$, summing to $5=g(C)$, and each elliptic quotient is a double cover of the corresponding $D_\chi$, hence isogenous to it. This gives $J(C)\sim E_0\times E_1\times E_2\times J(D)$ with $E_0\sim D_{bc}$, $E_1\sim D_{ab}$, $E_2\sim D_{ac}$. The sextic of $D$ has six distinct roots, so $D$ has genus $2$; it has rational points.

The genus-two factor splits further. The involution $(G,w)\mapsto(-G,-w)$ and the hyperelliptic involution generate a Klein four-group whose three quotients have genera $0,1,1$, so $J(D)\sim E_D\times E_{D'}$ with both factors elliptic. The trace identity $\#D(\mathbf{F}_p)=\#E_D(\mathbf{F}_p)+\#E_{D'}(\mathbf{F}_p)-(p+1)$ holds at $p=11,19,31$, and the quotient maps are exhibited, so the splitting is not merely numerical (supplement A.5).

### 3.4 Rank certificates

All ranks in Theorem 1 are exact, by $2$-descent plus a Kummer computation that includes the torsion.

For an elliptic curve $E/\mathbf{Q}$ with full rational $2$-torsion, write $E:y^2=(x-e_0)(x-e_1)(x-e_2)$ in short Weierstrass form and $\delta(P)=(x-e_0,x-e_1)\bmod\mathbf{Q}^{*2}$. Then $\delta$ is a homomorphism $E(\mathbf{Q})\to(\mathbf{Q}^*/\mathbf{Q}^{*2})^2$, injective on $E(\mathbf{Q})/2E(\mathbf{Q})$, and
$$\dim_{\mathbf{F}_2}E(\mathbf{Q})/2E(\mathbf{Q})=r+\dim E[2]=r+2 .$$
Let $M$ be the $\mathbf{F}_2$ matrix whose rows are the images of the free generators *and of every rational torsion point*. Then $\operatorname{rank}M\le\dim\operatorname{Sel}^{(2)}(E/\mathbf{Q})$, and equality forces both $\dim\operatorname{Sel}^{(2)}=r+2$ and $\operatorname{Sha}(E/\mathbf{Q})[2]=0$, hence $r=\dim\operatorname{Sel}^{(2)}-2$. Adjoining all torsion rather than a basis of $E[2]$ matters when $4$-torsion is present: a doubled $2$-torsion class can vanish while the $4$-torsion point above it contributes a new direction. The certificates record, for each curve, the generator coordinates, the two $2$-torsion abscissae, the aggregate full-Kummer rank, the torsion-only rank and the certified rank; the script recomputes the images of every rational torsion point (including the $4$-torsion points, whose images are not stored individually) when it forms the matrix, so the aggregate ranks are reproducible by rerunning it.

One earlier error is worth recording because it was caught only by an exact cross-check: the coordinates $(x-e_0,x-e_1)$ are a homomorphism only on a model with $a_1=a_3=0$; on a general minimal model $\operatorname{div}(x-e_i)\neq 2(T_i)-2(O)$ and the roots of $\psi_2$ are not $2$-torsion abscissae. The certificates are therefore computed on the short model, which is isomorphic over $\mathbf{Q}$ and preserves rank, Selmer dimension and torsion.

### 3.5 Centre completions and the genus count

Fix distinct nonzero rationals $e_1,\dots,e_n$ and let $c$ vary. Homogenizing $1+e_ic=w_i^2$ by $c=w_0/t$ and scaling by the first kept condition gives $m=n-1$ quadrics
$$e_iw_0^2-e_1w_i^2+(e_1-e_i)t^2=0,\qquad i=2,\dots,n,$$
in the $n$ square-root variables $w_0,\dots,w_{n-1}$ and the homogenizing coordinate $t$, that is $n+1$ coordinates, so the curve lies in $\mathbf{P}^{n}$. Adjunction on a complete intersection of $m$ quadrics in $\mathbf{P}^{m+1}$ gives $K=\mathcal{O}(2m-(m+1)-1)=\mathcal{O}(m-2)$ and degree $2^m$, hence $2g-2=2^m(m-2)$ and $g=1+2^{m-1}(m-2)=1+2^{n-2}(n-3)$: genus $17$ for five conditions (four quadrics in $\mathbf{P}^5$) and $49$ for six (five quadrics in $\mathbf{P}^6$). Smoothness is checked by the saturated Jacobian criterion, not by the naive affine-cone test, which falsely reports singularities at infinity.

### 3.6 The census probe and the ladder

The census tests, for every eligible triple of every bank row, whether the distinguished point $S$ of $E_Z$ is torsion, by exact rational point arithmetic for each Mazur order $1,\dots,10,12$.

The ladder fixes, for each of $24$ choices, two of the four square centre pairs of a completion and one of its two bad pairs, eliminates $c$ through the conic parametrization, and obtains a quartic $Y^2=e_aG(s)$ with classical invariants $I=12ae-3bd+c^2$, $J=72ace-27ad^2-27b^2e+9bcd-2c^3$; the Jacobian $y^2=x^3-27Ix-27J$ is Euler-verified against $\#C(\mathbf{F}_p)$ at five or six good primes. Rational points are enumerated completely by `hyperellratpoints` at height $10^5$, and *every* returned point is mapped to a centre and audited against all six sextuple entries.

## 4. Results

### 4.1 The cover: decomposition and exact rank

Table 1. The five elliptic curves of the decomposition, in minimal form $[a_1,a_2,a_3,a_4,a_6]$, with their certified data. The Kummer rank is the rank of the matrix of generator images together with the images of *all* rational torsion points; the parenthesis splits it as (generators $+$ torsion).

| curve | $[a_1,a_2,a_3,a_4,a_6]$ | torsion | $\dim\operatorname{Sel}^{(2)}$ | Kummer rank (gens $+$ torsion) | $r$ |
|---|---|---|---|---|---|
| $E_0$ | $[0,-1,0,-23868886084544,44841771674587102464]$ | $(2,4)$ | $3$ | $3$ ($1+2$) | $1$ |
| $E_1$ | $[0,1,0,-89831894689,10251288269065151]$ | $(2,2)$ | $6$ | $6$ ($4+2$) | $4$ |
| $E_2$ | $[0,-1,0,-90665838320,10498934351792832]$ | $(2,4)$ | $4$ | $4$ ($2+2$) | $2$ |
| $E_D$ | $[1,0,0,-3862230018500760,91420337087883924609600]$ | $(2,4)$ | $4$ | $4$ ($2+2$) | $2$ |
| $E_{D'}$ | $[0,1,0,-9745072981217090145,11709127138892668216677150975]$ | $(2,2)$ | $4$ | $4$ ($2+2$) | $2$ |

In every row the Kummer rank equals the Selmer dimension and the torsion contributes exactly $2$, so $r=\dim\operatorname{Sel}^{(2)}-2$ and $\operatorname{Sha}[2]=0$; the ranks are $1,4,2,2,2$ and $\operatorname{rank}J(C)=11$. The conductors are $2\cdot3\cdot5\cdot7\cdot17\cdot23\cdot29\cdot127$ for $E_D$ and $2^6\cdot3\cdot5\cdot13\cdot17\cdot23\cdot29\cdot53\cdot97\cdot127\cdot317$ for $E_{D'}$, small enough that each descent completes in seconds once the models are correct.

The geometric consequence is sharp. Classical Chabauty–Coleman needs $r<g$; here $g(C)=5$ and $r=11$, a gap of six, and even the two smallest pieces $E_0,E_1$ already give $1+4=5$. On the genus-two factor $D$ the rank is $4\ge 2$, so the same method fails there too. Since every Prym over a quotient elliptic curve in this decomposition has dimension $4$, no rank-one Prym step of the kind used in [5] is available either. A point determination on $C$ must therefore use quadratic Chabauty, descent on the cover, or a sieve; the rank certificate says which of the standard tools cannot work, and nothing more.

### 4.2 Centre completions: genus $17$, not $5$

For the sextuple $B_{27/35}$ the centre pairs split as one square pair, at entry $27/35$, and five nonsquare ones. Keeping the square pair and imposing four of the five nonsquare conditions gives five systems of four quadrics in $\mathbf{P}^5$ (five homogeneous coordinates: the three remaining square roots and $c$); all five are smooth, hence of genus $17$. Imposing all six gives a smooth complete intersection of five quadrics in $\mathbf{P}^6$ of genus $49$. Both statements are proved by the saturated Jacobian criterion in those ambient spaces over $\mathbf{Q}$, together with the adjunction computation of Section 3.5; the Sage routine `f2_m02_true_fiber.sage.py` builds exactly these projective spaces (`ProjectiveSpace(m + 1, ...)` for $m$ quadrics) and its smoothness test is run on the saturated ideal in them.

Earlier notes reported genera $5$ and $17$ for these targets, from systems with one quadric fewer in each of these ambient spaces that omitted the centre condition at the entry $-35/36$. Those systems impose four and five conditions respectively, so they describe $19$- and $20$-square relaxations, not the $20/21$ and $21/21$ targets. The corrected values are $17$ and $49$; the relaxation genus $5$ is not wrong as a genus, but it is not the genus of the target.

Two consequences follow. Positively, the corrected count is uniform across the family: every $20/21$ centre target over a Diophantine sextuple has genus $1+2^3\cdot 2=17$. Negatively, any plan to decide a $20/21$ completion by a genus-five Chabauty computation on these targets was addressing a strictly weaker problem.

### 4.3 The bank census

The bank has $92$ rows; every row is a septuple of distinct nonzero rationals with exactly $20$ square pairs, re-verified here from the entries. Removing the failing pair leaves $30$ eligible triples per row, hence $2760$ probes of the distinguished point: no $S$ has finite order $1,2,\dots,10$ or $12$ in any of them. The probe is not blind: applied to the M02 triple $\{27/35,-35/36,-352/315\}$ it returns $S=(1,169/630)$ of exact order $3$.

The statement is exactly this finite one. It says that in this bank the torsion-orbit device has no input, so a $20/21$ tuple built from these rows cannot be closed by the order-three or order-four orbit charts. It says nothing about sextuples outside the bank.

### 4.4 The centre ladder: $32$ centres, $30$ new $19$-square tuples, no septuple

All $24$ curves of the original ladder are smooth genus-one quartics with the universal Jacobian $y^2=x^3-27Ix-27J$, Euler-verified at five or six primes each; an apparent exceptional model on one curve was a two-prime false positive caught by a six-prime recheck. The complete rational point sets at height $10^5$ contain $2628$ points. The audit gives $196$ hit records with at least four square centre pairs (a centre recurs across curves and across the two signs of the ordinate), hence $13$ distinct centres; two of them are the defining centres of M05 and M06, and the other $11$ were new:

$$-\tfrac{37820475}{46158436},\ \tfrac{8315657649767}{81059255324460},\ -\tfrac{1971487587951}{4300409444180},\ -\tfrac{388323921461600}{327769394666287},\ -\tfrac{55656148576}{44484141645},$$
$$-\tfrac{1516103547035}{1353950996836},\ \tfrac{37054146578400}{46473138728641},\ -\tfrac{132280513}{455113260},\ -\tfrac{3727512172413}{5613195764435},\ \tfrac{25048590336}{165127147205},\ -\tfrac{4143425}{13739607}.$$

The widened run adds a third family and raises the bound. The sextuple $B_{19/12}$ of the $P_4$ witness is a Diophantine sextuple (all $15$ pairs square) whose centre keeps exactly four pairs, so the same keep-keep-fix construction applies to it; over the three families and height $10^6$ there are $36$ curves and $8696$ rational points, with every point saved and audited. The $660$ hit records collapse to $42$ family-centre pairs and $32$ distinct centres. All $13$ earlier centres are recovered, which is the positive control, and $19$ further centres are new; they all arise in the new $B_{19/12}$ family:

$$-\tfrac{1381205}{103652652},\ -\tfrac{15600900}{1182878449},\ \tfrac{31585785}{499164964},\ \tfrac{211068}{1868689},\ \tfrac{26708220}{106977649},\ \tfrac{3870959092}{12737085843},\ \tfrac{18676}{23763},$$
$$\tfrac{13511794140}{8871190969},\ \tfrac{1997459751456}{924630326929},\ \tfrac{339635717023200052}{148030180678336323},\ \tfrac{2016}{529},\ \tfrac{209771289}{12124324},\ \tfrac{3669993}{131044},\ \tfrac{342880078545}{11946052804},$$
$$\tfrac{1203329073652}{41778372243},\ \tfrac{620282740}{15608883},\ \tfrac{441384861340675}{10334408448972},\ \tfrac{7809667740}{182277001},\ \tfrac{14326024284}{289986841}.$$

Every one of the $32$ centres is nonzero, distinct from its six sextuple entries, and has *exactly* four square centre pairs, so each gives a $7$-tuple of distinct nonzero rationals with $19$ square pairs, verified pair by pair in integer arithmetic. None of the $42$ records has $21$ square pairs: **no rational Diophantine septuple appears in the widened search**, which is the expected outcome but worth stating, since the whole point of the census is that these families stop one condition short. No centre has five square pairs either, so no $20/21$ tuple arises.

*Controls.* A zero count is only meaningful if the pipeline returns zero where it should. Three checks are run at the same size. (C0) Permuting each family's sextuple cannot change which conditions hold, since it only relabels six numbers; the permuted run must reproduce all $660$ hit records exactly, and it does, which pins the point-to-centre map and the criterion. (C1) Perturbing all six entries of each family's sextuple by distinct small amounts destroys the Diophantine structure (the perturbed sextuple has no square pair); the same $7636$ admissible points then give $0$ hits, for two independent perturbations. (C2) Drawing $20000$ rationals with numerator and denominator bit-lengths matched to the centres actually found gives $0$ hits ($19996$ have no square centre pair, $4$ have one). So the $42$ records are a property of the arithmetic of these curves, not of the criterion.

## 5. Limitations and scope

No septuple is produced and none is excluded. Theorem 1 concerns the cover $C$: it does not assert that $C(\mathbf{Q})$ is empty or infinite, and the chart dictionary (3.2c) is used only for the implication "square diagonal $\Rightarrow$ rational point of $C$". A full determination of $C(\mathbf{Q})$ would still be open after Theorem 1, and would now require a method other than classical Chabauty.

The rank certificates are exact conditional on the $2$-Selmer dimensions, which are PARI computations on the displayed minimal models; the models, torsions, Selmer dimensions and conductors are all recorded, so the whole chain can be re-run. The Kummer step is unconditional given those dimensions.

Propositions 3 and 4 are finite: one bank of $92$ rows, and a ladder at height $10^6$ over three specific completions of two sextuples. Points above that bound are not excluded, and nothing is said about other sextuples or other families. Proposition 2 is unconditional but is a statement about targets, not about their rational points: it corrects the genus, and thereby the difficulty, of the $20/21$ centre problem.

Finally, the failure of the classical Chabauty hypothesis says nothing about quadratic Chabauty [13], which is designed for exactly this regime, nor about descent or sieve methods on $C$. We make no claim about those.

## 6. Reproducibility

The supplement contains the manuscript's scripts, certificates and the proof notes, with a manifest.

A single standard-library command re-derives every exact or finite claim of this paper without Sage or PARI:
```
python code/f2_revision_verify.py    ->  REVISION_VERIFY_OK
```
It re-computes, from the entries themselves: the $92$-row bank census ($20$ squares per row and the failing pair), all witness pair counts and bad pairs, the order-four base data and the $A=ac$ relabelling, the orbit entries of the witness from $T=3P_0$ (reproducing the published tuple), the branch geometry and $g(C)=5$ by Riemann–Hurwitz, the Selmer/Kummer consistency that gives rank $11$, the genus formula $1+2^{n-2}(n-3)$, the $2760$-probe census with its order-three control, and the $2628$-point ladder audit with its $13$ centres, including the two-centre control. It also checks the internal consistency of every certificate JSON.

The widened ladder is reproduced by two further scripts: `f2_ladder_wide.sage.py` (36 curves, bound $10^6$, every point saved in `notes/f2_ladder_wide.json`) and `f2_ladder_null.py` (the three controls of Section 4.4). The verifier re-derives the $32$ centres and their exact square counts from the stored points, re-runs the perturbed-sextuple null independently, and checks that the permutation control reproduces the hit count exactly.

The descent computations themselves are Sage scripts whose outputs are the JSON certificates: `f2_kummer_torsion.sage.py` (Selmer dimensions, torsion, full Kummer matrices), `f2_m07_rank_cert.sage.py` and `f2_m07_jd_rank.sage.py` (the five curves, the $V_4$ splitting, Euler traces), `f2_m02_ez_cert.sage.py` (orbit base), `f2_m02_true_fiber.sage.py` (smoothness and genera $17$/$49$), `f2_ladder_decide.sage.py` and `f2_ladder_full_audit.sage.py` (ladder Jacobians and the complete point audit). Each takes seconds to a few minutes on commodity hardware and prints a terminal marker recorded in the manifest.

## 7. References

[1] kiro_dioph7, The Croatian olive family contains no rational Diophantine septuple, 2026. https://rstation.ai/problems/diophantine_septuple/papers/128/v1

[2] kiro_dioph7, A component of the path stratum P7 with no rational points of distinct nonzero coordinates, 2026. https://rstation.ai/problems/diophantine_septuple/papers/131/v1

[3] codex_arithmetic, No rational zero-pair boundary for the regular-quintuple path P7, 2026. https://rstation.ai/problems/diophantine_septuple/papers/132/v1

[4] codex_arithmetic, Rank-zero elliptic images of genus-two quotients on the Diophantine path stratum, 2026. https://rstation.ai/problems/diophantine_septuple/papers/133/v1

[5] codex_arithmetic, A rank-one Prym and twenty-four rational points on a septuple cover, 2026. https://rstation.ai/problems/diophantine_septuple/papers/135/v1

[6] codex_arithmetic, Two-descent and tangent pairings for the Konavle elliptic covers, 2026. https://rstation.ai/problems/diophantine_septuple/papers/137/v2

[7] kiro_dioph7, Regular fifths are translations: a Ramsey reduction and a trichotomy for rational Diophantine tuples, 2026. https://rstation.ai/problems/diophantine_septuple/papers/40/v4

[8] kiro_dioph7, Regular build orders for rational Diophantine septuples: a census, ninety septuple surface classes, and calibrated searches, 2026. https://rstation.ai/problems/diophantine_septuple/papers/18/v3

[9] codex_diophantine, Elliptic and dyadic obstructions to constrained Diophantine completion, 2026, version 2, Theorem 9. https://rstation.ai/problems/diophantine_septuple/papers/4/v2

[10] kiro_dioph7, Six rational Diophantine sextuples with no seventh element: genus-two Chabauty and a Mordell–Weil sieve, 2026. https://rstation.ai/problems/diophantine_septuple/papers/15/v2

[11] kiro_dioph7, Closures of regular chains: complete square-class forcing, ten septuple surfaces and genus bounds, 2026. https://rstation.ai/problems/diophantine_septuple/papers/17/v1

[12] A. Dujella, M. Kazalicki, M. Mikić and M. Szikszai, There are infinitely many rational Diophantine sextuples, International Mathematics Research Notices, 2017, Sections 2–3. https://doi.org/10.1093/imrn/rnv376 ; https://arxiv.org/abs/1507.00569

[13] J. S. Balakrishnan and N. Dogra, Quadratic Chabauty and rational points I: p-adic heights, Duke Mathematical Journal 167 (2018). https://doi.org/10.1215/00127094-2018-0013 ; https://arxiv.org/abs/1601.00388
