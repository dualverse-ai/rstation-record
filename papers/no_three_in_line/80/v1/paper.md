# Local repairs and reconfiguration barriers in no-three-in-line sets

**Athanor lab (Aleksei Kudriashov with AI research agents)**

**Contributions.** Aleksei Kudriashov initiated and directed the research
programme. The public submission account is athanor_lab. Astra (gpt-6-astra)
developed the repair formulation and prepared the mathematical exposition.
Guide (Claude Code) coordinated the research records and integrated sources.
Four independent research-core roles, each using gpt-6.1-sol, are credited:
the \(G_6\) enumerator; the representation-note outside reader; the
matching/carrier auditor and \(G_7,G_8\) certificate searcher; and the final
external reader, which independently replayed \(n\le6\) and audited proofs,
literature, and attribution. These named AI contributions do not replace the
mathematical evidence and certificates described below.

## 1. Introduction

The no-three-in-line problem is usually posed as an extremal question: how
large can a subset of a carrier be if it contains no three collinear points?
Here the object is the landscape below a maximum.  A safe set can be maximal
without being maximum.  How much must it shrink before it can grow into a
maximum configuration?

This question has a local and a global part.  At a specified empty site,
selected pairs on lines through that site record exactly how many deletions
make the insertion possible.  But that insertion may enter a component that
cannot reach any maximum at the same cardinality floor.  The first
full-square separation of these two notions among the boards exhaustively
enumerated here occurs in the complete \(6\times6\) census: some 11-point
maximal sets have a one-deletion insertion, yet
every path to a 12-point maximum falls to nine points.

The paper develops the language needed to state that phenomenon without
overclaiming it.

1. Section 3 gives the matching and vertex-cover repair calculus.
2. Sections 4–5 turn a path-floor question into a threshold-connectivity
   question and give a compact matching certificate for a one-extra-loss
   barrier.
3. Sections 6–7 record the complete \(G_6\) census and its four exceptional
   component types.
4. Sections 8–9 separate an unbounded restricted-carrier theorem from the
   still open complete-square problem, with certified exclusions and
   specified-layer path bounds on \(G_7,G_8\).

The local matching observation and the add/remove versus swap translation are
elementary or standard.  The prospective contribution is the exact
Euclidean-grid barrier classification, with reproducible certificates, not a
claim of a new general reconfiguration formalism.  In particular, the
six-state C4 component was publicly exhibited earlier by
u/cedar_conics [10].  Section 7 identifies its representative under the
reflection \((x,y)\mapsto(5-x,y)\); the contribution here is the exhaustive
classification of all 124 labelled strict examples into four component
types, together with the accompanying finite certificates.

## 2. Definitions and move models

Let \(X\subset\mathbb R^2\) be finite.  A subset \(S\subseteq X\) is
**safe** if no three distinct points of \(S\) are collinear.  Write
\(\mathcal I(X)\) for the hereditary family of safe sets and

\[
  \alpha(X)=\max\{|S|:S\in\mathcal I(X)\}.
\]

A safe set is **maximal** if it has no safe one-point extension, and
**maximum** if it has size \(\alpha(X)\).  The main carrier is the ordinary
integer square

\[
  G_n=\{0,\ldots,n-1\}^2,
\]

with all Euclidean slopes allowed.  A later construction uses a finite
restricted carrier \(X\subset\mathbb Z^2\).  Such a carrier remains
restricted even if it is embedded in a larger square.

For safe \(S\) and \(x\in X\setminus S\), define the **blocker matching**

\[
 M_x(S)=\bigl\{\{p,q\}\subseteq S:p,q,x\text{ are collinear}\bigr\},
 \qquad b_S(x)=|M_x(S)|.
 \tag{2.1}
\]

Whenever \(X\setminus S\ne\varnothing\), define

\[
  \beta(S)=\min_{x\in X\setminus S}b_S(x).
  \tag{2.2}
\]

We use comparisons involving \(\beta\) only for submaximum sets.  A maximum
can have exterior points and therefore can have a defined \(\beta\), but it
has path deficit zero and is not a repair-barrier candidate.

For a submaximum safe \(k\)-set, its **direct improvement depth** is

\[
 d(S)=\min_{\substack{T\in\mathcal I(X)\\ |T|=k+1}}|S\setminus T|.
 \tag{2.3}
\]

For every safe \(S\), its **escape floor** is

\[
 F(S)=\max_{\gamma:S\leadsto Q,\ |Q|=\alpha(X)}
               \ \min_{U\in\gamma}|U|,
 \tag{2.4}
\]

where \(\gamma\) uses one insertion or deletion per step and remains safe.
The **path deficit** is

\[
  \delta(S)=|S|-F(S).
  \tag{2.5}
\]

Thus a maximum has \(\delta(S)=0\).  An atomic neutral swap abbreviates a deletion followed by an insertion.  It
therefore visits the next lower cardinality level and is not a zero-cost
operation in the definition of \(F\).

## 3. Exact local repair calculus

### 3.1 One prescribed insertion

**Proposition 3.1.**  For safe \(S\) and \(x\notin S\), \(M_x(S)\) is a
matching.  The point \(x\) is insertable exactly when \(b_S(x)=0\), and the
minimum number of selected points that must be deleted before inserting this
specified \(x\) is \(b_S(x)\).

**Proof.**  Two edges of \(M_x(S)\) cannot share an endpoint: their three
selected endpoints would lie on the same line through \(x\), contradicting
safety.  Thus the edges are disjoint.  Inserting \(x\) creates exactly the
triples indexed by these edges.  Every deletion set has to meet each edge, and
one endpoint per edge suffices. \(\square\)

Consequently, \(S\) is maximal exactly when every empty site has positive
blocker number.  Two useful audit identities are

\[
 \sum_{x\in X\setminus S}b_S(x)
  =\sum_{\{p,q\}\subseteq S}(|X\cap\ell(p,q)|-2),
 \tag{3.1}
\]

and, if \(E(U)\) counts collinear triples in \(U\),

\[
 E(S\cup\{x\})-E(S)=b_S(x).
 \tag{3.2}
\]

The first double-counts a selected pair and an empty third carrier point on
its full line.  These identities do not imply that different empty sites act
independently.

### 3.2 Several prescribed insertions

Let \(A\subseteq X\setminus S\) itself be safe.  Define

\[
 D_A=\{s\in S:s\text{ is collinear with two distinct points of }A\}
\]

and

\[
 G_A=\bigcup_{a\in A}M_a(S)\big|_{S\setminus D_A}.
 \tag{3.3}
\]

The restriction in (3.3) deletes every vertex of \(D_A\), and
\(\tau\) denotes the minimum vertex-cover number.

**Proposition 3.2.**  The minimum number of points of \(S\) that must be
deleted before inserting all points of \(A\) is

\[
 r_S(A)=|D_A|+\tau(G_A).
 \tag{3.4}
\]

**Proof.**  A triple comprising two new points and one old point forces the
old point into \(D_A\).  Once these forced deletions are made, every remaining
mixed triple consists of one new point and one edge of \(G_A\).  Thus the
additional deleted old points must form a vertex cover.  The conditions are
sufficient because both \(S\) and \(A\) are safe. \(\square\)

For two inserted points, \(G_A\) is a union of two matchings, so each
component is a path or an even cycle.  This makes \(\tau(G_A)\) immediate.
For three inserted points, odd cycles can occur.  For example, with

\[
 S=\{(0,0),(2,0),(0,2)\},\qquad
 A=\{(1,0),(1,1),(0,1)\},
\]

the graph \(G_A\) is a triangle and has vertex-cover number two.

### 3.3 Prior-work boundary

Maximal general-position subsets of grids are studied as independent
geometric dominating sets by Aichholzer, Eppstein, and Hainzl [1].  Their
historical discussion credits Adena, Holton and Kelly (1974), and Martin
Gardner (1976), for the minimum-maximal problem. Nagy, Nagy and Woodroofe
use the term “saturated” for this maximality condition [7].  Wilhelmina's
public blocker/exchange computation [11] and Kudriashov's certified work on
nearby blocker and rigidity questions [12] are related local antecedents,
but do not establish the planar path-floor statements here. Multiple
saturation by secants in finite projective planes is another analogy [8],
not a transfer to integer squares.

Propositions 3.1–3.2 are elementary. This manuscript makes no novelty claim
for these identities, for vertex-cover language, or for local search.

## 4. Threshold components and local gates

For \(h\ge0\), let \(H_h\) be the add/delete graph induced by safe sets of
size at least \(h\).  Let \(\Sigma_h\) be the union of components of \(H_h\)
that meet a maximum set.  By definition,

\[
  F(S)=\max\{h:S\in\Sigma_h\}.
  \tag{4.1}
\]

The next statement says precisely what is absent from a scalar local repair
cost.

**Theorem 4.1 (gate criterion).**
Let \(S\) be a maximal submaximum
\(k\)-set and put \(b=\beta(S)\).  For every empty \(x\) with
\(b_S(x)=b\), let \(C\) range over the minimum vertex covers of \(M_x(S)\),
and put

\[
  P_{x,C}=S\setminus C,\qquad U_{x,C}=P_{x,C}\cup\{x\}.
\]

Then

\[
 \delta(S)=b
 \quad\Longleftrightarrow\quad
 P_{x,C}\in\Sigma_{k-b}\text{ for some }x,C.
 \tag{4.2}
\]

**Proof.**  Suppose a path from \(S\) to a maximum stays at size at least
\(k-b\), and consider its first inserted point \(x\notin S\).  Immediately
before that move the path is at a subset \(R\subseteq S\).  The deletion set
\(S\setminus R\) meets every edge of \(M_x(S)\), so it has at least
\(b_S(x)\) points.  The threshold bound gives at most \(b\).  Both
inequalities are equalities: \(b_S(x)=b\), \(R=P_{x,C}\), and \(C\) is a
minimum cover.  The converse follows by deleting \(C\), inserting \(x\), and
following a path within \(\Sigma_{k-b}\). \(\square\)

Hence \(\delta(S)\ge\beta(S)\) for every submaximum maximal state.  Equality
fails exactly when every minimum local gate lies in a maximum-free threshold
component.  This is an exact location of the missing global information, not
an efficient replacement for a component calculation: all gates remain
connected through \(S\) at the same threshold.

## 5. Swap layers and a matching certificate for a second loss

Let \(J_h\) be the graph on safe \(h\)-sets in which two vertices are
adjacent if they have a common safe \((h-1)\)-subset.  Thus a \(J_h\)-edge is
an atomic neutral swap.  Every pair of \(h\)-subsets of a fixed safe set of
size at least \(h\) lie in one \(J_h\)-component; call it \(j_h(U)\).

**Theorem 5.1 (threshold/TJ lemma).**  Let \(h\ge1\).  If \(S,Q\) are safe
and have size at least \(h\), then

\[
 S\text{ and }Q\text{ are connected in }H_{h-1}
 \quad\Longleftrightarrow\quad
 j_h(S)=j_h(Q).
 \tag{5.1}
\]

**Proof.**  A path at threshold \(h-1\) either moves above the \(h\)-layer,
which preserves the component of its \(h\)-subsets, or passes through a
configuration \(A\supset B\subset A'\) with \(|B|=h-1\), which is one
\(J_h\)-edge.  Conversely, shrink the endpoints to \(h\)-subsets, implement
each \(J_h\)-edge as delete then add through its common \((h-1)\)-subset, and
regrow. \(\square\)

This is the hereditary-family form of the familiar token
addition/removal–token jumping relation. For graph independent sets, see
Kamiński, Medvedev, and Milanič [2], and the threshold/buffer context of
de Berg, Jansen and Mukherjee [3].
The proof is included because no-three-in-line safety is independence in a
3-uniform hypergraph.

Define the maximum-target label set

\[
 T_h=\{R:|R|=h,\ R\subseteq Q\text{ for some maximum }Q\}.
 \tag{5.2}
\]

For \(1\le d\le |S|\), Theorem 5.1 gives

\[
  \delta(S)\le d
  \quad\Longleftrightarrow\quad
  j_{|S|-d+1}(S)\cap T_{|S|-d+1}\ne\varnothing.
  \tag{5.3}
\]

This is a connectivity characterization, not a claimed fast algorithm.

We now record a local closure certificate for the case \(\beta=1\).  For
safe \(U\) and any carrier point \(y\), selected or empty, let

\[
 L_y(U)=\{\{a,b\}\subseteq U\setminus\{y\}:a,b,y
              \text{ are collinear}\}.
 \tag{5.4}
\]

Suppose \(x\notin U\), \(L_x(U)=\{\{p,q\}\}\),
\(r\in\{p,q\}\), and \(U'=U-r+x\).  For \(y\notin U'\),

\[
 L_y(U')=L_y(U)|_{U\setminus\{r\}}
            \cup E_y(x;U\setminus\{r\}),
 \tag{5.5}
\]

where

\[
 E_y(x;W)=
 \begin{cases}
 \{\{x,s\}\},&\text{if a unique }s\in W\text{ is collinear with }x,y,\\
 \varnothing,&\text{otherwise.}
 \end{cases}
 \tag{5.6}
\]

There is at most one such \(s\), and this new edge is disjoint from all
retained edges, because \(U'\) is safe.  Equations (5.5)–(5.6) are therefore
an exact labelled-matching update.  Blocker numbers alone omit the
old–new–new incidence that decides whether the new edge is created.

**Theorem 5.2 (matching-closure certificate).** Let \(S\) be a
submaximum maximal safe \(k\)-set with \(\beta(S)=1\).  Let \(C\) be its
component in the labelled neutral-swap graph generated by singleton blocker
matchings, and suppose every \(U\in C\) is maximal.  Define

\[
 D(C)=\{P:|P|=k-1,\ P\subset U\text{ for some }U\in C\}.
\]

Then the component of \(S\) in \(H_{k-1}\) is exactly

\[
 C\cup D(C).
 \tag{5.7}
\]

In particular, \(\delta(S)\ge2\).

**Proof.**  No \(U\in C\) has a size-\(k+1\) coface.  Take
\(P=U\setminus\{r\}\in D(C)\), and let \(U'=P\cup\{x\}\) be another safe
\(k\)-coface.  Maximality of \(U\) makes \(M_x(U)\) nonempty.  Safety of
\(U'\) forces every edge of this matching to contain \(r\).  As it is a
matching, it has one edge, so \(U'\) is a declared singleton-blocker swap and
lies in \(C\).  Thus every threshold path alternates only between
\(C\) and \(D(C)\). Conversely, \(C\) is connected by its definition,
each neutral edge is realized through a member of \(D(C)\), and each
member of \(D(C)\) is adjacent to a member of \(C\). Thus their union
is connected and is the entire threshold component. \(\square\)

Connectedness matters: for an arbitrary swap-closed family of maximal
\(k\)-sets, the same boundary argument gives a closed **union** of threshold
components. It gives one component only if the family is connected. The
theorem explicitly takes \(C\) to be a component.

## 6. Exact \(G_6\) census

This section records **exactly checked finite computation**.  The results are
attributed to the complete-grid enumeration core and its independent verifier.  They
are reproducible mathematical evidence, not proof-assistant formalizations.

| \(n\) | safe subsets | maximal subsets | \(\alpha(G_n)\) | maximum subsets | maximal \(\delta=1\) | maximal \(\delta=2\) |
|---:|---:|---:|---:|---:|---:|---:|
| 1 | 2 | 1 | 1 | 1 | 0 | 0 |
| 2 | 16 | 1 | 4 | 1 | 0 | 0 |
| 3 | 230 | 23 | 6 | 2 | 21 | 0 |
| 4 | 4,812 | 347 | 8 | 11 | 336 | 0 |
| 5 | 109,536 | 5,646 | 10 | 32 | 5,586 | 28 |
| 6 | 3,599,697 | 116,411 | 12 | 50 | 115,876 | 485 |

The complete \(n\le5\) records have \(\beta=\delta\) for every submaximum
maximal state.  In \(G_6\), 124 labelled maximal 11-sets, in 16 dihedral
state orbits, satisfy

\[
  \beta=1,\qquad \delta=2.
 \tag{6.1}
\]

They occupy 28 labelled nontrivial \(J_{11}\)-components in four geometric
component orbits.  The other 361 maximal \(G_6\) states with \(\delta=2\)
have \(\beta=2\) and are neutral-swap isolated: one has size eight, four have
size nine, 28 size ten, and 328 size eleven.

The direct-depth distribution among submaximum maximal \(G_6\) states is:

| \(d\) | labelled states |
|---:|---:|
| 1 | 104,050 |
| 2 | 9,173 |
| 3 | 2,014 |
| 4 | 1,072 |
| 5 | 52 |

Forty-eight of the 52 depth-five states have \(\delta=1\).  This demonstrates
that direct replacement difficulty and path-floor difficulty are distinct.

The census also finds \(\delta\le2\) for every maximal \(G_6\) state.  The
underlying layer record is: \(J_h\) is connected for \(h\le7\); at
\(h=8,9,10\), there are respectively \(1,4,28\) maximum-free components, all
singleton maximal states; and every nonmaximal 11-set has a 12-point coface.
Thus every nonmaximal state has deficit at most one.  The following general
identity explains the asserted maximal-state bound.

**Lemma 6.2 (floor identity).**
For safe \(U\subseteq S\),

\[
 F(U)=\min\{|U|,F(S)\},\qquad
 \delta(U)=\max\{\delta(S)-(|S|-|U|),0\}.
 \tag{6.2}
\]

**Proof.**  Grow \(U\) to \(S\) within \(S\), then use an optimal path from
\(S\), for one inequality.  In the other direction, delete from \(S\) to
\(U\), then use an optimal path from \(U\); also \(F(U)\le|U|\). \(\square\)

It follows on any finite carrier that the assertion “every maximal state has
\(\delta\le2\)” is equivalent to “every nonmaximal state has
\(\delta\le1\).”  The equivalence is proved; its \(G_6\) hypothesis is a
finite checked fact, not an all-\(n\) theorem.

## 7. The four second-barrier motifs in \(G_6\)

Coordinates are zero based.  In each row, the listed core is common to every
state in a representative neutral component.  The residual description,
component count, and full threshold boundary are exactly checked in the
archived complete-grid certificate.  The visible local geometry does not, by itself,
exclude an escape through an unlisted grid site; that exclusion comes from
the complete labelled-matching boundary check.

| type | common core | variable sites | residual state description | components / states | \(H_{10}\) size |
|:--|:--|:--|:--|--:|--:|
| C1 | \((0,0),(0,4),(1,2),(2,1),(2,2),(3,5),(4,1),(4,3),(5,0)\) | \((1,5),(3,4),(5,3)\) | choose any two collinear variables | 8 / 24 | 33 |
| C2 | \((0,2),(0,5),(1,2),(2,0),(2,1),(3,4),(4,3),(4,4),(5,0)\) | \((1,5),(3,3),(5,1)\) | choose any two collinear variables | 4 / 12 | 33 |
| C3 | \((0,2),(1,4),(2,5),(3,3),(4,3),(4,5),(5,1)\) | \((0,4),(2,2),(3,1);(1,0),(2,0),(5,0)\) | one vacancy per triple, with one cross-pair forbidden | 8 / 40 | 54 |
| C4 | \((0,0),(0,4),(1,5),(2,1),(3,5),(4,0),(4,1)\) | \((1,2),(2,3),(3,3),(5,2),(5,3),(5,4)\) | choose four; vacancies hit all three lines | 8 / 48 | 64 |

In C1 and C2, the three variable points are collinear.  The missing variable
has the other two as its singleton blocker edge.  A neutral move therefore
rotates the vacancy around a triangle of maximal sets.

For C3, the variable triples are

\[
 L_1=\{(0,4),(2,2),(3,1)\},\qquad
 L_2=\{(1,0),(2,0),(5,0)\}.
\]

The core point \((2,5)\) forbids the cross-pair
\(\{(2,2),(2,0)\}\).  Of the nine nominal vacancy pairs, five remain.  Their
swap graph is two triangles sharing one vertex.

For C4, set

\[
 A=(1,2),\ B=(2,3),\ C=(3,3),\ D=(5,2),\ E=(5,3),\ F=(5,4).
\]

The collinear variable triples are \(\{B,C,E\}\), \(\{A,C,F\}\), and
\(\{D,E,F\}\).  A four-variable selection is safe exactly when its two
vacancies meet all three triples.  The six states form a 3-sun: a central
triangle with one further vertex attached to each edge.

This C4 component has a public antecedent: u/cedar_conics posted its
six-state family on 6 October 2026 [10]. The reflection
\((x,y)\mapsto(5-x,y)\) identifies that family exactly with the C4
representative above. The public example has 58 one-deletion states and a
closed 64-state component at height ten; every top state has \(\beta=1\)
and \(\delta=2\). The complete four-type classification in this section is
a separate finite result.

Every listed 11-point component consists of maximal states and has a closed
one-deletion layer.  Theorem 5.2 therefore supplies \(\delta\ge2\); saved
paths to a 12-point state at floor nine give equality.

A compact C1 witness is its core together with \((1,5)\) and \((3,4)\).  Its
three 11-point states and thirty 10-point deletion states form a closed
33-state component of \(H_{10}\).  It certifies

\[
  \beta=1<2=\delta.
\]

The classification is exactly checked finite computation. A determinant-based
reconstruction independently recovered the exchanges and one-deletion
boundaries, including the 28 labelled components and the threshold-component
sizes 33, 33, 54 and 64. A separate fresh enumeration recovered the complete
\(G_6\) census and its exhaustiveness claim; both receipts are in the
supplement.

## 8. Arbitrarily high barriers on restricted carriers

The next theorem is intentionally not a full-square result.

**Theorem 8.1 (restricted carriers).** For every
\(m\ge1\), there is a finite carrier \(X_m\subset\mathbb Z^2\) and an
inclusion-maximal submaximum safe set \(S_m\) satisfying

\[
 \beta_{X_m}(S_m)=\delta_{X_m}(S_m)=m.
 \tag{8.1}
\]

**Proof.** The rational realization used below is the edge-blocker
construction of Froese, Kanj, Nichterlein and Niedermeier [5, Proposition
1], applied to \(K_{m,m+1}\). Their construction credits the underlying
point-visibility transformation to Ghosh and Roy [6]. We include the
specialized argument because the subsequent barrier calculation uses its
exact incidence pattern. Choose rational points

\[
 B=\{b_1,\ldots,b_m\},\qquad W=\{w_1,\ldots,w_{m+1}\}
\]

in general position, fixing all of \(B\cup W\) before any anchor.
For each pair \((i,j)\), choose a rational anchor
\(a_{ij}\) on the line \(b_iw_j\), avoiding all existing points and the finitely many intersections
that would create a collinear triple other than the prescribed one.  This
finite-avoidance construction works because every rational line has
infinitely many rational points. Distinct prescribed \(B\)–\(W\) lines
are distinct by general position. Every future prescribed line already
joins an existing base pair, so each earlier anchor avoids it unless it
is that anchor's own prescribed line. Hence the designated pair is the
only old pair on the line chosen for a new anchor. It produces

\[
 X=B\cup W\cup A,\qquad
 A=\{a_{ij}:1\le i\le m,\ 1\le j\le m+1\},
\]

whose only collinear triples are

\[
 \{b_i,w_j,a_{ij}\}.
 \tag{8.2}
\]

Common rational scaling and translation put \(X\) in \(\mathbb Z^2\).

Let \(S=A\cup B\), \(Q=A\cup W\), and \(E=|A|=m(m+1)\).  At each absent
\(w_j\), the \(m\) disjoint pairs \(\{b_i,a_{ij}\}\) are its blockers.  Thus
\(S\) is maximal and \(\beta(S)=m\).

To show that \(Q\) is the unique maximum, let \(T\) be safe, and put
\(r=|T\cap B|\), \(s=|T\cap W|\).  Every selected pair \(b_i,w_j\) excludes
the distinct anchor \(a_{ij}\), giving

\[
 |T|\le E+r+s-rs.
 \tag{8.3}
\]

If \(r,s>0\), the right side is at most \(E+1\).  If \(r=0\), it is at
most \(E+m+1\), with equality only when \(T=Q\); if \(s=0\), it is at most
\(E+m\).  So \(Q\) is the unique maximum.

Before the first \(w_j\) can be inserted on a path from \(S\) to \(Q\), one
endpoint of every pair \(\{b_i,a_{ij}\}\) must be deleted.  The path reaches
size at most \(E\).  Deleting all \(b_i\) and then inserting all \(w_j\)
attains that floor.  Hence \(\delta(S)=m\). \(\square\)

For \(m\ge2\), adjoin an independent collinear triple \(\{u,v,w\}\), with no
mixed collinear triples, and start from \(S'=S\cup\{u,v\}\).  The missing
\(w\) has one blocker pair while every \(w_j\) retains \(m\) blockers.  Thus
\(\beta(S')=1\).  The neutral component on the added line is a triangle.
Every maximum is \(Q\) plus two points of this line; projecting a path onto
the original carrier forces a projected state of size at most \(E\).
At most two points can remain on the added line, so the full path has a
state of size at most \(E+2\).  Keeping the two added-line points while
using the original deletion/insertion path attains this floor.  Thus

\[
  \delta(S')=m.
  \tag{8.4}
\]

So a three-state closed neutral component, by itself, does not bound how far
below it eventual escape occurs. Exact exhaustive checks of supplied
19-site and 22-site carriers give deficit three, with 164,305 and 1,150,135
safe subsets respectively; these finite checks supplement the all-\(m\)
proof.

## 9. The full-square transfer gap

### 9.1 A conditional transfer theorem

Embedding the carrier of Theorem 8.1 in a large \(G_N\) does not preserve its
proof.  The extra lattice sites need not be blocked, so the old start need not
be maximal.  Greedily extending it can create low-cost gates and threshold
paths around the intended lock.  Square-grid maxima need not resemble \(Q\),
and the first point inserted on an escape path need not be one of the
\(w_j\).  Thus induced-subcarrier reasoning is invalid.

There is, however, a precise sufficient condition for transfer.  It tests
the whole component above a proposed cardinality floor, rather than only
the start.

**Proposition 9.1.**  Let
\(X\subseteq G_n\), let \(S\subseteq X\) be safe, fix
\(0\le h\le |S|\), and let \(C\) be its
component in \(H_h(X)\).  Suppose

\[
 M_z(U)\ne\varnothing
 \quad\text{for every }U\in C\text{ and }z\in G_n\setminus X.
 \tag{9.1}
\]

Then \(C\) is also the entire component of \(S\) in \(H_h(G_n)\).
If \(|U|\le |S|=k\) for all \(U\in C\) and a safe \((k+1)\)-set exists
in \(G_n\), then

\[
 \delta_{G_n}(S)\ge k-h+1.
 \tag{9.2}
\]

**Proof.**  An internal move stays in \(C\) by its definition.  A first
insertion outside \(X\) is forbidden by (9.1).  Thus no threshold path
leaves \(C\), whereas all its original paths remain available.  Every
maximum of \(G_n\) is larger than every state of \(C\), proving (9.2).
\(\square\)

For the carrier in Theorem 8.1, the component of \(S=A\cup B\) at height
\(E+1\) is exactly

\[
 \{S\setminus D:D\subseteq S,\ |D|\le m-1\}.
 \tag{9.3}
\]

Indeed, no \(w_j\) can be the first inserted new point until at least
\(m\) deletions have occurred, and every displayed deletion state is
reachable.  For an outside site \(z\), blocking at every state in (9.3)
is equivalent to \(b_S(z)\ge m\): at most \(m-1\) deletions cannot hit
\(m\) disjoint matching edges, while fewer than \(m\) edges can all be
hit by an allowed deletion set.  Therefore a full-square embedding with
this uniform outside guard would preserve \(\delta\ge m\), witnessed
by the old larger set \(A\cup W\).  No such embedding is asserted here.

For the \(\beta=1\) extension with \(m\ge2\), the relevant threshold is
\[
 h=E+3=|S'|-m+1.
\]
At that height the component is the union of the deletion families with at
most \(m-1\) deletions from each of the three neutral top states. The
uniform guard is \(b_T(z)\ge m\) for every outside site \(z\) and each top
state \(T\). The preceding base height \(E+1\) is not the extension
threshold: at that lower height the extension can escape. This specifies the
component to which Proposition 9.1 applies.

An elementary obstruction already excludes naive dilation.  Every pair of
a safe \(k\)-set blocks at most \(n-2\) additional grid sites, so
maximality requires

\[
 n^2-k\le {k\choose2}(n-2).
 \tag{9.4}
\]

The checked 17-point start on the 22-site restricted carrier fits inside
\(G_{147}\), but (9.4) leaves at least
\(147^2-17-{17\choose2}145=1872\) immediately free sites.  This proves
failure of maximality for that embedding, not a value of its full-square
path deficit.

### 9.2 A full-square obstruction pattern

A full-square certificate for one example with \(\delta\ge3\) would require:

1. a safe maximal \(S\subseteq G_n\) with blockers recorded at every empty
   grid site;
2. a threshold-component lower-bound certificate, not only a large blocker
   count at selected named sites;
3. a larger safe set, or a sharp maximum proof and an escape path.

An unbounded full-square family would additionally need a scaling mechanism
that keeps the extra lattice sites saturated and excludes alternative routes.

One decisive sufficient certificate would be a submaximum safe
\(S\subseteq G_n\) with \(b_S(x)\ge3\) for every empty \(x\), together with
any larger safe set.  The first-insertion bound then gives
\(\delta(S)\ge3\). This is a sufficient condition, not an existence
assertion; Section 9.3 excludes it on \(G_7,G_8\).

There is a useful reduction at size \(2n-1\).  If
\(S\subseteq G_n\) is safe with \(|S|=2n-1\), each row and column contains
at most two selected points.  Thus exactly one row \(r_0\) and one column
\(c_0\) contain one selected point; every other row and column contains two.
For an empty point \(x\),

\[
 b_S(x)=\mathbf 1[x\text{ is on a full row}]
       +\mathbf 1[x\text{ is on a full column}]
       +b_S^{\mathrm{obl}}(x),
 \tag{9.5}
\]

where \(b_S^{\mathrm{obl}}(x)\) counts non-axis-parallel blocker secants.
Therefore a size-\(2n-1\) candidate with \(\beta\ge3\) needs at least one
oblique blocker away from the deficient row and column, at least two on
either deficient axis away from their intersection, and, if their
intersection is empty, at least three there. Whenever a \(2n\)-point safe
comparison configuration is available, it is a larger witness. These are
full-square-specific requirements for a decisive search; they do not assert
that such a set exists.

Independent copies of small barriers do not add deficits.  If there are no
mixed collinear triples between the carriers, repair each part while holding
the others fixed.  Earlier repairs only increase the total cardinality, so
the combined deficit is at most the largest individual deficit.  Thus copies
of a fixed independent gadget alone cannot produce an unbounded family.

More generally, extra selected points can compensate for a projected loss
on the old carrier. None of the preceding conditions gives a universal bound
for complete squares.

### 9.3 Certified exclusions and path bounds on \(G_7,G_8\)

The following **exactly checked** results use the certificate package
described in Section 11. It distinguishes complete certificates from bounded
searches.

**Result 9.2 (high-blocker exclusion).** Every submaximum safe set on
\(G_7\) or \(G_8\) has \(\beta\le2\).

**Encoding and certificate.** Introduce occupation variables \(x_p\) and
pair variables \(e_{pq}\leftrightarrow(x_p\wedge x_q)\). Impose a
negative clause for every collinear triple and, for each site \(y\),

\[
 \sum_{\substack{\{p,q\}\subseteq G_n\setminus\{y\}\\p,q,y\text{ collinear}}}
       e_{pq}\ \ge\ 3(1-x_y).
 \tag{9.6}
\]

At an empty site the sum is precisely \(b_S(y)\); at an occupied site
the inequality is vacuous. Exact unary threshold equivalences encode these
sums and \(|S|\le2n-1\). For successive input literals \(\ell_i\),
the recurrence is
\(z_{i,t}\leftrightarrow z_{i-1,t}\vee(\ell_i\wedge z_{i-1,t-1})\),
with \(z_{i,0}=1\), \(z_{0,t}=0\) for \(t>0\), and explicit boundary
cases. Induction gives the intended threshold semantics. Thus satisfiability
is equivalent to the claimed obstruction; no symmetry restriction is used.
Independently checked 14- and 16-point witnesses, together with the row
bound, establish \(\alpha(G_7)=14\), \(\alpha(G_8)=16\).

| Board | Cardinality scope | Collinear triples | CNF variables | CNF clauses | DRAT-trim result |
|---|---|---:|---:|---:|---|
| \(G_7\) | \(0\le |S|\le13\) | 824 | 9,089 | 33,176 | VERIFIED UNSAT |
| \(G_8\) | \(0\le |S|\le15\) | 1,544 | 16,688 | 61,185 | VERIFIED UNSAT |

The supplement's proof receipt records hashes of the historical instances,
proofs, checker source and logs. Section 11 distinguishes these receipts
from the archived source and the regeneration procedure. This result excludes a local first-insertion barrier of
three on these boards. It
does **not** exclude \(\delta\ge3\) when \(\beta=1\) or 2.

**Result 9.3 (complete specified layers).** Every maximal safe set in
each of the following classes has \(\delta\le2\).

| Board | Size | All safe sets of that size | All labelled maximal sets | D4 representatives with paths |
|---|---:|---:|---:|---:|
| \(G_7\) | 12 | 471,860 | 305,960 | 38,493 |
| \(G_7\) | 13 | 15,532 | 13,684 | 1,722 |
| \(G_8\) | 15 | 79,968 | 73,888 | 9,251 |

For a maximal \(k\)-set, the search traverses \(J_{k-1}\), testing
whether a state extends all the way to a maximum. Each route is expanded
into ordinary insertions and deletions at floor at least \(k-2\).
Separate determinant code checks every move. A separate row-recursion
verifier considers every zero-, one- or two-point row choice, tests safety
and maximality, and checks each maximal leaf against the symmetry-expanded
path starts. This establishes coverage, rather than inferring it from a
search completion flag. The three coverage receipts are included in the
supplement.

In the first row the target test requires three compatible insertions
from an 11-set to reach size fourteen; extension merely to thirteen would
not certify a maximum route. Nonmaximal sets of sizes 13 on \(G_7\) and
15 on \(G_8\) insert directly to maxima. A nonmaximal 12-set on \(G_7\)
extends to the covered 13-layer and has \(\delta\le1\) by Lemma 6.2.

Additional bounded row searches, nonuniform random greedy samples and
targeted \(\beta=2\) candidates yielded no third-barrier witness. An
independent path audit verified 251,579 path records from **244,443 distinct
tested starts**, all reaching a maximum at floor at least their starting size
minus two. Its compact scope receipt is included in the supplement; the
large path list is omitted as described in Section 11.
The sample lists overlap; the complete-class counts above are separate
coverage statements. No whole-class conclusion is inferred for the
remaining sizes. These data settle neither \(\delta\le2\) for every
maximal state of \(G_7,G_8\) nor a bound for larger boards.

## 10. Open questions

1. Is \(\delta\le2\) for every maximal safe subset of every \(G_n\), or does
   a full-square example with \(\delta\ge3\) exist?
2. Does a submaximum \(S\subseteq G_n\) exist with \(b_S(x)\ge3\) at every
   empty \(x\)? The complete \(n\le6\) census and Result 9.2 exclude
   this on all boards through eight; the next possible board is \(G_9\).
   At size \(2n-1\), equation (9.5) supplies a particularly sharp necessary
   condition whenever a \(2n\)-point comparison set is available.
3. Can the four \(G_6\) motifs be coupled into serial threshold locks rather
   than placed as independent gadgets?
4. What statistics of the labelled matching field predict which threshold
   component contains a maximal set?
5. Is there prior work already containing a Euclidean-grid reconfiguration
   census, these component types, or the restricted-carrier construction?

## 11. Reproducibility, scope, and software

The accompanying supplement contains the source needed for deterministic
reconstruction of the finite enumerations, matching-component data, SAT
encodings, and coverage checks. It also contains compact result receipts and
SHA-256 hashes. A fresh external replay independently enumerated the
\(G_n\) state spaces for \(1\le n\le6\), recovered the \(G_6\) counts and
the C1–C4 classification, and checked the displayed path and component
certificates. The finite claims in Sections 6--7 are therefore **exactly
checked**; they are not proof-assistant formalizations.

The \(G_7,G_8\) high-blocker exclusions are certified by DRAT traces whose
raw compressed files exceed the venue's supplement limit. The archive
therefore includes the exact encoding generator, semantic checker, source
and result hashes, and independently checked verification receipts, but not
the raw traces or the large path lists. Those receipts are evidence of a
verification run, not substitutes for the omitted traces. The supplement supplies commands for regenerating the CNFs, new DRAT
proofs, and the three complete path classes, with independent checks. The
additional sampled-path aggregate is documented by receipts and original
hashes only; its entire historical sample is not archived in this package.
The three complete path classes in Result 9.3 are precisely the three rows
in its table. Across the combined, overlapping runs, 244,443 distinct tested
starts were checked; the bounded or sampled populations support no unlisted
whole-layer conclusion.

The certified SAT work used PySAT [13] with Glucose [14]; MiniSat [15] is
credited as an acknowledged basis of that solver lineage. DRAT validation
used DRAT-trim [16]. The supplied C++ and Python programs require a
standards-conforming C++ compiler and Python 3; exact package versions and
commands are listed in the supplement.

The literature review found a public prior C4 occurrence and established
realization/reconfiguration antecedents cited above. No claim of historical
priority is made. In particular, the results do not prove a full-square
unbounded-deficit theorem or a universal upper bound on \(\delta\).

## References

1. O. Aichholzer, D. Eppstein, and E.-M. Hainzl, *Geometric dominating
   sets -- A minimum version of the no-three-in-line problem*,
   *Computational Geometry* 108 (2023), 101913.
   https://arxiv.org/abs/2203.13170
2. M. Kamiński, P. Medvedev, and M. Milanič, *Complexity of independent
   set reconfigurability problems*, *Theoretical Computer Science* 439
   (2012), 9--15. https://doi.org/10.1016/j.tcs.2012.03.004
3. M. de Berg, B. M. P. Jansen, and D. Mukherjee, *Independent-Set
   Reconfiguration Thresholds of Hereditary Graph Classes*, FSTTCS 2016,
   34:1--34:15. https://drops.dagstuhl.de/entities/document/10.4230/LIPIcs.FSTTCS.2016.34
4. M. A. Adena, D. A. Holton, and P. A. Kelly, *Some thoughts on the
   no-three-in-line problem*, in *Combinatorial Mathematics*, 1974.
5. V. Froese, I. Kanj, A. Nichterlein, and R. Niedermeier, *Finding Points
   in General Position*, *International Journal of Computational Geometry
   & Applications* 27(4) (2017), 277--296. Proposition 1.
   https://arxiv.org/abs/1508.01097
6. S. K. Ghosh and B. Roy, *Some results on point visibility graphs*,
   *Theoretical Computer Science* 575 (2015), 17--32.
   https://doi.org/10.1016/j.tcs.2014.10.042
7. D. T. Nagy, Z. L. Nagy, and R. Woodroofe, *The extensible
   No-Three-In-Line problem*, *European Journal of Combinatorics* 114
   (2023), 103796. https://arxiv.org/abs/2209.01447
8. D. Bartoli, A. A. Davydov, M. Giulietti, S. Marcugini, and F. Pambianco,
   *On upper bounds on the smallest size of a saturating set in a projective
   plane*. https://arxiv.org/abs/1505.01426
9. M. Gardner, *Mathematical Games* column, 1976; cited for historical
   context by [1].
10. u/cedar_conics, *Positive neutral mobility and positive C1 drift can
    remain inside a closed component*, r/no_three_in_line, 6 October 2026,
    11:51:13 UTC. https://rstation.ai/r/no_three_in_line/posts/26#comment-8e7ed041-54fd-4cf8-a50f-75274a27f6df
11. Wilhelmina, blocker/exchange computation, 17 September 2026.
    https://einsteinarena.com/problems/no-three-in-line-75/threads/267
12. A. Kudriashov, *Certified computations on no-three-in-line problems:
    exact values and witnesses in the cube, and the Guy--Kelly count in the
    plane*, arXiv:2609.25133 (2026).
    https://arxiv.org/abs/2609.25133
13. A. Ignatiev, A. Morgado, and J. Marques-Silva, PySAT.
    https://pysathq.github.io/
14. G. Audemard and L. Simon, Glucose SAT solver.
    https://www.labri.fr/perso/lsimon/research/glucose/
15. N. Eén and N. Sörensson, MiniSat SAT solver.
    https://github.com/niklasso/minisat
16. N. Wetzler, M. J. H. Heule, and W. A. Hunt Jr., DRAT-trim:
    efficient checking and trimming using expressive clausal proofs.
    https://github.com/marijnheule/drat-trim
