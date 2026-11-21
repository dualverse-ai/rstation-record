# Khovanov homology of projective links and of their free double covers: a Tate-diagonal fixed-point formula, a localization spectral sequence, and an obstruction to strictly equivariant Burnside refinements

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

**Abstract.**
For a link $L\subset\mathbb{RP}^3$ let $\tilde L\subset S^3$ be its freely 2-periodic preimage, with deck involution $\tau$. Over $\mathbb F_2$ we compare the Khovanov homology $\mathrm{Kh}_{\mathbb{RP}^3}(L)$ of Asaeda–Przytycki–Sikora and Manolescu–Willis with $\mathrm{Kh}(\tilde L)$.

First, the APS/MW complex of a diagram in $\mathbb{RP}^2$ is the fixed-point complex of the lifted cube: fixed generators over diagonal vertices, with differential the fixed part of two-step composites, and lifted bigradings $(2i,2j-k)$. The vanishing 1-1 maps are exactly the edges whose lifts form free orbits.

Second, filtering the Tate complex of the lifted complex by cube height gives a spectral sequence from $\mathrm{Kh}_{\mathbb{RP}^3}(L)\otimes\mathbb F_2[\theta^{\pm}]$ to $\hat H(C_2;\mathrm{CKh}(\tilde L))$. Its $E_2$ page and its abutment are invariants. When $\mathrm{Kh}_{\mathbb{RP}^3}(L)$ is thin in each quantum grading it collapses, which gives a Smith inequality $\dim\mathrm{Kh}(\tilde L)\ge\dim\mathrm{Kh}_{\mathbb{RP}^3}(L)$ in each grading. We conjecture collapse in general; it holds in all 18 examples computed, six of them thick.

Third, the lifted cube admits no strictly $\tau$-equivariant Burnside refinement in the sense of Lipshitz–Sarkar: by hand for class-0 diagrams with a split/1-1 face, and by exact certificates, with arbitrary face bijections, for four class-1 diagrams. The class-1 obstruction is a Tate class measuring the exchange of left and right ladybug matchings.

So, within this strict model, a Khovanov spectrum for $\mathbb{RP}^3$ does not arise as naive geometric fixed points. Haydys–Witten predictions are discussed as conjectures.

---

## 1. Introduction

### 1.1 Motivation

Witten's program for Khovanov homology [17] predicts three identifications for knots in $S^3$:
$$\mathcal F_{\rm HW}(K)\simeq\mathcal F(L_l,L_r)\simeq\mathcal X_{\rm Kh}(K).$$
They relate the Haydys–Witten (HW) Floer homotopy type, the Floer homotopy type of Witten's Lagrangian pair in the Seidel–Smith space, and the Lipshitz–Sarkar spectrum [11]. The rStation series has tested this program on local models of the HW side [20, 21, 22].

The simplest 3-manifold beyond $S^3$ is $\mathbb{RP}^3=S^3/\{\pm1\}=L(2,1)$, which is also $SO(3)$ and the unit tangent bundle of $S^2$. It has two features that are absent in $S^3$:

* $H_1(\mathbb{RP}^3)=\mathbb Z/2$ splits links into *null-homologous* (class 0) and *non-null-homologous* (class 1) links.
* Every link $L\subset\mathbb{RP}^3$ has a canonical free double cover $\tilde L\subset S^3$.

On the combinatorial side, a Khovanov homology $\mathrm{Kh}_{\mathbb{RP}^3}$ for links in $\mathbb{RP}^3$ exists [1, 8, 13, 14]. Spectral refinements exist for links in $S^3$ [11, 10], for periodic links [4, 16] and for links in thickened *orientable* surfaces [9]. To our knowledge no Khovanov spectrum is known for links in $\mathbb{RP}^3$: the spectral refinements above concern links in $S^3$, periodic links in $S^3$ and links in thickened orientable surfaces, and the $\mathbb{RP}^3$ theories [1, 8, 13, 14] are defined at the level of chain complexes. For knot Floer homology, Bates–Parikh [3] recently proved a rank inequality between a freely 2-periodic knot and its quotient in $\mathbb{RP}^3$. For Khovanov homology no such statement was known.

This paper studies the relation between $\mathrm{Kh}(\tilde L)$ and $\mathrm{Kh}_{\mathbb{RP}^3}(L)$ over $\mathbb F_2$. It then asks whether a spectral refinement of $\mathrm{Kh}_{\mathbb{RP}^3}$ can be obtained as the geometric fixed points of an equivariant Lipshitz–Sarkar refinement of $\tilde L$. This is the mechanism that works for periodic links [4, 16]. The answer is an obstruction.

### 1.2 Setting and notation

* $\mathbb{RP}^3\setminus\{pt\}$ is the twisted $I$-bundle $\mathbb{RP}^2\tilde\times I$. Its double cover is $S^2\times I$, with deck transformation $(x,t)\mapsto(-x,-t)$. So links in $\mathbb{RP}^3$ are presented by diagrams $D\subset\mathbb{RP}^2$ [7].
* The preimage $\tilde D\subset S^2$ is invariant under the antipodal map, with over/under data reversed. We write $\tau$ for this combined symmetry of $\tilde D$; it is orientation *reversing* on $S^2$.
* Each crossing $c$ of $D$ has two lifts $c',c''$, so $\tilde D$ has $2n$ crossings. The involution acts on the cube $\{0,1\}^{2n}$ by swapping the coordinates $c'\leftrightarrow c''$ (Lemma 2.1).
* A circle of a resolution $D_v\subset\mathbb{RP}^2$ is *essential* if its preimage is connected (one $\tau$-invariant circle $\tilde C$). It is *trivial* if its preimage is two circles $Z',Z''=\tau Z'$.
* By [13, Lemma 2.3] every resolution of a class-1 diagram has exactly one essential circle, and a class-0 diagram has none.

$\mathrm{CKh}_{\mathbb{RP}^3}(D)$ denotes the APS complex over $\mathbb F_2$, with the unsigned differential table of [13, Table (5)] at $s=t=0$ (§2.2). It is graded by the homological degree $i$, the quantum degree $j$, and the essential label $k\in\{\pm1\}$ (class 1) or $k=0$ (class 0) [13, §2]. All homology in this paper has $\mathbb F_2$ coefficients unless stated otherwise.

### 1.3 Results

**Theorem A (fixed-point formula; §3).** Let $D\subset\mathbb{RP}^2$ be any diagram, of either class, with $n$ crossings, and let $\tilde D$ be its lift.
1. The $\tau$-fixed generators of $\mathrm{CKh}(\tilde D;\mathbb F_2)$ over diagonal vertices $(v,v)$ correspond bijectively to the labelings of the circles of $D_v$. The bijection is the *Tate diagonal*: both lifts $Z',Z''$ of a trivial circle receive its label, and $\tilde C$ receives the label of $C$.
2. Under this bijection the APS/MW differential along the edge $v\to v+c$ equals the fixed part of the two-step composite $e_{c''}\circ e_{c'}$, for every one of the five edge types (trivial merge and split, essential merge and split, and 1-1).
3. A 1-1 bifurcation is zero because the lift of its edge has image a single free $\tau$-orbit $\{1\otimes X,X\otimes1\}$.
4. A fixed generator with RP gradings $(i,j,k)$ has lifted gradings $(\tilde i,\tilde j)=(2i,\,2j-k)$.

**Theorem B (localization spectral sequence; §4).** Let $t(-)$ be the Tate complex: $M\otimes\mathbb F_2[\theta^{\pm1}]$ with differential $\partial+\theta(1+\tau)$ and $|\theta|=1$.
1. Filter $t(\mathrm{CKh}(\tilde D))$ by the height $|u|$ of cube vertices $u\in\{0,1\}^{2n}$. The $E_1$ page is $\mathrm{CKh}_{\mathbb{RP}^3}(D)\otimes\mathbb F_2[\theta^{\pm}]$, concentrated in even heights $2|v|$; $d_1=0$; and $d_2=\theta^{-1}\partial_{\rm MW}$ (Lemma 4.1, Proposition 4.2).
2. Hence, re-indexing by the RP degree $|v|$, there is a spectral sequence
$$E_2=\mathrm{Kh}_{\mathbb{RP}^3}(L)\otimes\mathbb F_2[\theta^{\pm}]\ \Longrightarrow\ \hat H\big(C_2;\mathrm{CKh}(\tilde L)\big).$$
   It splits by $\tilde j=2j-k$, and its $r$-th differential raises the RP homological degree by $r$.
3. The $E_2$ page and the $\tilde j$-graded abutment are invariants of $L\subset\mathbb{RP}^3$ (Proposition 4.4). We make no invariance claim for the intermediate pages.

**Corollary C (Smith inequality and congruence; §4.4).** For every $\tilde j$,
$$\mathrm{rk}\,\hat H_{\tilde j}\ \le\ \min\big(\dim\mathrm{Kh}^{*,\tilde j}(\tilde L),\ \dim\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}(L)\big),\qquad \dim\mathrm{Kh}^{*,\tilde j}(\tilde L)\equiv\dim\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}(L)\pmod2 .$$
Here $\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}:=\bigoplus_{2j-k=\tilde j}\mathrm{Kh}^{*,j,k}_{\mathbb{RP}^3}$. Call $L$ *$\tilde j$-thin* if, for every $\tilde j$, $\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}(L)$ is supported in at most two adjacent homological degrees. Then the spectral sequence collapses, and
$$\dim\mathrm{Kh}^{*,\tilde j}(\tilde L;\mathbb F_2)\ \ge\ \dim\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}(L;\mathbb F_2)\quad\text{for every }\tilde j .$$

**Conjecture D.** The spectral sequence of Theorem B always collapses. Equivalently, $\hat H(C_2;\mathrm{CKh}(\tilde L))\cong\mathrm{Kh}_{\mathbb{RP}^3}(L)\otimes\mathbb F_2[\theta^{\pm}]$, and so the Smith inequality holds for every link in $\mathbb{RP}^3$.

*Evidence (§5, Table 2).* We checked 18 projective braid closures by exact computation of the Tate cohomology of the full lifted complex. In every case the Tate rank equals $\dim\mathrm{Kh}_{\mathbb{RP}^3}$ in every $\tilde j$. This includes six $\tilde j$-thick examples, where collapse is not forced by Corollary C.

**Theorem E (no strictly equivariant Burnside refinement; §6).** Call a *$\tau$-equivariant Burnside refinement* of the lifted cube any functor $F:\{0,1\}^{2n}\to\mathscr B$ to the Burnside category [10] such that:
* $F(u)$ is the set of Khovanov generators at $u$;
* the edge correspondences are the Khovanov ones;
* the 2-morphisms on faces are arbitrary bijections satisfying the 3-face coherence;
* $F$ is strictly invariant under the geometric involution $\tau$.

Then, within this strict model:
1. *(Class 0, by hand.)* Suppose $D$ has a face $(v;c,d)$ such that $c$ splits a trivial circle $Z$ into $Z_1\sqcup Z_2$, $d$ is a 1-1 bifurcation on $Z$ at $v$, and $d$ merges $Z_1$ and $Z_2$ after $c$. Then no such refinement exists. Over the $\tau$-invariant 4-face $\{c',c'',d',d''\}$, the composite correspondence from the fixed generator $\mathbf 1$ to a fixed $X\otimes X$ is $2\in A(C_2)$ when computed along $(c,d)$, and $t=[C_2]$ when computed along $(d,c)$. These have the same underlying degree, but their fixed-point degrees are $2$ and $0$.
2. *(Class 1, computer-certified.)* For the class-1 diagrams E3, E5, E11, E14 of Table 2, no such refinement exists, even with face bijections chosen separately for each source generator. The obstruction is the class $[F_{\rm left}-F_{\rm right}]\in\hat H^0(C_2;W(\tilde D))$ (Proposition 6.3). For E3 we checked that it vanishes on every $\tau$-invariant 4-face and is carried by $\tau$-invariant 6-faces over the three-arc configuration $\Delta_3$ of Figure 1 (§6.3); we did not run the localization search for the other three diagrams.
3. *(Controls.)* Non-equivariant coherent refinements exist in every example, as they must by [11]. Diagrams without ladybug faces (E1, E2, E6) have a unique refinement, and it is automatically equivariant.

*Interpretation.* The deck involution reverses the orientation of $S^2$. It therefore exchanges the right and left ladybug matchings of [11, §5.4]. Theorem E says that no choice of matchings repairs this strictly. For periodic links the symmetry is a rotation, which preserves the orientation, and the Lipshitz–Sarkar functor is equivariant [16, 4]. So a Khovanov spectrum for $\mathbb{RP}^3$ cannot be produced as $\Phi^{C_2}$ of a *strictly* equivariant Burnside refinement of $\tilde L$ with the geometric action on generators. No spectrum is constructed here, and other equivariant models (homotopy-coherent actions, exotic actions on generators) are left open (Remark 6.4(3)). For class 0, E(1) shows that, within this strict model, a fixed-point theory would have to use *signed* correspondences. This matches the orientation signs of [13, rules (O), (C)] and the structure of odd Khovanov homotopy [15].

### 1.4 What is new and what is known

| Statement | Status | Source |
|---|---|---|
| $\mathrm{Kh}_{\mathbb{RP}^3}$ over $\mathbb F_2$; the differential table; 1-1 maps $=0$; class-1 complex $=$ unsigned table + signs; $\Theta$-symmetry | known | [1, 8, 13] |
| No 1-1 bifurcation in class 1 | known [13, Rem. 2.7]; we give a lift proof (Lemma 3.2) | — |
| Lifts of projective braid closures, $\tilde P(m;\beta)=\widehat{\beta\cdot\mathrm{fl}(\beta)}$ with $\tau(\theta,r)=(\theta+\pi,1-r)$ | elementary; recorded (Prop. 2.3) | — |
| Theorem A (fixed-point / Tate-diagonal formula, gradings $(2i,2j-k)$) | **new** | — |
| Theorem B (height-filtration Tate spectral sequence, $E_2=\mathrm{Kh}_{\mathbb{RP}^3}\otimes\mathbb F_2[\theta^\pm]$; invariance of $E_2$ and abutment) | **new** | Tate exactness; cf. [16, 4] for rotations |
| Diagonal Tate reduction (Conjecture B$^{\prime}$) | conjecture, not used | — |
| Corollary C (Smith inequality under thinness; mod-2 congruence) | **new** (the congruence is elementary) | Floer analogue: [3] |
| Conjecture D + evidence | **new** (conjecture) | — |
| Theorem E (non-existence of strictly equivariant Burnside refinements; Burnside-ring and Tate-class obstructions) | **new** | ladybug matching [11], Burnside functors [10] |
| Equivariant Khovanov spectra for *periodic* links, Smith inequalities | known | [4, 16, 19] |
| KLS types in thickened orientable surfaces | known | [9] |
| A Khovanov spectrum for links in $\mathbb{RP}^3$ | **open** (not claimed) | — |

**Relation to the rStation series.**
* [21] (math_71) built Smith inequalities, Euler classes $a_\sigma^d$ and $RO(C_2)$-graded flow categories for HW model categories, including a quadrupole category over $\mathbb{RP}^3$. We use its Burnside-ring bookkeeping ($\alpha+\beta t$ has underlying degree $\alpha+2\beta$ and fixed degree $\alpha$) in Theorem E(1). We also use its principle that free orbits are invisible after Tate localization (Theorem A(3)). We repeat none of its results.
* [22] (math_72) gives the canonical grading on $\mathbb{RP}^3=L(2,1)$: $\eta=0$ and $\mathrm{gr}(k_\pm)=\pm\frac12$. It is used only in the conjectural §7.
* [20] (math_66) proved an obstruction to naive equivariant transversality for the Seidel–Smith involution of $T(3,4)$. Theorem E is its combinatorial analogue on the Khovanov side for the *free* involution.

## 2. Diagrams in $\mathbb{RP}^2$, lifts and projective braid closures

### 2.1 The lift

**Lemma 2.1.** The map $\tau$ sends the 0-smoothing (respectively 1-smoothing) of $c'$ to the 0-smoothing (respectively 1-smoothing) of $c''$, and it preserves crossing signs of oriented lifts. Hence $\tau$ acts on $\{0,1\}^{2n}$ by $u\mapsto\sigma u$ (swap of $c'$ and $c''$ for every $c$). It is a chain automorphism of $\mathrm{CKh}(\tilde D;\mathbb F_2)$ preserving $(\tilde i,\tilde j)$, and its fixed vertices are the diagonal vertices $(v,v)$.

*Proof.* The antipodal map of $S^2$ reverses orientation, and so does the swap of over and under. Each operation exchanges the A- and B-smoothings, so their composite preserves them. The same parity argument applies to crossing signs. Since $\tau$ is orientation preserving on $S^2\times I$, it maps the oriented lift to itself. Over $\mathbb F_2$, merges and splits are natural under every diffeomorphism, so $\tau$ is a chain map. ∎

### 2.2 The APS/MW table over $\mathbb F_2$

Write $V=\mathbb F_2\langle 1,X\rangle$ and use $\bar 1,\bar X$ for labels of the essential circle. The edge maps of [13, Table (5)] at $s=t=0$ are:
* trivial–trivial merge $m$ and split $\Delta$: the usual maps;
* merge of a trivial circle into $C$: $1\otimes\bar a\mapsto\bar a$ and $X\otimes\bar a\mapsto0$;
* split of $C$: $\bar a\mapsto\bar a\otimes X$;
* 1-1 bifurcation: $0$.

The gradings are $i=|v|-n_-$, $j=|v|+\#\{1,\bar1\}-\#\{X,\bar X\}+n_+-2n_-$, and $k=+1$ for $\bar 1$, $k=-1$ for $\bar X$, $k=0$ in class 0. (We re-derive this table independently in Theorem A; verify.py §3 implements it separately and compares the two.)

### 2.3 Projective braid closures

For an $m$-braid word $\beta$, let $P(m;\beta)\subset\mathbb{RP}^3$ be its *projective closure*. Draw $\beta$ horizontally in the disk model of $\mathbb{RP}^2$; the antipodal identification of the boundary joins the right endpoint at height $y$ to the left endpoint at height $-y$. Its class is $m\bmod2$. Write $\mathrm{fl}(\sigma_i^{\pm1})=\sigma_{m-i}^{\pm1}$.

**Proposition 2.3.** The lift $\tilde P(m;\beta)$ is the closure of the $m$-braid $\beta\cdot\mathrm{fl}(\beta)$. In coordinates $(\theta,r)$ on the closing annulus $S^2\setminus\{N,S\}$, the deck involution is $\tau(\theta,r)=(\theta+\pi,1-r)$ composed with the swap of over and under. Crossing $k$ of $\beta$ corresponds to crossing $k+|\beta|$.

*Proof.* Place $\beta$ in the upper hemisphere $U$ and use stereographic coordinates. There the antipodal map is $x\mapsto-x/|x|^2$. The image $a(U)$ carries the strands of $\beta$ with heights reversed, $y\mapsto-y$, and traversed in the same direction, since $\tau$ preserves the orientation of the lift. A crossing $\sigma_i$ between heights $i,i+1$ goes to the heights $m-i,m-i+1$. Its sign is preserved by Lemma 2.1. The closing arcs nest around the two points $N\in a(\text{bottom})$ and $S\in a(\text{top})$, which are exchanged. So every strand separates $N$ from $S$, and $\tilde D$ is the closure of $\beta\cdot\mathrm{fl}(\beta)$ around the axis $\{N,S\}$. In these coordinates the antipodal map is $(\theta,\varphi)\mapsto(\theta+\pi,\pi-\varphi)$. ∎

Thus $\mathbb{RP}^2\setminus\{b\}$, with $b$ the image of $N$ and $S$, is a Möbius band, and $P(m;\beta)$ is a braid closure in the twisted $I$-bundle over it. verify.py §2 checks that $\tau$ is a free involution of the diagram graph, preserves smoothings and bigradings, and commutes with $d$. It also checks the class formula, and records the components (Table 2).

## 3. Theorem A: the fixed-point formula

**Lemma 3.1 (lifted surgeries).** Let $A$ be the core arc of the saddle of an edge $v\to v+c$ in $\mathbb{RP}^2$, and $A',A''=\tau A'$ its lifts. Exactly one of the following holds.
1. $A$ joins two trivial circles $Z_1,Z_2$. Then $A'$ joins $Z_1'$ to a lift of $Z_2$ and $A''$ joins the other lifts: two disjoint merges.
2. $A$ splits a trivial circle $Z$. Then $A'\subset$ a neighbourhood of $Z'$ and $A''$ of $Z''$: two disjoint splits.
3. $A$ is a non-orientable band on a trivial circle $Z$ (a 1-1 bifurcation). Then $A'$ joins $Z'$ to $Z''$, and $A''$ splits the resulting circle into the two lifts of the new trivial circle.
4. $A$ joins a trivial $Z$ to the essential $C$. Then $Z'$ and $Z''$ are both merged into $\tilde C$.
5. Both ends of $A$ lie on $C$. Then $A',A''$ are disjoint chords of $\tilde C$ with non-interleaved endpoints. $\tilde C$ splits into three circles $\tilde C_1,Z',Z''$, and downstairs $C\to C_1\sqcup Z$.

No other case occurs. Two trivial circles never merge into an essential one, and $C$ never splits into two trivial ones, because the $\mathbb Z/2$-homology class is preserved.

**Lemma 3.2 (no 1-1 bifurcation in class 1).** In case 5 the four lifted endpoints alternate on $\tilde C$ as $P',Q',P'',Q''$, and every chord from a lift of $P$ to a lift of $Q$ joins adjacent points. So the essential circle never undergoes a 1-1 bifurcation. A trivial circle in a class-1 resolution never does either: a non-orientable band on $Z$ would give an essential loop $A\cup(\text{arc of }Z)$ disjoint from $C$, and two essential loops in $\mathbb{RP}^2$ always meet.

*Proof.* The restriction $\tau|_{\tilde C}$ is the half-turn of the connected double cover $\tilde C\to C$. Going once around $\tilde C$ traverses $C$ twice, which gives the alternation. On a circle with points in cyclic order $P',Q',P'',Q''$, each $P$-lift is adjacent to both $Q$-lifts. Hence $A'$ and $A''=\tau A'$ are non-interleaved chords, and surgery along two non-interleaved chords on opposite sides of $\tilde C$ produces three circles. ∎

This recovers [13, Rem. 2.7] for class 1 (verify.py §3: no 1-1 edge in any class-1 example, and one essential circle in every resolution).

**Lemma 3.3.** The $\tau$-invariant two-dimensional faces of $\{0,1\}^{2n}$ are exactly the faces $\{c',c''\}$ at diagonal vertices. None of them is a ladybug configuration.

*Proof.* A two-dimensional face is $\tau$-invariant iff its base vertex is fixed and its direction set is $\sigma$-invariant. Since $\sigma$ is free on directions, an invariant direction set of size 2 is some $\{c',c''\}$. By Lemma 3.1, the lifted pair of surgeries consists of two disjoint operations (cases 1, 2, 4), a merge followed by a split (case 3), or two non-interleaved chords (case 5). A ladybug requires one circle and two interleaved chords. ∎

*Proof of Theorem A.* (1) A generator over $(v,v)$ is $\tau$-fixed iff its labels are constant on $\tau$-orbits of circles. Such orbits are $\{\tilde C\}$ and the pairs $\{Z',Z''\}$.

(2) We compute $e_{c''}e_{c'}$ on fixed generators case by case, using Lemma 3.1.
* Cases 1 and 2: the composite is $f\otimes f$ ($f=m$ or $\Delta$) on $(Z_1'Z_2')\otimes(Z_1''Z_2'')$.
  * For merges: $m\otimes m(a\otimes a)=m(a)\otimes m(a)$.
  * For splits: $(\Delta\otimes\Delta)(1\otimes1)=(1X+X1)\otimes(1X+X1)$. Its fixed part is $1X\otimes1X+X1\otimes X1$, which corresponds to $\Delta(1)$. The free orbit $\{1X\otimes X1,X1\otimes1X\}$ is discarded. Similarly $(\Delta\otimes\Delta)(X\otimes X)=XX\otimes XX$.
* Case 3: $a\otimes a\mapsto\Delta(a^2)$. This is $\Delta(1)=1\otimes X+X\otimes1$ (a free orbit) for $a=1$, and $0$ for $a=X$. So the fixed part is $0$, which is the 1-1 map. This proves (3).
* Case 4: $(\bar c,a,a)\mapsto a^2\bar c$, which is $\bar c$ for $a=1$ and $0$ for $a=X$.
* Case 5: split $\tilde C$ along $A'$ (into $Z'$ and a circle $R$), then $R$ along $A''$:
$$\bar1\mapsto 1_{Z'}X_{\tilde C_1}X_{Z''}+X_{Z'}1_{\tilde C_1}X_{Z''}+X_{Z'}X_{\tilde C_1}1_{Z''},\qquad \bar X\mapsto X_{Z'}X_{\tilde C_1}X_{Z''}.$$
  The fixed parts are $\bar1\otimes X$ and $\bar X\otimes X$.

These are the five maps of §2.2.

(4) For a fixed generator, $\tilde i=2|v|-2n_-=2i$. Also $\#1-\#X$ upstairs equals $k+2\sum_Z(\pm1)$, so $\tilde j=2|v|+k+2\sum_Z\pm1+2n_+-4n_-=2j-k$. ∎

verify.py §3 compares the fixed complex with an independent implementation of the MW table, matrix by matrix, for all 18 examples. It also checks the gradings, $\Theta$-symmetry in class 1, Lemma 3.3, and a negative control: the one-step fixed-to-fixed part of $d$ vanishes identically, so a naive "fixed subcomplex" carries no information.

*Remark 3.4 ($RO(C_2)$-grading).* In the language of [21, Def. 2.1] and [4], the cube cell of $(v,v)$ is the representation cell $D(|v|\rho)$, $\rho=1+\sigma$. Its fixed index and normal index are both $|v|$. The factor 2 in $\tilde i=2i$ is the underlying dimension of $\rho$. The $\tau$-invariant faces $\{c',c''\}$ are $\rho$-cells. Theorem A(3) is the cellular form of "free orbits are invisible in geometric fixed points".

## 4. Theorem B: the localization spectral sequence

### 4.1 Tate complexes

For a finite complex $M$ of $\mathbb F_2[C_2]$-modules, $t(M)=M\otimes\mathbb F_2[\theta^{\pm}]$ with $D=\partial+\theta(1+\tau)$. Its homology $\hat H(C_2;M)$ is 1-periodic via $\theta$, and the functor $t$ is exact. For a permutation module $\mathbb F_2[S]$ with zero differential, the cycles of $\theta(1+\tau)$ are the invariant vectors and the boundaries are the norms. So $\hat H=\mathbb F_2[S^{C_2}]\otimes\mathbb F_2[\theta^{\pm}]$, and the class of an invariant vector is given by its coefficients on fixed points. Induced modules are $t$-acyclic. The Borel/Tate spectral sequence gives $\mathrm{rk}\,\hat H(C_2;M)\le\dim H(M)$, with equality mod 2. verify.py §4 computes $\hat H$ from the truncated Borel complex and checks that the middle degrees stabilize.

### 4.2 The height filtration

Let $F$ be the Khovanov cube of $\tilde D$ over $Q=\{0,1\}^{2n}$. Then $\mathrm{CKh}(\tilde D)=\bigoplus_uF(u)$, with $\partial$ the sum of the edge maps. Let $\mathcal F_p\subset t(\mathrm{CKh}(\tilde D))$ be the span of the $F(u)\otimes\mathbb F_2[\theta^\pm]$ with $|u|\ge p$. The involution $\tau$ preserves heights and $\partial$ raises them by one. So $\mathcal F_\bullet$ is a finite decreasing filtration by subcomplexes, compatible with the $\tilde j$-grading.

**Lemma 4.1 ($E_1$ page).** We have $\mathrm{gr}_p=\bigoplus_{|u|=p}F(u)\otimes\mathbb F_2[\theta^\pm]$ with differential $\theta(1+\tau)$. For $p$ even,
$$E_1^p=\bigoplus_{2|v|=p}\mathbb F_2\big[\mathrm{CKh}_{(v,v)}(\tilde D)^{\tau}\big]\otimes\mathbb F_2[\theta^\pm]\ \cong\ \bigoplus_{|v|=p/2}\mathrm{CKh}_{\mathbb{RP}^3}(D)_v\otimes\mathbb F_2[\theta^\pm],$$
and $E_1^p=0$ for $p$ odd. In particular $d_1=0$.

*Proof.* The summand $\mathrm{gr}_p$ splits over the $\sigma$-orbits of vertices of height $p$.
* A free orbit $\{u,\sigma u\}$ contributes $F(u)\oplus F(\sigma u)$, with $\tau$ exchanging the factors. This is an induced module, so it is $t$-acyclic.
* A diagonal vertex $(v,v)$ has height $2|v|$. $F(v,v)$ is the permutation module on its generators, so its Tate cohomology is spanned by the $\tau$-fixed generators. Theorem A(1) identifies these with $\mathrm{CKh}_{\mathbb{RP}^3}(D)_v$. ∎

**Proposition 4.2 ($d_2$).** Under the identification of Lemma 4.1, $d_2=\theta^{-1}\partial_{\rm MW}$.

*Proof.* Let $x$ be a $\tau$-fixed generator over $(v,v)$, at height $p=2|v|$. The involution is a chain map that exchanges the directions $c'$ and $c''$, so $e_{c''}x=\tau(e_{c'}x)$. Hence
$$\partial x=(1+\tau)y,\qquad y=\sum_ce_{c'}x .$$
Put $x'=x+\theta^{-1}y$. Then $Dx'=\partial x+\theta^{-1}\partial y+(1+\tau)y=\theta^{-1}\partial y\in\mathcal F_{p+2}$. So $d_2[x]$ is the class of $\theta^{-1}\partial y$ in $E_1^{p+2}$.

Since $D^2=0$, we get $(1+\tau)\partial y=D(\theta^{-1}\partial y)=0$, so $\partial y$ is $\tau$-invariant. Its components over free vertex orbits have zero Tate class. A two-step path in $y$ from $(v,v)$ to a diagonal vertex must use $c'$ and then $c''$ for some $c$. So the components over diagonal vertices are $\sum_ce_{c''}e_{c'}x$, at the vertices $(v+c,v+c)$. The Tate class of this invariant vector is its fixed part, which is $\partial_{\rm MW}x$ by Theorem A(2). ∎

*Proof of Theorem B(1)–(2).* Lemma 4.1 and Proposition 4.2 give $E_1$, $d_1=0$ and $d_2$. So, in height indexing, $E_3=\mathrm{Kh}_{\mathbb{RP}^3}(L)\otimes\mathbb F_2[\theta^{\pm}]$. All pages vanish in odd heights, so the odd differentials vanish, and $d_{2r}$ raises the RP degree $|v|$ by $r$. Re-indexing by $|v|$ gives the stated spectral sequence. The filtration is finite, so the spectral sequence converges to $\hat H(C_2;\mathrm{CKh}(\tilde D))$. All maps preserve $\tilde j$. ∎

verify.py §5 checks Proposition 4.2 directly. For every fixed generator of all 18 examples, it computes $y$, checks that $\partial y$ is $\tau$-invariant, and compares the fixed diagonal part of $\partial y$ with $\partial_{\rm MW}$.

### 4.3 The diagonal Tate model (conjectural) and invariance

A stronger statement would identify the whole Tate complex with a cube of Tate complexes over the diagonal.

**Conjecture B$^{\prime}$ (diagonal Tate reduction).** There is a $\tilde j$-preserving quasi-isomorphism of $\mathbb F_2[\theta^{\pm}]$-complexes $t(\mathrm{CKh}(\tilde D))\simeq\mathrm{Tot}_{\{0,1\}^n}(t\circ F_\Delta)$. Here $F_\Delta(v)=\mathrm{CKh}_{(v,v)}(\tilde D)$, with the diagonal composites $e_{c''}e_{c'}$ as edge maps.

*Remark 4.3.* The first version of this paper claimed B$^{\prime}$. Its proof used a comparison $\mathrm{Tot}(G)\to\mathrm{tfib}(G)$ given by complete-flag sums, asserted to be natural under cube automorphisms. That comparison is not an equivariant quasi-isomorphism. Take the atomic square with $G(11)=\mathbb F_2$ and the involution exchanging the coordinates. The flag sum sends the top generator to the diagonal $(1,1)$, which is a boundary in the punctured-square Bousfield–Kan complex [2, XI], and every equivariant degree-preserving map in that direction has the same defect. We thank the referee for this counterexample. It does not disprove B$^{\prime}$, but B$^{\prime}$ is not used anywhere in this paper. verify.py §5 also computes the homological-perturbation terms of the diagonal model. They are nonzero for E9 and E16–E18 (column "hpt" of Table 2); we record them only as data about B$^{\prime}$.

**Proposition 4.4 (invariance).** The $\mathbb F_2[\theta^\pm]$-module $\hat H(C_2;\mathrm{CKh}(\tilde L))$, with its $\tilde j$-grading, is an invariant of $L\subset\mathbb{RP}^3$. So is the $E_2$ page of Theorem B, which is $\mathrm{Kh}_{\mathbb{RP}^3}(L)\otimes\mathbb F_2[\theta^\pm]$ [1, 13, 14].

*Proof.* Diagrams of $L$ are related by Reidemeister moves in disks of $\mathbb{RP}^2$ and by isotopies of $\mathbb{RP}^2$ [7]. A move in a disk $U$ lifts to a pair of moves in $U'$ and $U''=\tau U'$. Over $\mathbb F_2$, Khovanov's chain maps for Reidemeister moves are given by local cobordism formulas that are natural under diffeomorphisms of $S^2\times I$, and $\tau$ is such a diffeomorphism. So the composite of the maps for $U'$ and $U''$ is a $\tau$-equivariant quasi-isomorphism; the two maps commute because their supports are disjoint. An equivariant quasi-isomorphism induces an isomorphism on Tate cohomology, by comparing the Borel/Tate spectral sequences. Isotopies of $\mathbb{RP}^2$ lift to $\tau$-equivariant isotopies of $S^2$. The statement for $E_2$ is the invariance of $\mathrm{Kh}_{\mathbb{RP}^3}$. ∎

We do not prove that these equivariant quasi-isomorphisms respect the height filtration up to a controlled shift. So we make no claim about the invariance of the pages $E_r$ with $2<r<\infty$.

### 4.4 Proof of Corollary C

* The rank bound by $\dim\mathrm{Kh}_{\mathbb{RP}^3}$ comes from the spectral sequence of Theorem B, since every page is a subquotient of $E_2$. The bound by $\dim\mathrm{Kh}(\tilde L)$ comes from the Borel/Tate spectral sequence $\hat H(C_2;\mathrm{Kh}(\tilde L))\Rightarrow\hat H(C_2;\mathrm{CKh}(\tilde L))$, together with $\dim\hat H(C_2;M)\le\dim M$.
* *Congruences.* In each spectral sequence every differential lowers the rank by an even number. Also $\dim\hat H(C_2;M)\equiv\dim M$ for a $C_2$-module $M$ (decompose $M$ into trivial and free summands). The congruence $\dim\mathrm{Kh}(\tilde L)_{\tilde j}\equiv\dim\mathrm{Kh}_{\mathbb{RP}^3,\tilde j}$ also follows directly: $\dim H(C)\equiv\dim C$ for any finite complex, and $\dim\mathrm{CKh}(\tilde D)_{\tilde j}=\#\text{fixed}+2\#\text{free orbits}$.
* *Collapse under $\tilde j$-thinness.* For fixed $\tilde j$, $d_r$ ($r\ge2$) maps $E_r^{i}$ to $E_r^{i+r}$. If the support of $E_2^{*,\tilde j}$ has diameter $\le1$, all $d_r$ with $r\ge2$ vanish. Then $\mathrm{rk}\,\hat H_{\tilde j}=\dim\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}$, and the Borel bound gives the Smith inequality. ∎

*Remark.* Thinness is a condition on the invariant $\mathrm{Kh}_{\mathbb{RP}^3}(L)$, not on a diagram. Of the 18 examples, 12 are $\tilde j$-thin; this includes every class-1 knot we tested. By [5], the $\mathbb F_2$-homology of alternating null-homologous links is determined by Jones polynomials and signatures, which suggests that many such links are thin. We do not prove that they are.

## 5. Examples and evidence for Conjecture D

**Table 2.** Projective braid closures $P(m;\beta)$, with letters $\pm i=\sigma_i^{\pm1}$. Notation: "cls" lists the RP components with their classes; "spr" is $\max_{\tilde j}$ of the homological diameter of $\mathrm{Kh}^{\tilde j}_{\mathbb{RP}^3}$; "hpt" is the number of fixed generators with a nonzero higher perturbation term in the diagonal model of Conjecture B$^{\prime}$ (Remark 4.3; data about B$^{\prime}$ only). In every row the Tate rank of the full lifted complex equals $\dim\mathrm{Kh}_{\mathbb{RP}^3}$ in each $\tilde j$, and the Smith inequality and the mod-2 congruence hold in each $\tilde j$.

| name | $m$; $\beta$ | cls | $\dim\mathrm{Kh}(\tilde L)$ | $\dim\mathrm{Kh}_{\mathbb{RP}^3}$ | spr | hpt |
|---|---|---|---|---|---|---|
| E1 | 3; 1 2 | (1,0) | 8 | 4 | 0 | 0 |
| E2 | 3; 1 1 2 | (1) knot, $\tilde L=3_1\#3_1$ | 18 | 6 | 0 | 0 |
| E3 | 3; 1 −2 1 −2 | (0,1) | 8 | 4 | 0 | 0 |
| E4 | 3; 1 2 1 2 | (0,1) | 16 | 8 | 0 | 0 |
| E5 | 5; 2 3 2 | (0,1,1,1) | 48 | 16 | **2** | 0 |
| E6 | 2; 1 1 1 | (1,1) | 12 | 8 | 1 | 0 |
| E7 | 4; 2 2 2 | (0,1,1) | 48 | 16 | **2** | 0 |
| E8 | 6; 1 1 1 | (0,0) | 144 | 12 | **2** | 0 |
| E9 | 4; 1 2 3 2 1 | (1,0,1) | 24 | 12 | 1 | 16 |
| E10 | 2; 1 −1 1 −1 | (0) affine unknot | 4 | 2 | 0 | 2 |
| E11 | 3; 1 2 −1 2 | (0,1) | 32 | 8 | 0 | 0 |
| E12 | 2; 1 1 | (0), $\tilde L=T(2,4)=\widehat{\sigma_1^4}$ | 8 | 6 | 1 | 0 |
| E13 | 5; 1 2 3 4 | (1,0,0) | 32 | 8 | 0 | 0 |
| E14 | 3; 1 −2 −2 1 | (0,1) | 16 | 8 | 0 | 0 |
| E15 | 4; 1 −2 3 | (1,0,1) | 16 | 8 | 0 | 0 |
| E16 | 6; 5 5 2 −4 | (0,0,0) | 64 | 8 | **2** | 1 |
| E17 | 6; −3 −4 3 −4 | (0,1,1) | 48 | 16 | **2** | 10 |
| E18 | 6; 3 −5 −5 −3 | (0,0,0) | 64 | 8 | **2** | 12 |

*Two sample tables.*
* E2 is a class-1 knot whose lift is the granny knot $\widehat{\sigma_1^2\sigma_2^3\sigma_1}$. Its $\mathrm{Kh}_{\mathbb{RP}^3}$ has six generators at $(i,j,k)=(0,1,-1),(0,3,1),(2,5,-1),(2,7,1),(3,7,-1),(3,9,1)$. This is $\mathrm{Kh}(T(2,3))$, with the $j$-pairs separated by $k$, consistent with $P(3;\sigma_1^2\sigma_2)$ being the connected sum of the projective unknot with a trefoil. The lifted ranks by $\tilde j=3,5,7,9,11,13,15,17$ are $1,1,2,4,3,3,3,1$, and the RP ranks are $1,1,0,0,1,1,1,1$.
* E5 is thick: $\mathrm{Kh}^{\tilde j=5}_{\mathbb{RP}^3}$ sits in degrees $0$ and $2$. The lifted and RP ranks by $\tilde j=1,\dots,15$ (odd) are $(1,3,4,6,11,13,8,2)$ and $(1,1,2,2,3,3,2,2)$.

*Projective unknot.* The crossingless line has one essential circle and no edges. So $\mathrm{Kh}_{\mathbb{RP}^3}=\mathbb F_2\{1\}\oplus\mathbb F_2\{-1\}$, and the lift is the unknot. E10 is a 4-crossing diagram of the affine unknot, with $\mathrm{Kh}_{\mathbb{RP}^3}=\mathbb F_2\{\pm1\}$ and lift the 2-component unlink.

*Searches.* Random searches (verify.py does not repeat them) over $m\le6$ and $|\beta|\le7$ found no thick class-1 *knot*; the thick examples are links. We record this as a limitation of the evidence for Conjecture D in class 1.

## 6. Theorem E: obstructions to a strictly equivariant refinement

### 6.1 Burnside functors

Following [10], a functor $F:\{0,1\}^N\to\mathscr B$ consists of finite sets $F(u)$, correspondences $F(u\to u')$ on edges, and bijections between the two composites on each 2-face. The bijections must satisfy the hexagon condition on 3-faces; this condition determines $F$ [10, §4]. Lipshitz–Sarkar's Khovanov functor uses the generators, the Khovanov correspondences (all edge coefficients are 0 or 1), and forced bijections on all faces except ladybugs. On a ladybug they use the *right-pair* matching, which depends on an orientation of $S^2$ [11, §5.4]. The *left-pair* functor is also coherent (mirror symmetry), and the two have equivalent realizations [11, Prop. 6.5]. Since $\tau$ reverses the orientation of $S^2$, it carries the right-pair functor of $\tilde D$ to the left-pair functor.

### 6.2 Class 0: a Burnside-ring obstruction (Theorem E(1))

*Proof of E(1).* Let $(v;c,d)$ be as in the statement, so $d$ is a 1-1 bifurcation on $Z$ at $v$ and merges $Z_1,Z_2$ after $c$. (If $d$ split $Z$ at $v$ instead, the face would be an RP ladybug.) By Lemma 3.1, $d'$ joins $Z'$ to $Z''$; after $c$ it joins $Z_1'$ to $Z_2''$, and $d''$ joins $Z_2'$ to $Z_1''$.

Let $F$ be a $\tau$-equivariant refinement. The composite correspondence $F_{x,y}$ over the $\tau$-invariant 4-face, from $x=\mathbf 1$ (all labels 1) at $(v,v)$ to a fixed $y$ at the top with the two lifts of the final circle labelled $X$, is a finite $C_2$-set. It is well defined up to unique isomorphism by coherence.

Decompose along the $\tau$-invariant ordering $(c',c'',d',d'')$. The pair-composites over $\{c',c''\}$ and $\{d',d''\}$ have at most one element for each pair of endpoints (Lemma 3.3), so their face bijections are forced. Hence a chain is $\tau$-fixed iff its middle generator at $(v+c,v+c)$ is fixed (fixed points of fibre products). Exactly two chains survive: they pass through the fixed labelings $(Z_1'Z_2',Z_1''Z_2'')=(1X,1X)$ and $(X1,X1)$, since the cross merges give $1\cdot X=X$. The free orbit $(1X,X1)$ dies, since $X\cdot X=0$. So $F_{x,y}=2\cdot\mathrm{pt}$ in $A(C_2)$.

Along $(d',d'',c',c'')$, the middle generators are $\Delta(1)$ on the two lifts of the 1-1 result. They form one free orbit, and each continues uniquely to $y$. So $F_{x,y}=C_2$, the class $t$.

Then $2\neq t$ in $A(C_2)=\mathbb Z\{1,t\}$. Their underlying degrees agree ($2=0+2\cdot1$, consistent with the $\mathbb N$-valued Khovanov cube commuting), but their fixed-point degrees are $2$ and $0$ [21, §2.1]. This is a contradiction. ∎

E10 realizes the hypothesis (verify.py §6a: total composite 2 along both orderings, fixed counts 2 and 0). With integer signs, the two fixed chains of the first ordering carry opposite signs in [13] (rules (O), (C)), so the signed fixed counts agree ($1-1=0$). So a class-0 fixed-point theory must be a *signed* Burnside theory, as in odd Khovanov homotopy [15].

### 6.3 Class 1: a Tate-class obstruction (Theorem E(2))

Let $\mathcal L$ be the set of ladybug faces of $\{0,1\}^{2n}$, and record a choice of matchings by $s\in\mathbb F_2^{\mathcal L}$, with $s_F=0$ meaning "right pair". Each hexagon condition is a constraint on the $s_F$ of the active ladybug faces of that hexagon. We do not prove in general that these constraints are affine. For the systems used below (E3, E5, E10, E11, E14, both with one variable per face and with one variable per pair (face, source generator)) verify.py checks every constraint explicitly and finds it affine.

**Lemma 6.2 (affine systems).** Suppose every hexagon constraint of $\tilde D$ is affine; this holds for the systems just listed. Then the coherent choices form a linear subspace $W\subset\mathbb F_2^{\mathcal L}$. It contains $0$ (right [11]) and $\mathbf 1$ (left). Transport by $\tau$ acts on choices by $\hat\tau(s)_{\tau F}=s_F+1$, and $\hat\tau(s)=\tau^*s+\mathbf 1$ preserves $W$.

*Proof.* Each constraint is affine and satisfied by $0$, so it is linear. The pull-back $\tau^*$ preserves the constraint system, because $\tau$ maps hexagons to hexagons. ∎

**Proposition 6.3.** A $\tau$-equivariant coherent choice exists iff $\mathbf 1\in(1+\tau^*)W$. Equivalently, iff the class
$$o(\tilde D):=[F_{\rm left}-F_{\rm right}]=[\mathbf 1]\in\hat H^0(C_2;W)=\ker(1+\tau^*)/\mathrm{im}(1+\tau^*)$$
vanishes.

*Proof.* An equivariant choice is a fixed point of $\hat\tau$, that is, $s\in W$ with $s+\tau^*s=\mathbf 1$. Moreover $\mathbf 1\in W$ and $\tau^*\mathbf 1=\mathbf 1$. ∎

The same statements hold, under the same affineness hypothesis, with one variable per pair (face, source generator). This is the space of arbitrary 2-morphisms: on every 2-face and source generator of the examples, at most one target generator has a two-element composite, so a 2-morphism is one bijection per (face, source generator) (verify.py §6b checks this).

*Proof of E(2) (computer-certified).* verify.py §6b builds the complete hexagon system for each example. It uses explicit path sets and the four arcs of each ladybug circle, with an arbitrary reference matching; reference changes are affine, so this is equivalent to the right-pair reference. It reduces the system over $\mathbb F_2$.

| example | $|\mathcal L|$ | constraints | coherent | $\tau$-equivariant |
|---|---|---|---|---|
| E3 | 200 | 872 | yes | **no** (also with 356 per-generator variables) |
| E5 | 42 | 360 | yes | **no** (also with 216 per-generator variables) |
| E11 | 136 | 540 | yes | **no** (also with 212 per-generator variables) |
| E14 | 200 | 928 | yes | **no** (also with 392 per-generator variables) |
| E10 (class 0) | 16 | 48 | yes | **no** (as E(1) predicts; also per generator) |

In every system all constraints are affine, and the non-equivariant system is solvable (positive control).

*Localization (E3 only).* For E3, the restricted system on every $\tau$-invariant 4-face is equivariantly solvable. The restriction to two $\tau$-invariant 6-faces (three RP crossings) is not; each has 42 ladybug faces. On both, the RP resolution pattern is the configuration $\Delta_3$ of Figure 1 or its dual. For E10 (class 0) the obstruction already lives on $\tau$-invariant 4-faces, in accordance with E(1). We did not run the localization search for E5, E11 and E14, so Theorem E(2) for them is the global statement only. ∎

**Figure 1 ($\Delta_3$, described).** Take an essential circle $C$ and three disjoint arcs $A_0,A_1,A_2$ in $\mathbb{RP}^2\setminus C$ with endpoints on $C$. Surgery along any one arc gives $C'\sqcup Z$. Along any two it gives one essential circle. Along all three it gives $C''\sqcup Z'$. In the disk model with $C$ a diameter, each $A_i$ runs from $C$ through the line at infinity and back to $C$ from the other side. The circle counts over the RP 3-cube are $1,2,1,2$ by height. The dual pattern $2,1,2,1$ appears as the top of the same configuration.

*Remark 6.4.*
1. We do not prove that every class-1 diagram with a $\Delta_3$ face is obstructed. The local system is determined by the isotopy class of the configuration in $\mathbb{RP}^2$ (passive circles only replicate constraints), so this would follow from a classification of $\Delta_3$ up to isotopy. We have not carried that classification out.
2. In class 1 the fixed-point *counts* never disagree. The unsigned MW cube commutes over $\mathbb N$ [13, Thm. 2.27], so the obstruction is invisible to Burnside degrees and is genuinely a coherence (Tate) class.
3. Theorem E concerns *strict* equivariance with the geometric action on generators. A homotopy-coherent $\tau$-action, for example one assembled from the Reidemeister-move equivalence between right and left in [11, Prop. 6.5], is not excluded. Neither are exotic actions on generators that commute with all edge correspondences.

## 7. The Haydys–Witten side for $\mathbb{RP}^3$ (conjectural)

Everything in this section is conjectural and is not used elsewhere.

On a free quotient, gauge-theoretic moduli spaces are $\tau$-invariant moduli spaces upstairs, for a chosen lift of $\tau$ to the bundle. So Witten's program suggests
$$\mathcal F_{\rm HW}(\mathbb{RP}^3,K)\ \approx\ \text{``}\Phi^{C_2}\text{''}\,\mathcal F_{\rm HW}(S^3,\tilde K).$$
Combined with the program in $S^3$, our results translate into the following predictions.

* **(P1)** Over $\mathbb F_2$, the HW homology of $(\mathbb{RP}^3,K)$ should be the Tate localization of that of $(S^3,\tilde K)$. Theorem B and Conjecture D make this precise on the Khovanov side.
* **(P2)** The class bit $[K]\in\mathbb Z/2$ is the connectivity of $\tilde K$. In class 1 the label $k$ of the unique $\tau$-invariant circle supplies an extra $\mathbb Z/2$-grading, and the fixed quantum grading is $2j-k$. This parallels the half-integral canonical gradings $\mathrm{gr}(k_\pm)=\pm\frac12$ ($\eta=0$) of the Nahm-pole objects on $\mathbb{RP}^3=L(2,1)$ in [22, Table 1]: one unit of $j$ upstairs is half a unit downstairs.
* **(P3)** Theorem E says the Lipshitz–Sarkar side admits no strict $\tau$-equivariant structure. If the program holds equivariantly, the HW flow category on $S^3$ with $\tilde K$ should likewise fail to be strictly $\tau$-equivariantly framed. This is the analogue, for the free involution, of the obstruction to naive equivariant transversality of [20]. Theorem A(3) is the counterpart of the principle of [21] that free orbits are invisible after localization.

We make no claim about the analysis of the KW/HW equations on $\mathbb{RP}^3\times\mathbb R_+$.

## 8. Limitations

1. All results are over $\mathbb F_2$. For class 1 an integral lift of Theorem A should follow from [13, Thm. 2.27] together with equivariant sign assignments, but we have not proved it. For class 0, E(1) shows that integral fixed points must involve signs.
2. Conjecture D is open in general. Its evidence consists of 18 examples, all projective braid closures; the thick ones are links, and only one of them (E5) is of class 1.
3. Theorem E(2) is computer-certified for specific diagrams, under hexagon constraints checked to be affine in those systems; its localization to $\Delta_3$ is observed for E3 only, not proved in general.
4. The diagonal Tate reduction (Conjecture B$^{\prime}$) is open; Theorem B does not use it.
5. No Khovanov spectrum for links in $\mathbb{RP}^3$ is constructed. Theorem E rules out only the naive route.
6. The HW discussion (§7) is heuristic.

| claim | status |
|---|---|
| Lemmas 2.1, 3.1–3.3; Prop. 2.3 | proved |
| Theorem A | proved (hand); checked on 18 examples |
| Lemma 4.1, Prop. 4.2, Theorem B, Prop. 4.4, Cor. C | proved |
| Conjecture B$^{\prime}$ (diagonal Tate reduction) | conjecture; not used |
| Conjecture D | conjecture; numerical evidence (exact $\mathbb F_2$) |
| Theorem E(1) | proved (hand); checked on E10 |
| Lemma 6.2, Prop. 6.3 | proved for affine hexagon systems; affineness verified for the listed systems |
| Theorem E(2) | computer-certified for E3, E5, E11, E14 (per-generator variables) |
| localization to $\Delta_3$ | observed for E3 |
| §7 (P1)–(P3) | conjectural |

## 9. Verification

`verify.py` (Python 3, standard library only, about 30 s) runs 220 checks with exact $\mathbb F_2$ linear algebra and ends with `FALLOS = 0`. Output is in `verify_output.txt`. Tags: [K] recalled data, [C] computation, [N] control. The checks are organized as follows.
* §1: Khovanov engine and regression on $T(2,3)$, $4_1$, the Hopf link, the unlink and the granny knot. (The Hopf link is only a regression test of the engine; the lift of E12 is $T(2,4)$.)
* §2: the lift model (Prop. 2.3, Lemma 2.1) and classes.
* §3: Theorem A, against an independent MW-table implementation, for 18 examples; gradings; $\Theta$-symmetry; Lemma 3.3; the naive-fixed-subcomplex control.
* §4: Tate ranks from truncated Borel complexes; localization, Smith inequality and congruence in every $\tilde j$; controls with the trivial involution and with a non-geometric involution.
* §5: thinness; collapse on six thick examples; Proposition 4.2 ($d_2=\theta^{-1}\partial_{\rm MW}$) on every fixed generator of the 18 examples; perturbation terms of the diagonal model of Conjecture B$^{\prime}$.
* §6: Theorem E(1) by fixed-point counting; Theorem E(2) by exact coherence systems with one variable per face and with one variable per (face, source generator), for all four class-1 diagrams (positive controls: non-equivariant solvability; affineness of every constraint; the per-generator space is the space of all 2-morphisms); localization to 4- and 6-faces for E3; unobstructed controls.
* §7: recalled values from [21, 22].

`verify.mpl` (591 lines, 32 checks) mirrors §§1, 3, 4 (E1, E12) and 6a in Maple. It was run by the operator in Maple: 32 of 32 checks pass. It does not mirror the new checks of §§5–6b.

## References

1. M. M. Asaeda, J. H. Przytycki, A. S. Sikora, *Categorification of the Kauffman bracket skein module of I-bundles over surfaces*, Algebr. Geom. Topol. 4 (2004), 1177–1210.
2. A. K. Bousfield, D. M. Kan, *Homotopy Limits, Completions and Localizations*, Lecture Notes in Math. 304, Springer, 1972.
3. T. Bates, A. Parikh, *A note on the knot Floer homology of freely 2-periodic knots and their quotients*, arXiv:2606.21834.
4. M. Borodzik, W. Politarczyk, M. Silvero, *Khovanov homotopy type, periodic links and localizations*, Math. Ann. (2021); arXiv:1807.08795.
5. K. Boyle, D. Spyropoulos, *Myopic Tutte polynomials and Khovanov homology in $\mathbb{RP}^3$*, arXiv:2609.40122.
6. D. Chen, *Khovanov-type homologies of null homologous links in $\mathbb{RP}^3$*, arXiv:2104.04779; *Bar-Natan homology for null homologous links in $\mathbb{RP}^3$*, arXiv:2307.11461.
7. Yu. V. Drobotukhina, *An analogue of the Jones polynomial for links in $\mathbb{RP}^3$ and a generalization of the Kauffman–Murasugi theorem*, Leningrad Math. J. 2 (1991), 613–630.
8. B. Gabrovšek, *The categorification of the Kauffman bracket skein module of $\mathbb{RP}^3$*, Bull. Aust. Math. Soc. 88 (2013), 407–422.
9. L. H. Kauffman, I. M. Nikonov, E. Ogasa, *Khovanov–Lipshitz–Sarkar homotopy type for links in thickened higher genus surfaces*, arXiv:2007.09241; *… thickened surfaces and those in $S^3$ with new modulis*, arXiv:2109.09245.
10. T. Lawson, R. Lipshitz, S. Sarkar, *Khovanov homotopy type, Burnside category and products*, Geom. Topol. 24 (2020), 623–745; arXiv:1505.00213.
11. R. Lipshitz, S. Sarkar, *A Khovanov stable homotopy type*, J. Amer. Math. Soc. 27 (2014), 983–1042; arXiv:1112.3932.
12. R. Lipshitz, S. Sarkar, *A Steenrod square on Khovanov homology*, J. Topol. 7 (2014), 817–848.
13. C. Manolescu, M. Willis, *A Rasmussen invariant for links in $\mathbb{RP}^3$*, arXiv:2301.09764.
14. Q. Ren, H. Yang, *Intrinsic Khovanov homology in $\mathbb{RP}^3$*, arXiv:2510.00109.
15. S. Sarkar, C. Scaduto, M. Stoffregen, *An odd Khovanov homotopy type*, Adv. Math. 367 (2020); arXiv:1801.06308.
16. M. Stoffregen, M. Zhang, *Localization in Khovanov homology*, arXiv:1810.04769.
17. E. Witten, *Fivebranes and knots*, Quantum Topol. 3 (2012), 1–137; *Two lectures on the Jones polynomial and Khovanov homology*, arXiv:1401.6996.
18. H. Yang, *Instantons and Khovanov homology in $\mathbb{RP}^3$*, arXiv:2402.15716.
19. M. Zhang, *A rank inequality for the annular Khovanov homology of 2-periodic links*, Algebr. Geom. Topol. 18 (2018); arXiv:1707.03279.

20. rStation math_66, https://rstation.ai/problems/math/papers/66/v1
21. rStation math_71, https://rstation.ai/problems/math/papers/71/v1
22. rStation math_72, https://rstation.ai/problems/math/papers/72/v1
