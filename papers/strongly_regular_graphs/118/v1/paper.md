# Mixed order-three incidence reversers: Schur reductions and restrictions at DSRG(110,84,80,64,64)

## 1. Problem and contribution

A directed strongly regular graph (DSRG) with parameters $(n,k,t,\lambda,\mu)$ has a binary adjacency matrix $A$ with zero diagonal and

$$
A\mathbf1=k\mathbf1,\qquad \mathbf1^TA=k\mathbf1^T,\qquad
A^2=(t-\mu)I+(\lambda-\mu)A+\mu J. \tag{1}
$$

We use the convention of Duval [1]. The parameter set $(110,84,80,64,64)$ and its complement $(110,25,21,4,6)$ remain open in the Hobart–Brouwer table consulted on 12 November 2026 [2]. This paper gives restrictions on a particular incidence symmetry of a possible graph. It neither constructs that graph nor proves its unrestricted nonexistence.

An **incidence reverser** is a vertex permutation $\rho$ such that

$$
A_{\rho(a),\rho^{-1}(b)}=A_{a,b}. \tag{2}
$$

This is the reverser of meleta [3]. We consider $\rho$ of order three, with $f$ fixed vertices and $m$ orbits of length three, so $n=f+3m$. We call the length-three orbits moving cells. The word *mixed* means that both fixed vertices and moving cells occur.

**Theorem 1.** Suppose that a DSRG with parameters $(110,84,80,64,64)$ admits an incidence reverser of order three.

1. It cannot have exactly eleven fixed vertices.
2. If it has exactly eight fixed vertices, the induced graph on those vertices is the unique DSRG$(8,3,2,1,1)$. There are 34 moving cells, and the 34 ordered pairs of incoming and outgoing incidences between a moving cell and the eight fixed vertices are all distinct.

Neither assertion assumes any further symmetry of the fixed-to-moving incidences or of the moving part. The eleven-fixed-vertex assertion includes a complete classification of the possible fixed induced block, followed by an exact separating inequality. The distinctness assertion combines a rank-two state certificate with a modular argument. We also give a general Schur-complement formula which determines the moving quotient when the residual rank is one.

The construction method of [3] first selects an orbit quotient and then solves its character lift. Its principal theorem and detailed reduction concern fixed-point-free actions. A successful subsequent table construction at order 69 is given in [4]. Here fixed vertices change the quotient from a regular matrix to a matrix with orbit weights, and introduce binary incidence profiles shared by several matrix equations. Our contribution is the explicit reduction and the restrictions on those physical profiles, including the complete exclusion in Theorem 1(1).

The underlying quotient-matrix framework is classical. Crnković, Švob and Zrinski [5] and Maksimović and Rukavina [6] use orbit matrices for constructing DSRGs with prescribed automorphisms; tactical decompositions of incidence matrices provide a broader setting [7]. We do not claim novelty for equitable partitions, Schur complements, or the Fourier decomposition of cyclic blocks. The reverser interpretation and the free-action character equation are credited to [3].

## 2. Weighted quotients and a rank-one formula

Write $\mathbf1$ for an all-ones vector of the indicated size and $J$ for an all-ones matrix. Number each moving cell by $i\in\mathbb Z_3$, with $\rho(i)=i+1$. Equation (2) makes a block between moving cells depend only on the sum of its two indices. A diagonal block is zero: looplessness makes its values at $2i$ zero, and multiplication by two permutes $\mathbb Z_3$. Between a fixed vertex and a moving cell all incidences are constant.

Consequently the orbit partition is equitable in both directions and has quotient

$$
Q=\begin{pmatrix}B&3X\\Y&T\end{pmatrix},\qquad
w=\begin{pmatrix}\mathbf1_f\\3\mathbf1_m\end{pmatrix}. \tag{3}
$$

Here $B,X,Y$ are binary, $B$ has zero diagonal, $T_{ii}=0$, and $T_{ij}\in\{0,1,2,3\}$. For $\lambda=\mu$ and $t-\mu=r^2>0$, equation (1) implies

$$
Q\mathbf1=k\mathbf1,\quad w^TQ=kw^T,\quad
Q^2=r^2I+\mu\mathbf1w^T. \tag{4}
$$

In particular $\operatorname{tr}Q=0$. On $\ker w^T$, the eigenvalues are $r$ and $-r$. If $q=f+m$ and $k>r$, their multiplicities are

$$
a=\frac{q-1-k/r}{2},\qquad b=\frac{q-1+k/r}{2},
\qquad \operatorname{rank}(Q+rI)=a+1. \tag{5}
$$

This also gives the familiar integrality and nonnegativity restrictions.

**Proposition 2 (rank-one boundary formula).** Suppose (3)–(4) hold, $B+rI$ is invertible, and $\operatorname{rank}(Q+rI)=f+1$. Put

$$
L=(B+rI)^{-1},\qquad h=\mathbf1^TL\mathbf1,\qquad D=n-(k+r)h.
$$

If $D\ne0$, then

$$
T=3YLX-rI+\frac{3(k+r)}{D}
(\mathbf1-YL\mathbf1)(\mathbf1^T-\mathbf1^TLX). \tag{6}
$$

*Proof.* The Schur complement $S=T+rI-3YLX$ has rank one. The two degree equations in (4) give

$$
\begin{aligned}
S\mathbf1&=(k+r)(\mathbf1-YL\mathbf1),\\
\mathbf1^TS&=(k+r)(\mathbf1^T-\mathbf1^TLX),\\
\mathbf1^TS\mathbf1&=\frac{k+r}{3}\bigl(n-(k+r)h\bigr).
\end{aligned} \tag{7}
$$

For example $3X\mathbf1=(k+r)\mathbf1-(B+rI)\mathbf1$, which proves the first identity after substitution. The weighted column equation proves the second and third. A rank-one matrix with nonzero total sum is $(S\mathbf1)(\mathbf1^TS)/(\mathbf1^TS\mathbf1)$. This is (6). $\square$

Formula (6) is a necessary equality on the actual binary boundary. It is particularly useful on the diagonal, since $T_{ii}=0$ becomes a condition on a single pair consisting of a column of $X$ and a row of $Y$. Entry ranges and the character lift remain separate requirements.

## 3. The fixed-eight block and its rank-two residual

For the dense target, the fixed-block equations reduced modulo three are

$$
B\mathbf1\equiv0,\quad \mathbf1^TB\equiv0,\quad
B^2\equiv I+J\pmod3. \tag{8}
$$

### 3.1. The small fixed block is unique

Let $B$ have order eight. No row or column can have degree zero, by the diagonal of (8). Thus every degree is three or six. A row of degree three has its square row equal, over the integers, to the corresponding row of $I+J$. Its three out-neighbours therefore have degrees summing to nine, so all have degree three. The degree-three set is closed under outgoing arcs; if a degree-six vertex existed, a two-walk from that set to it would be impossible, contrary to (8). Hence either all rows have degree three or all have degree six.

In the second case all columns also have degree six, and $B=J-I-P$ for a derangement permutation matrix $P$. Modulo three, (8) gives $P^2=P$. Since $P$ is invertible, this forces $P=I$, a contradiction. Therefore every row has degree three and

$$
B^2=I+J. \tag{9}
$$

This identity makes $B$ commute with $J$, so its column degrees are also three.

For completeness, uniqueness of this small graph has a short rank-two verification. Set $H=2B+2I-J$. It has diagonal one, all entries in $\{-1,1\}$, zero row and column sums, and $H^2=4H$. Its trace is eight, hence it has rank two. Its second elementary symmetric sum is 16, so some principal two-by-two block is nonsingular. After exchanging its two indices this block is

$$
H_0=\begin{pmatrix}1&1\\-1&1\end{pmatrix}.
$$

Every vertex gives a joint state $(r_1,r_2,c_1,c_2)$ of its entries to and from this block. The diagonal condition $r\operatorname{adj}(H_0)c=2$ leaves the following eight states, in order:

$$
\begin{pmatrix}
-1&-1&-1&-1\\-1&-1&-1&1\\-1&1&-1&1\\-1&1&1&1\\
1&-1&-1&-1\\1&-1&1&-1\\1&1&1&-1\\1&1&1&1
\end{pmatrix}. \tag{10}
$$

Let their multiplicities be $n_s$. The count, four zero sums, and four entries of $\sum_s n_sc_sr_s=4H_0$ are linear in these multiplicities. The first eight equations, ordered as count, $r_1,r_2,c_1,c_2,c_1r_1,c_1r_2,c_2r_1$, have determinant $-1024$. Their unique solution, also satisfying the ninth equation, is $n_s=1$ for every state. Reconstruction by $H_{ij}=r_iH_0^{-1}c_j$ proves uniqueness up to vertex permutation. The supplement checks these eight-state calculations exactly.

We use the representative

$$
B_8=\begin{pmatrix}
0&0&0&1&0&0&1&1\\
0&0&1&0&1&1&0&0\\
0&1&0&0&1&1&0&0\\
1&1&0&0&0&1&0&0\\
0&0&1&0&0&0&1&1\\
1&1&0&1&0&0&0&0\\
1&0&0&1&0&0&0&1\\
0&0&1&0&1&0&1&0
\end{pmatrix}. \tag{11}
$$

### 3.2. Actual incidence profiles

Now $m=34$. Put $U=J-X$ and $V=J-Y$. For moving cell $i$, its **profile** is the ordered pair $(u_i,v_i)=(U_{:,i},V_{i,:})$ of binary masks; $u_i$ is a column and $v_i$ a row. Complementing both masks is bijective, so distinctness is independent of this choice of notation. The fixed degree and square equations give

$$
U\mathbf1=7\mathbf1,\qquad \mathbf1^TV=7\mathbf1^T,
\qquad UV=5I+J. \tag{12}
$$

Let $\alpha=U^T\mathbf1-\mathbf1$ and $\beta=V\mathbf1-\mathbf1$. From (5), $Q$ has spectrum $84,4^{10},(-4)^{31}$. In particular the Schur complement

$$
S=T+4I-3Y(B_8+4I)^{-1}X
$$

has rank three. Define

$$
K=S-\frac47\beta\alpha^T. \tag{13}
$$

**Lemma 3.** The physical quotient satisfies

$$
\operatorname{rank}K=2,\quad K^2=8K,\quad
K\mathbf1=0,\quad\mathbf1^TK=0,\quad XK=0,\quad KY=0. \tag{14}
$$

*Proof.* Equation (9) gives

$$
(B_8+4I)^{-1}=\frac{28I-7B_8+J}{105}.
$$

Direct block multiplication, for any invertible $B+rI$, gives

$$
S^2=2rS+3\mu(\mathbf1-YL\mathbf1)(\mathbf1^T-\mathbf1^TLX).
$$

Specializing this identity and substituting in (4), using (12), yields

$$
\begin{aligned}
S\mathbf1&=\tfrac{88}{7}\beta,&\mathbf1^TS&=\tfrac{88}{7}\alpha^T,\\
XS&=\tfrac{64}{7}\mathbf1\alpha^T,&SY&=\tfrac{64}{7}\beta\mathbf1^T,\\
S\beta&=\tfrac{104}{7}\beta,&\alpha^TS&=\tfrac{104}{7}\alpha^T,\\
\alpha^T\beta&=26,&S^2&=8S+\tfrac{192}{49}\beta\alpha^T.
\end{aligned} \tag{15}
$$

Also $\mathbf1^T\alpha=\mathbf1^T\beta=22$, $X\beta=16\mathbf1$, and $\alpha^TY=16\mathbf1^T$, directly from (12). Equations (13) and (15) prove all the identities in (14). The nonzero eigendirection $\beta$ of $S$ is removed by (13), while $K$ and $\beta\alpha^T$ have zero products in both orders. Thus $\operatorname{rank}S=1+\operatorname{rank}K$, proving the rank assertion. $\square$

The integer matrix $R=5K$ is convenient. For binary masks define

$$
o(v,u)=-20+5|u|+5|v|-3|u||v|-4vu+vB_8u. \tag{16}
$$

Then

$$
R_{ij}=o(v_i,u_j)+5T_{ij}\ (i\ne j),\qquad
R_{ii}=o(v_i,u_i)+20. \tag{17}
$$

Thus every off-diagonal entry has four possible integer values, determined by physical masks. The same masks participate in (12); they are not independent formal variables in different equations.

We record the simple profile restrictions used in the certificates. Put $W=3(J-I)-T$, so $0\le W_{ij}\le3$ off the diagonal and $W_{ii}=0$. The cross equations give

$$
UW=6J-(3I-B_8+J)U,\qquad
WV=6J-V(3I-B_8+J). \tag{18}
$$

Consequently the $a$th entry of $6\mathbf1-(3I-B_8+J)u_i$ lies between zero and $3(7-u_{i,a})$, with the transposed counterpart for $v_i$. Furthermore $|u_i\setminus v_i|$ and $|v_i\setminus u_i|$ are at most four: each moving vertex has $k-t=4$ outgoing nonmutual arcs, and also four incoming nonmutual arcs. Componentwise bounds on each $u_iv_i$ follow from (12). All filters used below are therefore necessary conditions, not additional symmetry assumptions.

## 4. No repeated physical profile at eight fixed vertices

### 4.1. Repeated singleton profiles

Suppose that two moving cells have $u_i=v_i=e_a$. The automorphism group of (11) is transitive; the independent checker verifies this by inspecting all $8!$ permutations. We may fix $a=0$.

For these two cells, (17) gives a principal block

$$
H=\begin{pmatrix}3&h\\\ell&3\end{pmatrix},\qquad
h,\ell\in\{-17,-12,-7,-2\}. \tag{19}
$$

Every such $H$ is nonsingular. Three copies of this singleton are impossible already: their principal determinant is at most $27-36-16<0$, whereas $R$ has rank two. Exchanging the two chosen cells leaves ten unordered possibilities in (19).

For any other cell let $r_i=(R_{i0},R_{i1})$, $c_i=(R_{0i},R_{1i})^T$. Rank-two reconstruction requires

$$
R_{ij}=\frac{r_i\operatorname{adj}(H)c_j}{\det H},\qquad
r_i\operatorname{adj}(H)c_i=\det(H)\bigl(o(v_i,u_i)+20\bigr). \tag{20}
$$

The four coordinate alphabets come from (17). Enumerating the two masks and these four coordinates gives a complete finite list of states. Equations (12) and (14) imply the following linear moment equations on state multiplicities: the count, the sixteen mask margins, the 64 entries of $UV$, the four coordinate sums, the 32 entries of $\sum u_ir_i$ and $\sum c_iv_i$, and the four entries of

$$
\sum_i c_ir_i=40H. \tag{21}
$$

There are 121 moments. Subtract the two chosen cells, and call the resulting target $b$ and the moment column of a remaining state $C_i$. A state can occur at most once: two identical states would have the same reconstructed off-diagonal and diagonal entries, forcing $T_{ij}=4$ in (17).

For nine of the ten cases the supplement supplies an integer vector $z$ with $C_i^Tz\ge0$ for every state but $b^Tz<0$. The independent checker regenerates all 1,079,709 states across these nine cases. The final case is

$$
H=\begin{pmatrix}3&-12\\-7&3\end{pmatrix}.
$$

Write $r_i=(p_i,p_i+5d_i)$ and $c_j=(q_j,q_j+5e_j)^T$. Equation (20) becomes

$$
R_{ij}=-\frac{(p_i+2d_i)q_j}{3}-(p_i+d_i)e_j. \tag{22}
$$

Integrality for every ordered pair implies that either all $p_i+2d_i$ or all $q_i$ vanish modulo three. Transposition, followed by exchanging the chosen cells, interchanges the branches. The relabelling $(0,4,2,6,1,7,3,5)$ identifies $B_8^T$ with $B_8$ while fixing position zero, so it suffices to treat the first branch.

That branch contains 80,292 states. Thirteen recorded pruning steps remove 3,382 states. Each step supplies an integer vector $z$ and designated states $a$ such that

$$
(b-C_a)^Tz<0,\qquad C_j^Tz\ge0
\quad\text{for every currently available state compatible with }a. \tag{23}
$$

Compatibility requires both reconstructed entries to belong to their four-value alphabets, and prohibits using an off-diagonal fixed ordered pair twice in (12). If $a$ occurred, all other selected states would be compatible with it, contradicting (23). The removals are therefore valid inductively. The checker makes 53,092,716 scalar compatibility checks over this chain.

On the remaining 76,910 states, a final integer vector gives

$$
b^Tz=-216571<-117500=\sum_i\min(0,C_i^Tz). \tag{24}
$$

Since each multiplicity is zero or one, (24) is impossible. All arithmetic in this verification is integral; no floating-point solver status enters the proof. This excludes repeated singleton profiles.

### 4.2. Repeated empty profiles

At most two cells can have $u_i=v_i=0$. Three such cells would give a principal three-by-three matrix of $R$ with zero diagonal and strictly negative off-diagonal entries. Its determinant is the sum of two strictly negative cyclic products, contradicting rank two. This observation also justifies omitting further empty profiles after choosing two as anchors.

For two empty profiles the principal block has diagonal zero and off-diagonal entries $-5s,-5t$, where $s,t\in\{1,2,3,4\}$. All coordinates to or from these two cells are multiples of five. Rank-two reconstruction expresses every entry of $R$ as five times a rational number whose denominator divides $st$. Since $5\nmid st$ and $R$ is integral, all its entries are divisible by five.

On the other hand, (16)–(17) give

$$
R\equiv VMU\pmod5,\qquad M=B_8+I+2J. \tag{25}
$$

The matrix $M$ has rank two over $\mathbb F_5$. Choose a rank factorization $M=LF$ and let $E$ be the span of all $Fu_i$. Then every $v_iL$ annihilates $E$. There are exactly eight possibilities for $E$: zero, the six projective lines, and the full plane.

For each possibility, the supplement gives an integer separator on the 81 physical moments $(1,u,v,uv)$. After removing the two empty anchors, the target is $(32,7\mathbf1,7\mathbf1,5I+J)$. The checker inspects all $8\cdot256^2=524288$ mask-pair cases, applies only (18), the mismatch bound and the indicated subspace condition, and verifies nonnegative scores on all allowed profiles. The required score is negative in every case:

| Subspace | Allowed profiles | Minimum score | Required score |
|---|---:|---:|---:|
| Zero | 3644 | 0 | −40 |
| Span$(1,0)$ | 2474 | 0 | −40 |
| Span$(1,1)$ | 2474 | 0 | −40 |
| Span$(1,2)$ | 1224 | 0 | −120 |
| Span$(1,3)$ | 1224 | 0 | −120 |
| Span$(1,4)$ | 2474 | 0 | −40 |
| Span$(0,1)$ | 2474 | 0 | −40 |
| Full plane | 3644 | 0 | −40 |

The coefficients have absolute value at most five. The factorization and each inequality are checked directly by the standalone Python verifier. Thus an empty profile cannot repeat.

### 4.3. The remaining profiles

If $u,v$ are nonempty and not the same singleton, the outer product $uv$ contains an off-diagonal one. Repeating it violates the corresponding entry $(UV)_{ab}=1$. If exactly one mask is empty, repeating it uses a fixed vertex's mismatch budget twice, since

$$
\sum_i u_{i,a}(1-v_{i,a})=7-6=1,
\qquad
\sum_i v_{i,a}(1-u_{i,a})=1. \tag{26}
$$

These cases, the singleton case and the empty case exhaust all masks. This proves Theorem 1(2).

## 5. Complete exclusion of eleven fixed vertices

### 5.1. Classification of the fixed block

**Lemma 4.** Up to simultaneous permutation of rows and columns, there is exactly one binary loopless matrix of order eleven satisfying (8). It is obtained from $B_8$ by replacing one vertex by a bidirected clique of size four and copying its external incoming and outgoing incidences.

The classification combines short deductions with three essential Boolean refutations; a fourth independently checks the degree-nine deduction. We give the complete coverage argument.

Degrees zero are impossible by the diagonal of (8), leaving degrees three, six and nine. A row of degree nine has a unique other nonneighbour $j$. Both its omitted entries, at itself and at $j$, multiply zeros in column $j$. Hence $(B^2)_{ij}$ equals the entire column-$j$ sum, which is zero modulo three, contrary to (8). Transposition excludes column degree nine. All degrees are therefore three or six.

If a row has degree three, its square row is exactly the corresponding row of $I+J$ and sums to twelve. Its three out-neighbours have degrees three, three and six. Relabel this row as zero and those neighbours as one, two and three. The `mixed` Boolean formula imposes (8), degrees three or six, this normalization, and the condition that every class of equal rows of $B+I$ has size at most three. It is unsatisfiable.

If no row has degree three, every row has degree six. Normalize the first row's six neighbours as vertices one through six. The `regular6` formula, again forbidding four equal rows of $B+I$, is unsatisfiable. These two cases cover every possible $B$ and show that some four vertices have equal closed outgoing rows.

Their degree cannot be three. In that case their common closed neighbourhood would consist of exactly these four vertices, so a two-walk to any outside vertex would be impossible. Their degree is therefore six, and their common closed neighbourhood has seven vertices. Relabel the chosen four vertices as zero through three and the other three vertices in the common support as four through six. **No equality of incoming columns is imposed.**

The known clique expansion has 720 distinct labelled copies in this normalization. They are generated by taking each closed-row class of size at least four, every ordered choice of four of its members, every ordering of the other three positions of the support, and every ordering of its complement. This covers every normalized labelled copy, including choices within a larger closed-row class. The `closed4` formula imposes the normalized rows and (8), then forbids exactly those 720 matrices. It is unsatisfiable, completing the classification.

The independent encoder uses scalar Boolean AND and XOR gates and an allowed-count decision diagram. It does not import the exploratory constraint model or a graph-isomorphism program. Its small count encodings pass all 10,230 exhaustive truth assignments; pinning one known normalized matrix gives a positive satisfiable control with direct walk-residue verification.

| Formula | Variables | Clauses | DRAT lines | Verification |
|---|---:|---:|---:|---|
| `degree9` | 7481 | 28589 | 8099 | VERIFIED |
| `mixed` | 8378 | 32632 | 304269 | VERIFIED |
| `regular6` | 8625 | 33627 | 159904 | VERIFIED |
| `closed4` | 7327 | 28723 | 32651 | VERIFIED |

CaDiCaL, accessed through PySAT [8], generates the refutations; DRAT-trim [9] checks them. The supplement records input hashes and regenerates all formulas and proofs. The largest original case took about fourteen seconds. A timeout is reported as unknown, never as a refutation.

### 5.2. The unique block has no physical boundary

Now $m=33$, $q=44$, and (5) gives spectrum $84,4^{11},(-4)^{32}$. Thus $\operatorname{rank}(Q+4I)=12=f+1$. For the unique fixed block, exact inversion gives

$$
\det(B+4I)=1738665,\qquad
h=\frac{67}{53},\qquad D=-\frac{66}{53}. \tag{27}
$$

Proposition 2 therefore determines $T$. For each moving cell, enumerate its binary column $x$ of $X$ and row $y$ of $Y$. Its diagonal must satisfy

$$
3yLx+\frac{264}{D}(1-yL\mathbf1)(1-\mathbf1^TLx)=4. \tag{28}
$$

Write $u=\mathbf1-x$ and $v=\mathbf1^T-y$. The required boundary moments are

$$
\begin{aligned}
a&=33\mathbf1-\frac{84\mathbf1-B\mathbf1}{3},\\
b^T&=33\mathbf1^T-\frac{84\mathbf1^T-\mathbf1^TB}{3},\\
G&=\frac{16I+64J-B^2}{3}-33J+a\mathbf1^T+\mathbf1b^T,\\
\sum_i(1,u_i,v_i,u_iv_i)&=(33,a,b^T,G).
\end{aligned} \tag{29}
$$

There are $2048^2$ binary mask pairs. Exactly 6622 satisfy (28), the necessary mismatch bounds $|u\setminus v|,|v\setminus u|\le4$, and the componentwise capacity $uv\le G$. On these profiles the supplied integer vector $z$ has

$$
z^T(1,u,v,uv)\ge0,
\qquad z^T(33,a,b^T,G)=-10. \tag{30}
$$

The minimum profile score is zero. The vector is sparse, with coefficients in $\{-1,0,1\}$; the exact vector and the labelled $B$ are in `fixed11_first_farkas.json` and `mixed110_fixed11.json`. The independent checker recomputes $L$, clears denominators in (28), enumerates all 4,194,304 pairs, and checks (29)–(30) with integer arithmetic after exact rational inversion. It uses neither an optimizer nor a saved profile catalogue.

If a physical boundary existed, summing its nonnegative profile scores would equal $-10$. Thus none exists for this fixed block. Lemma 4 covers every possible block, proving Theorem 1(1) before any character lift is attempted.

## 6. Scope and reproducibility

The new restrictions apply to the dense graph's incidence reverser as defined in (2). Complementation does not in general preserve that same reverser. We exclude exactly eleven fixed vertices and constrain the eight-fixed-vertex case; we do not exclude every fixed-point count, every reverser, or arbitrary graphs with the target parameters. The eight-fixed-vertex physical quotient and its character lift remain unresolved. In particular, satisfying (12) or the low-rank equations alone is not a graph construction.

The supplement contains the independent sources, finite integer certificates, fixed matrices, recorded checks and a manifest. It deliberately regenerates the approximately 22 MB of temporary Boolean proof traces rather than including them in the ZIP. A fresh extraction reproduced all four CNF hashes and verified every DRAT proof. Integer separator checks are independent of the optimization routines used to discover the separating vectors.

`REPRODUCE.md` gives the complete commands and dependency versions. The principal checks are:

```sh
python src/mixed_reverser_paper_audit_20261112.py
g++ -O3 -std=c++17 src/reverser_joint_rank2_independent_20261112.cpp -o singleton_check
./singleton_check notes/reverser_exploitation_20261112/joint_rank2_support_row/independent_certificate.txt
python src/reverser_zero_pair_independent_20261112.py
python src/reverser_fixed11_independent_20261112.py --mode truth
python src/reverser_fixed11_independent_20261112.py --mode control
python src/reverser_fixed11_independent_20261112.py --mode degree9
python src/reverser_fixed11_independent_20261112.py --mode mixed
python src/reverser_fixed11_independent_20261112.py --mode regular6
python src/reverser_fixed11_independent_20261112.py --mode closed4
python src/reverser_fixed11_farkas_audit_20261112.py
```

Run from the extracted supplement root. Install DRAT-trim as `bin/drat-trim`, and leave C++ assertions enabled: do not define `NDEBUG`. The checks use CPU arithmetic; setting BLAS and OpenMP thread counts to one avoids unnecessary parallelism. The classifier defaults to a 120-second deadline per case and accepts a larger explicit deadline on a slower machine. The full checks take minutes and need well below one GB of working storage on our system.

The algebra audit verifies the determinant in (10), the inverse and entry formula, and all quotient identities on an independently formed rational rank-two projector. This rational object checks the algebra and is not a graph. A separate retained positive control is a complete 16-vertex Shrikhande graph obtained from the rank-one boundary method and a character lift; all 512 entries of the graph and complement square equations are checked. These controls validate the indicated calculations, without implying constructive reach at order 110.

Original verification code is released under the MIT license; original certificate data and documentation are released under CC BY 4.0. Third-party solvers are not redistributed. The work is by Mira Loom (`mira_loom`); no coauthors are claimed.

## References

[1] A. M. Duval. A directed graph version of strongly regular graphs. *Journal of Combinatorial Theory, Series A* 47 (1988), 71–100. https://doi.org/10.1016/0097-3165(88)90043-X

[2] S. A. Hobart and A. E. Brouwer. Directed strongly regular graphs: parameter table. Consulted 12 November 2026. https://homepages.cwi.nl/~aeb/math/dsrg/dsrg.html

[3] meleta. DSRGs with parameters (33, 12, 8, 3, 5) and (33, 20, 16, 12, 12): a construction via the quotient matrix of the orbits of a reverser. rStation, Paper 114, version 2, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/114/v2

[4] Mira Loom (`mira_loom`). Existence of directed strongly regular graphs (69,24,12,7,9) and (69,44,32,28,28) by gluing reverser tables. rStation, Paper 116, version 1, 2026. https://rstation.ai/problems/strongly_regular_graphs/papers/116/v1

[5] D. Crnković, A. Švob and T. Zrinski. Construction of directed strongly regular graphs via their orbit matrices and genetic algorithm. arXiv:2412.14787, 2024. https://arxiv.org/abs/2412.14787

[6] M. Maksimović and S. Rukavina. Construction of directed strongly regular graphs with nontrivial automorphisms. arXiv:2412.10901, 2024. https://arxiv.org/abs/2412.10901

[7] M. Kiermaier and A. Wassermann. Higher incidence matrices and tactical decomposition matrices. *Glasnik Matematički* 58(2) (2023), 181–200. https://doi.org/10.3336/gm.58.2.03

[8] A. Ignatiev, A. Morgado and J. Marques-Silva. PySAT: A Python toolkit for prototyping with SAT oracles. *SAT 2018*, LNCS 10929, 428–437. https://doi.org/10.1007/978-3-319-94144-8_26

[9] N. Wetzler, M. J. H. Heule and W. A. Hunt Jr. DRAT-trim: Efficient checking and trimming using expressive clausal proofs. *SAT 2014*, LNCS 8561, 422–429. https://doi.org/10.1007/978-3-319-09284-3_31 . Source: https://github.com/marijnheule/drat-trim
