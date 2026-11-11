# The Exact Tensor-Filtration Defect on Products of a Fermat Curve and a Fermat Hypersurface

*This work was conducted autonomously by an AI agent with human oversight primarily on problem selection, verification, and resource support.*

## 1. Problem and contribution

Let $m \ge 3$ and $n \ge 1$ be integers, and let $X_m^1 \subset \mathbf{P}^2$ and $X_m^n \subset \mathbf{P}^{n+1}$ denote the smooth complex Fermat curve and $n$-dimensional Fermat hypersurface defined by

$$x_0^m + x_1^m + x_2^m = 0 \quad \text{and} \quad y_0^m + y_1^m + \cdots + y_{n+1}^m = 0,$$

respectively. Write

$$H_m := H^1(X_m^1, \mathbf{Q}), \qquad K_{m,n} := H^n_{\mathrm{prim}}(X_m^n, \mathbf{Q})$$

for their rational primitive middle cohomology groups, endowed with their pure $\mathbf{Q}$-Hodge structures of weights $1$ and $n$. For any finite-dimensional pure $\mathbf{Q}$-Hodge structure $V$ of weight $w$ and any integer $q \in \mathbf{Z}$, the *rational level filtration* (or *rational Hodge-level filtration*) $\mathsf{F}^q V \subseteq V$ is defined to be the largest $\mathbf{Q}$-sub-Hodge structure of $V$ such that

$$(\mathsf{F}^q V)_{\mathbf{C}} \subseteq F^q(V_{\mathbf{C}}) = \bigoplus_{\substack{p+r=w \\ p \ge q}} V^{p,r}.$$

Because $V$ is defined over $\mathbf{Q}$ and $\overline{V^{p,r}} = V^{r,p}$, any $\mathbf{Q}$-subspace $W \subseteq V$ satisfies $W_{\mathbf{C}} = \overline{W_{\mathbf{C}}}$, so $W_{\mathbf{C}} \subseteq F^q(V_{\mathbf{C}})$ holds if and only if

$$W_{\mathbf{C}} \subseteq F^q(V_{\mathbf{C}}) \cap \overline{F^q(V_{\mathbf{C}})} = \bigoplus_{\substack{p+r=w \\ p \ge q,\; r \ge q}} V^{p,r}.$$

Unlike the complex Hodge filtration $F^\bullet$ on $V_{\mathbf{C}}$, which satisfies the Künneth identity $F^q(V_{\mathbf{C}} \otimes_{\mathbf{C}} W_{\mathbf{C}}) = \sum_{i+j=q} F^i(V_{\mathbf{C}}) \otimes_{\mathbf{C}} F^j(W_{\mathbf{C}})$, the rational level filtration $\mathsf{F}^\bullet$ imposes simultaneous conjugate bounds on both factors and does not in general commute with tensor products over $\mathbf{Q}$.

On the tensor product $H_m \otimes_{\mathbf{Q}} K_{m,n}$ of weight $n+1$, the Künneth tensor product of the factor filtrations is a $\mathbf{Q}$-sub-Hodge structure whose complexification lies in $F^q((H_m \otimes_{\mathbf{Q}} K_{m,n})_{\mathbf{C}})$. By the maximality of $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})$, there is a canonical injective $\mathbf{Q}$-Hodge morphism

$$\iota_{m,n,q} : \sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n} \hookrightarrow \mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr).$$

Since $H_m$ has pure weight $1$ with Hodge types $(1,0)$ and $(0,1)$, we have $\mathsf{F}^i H_m = H_m$ for $i \le 0$ and $\mathsf{F}^i H_m = 0$ for $i \ge 1$. Moreover, $\mathsf{F}^j K_{m,n}$ is decreasing in $j$, so the image of $\iota_{m,n,q}$ simplifies for every $q \in \mathbf{Z}$ to

$$\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n} = H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}.$$

The problem studied in this paper is to determine, for all integers $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$, when the inclusion $\iota_{m,n,q}$ is an equality and to bound the rank of the resulting *tensor-filtration defect quotient*

$$\Delta_q(m,n) := \frac{\mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr)}{\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n}} = \frac{\mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr)}{H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}}.$$

Our main results resolve this problem completely across the entire $(m,n,q)$ parameter space.

**Theorem 1.1 (Exact tensor-filtration boundary).** *Let $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$. The tensor-filtration defect $\Delta_q(m,n)$ is nonzero if and only if*

$$mq \ge n+2 \quad \text{and} \quad 2q \le n+1.$$

*Equivalently:*
1. *For $q \le 0$ or $2q > n+1$, one has $\Delta_q(m,n) = 0$.*
2. *For $1 \le q \le \lfloor (n+1)/2 \rfloor$, the inclusion $\iota_{m,n,q}$ is an isomorphism ($\Delta_q(m,n) = 0$) in the sub-threshold regime $3 \le m \le \lfloor (n+1)/q \rfloor$, and fails to be surjective ($\Delta_q(m,n) \ne 0$) for every degree $m \ge \lfloor (n+1)/q \rfloor + 1 = \lceil (n+2)/q \rceil$.*

To state our constructive witness theorem and rank lower bound in the nonzero regime, let $\mu_m \subset \mathbf{C}^\times$ be the group of $m$-th roots of unity, and let $G_m^n := \mu_m^{n+2}/\mathrm{diag}(\mu_m)$ be the projective diagonal automorphism group of $X_m^n$. Its character group $\widehat{G_m^n}$ is identified with the set of tuples $\beta = (b_0,\dots,b_{n+1}) \in (\mathbf{Z}/m\mathbf{Z})^{n+2}$ satisfying $b_0 + \cdots + b_{n+1} \equiv 0 \pmod m$, and the primitive character set is

$$A_{m,n} := \Bigl\{ \beta = (b_0,\dots,b_{n+1}) \in \{1,\dots,m-1\}^{n+2} : \sum_{j=0}^{n+1} b_j \equiv 0 \pmod m \Bigr\}.$$

For an element $c \in \{1,\dots,m-1\}$ and an integer $r \ge 0$, we write $c^{(r)}$ for $r$ consecutive coordinates equal to $c$, and $(1,m-1)^{(s)}$ for $s$ consecutive blocks $(1,m-1)$.

**Theorem 1.2 (Explicit witness family and permutation-orbit rank lower bound).** *Assume $m \ge 3$, $n \ge 1$, $mq \ge n+2$, and $2q \le n+1$. Then there exists an integer $s \in \{0, 1, \dots, \lfloor (n-1)/2 \rfloor\}$ such that*

$$m \nmid (n-2s+1) \quad \text{and} \quad q = s + 1 + \Bigl\lfloor \frac{n-2s+1}{m} \Bigr\rfloor.$$

*Fix any such $s$, set $d := n - 2s \ge 1$, and let $\langle d+1 \rangle_m \in \{1,\dots,m-1\}$ denote the unique representative of $d+1 \bmod m$. Define the seed characters*

$$A := (1, 1, m-2) \in A_{m,1}, \qquad B = B(s) := \bigl((m-1)^{(d+1)},\, \langle d+1 \rangle_m,\, (1,m-1)^{(s)}\bigr) \in A_{m,n}.$$

*Then:*
1. *For every $\sigma \in \mathfrak{S}_3$ and $\tau \in \mathfrak{S}_{n+2}$, the $(\mathbf{Z}/m\mathbf{Z})^\times$-orbit of $(\sigma(A), \tau(B))$ in $A_{m,1} \times A_{m,n}$ has cardinality $\varphi(m)$ and spans a $\varphi(m)$-dimensional $\mathbf{Q}$-sub-Hodge structure of $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})$ whose intersection with $H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}$ is zero.*
2. *If two distinct integers $s_1 < s_2$ satisfy the admissibility conditions above for the same triple $(m,n,q)$, then $s_2 = s_1 + 1$, $n - 2s_1 + 1 \equiv 1 \pmod m$, and the tuples $B(s_1)$ and $B(s_2)$ have the exact same coordinate multiset (and hence the same $\mathfrak{S}_{n+2}$-orbit).*
3. *As $\sigma$ ranges over $\mathfrak{S}_3$ and $\tau$ ranges over $\mathfrak{S}_{n+2}$, the distinct $(\mathbf{Z}/m\mathbf{Z})^\times$-orbits of $(\sigma(A), \tau(B))$ are pairwise disjoint in $A_{m,1} \times A_{m,n}$ and yield the canonical rank lower bound*

$$\dim_{\mathbf{Q}} \Delta_q(m,n) \ge \nu_x(m,n,q) := \varphi(m) \cdot |\mathfrak{S}_3 \cdot A| \cdot |\mathfrak{S}_{n+2} \cdot B| = \varphi(m) \cdot c_A(m) \cdot \frac{(n+2)!}{\prod_{c=1}^{m-1} \mu_c(B)!},$$

*where $c_A(3) = 1$, $c_A(m) = 3$ for $m \ge 4$, and $\mu_c(B)$ denotes the multiplicity of the residue $c$ in $B$.*

When $n$ is odd, $K_{m,n} = H^n(X_m^n, \mathbf{Q})$ is the entire middle cohomology of $X_m^n$. When $n = 2k$ is even, $H^n(X_m^n, \mathbf{Q})$ is the orthogonal direct sum of $K_{m,n}$ and the one-dimensional hyperplane class line $\mathbf{Q}h^k \simeq \mathbf{Q}(-k)$. Our third result shows that passing from primitive to full middle cohomology does not alter the defect quotient.

**Proposition 1.3 (Invariance between primitive and full middle cohomology for even $n$).** *For every degree $m \ge 3$, every even dimension $n = 2k \ge 2$, and every filtration step $q \in \mathbf{Z}$, the hyperplane class summand $H_m \otimes_{\mathbf{Q}} \mathbf{Q}h^k \subset H_m \otimes_{\mathbf{Q}} H^n(X_m^n, \mathbf{Q})$ satisfies*

$$\mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} \mathbf{Q}h^k\bigr) = \sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j(\mathbf{Q}h^k) = H_m \otimes_{\mathbf{Q}} \mathsf{F}^q(\mathbf{Q}h^k).$$

*Consequently, the canonical inclusion $K_{m,n} \hookrightarrow H^n(X_m^n, \mathbf{Q})$ induces a canonical isomorphism*

$$\frac{\mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} H^n(X_m^n, \mathbf{Q})\bigr)}{\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j H^n(X_m^n, \mathbf{Q})} \xrightarrow{\;\sim\;} \Delta_q(m,n).$$

### Summary of contributions

- **All-parameter boundary criterion (Theorem 1.1 and Proposition 2.2):** Using the Galois/character-orbit decomposition of $H_m$ and $K_{m,n}$ under $G_m^1 \times G_m^n$ and the complex-conjugation involution $t = -1 \in (\mathbf{Z}/m\mathbf{Z})^\times$, we derive an exact combinatorial dimension formula for $\Delta_q(m,n)$ (Proposition 2.2) and prove that $\Delta_q(m,n) \ne 0 \iff mq \ge n+2 \text{ and } 2q \le n+1$.
- **Explicit witness family, multiset invariance, and rank lower bound (Theorem 1.2 and Proposition 3.3):** In every nonzero regime we construct explicit primitive character pairs $(A, B(s))$ via cyclic floor identities (Lemmas 3.1 and 3.2), prove that the coordinate multiset of $B(s)$ is canonically independent of the choice of admissible $s$ whenever two values of $s$ occur (Proposition 3.3), and prove disjointness of the $(\mathbf{Z}/m\mathbf{Z})^\times$-orbits across $\mathfrak{S}_3 \times \mathfrak{S}_{n+2}$ to obtain the lower bound $\dim_{\mathbf{Q}} \Delta_q(m,n) \ge \nu_x(m,n,q)$.
- **Even-dimension invariance and Borel–Moore translation (Proposition 1.3 and Corollary 4.1):** We prove that the algebraic $(k,k)$-class on even-dimensional Fermat hypersurfaces contributes zero defect for all $q \in \mathbf{Z}$, and translate Theorems 1.1 and 1.2 via Poincaré duality to the Borel–Moore homological level filtration $\mathsf{F}^{\mathrm{BM}}_p$ on $X_m^1 \times X_m^n$.
- **Exact scope of the level-filtration product formula in the literature:** We show that the Künneth equality for the rational level filtration asserted in Proposition 2.2(iv) of Kang [1] and applied to $X_m^1 \times X_m^n$ in Kang [2] holds at step $q \ge 1$ if and only if $m \le (n+1)/q$, and we provide a standalone standard-library verification package checking 91 pairs $(m,n)$, 309 filtration cells, and 17,534 explicit witness pairs.

### 1.1. Relation to the Hodge conjecture and the product filtration chain

For a smooth projective complex variety $Y$ and integers $k, q \ge 0$, Grothendieck's coniveau (arithmetic) filtration $N^q H^k(Y, \mathbf{Q})$ is defined by

$$N^q H^k(Y, \mathbf{Q}) := \sum_{\substack{Z \subset Y \text{ closed} \\ \mathrm{codim}_Y(Z) \ge q}} \ker\bigl(H^k(Y, \mathbf{Q}) \to H^k(Y \setminus Z, \mathbf{Q})\bigr).$$

Each $N^q H^k(Y, \mathbf{Q})$ is a $\mathbf{Q}$-sub-Hodge structure of $H^k(Y, \mathbf{Q})$ whose complexification lies in $F^q H^k(Y, \mathbf{C})$. By the definition of the rational level filtration $\mathsf{F}^q H^k(Y, \mathbf{Q})$ as the largest such $\mathbf{Q}$-sub-Hodge structure, one has the inclusion $N^q H^k(Y, \mathbf{Q}) \subseteq \mathsf{F}^q H^k(Y, \mathbf{Q})$, and Grothendieck's generalized Hodge conjecture for $(Y, k, q)$ is the equality $N^q H^k(Y, \mathbf{Q}) = \mathsf{F}^q H^k(Y, \mathbf{Q})$.

On the product $Y = X_m^1 \times X_m^n$ in degree $k = n+1$, projecting onto the Künneth summand $H_m \otimes_{\mathbf{Q}} K_{m,n} \subset H^{n+1}(X_m^1 \times X_m^n, \mathbf{Q})$ yields a three-term chain of decreasing $\mathbf{Q}$-sub-Hodge structures:

$$\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n} \;\subseteq\; \mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr), \qquad N^q\bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr) \;\subseteq\; \mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr).$$

If the generalized Hodge conjecture holds for $X_m^1$ and $X_m^n$ individually, external products of cycle-supported classes span the left-hand subfiltration $\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n} = H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n} \subseteq N^q(H_m \otimes_{\mathbf{Q}} K_{m,n})$. Theorem 1.1 shows that whenever $mq \ge n+2$ and $2q \le n+1$, the ambient rational level filtration $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})$ is strictly larger than the factorwise subfiltration $H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}$. The quotient $\Delta_q(m,n)$ precisely classifies the *entangled* rational sub-Hodge structures of $H_m \otimes_{\mathbf{Q}} K_{m,n}$ at level $q$: classes whose individual Künneth factors drop below level $q$ at one or more embeddings $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, yet whose tensor product satisfies the level-$q$ Hodge bound at every $t \in (\mathbf{Z}/m\mathbf{Z})^\times$ simultaneously because the curve factor supplies the missing Hodge weight $p_m(t\alpha) = 1$ at every $t$ where $p_m(t\beta) = q-1$.

Consequently, Theorem 1.1 and Theorem 1.2 are purely Hodge-theoretic theorems about the rational level filtration $\mathsf{F}^q$: they do not disprove the generalized Hodge conjecture on $X_m^1 \times X_m^n$ or $X_m^{n+1}$, nor do they assert that classes in $\Delta_q(m,n)$ fail to lie in $N^q$. Rather, they demonstrate that whenever $mq \ge n+2$ and $2q \le n+1$, establishing $N^q = \mathsf{F}^q$ on $X_m^1 \times X_m^n$ requires genuinely non-factorized correspondences on $X_m^1 \times X_m^n$ (such as the inductive blowup-quotient correspondences of Shioda and Katsura) rather than external products of subfiltrations from the two factors.

### 1.2. Related work and distinction

1. **Refined motivic dimension and the product level filtration (Kang [1, 2]):** In [1] (Section 2, pp. 519–521), Kang introduced the rational level filtration $\mathsf{F}_p H^{\mathrm{BM}}_i(X)$ on Borel–Moore homology (and $\mathsf{F}^q H^i(X, \mathbf{Q})$ on cohomology; see [1] (equation (2.1), p. 521)) to define a refined motivic dimension $\dim_m(X)$. In [1] (Proposition 2.2(iv), pp. 521–522), Kang stated the product inequality $\dim_m(X_1 \times X_2) \le \dim_m(X_1) + \dim_m(X_2)$; its proof on p. 522 asserts the Künneth identity $\mathsf{F}_p H^{\mathrm{BM}}_k(X_1 \times X_2) = \bigoplus_{s+t=k} \bigoplus_{i+j=p} \mathsf{F}_i H^{\mathrm{BM}}_s(X_1) \otimes \mathsf{F}_j H^{\mathrm{BM}}_t(X_2)$. In [2] (Theorem 3.1 and Corollary 3.2, pp. 226–227), Kang combined the Shioda–Katsura inductive blowup structure of Fermat varieties with [1] (Proposition 2.2(iv)) on $X_m^1 \times X_m^{n_{\mathrm{Kang}}-1}$, invoking the product inequality at $q=1$ in [2] (equation (3.3), p. 227, for $n_{\mathrm{Kang}} \in \{3,4\}$, corresponding to our $n = n_{\mathrm{Kang}}-1 \in \{2,3\}$) and at $q=2$ in [2] (equation (4.2), p. 228, for $m \le 4$ and $n_{\mathrm{Kang}} \ge 5$, corresponding to our $n = n_{\mathrm{Kang}}-1 \ge 4$). By Theorem 1.1 and Corollary 4.1 below, at $q=1$ the tensor identity holds for $3 \le m \le n+1$ (so $(m,n)=(3,2)$, $(3,3)$, and $(4,3)$ have $\Delta_1(m,n)=0$) and fails for all $m \ge n+2$; at $q=2$ and $m \in \{3,4\}$, it holds for $m \le (n+1)/2$ and fails at $(m,n,q)=(3,4,2)$ and at $(m,n,q)=(4,n,2)$ for $n \in \{4,5,6\}$.
2. **Distinction from Li [3] (`hodge_conjecture_104`):** In our earlier paper [3], the main results (Sections 1–5) classify residual Hodge characters on odd-degree Fermat fourfolds $X_m^4$ modulo Shioda's inductive contribution from $X_m^2 \times X_m^2$ and Aoki's $p$-standard classes, reducing all composite odd degrees $m \le 195$ with $\gcd(m,6) > 1$ to inflations of six explicit seeds in degrees $33, 39, 45$, and $105$. In [3] (Section 6, Proposition 6.1), we gave a 5-tuple specialization showing $\Delta_1(m,3) \ne 0$ solely for odd degrees $m \ge 5$ at the single parameter choice $(n,q) = (3,1)$ using $B = (2,2,2,m-5,m-1)$ for odd $m \ge 7$ and $B = (2,2,2,2,2)$ for $m = 5$. That construction is undefined for even degrees $m$ (where $\gcd(2,m) > 1$ and $B=(2,2,2,m-5,m-1)$ loses primitive-orbit control) and does not address $n \ne 3$ or $q \ge 2$. The present paper solves the general problem across all integers $m \ge 3$ (both even and odd), all dimensions $n \ge 1$, and all filtration steps $q \in \mathbf{Z}$, establishing the exact necessary and sufficient boundary $mq \ge n+2 \wedge 2q \le n+1$ (Theorem 1.1), a uniform witness family $B(s)$ valid for all parities of $m$ together with multiset invariance and the permutation-orbit rank lower bound (Theorem 1.2 and Proposition 3.3), and the even-$n$ full-cohomology invariance (Proposition 1.3).
3. **Character theory of Fermat varieties and recent applications:** The character decomposition of $H^n_{\mathrm{prim}}(X_m^n, \mathbf{C})$, the residue formula for Hodge types, and the inductive blowup-quotient geometry of $X_m^r \times X_m^s \dashrightarrow X_m^{r+s}$ are due to Shioda [4], Shioda and Katsura [5], Griffiths [6, 7], Aoki [8], and Deligne [9]. More recently, Miranda, Movasati, Rufino, and Villaflor [10] studied minimal lengths of Hodge characters on Fermat varieties and cited Kang [2] regarding Fermat fourfolds, while Bini, Laterveer, and Pacienza [11] (p. 93) cited [2] in the context of generalized Hodge and Voisin conjectures. Theorem 1.1 and Theorem 1.2 clarify the exact parameter range in which the Künneth level-filtration step in [1, 2] holds as stated and quantify the entangled character space $\Delta_q(m,n)$ beyond that boundary.

---

## 2. Character decomposition, rational descent, and the exact defect formula

### 2.1. Eigenspaces and Griffiths–Shioda Hodge weights

Fix integers $m \ge 3$ and $n \ge 1$. For any integer $x \in \mathbf{Z}$ with $m \nmid x$, let $\langle x \rangle_m \in \{1, 2, \dots, m-1\}$ denote the unique standard residue satisfying $x \equiv \langle x \rangle_m \pmod m$. The group $(\mathbf{Z}/m\mathbf{Z})^\times$ of units modulo $m$ has order $\varphi(m)$ and acts freely on the primitive character set $A_{m,n}$ by componentwise multiplication modulo $m$:

$$t \cdot \beta := \bigl(\langle t b_0 \rangle_m, \langle t b_1 \rangle_m, \dots, \langle t b_{n+1} \rangle_m\bigr) \in A_{m,n} \qquad \bigl(t \in (\mathbf{Z}/m\mathbf{Z})^\times,\; \beta \in A_{m,n}\bigr).$$

For each $\beta = (b_0, \dots, b_{n+1}) \in A_{m,n}$, define its normalized weight (or *age shift*) by

$$|\beta|_m := \frac{1}{m} \sum_{j=0}^{n+1} \langle b_j \rangle_m \in \{1, 2, \dots, n+1\}, \qquad p_m(\beta) := |\beta|_m - 1 \in \{0, 1, \dots, n\}.$$

By the classical theorem of Griffiths [6, 7] and Shioda [4] (Theorem I, p. 176; see also Shioda–Katsura [5], Section 2, and Aoki [8], p. 385), the complexified primitive middle cohomology $K_{m,n,\mathbf{C}} = H^n_{\mathrm{prim}}(X_m^n, \mathbf{C})$ decomposes under the action of $G_m^n$ into one-dimensional character eigenspaces

$$K_{m,n,\mathbf{C}} = \bigoplus_{\beta \in A_{m,n}} V(\beta), \qquad \dim_{\mathbf{C}} V(\beta) = 1,$$

such that $V(\beta)$ is pure of Hodge type $(n - p_m(\beta),\, p_m(\beta))$:

$$V(\beta) \subseteq H^{n - p_m(\beta),\, p_m(\beta)}_{\mathrm{prim}}(X_m^n).$$

In particular, for the Fermat curve $X_m^1$ ($n=1$), $H_{m,\mathbf{C}} = H^1(X_m^1, \mathbf{C}) = \bigoplus_{\alpha \in A_{m,1}} V(\alpha)$ with $p_m(\alpha) \in \{0, 1\}$ and $V(\alpha) \subseteq H^{1 - p_m(\alpha),\, p_m(\alpha)}(X_m^1)$.

For any $\beta \in A_{m,n}$ and $t = -1 \equiv m-1 \pmod m$, every coordinate satisfies $\langle (m-1)b_j \rangle_m = m - \langle b_j \rangle_m$, so

$$|(m-1)\beta|_m = \frac{1}{m}\sum_{j=0}^{n+1} \bigl(m - \langle b_j \rangle_m\bigr) = (n+2) - |\beta|_m,$$

which yields the fundamental involution identity

$$p_m((m-1)\beta) = n - p_m(\beta) \qquad (\forall\, \beta \in A_{m,n}),$$

and in particular $p_m((m-1)\alpha) = 1 - p_m(\alpha)$ for all $\alpha \in A_{m,1}$.

### 2.2. Rational descent along $(\mathbf{Z}/m\mathbf{Z})^\times$-orbits

Because the $G_m^n$-action on $X_m^n$ is defined over the cyclotomic field $\mathbf{Q}(\mu_m)$ and $\mathrm{Gal}(\mathbf{Q}(\mu_m)/\mathbf{Q}) \simeq (\mathbf{Z}/m\mathbf{Z})^\times$ permutes the character lines according to $\sigma_t(V(\beta)) = V(t\beta)$, the rational Hodge structure $K_{m,n}$ (and similarly $H_m$ and $H_m \otimes_{\mathbf{Q}} K_{m,n}$) decomposes over $\mathbf{Q}$ along the $(\mathbf{Z}/m\mathbf{Z})^\times$-orbits of characters. Specifically, for each $(\mathbf{Z}/m\mathbf{Z})^\times$-orbit $\mathcal{O} \subseteq A_{m,1} \times A_{m,n}$ of the diagonal unit action $t \cdot (\alpha, \beta) := (t\alpha, t\beta)$, there is a unique $\mathbf{Q}$-sub-Hodge structure $W(\mathcal{O}) \subseteq H_m \otimes_{\mathbf{Q}} K_{m,n}$ whose complexification is

$$W(\mathcal{O})_{\mathbf{C}} = \bigoplus_{(\alpha, \beta) \in \mathcal{O}} V(\alpha) \otimes_{\mathbf{C}} V(\beta).$$

Since $G_m^1 \times G_m^n$ acts on $X_m^1 \times X_m^n$ by algebraic automorphisms, every $\mathbf{Q}[G_m^1 \times G_m^n]$-stable $\mathbf{Q}$-sub-Hodge structure of $H_m \otimes_{\mathbf{Q}} K_{m,n}$ — and in particular both $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})$ and $H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}$ — decomposes as a direct sum of its intersections with the character-orbit subspaces.

**Lemma 2.1 (Orbit-level criterion for $\mathsf{F}^q$).** *Let $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$.*
1. *For any $\beta \in A_{m,n}$, the character line $V(\beta)$ lies in $(\mathsf{F}^q K_{m,n})_{\mathbf{C}}$ if and only if*
   $$\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta) \ge q \quad \text{and} \quad \max_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta) \le n - q,$$
   *and these two inequalities are equivalent to the single inequality $\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta) \ge q$.*
2. *For any pair $(\alpha, \beta) \in A_{m,1} \times A_{m,n}$, the tensor line $V(\alpha) \otimes_{\mathbf{C}} V(\beta)$ lies in $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})_{\mathbf{C}}$ if and only if*
   $$\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} \bigl(p_m(t\alpha) + p_m(t\beta)\bigr) \ge q \quad \text{and} \quad \max_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} \bigl(p_m(t\alpha) + p_m(t\beta)\bigr) \le n + 1 - q,$$
   *and these two inequalities are equivalent to the single inequality $\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} (p_m(t\alpha) + p_m(t\beta)) \ge q$.*

*Proof.* (1) For each $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, the line $V(t\beta)$ has Hodge type $(n - p_m(t\beta),\, p_m(t\beta))$. It lies in $F^q(K_{m,n,\mathbf{C}}) \cap \overline{F^q(K_{m,n,\mathbf{C}})}$ if and only if both Hodge indices are at least $q$, that is, $n - p_m(t\beta) \ge q$ and $p_m(t\beta) \ge q$. Since $\mathsf{F}^q K_{m,n}$ is defined over $\mathbf{Q}$, $V(\beta) \subseteq (\mathsf{F}^q K_{m,n})_{\mathbf{C}}$ if and only if $V(t\beta)$ satisfies both bounds for every $t \in (\mathbf{Z}/m\mathbf{Z})^\times$. Because multiplication by $m-1 \in (\mathbf{Z}/m\mathbf{Z})^\times$ is a bijection on $(\mathbf{Z}/m\mathbf{Z})^\times$ satisfying $p_m((m-1)t\beta) = n - p_m(t\beta)$, we have

$$\max_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta) = n - \min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta),$$

so the upper bound $\max_t p_m(t\beta) \le n - q$ is identical to the lower bound $\min_t p_m(t\beta) \ge q$.

(2) For $(\alpha, \beta) \in A_{m,1} \times A_{m,n}$ and $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, the tensor line $V(t\alpha) \otimes_{\mathbf{C}} V(t\beta)$ has Hodge type $(n + 1 - (p_m(t\alpha) + p_m(t\beta)),\, p_m(t\alpha) + p_m(t\beta))$. Thus $V(\alpha) \otimes_{\mathbf{C}} V(\beta) \subseteq \mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})_{\mathbf{C}}$ if and only if $q \le p_m(t\alpha) + p_m(t\beta) \le n + 1 - q$ for every $t \in (\mathbf{Z}/m\mathbf{Z})^\times$. Using $p_m((m-1)t\alpha) + p_m((m-1)t\beta) = (1 - p_m(t\alpha)) + (n - p_m(t\beta)) = n + 1 - (p_m(t\alpha) + p_m(t\beta))$, the upper and lower conditions across $t \in (\mathbf{Z}/m\mathbf{Z})^\times$ are again equivalent. $\square$

For each $(\alpha, \beta) \in A_{m,1} \times A_{m,n}$, define the orbit-minimum level functions

$$q(\beta) := \min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta), \qquad q(\alpha, \beta) := \min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} \bigl(p_m(t\alpha) + p_m(t\beta)\bigr).$$

Since $p_m(t\alpha) \in \{0, 1\}$ for every $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, we immediately have

$$q(\beta) \le q(\alpha, \beta) \le q(\beta) + 1.$$

Define the three character subsets of $A_{m,1} \times A_{m,n}$:

$$P_q(m,n) := \bigl\{ (\alpha, \beta) \in A_{m,1} \times A_{m,n} : q(\alpha, \beta) \ge q \bigr\},$$

$$D_q(m,n) := \bigl\{ (\alpha, \beta) \in A_{m,1} \times A_{m,n} : q(\beta) \ge q \bigr\},$$

$$E_q(m,n) := P_q(m,n) \setminus D_q(m,n) = \bigl\{ (\alpha, \beta) \in A_{m,1} \times A_{m,n} : q(\beta) = q - 1 \text{ and } q(\alpha, \beta) = q \bigr\}.$$

**Proposition 2.2 (Exact character formula for $\Delta_q(m,n)$).** *For all integers $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$:*
1. *The complexifications of $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} K_{m,n})$ and $\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n} = H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}$ are spanned by $\{V(\alpha) \otimes_{\mathbf{C}} V(\beta) : (\alpha, \beta) \in P_q(m,n)\}$ and $\{V(\alpha) \otimes_{\mathbf{C}} V(\beta) : (\alpha, \beta) \in D_q(m,n)\}$, respectively.*
2. *The defect quotient $\Delta_q(m,n)$ has complexification canonically isomorphic to $\bigoplus_{(\alpha, \beta) \in E_q(m,n)} V(\alpha) \otimes_{\mathbf{C}} V(\beta)$, and its rational dimension is*
   $$\dim_{\mathbf{Q}} \Delta_q(m,n) = |P_q(m,n)| - |D_q(m,n)| = |E_q(m,n)|.$$
3. *A pair $(\alpha, \beta) \in A_{m,1} \times A_{m,n}$ belongs to $E_q(m,n)$ if and only if $\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t\beta) = q - 1$ and, for every $t \in (\mathbf{Z}/m\mathbf{Z})^\times$ with $p_m(t\beta) = q - 1$, one has $p_m(t\alpha) = 1$.*

*Proof.* Parts (1) and (2) follow immediately from Lemma 2.1 and the equality $\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j K_{m,n} = H_m \otimes_{\mathbf{Q}} \mathsf{F}^q K_{m,n}$. For part (3), since $p_m(t\alpha) \in \{0, 1\}$, the condition $q(\beta) < q \le q(\alpha, \beta)$ forces $q(\beta) = q - 1$ and requires that whenever $p_m(t\beta) = q - 1$, the term $p_m(t\alpha)$ cannot be $0$ and therefore equals $1$. $\square$

### 2.3. Proof of Proposition 1.3 (even-$n$ full middle cohomology)

We now prove Proposition 1.3, establishing that when $n = 2k$ is even, replacing $K_{m,n} = H^n_{\mathrm{prim}}(X_m^n, \mathbf{Q})$ by the full middle cohomology $H^n(X_m^n, \mathbf{Q})$ leaves the defect quotient $\Delta_q(m,n)$ canonically unchanged.

*Proof of Proposition 1.3.* Let $n = 2k \ge 2$ be even, and let $h \in H^2(X_m^n, \mathbf{Q})$ be the hyperplane class. By the Lefschetz decomposition on the smooth hypersurface $X_m^n \subset \mathbf{P}^{n+1}$, the full middle cohomology splits as a direct sum of $\mathbf{Q}$-Hodge structures

$$H^n(X_m^n, \mathbf{Q}) = K_{m,n} \oplus \mathbf{Q}h^k,$$

where $L := \mathbf{Q}h^k \simeq \mathbf{Q}(-k)$ is a one-dimensional rational Hodge structure pure of Hodge type $(k, k)$. Because the rational level filtration $\mathsf{F}^\bullet$ is defined as a functor on pure $\mathbf{Q}$-Hodge structures via subobjects whose complexifications lie in $F^\bullet$, it commutes with direct sums of $\mathbf{Q}$-Hodge structures: for any $\mathbf{Q}$-Hodge structures $U_1, U_2$ of the same weight, $\mathsf{F}^q(U_1 \oplus U_2) = \mathsf{F}^q U_1 \oplus \mathsf{F}^q U_2$. Applying this to

$$H_m \otimes_{\mathbf{Q}} H^n(X_m^n, \mathbf{Q}) = \bigl(H_m \otimes_{\mathbf{Q}} K_{m,n}\bigr) \oplus \bigl(H_m \otimes_{\mathbf{Q}} L\bigr),$$

and similarly to each factor $\mathsf{F}^j H^n(X_m^n, \mathbf{Q}) = \mathsf{F}^j K_{m,n} \oplus \mathsf{F}^j L$, we obtain

$$\frac{\mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} H^n(X_m^n, \mathbf{Q})\bigr)}{\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j H^n(X_m^n, \mathbf{Q})} \simeq \Delta_q(m,n) \oplus \frac{\mathsf{F}^q\bigl(H_m \otimes_{\mathbf{Q}} L\bigr)}{\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j L}.$$

It therefore suffices to show that the second summand vanishes for every $q \in \mathbf{Z}$.

Since $L$ is pure of type $(k, k)$, its rational level filtration is

$$\mathsf{F}^j L = \begin{cases} L & \text{if } j \le k, \\ 0 & \text{if } j \ge k+1. \end{cases}$$

Using $\mathsf{F}^i H_m = H_m$ for $i \le 0$ and $\mathsf{F}^i H_m = 0$ for $i \ge 1$, the factorwise sum is

$$\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j L = H_m \otimes_{\mathbf{Q}} \mathsf{F}^q L = \begin{cases} H_m \otimes_{\mathbf{Q}} L & \text{if } q \le k, \\ 0 & \text{if } q \ge k+1. \end{cases}$$

On the other hand, $H_{m,\mathbf{C}} = H^{1,0}(X_m^1) \oplus H^{0,1}(X_m^1)$ and $L_{\mathbf{C}}$ is pure of type $(k, k)$, so $(H_m \otimes_{\mathbf{Q}} L)_{\mathbf{C}}$ is concentrated purely in Hodge bidegrees $(k+1, k)$ and $(k, k+1)$. For every $(p, r) \in \{(k+1, k), (k, k+1)\}$, we have $\min(p, r) = k$. Consequently,

$$F^q\bigl((H_m \otimes_{\mathbf{Q}} L)_{\mathbf{C}}\bigr) \cap \overline{F^q\bigl((H_m \otimes_{\mathbf{Q}} L)_{\mathbf{C}}\bigr)} = \begin{cases} (H_m \otimes_{\mathbf{Q}} L)_{\mathbf{C}} & \text{if } q \le k, \\ 0 & \text{if } q \ge k+1. \end{cases}$$

Thus $\mathsf{F}^q(H_m \otimes_{\mathbf{Q}} L)$ equals $H_m \otimes_{\mathbf{Q}} L$ for $q \le k$ and $0$ for $q \ge k+1$, matching $\sum_{i+j=q} \mathsf{F}^i H_m \otimes_{\mathbf{Q}} \mathsf{F}^j L$ for every $q \in \mathbf{Z}$. $\square$

---

## 3. Proof of the boundary criterion, the witness family, and multiset invariance

### 3.1. Vanishing of $\Delta_q(m,n)$ outside the boundary locus

We first establish the "only if" direction of Theorem 1.1 by showing that $E_q(m,n) = \emptyset$ whenever $q \le 0$, $2q > n+1$, or $mq \le n+1$.

**Proposition 3.0 (Vanishing regimes).** *Let $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$. Then $\Delta_q(m,n) = 0$ in each of the following three cases:*
1. *$q \le 0$;*
2. *$2q > n+1$;*
3. *$q \ge 1$ and $mq \le n+1$.*

*Proof.* (1) Suppose $q \le 0$. For every $\beta \in A_{m,n}$ and $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, each of the $n+2$ coordinates of $t\beta$ lies in $\{1, \dots, m-1\}$, so $|t\beta|_m \ge 1$ and $p_m(t\beta) = |t\beta|_m - 1 \ge 0 \ge q$. Hence $q(\beta) \ge 0 \ge q$ for every $\beta \in A_{m,n}$, which gives $D_q(m,n) = P_q(m,n) = A_{m,1} \times A_{m,n}$ and $\Delta_q(m,n) = 0$.

(2) Suppose $2q > n+1$. For any $(\alpha, \beta) \in A_{m,1} \times A_{m,n}$, setting $t = 1$ and $t = m-1$ gives

$$q(\alpha, \beta) \le \min\bigl(p_m(\alpha) + p_m(\beta),\, p_m((m-1)\alpha) + p_m((m-1)\beta)\bigr).$$

Since the two arguments on the right sum to $(p_m(\alpha) + p_m((m-1)\alpha)) + (p_m(\beta) + p_m((m-1)\beta)) = 1 + n = n+1$, their minimum is at most $\lfloor (n+1)/2 \rfloor < q$. Hence $P_q(m,n) = D_q(m,n) = \emptyset$ and $\Delta_q(m,n) = 0$.

(3) Suppose $q \ge 1$ and $mq \le n+1$. For every $\beta \in A_{m,n}$ and every $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, the tuple $t\beta = (\langle tb_0 \rangle_m, \dots, \langle tb_{n+1} \rangle_m)$ has $n+2$ coordinates, each at least $1$, and their sum is a positive multiple of $m$. Since $\sum_{j=0}^{n+1} \langle tb_j \rangle_m \ge n+2 \ge mq + 1 > mq$, the integer $|t\beta|_m = \frac{1}{m}\sum_{j=0}^{n+1} \langle tb_j \rangle_m$ satisfies $|t\beta|_m > q$, and being an integer it satisfies $|t\beta|_m \ge q+1$. Thus

$$p_m(t\beta) = |t\beta|_m - 1 \ge q \qquad \bigl(\forall\, \beta \in A_{m,n},\; \forall\, t \in (\mathbf{Z}/m\mathbf{Z})^\times\bigr).$$

Therefore $q(\beta) \ge q$ for every $\beta \in A_{m,n}$, which implies $D_q(m,n) = P_q(m,n) = A_{m,1} \times A_{m,n}$ and $\Delta_q(m,n) = 0$. $\square$

### 3.2. Cyclic floor identities and admissibility

To prove the "if" direction of Theorem 1.1 and establish Theorem 1.2, we analyze the cyclic behavior of the seed curve character $A = (1, 1, m-2) \in A_{m,1}$ and the base hypersurface character $B_0(d)$ of dimension $d \ge 1$.

**Lemma 3.1 (Cyclic evaluation of the base witness).** *Let $m \ge 3$ and $d \ge 1$ be integers such that $m \nmid (d+1)$. Set $\ell := d+1$ and write $\ell = rm + u$ with $r := \lfloor (d+1)/m \rfloor \ge 0$ and $u := \langle d+1 \rangle_m \in \{1, \dots, m-1\}$. Define*

$$A := (1, 1, m-2) \in A_{m,1}, \qquad B_0(d) := \bigl((m-1)^{(\ell)},\, u\bigr) \in A_{m,d}.$$

*Then for every unit $t \in \{1, \dots, m-1\}$ with $\gcd(t, m) = 1$:*
1. *One has*
   $$p_m(tA) = \Bigl\lfloor \frac{2t}{m} \Bigr\rfloor = \begin{cases} 0 & \text{if } 1 \le t < m/2, \\ 1 & \text{if } m/2 < t \le m-1. \end{cases}$$
2. *One has*
   $$p_m(t B_0(d)) = d - \Bigl\lfloor \frac{(d+1)t}{m} \Bigr\rfloor.$$
3. *As $t$ ranges over $(\mathbf{Z}/m\mathbf{Z})^\times$, the function $t \mapsto p_m(t B_0(d))$ is non-increasing, attains its minimum value $r = \lfloor (d+1)/m \rfloor$ at $t = m-1$, and every unit $t \in \{1, \dots, m-1\}$ for which $p_m(t B_0(d)) = r$ satisfies $t > m/2$ and hence $p_m(tA) = 1$. Consequently,*
   $$\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t B_0(d)) = r \quad \text{and} \quad \min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} \bigl(p_m(tA) + p_m(t B_0(d))\bigr) = r + 1.$$

*Proof.* Fix a unit $t \in \{1, \dots, m-1\}$ with $\gcd(t, m) = 1$.

(1) Since $1 \le t \le m-1$, the first two coordinates of $tA$ are $\langle t \rangle_m = t$. Because $\gcd(t, m) = 1$ and $m \ge 3$, we cannot have $2t = m$, so either $2 \le 2t \le m-1$ or $m+1 \le 2t \le 2m-2$.
- If $2t < m$, then $\langle (m-2)t \rangle_m = m - 2t$, so $|tA|_m = (t + t + (m-2t))/m = 1$ and $p_m(tA) = 0 = \lfloor 2t/m \rfloor$.
- If $2t > m$, then $\langle (m-2)t \rangle_m = 2m - 2t$, so $|tA|_m = (t + t + (2m-2t))/m = 2$ and $p_m(tA) = 1 = \lfloor 2t/m \rfloor$.

(2) In $B_0(d) = ((m-1)^{(\ell)}, u)$, the first $\ell$ coordinates equal $m-1 \equiv -1 \pmod m$ and the last coordinate equals $u \equiv \ell \pmod m$, so the coordinate sum is $\ell(m-1) + u = \ell m - (\ell - u) = (\ell - r)m \equiv 0 \pmod m$ and $B_0(d) \in A_{m,d}$. For our unit $t \in \{1, \dots, m-1\}$, we have $\langle t(m-1) \rangle_m = m - t$. Moreover, since $u \equiv \ell \pmod m$ and $m \nmid \ell$ while $\gcd(t, m) = 1$, the integer $\ell t$ is not divisible by $m$, so

$$\langle tu \rangle_m = \langle \ell t \rangle_m = \ell t - m \Bigl\lfloor \frac{\ell t}{m} \Bigr\rfloor \in \{1, \dots, m-1\}.$$

Summing the $\ell + 1 = d+2$ coordinates of $t B_0(d)$ yields

$$|t B_0(d)|_m = \frac{\ell(m-t) + \langle \ell t \rangle_m}{m} = \frac{\ell m - \ell t + \ell t - m \lfloor \ell t / m \rfloor}{m} = \ell - \Bigl\lfloor \frac{\ell t}{m} \Bigr\rfloor.$$

Subtracting $1$ and substituting $\ell = d+1$ gives $p_m(t B_0(d)) = d - \lfloor (d+1)t/m \rfloor$.

(3) Since $t \mapsto \lfloor \ell t/m \rfloor$ is non-decreasing on $\{1, \dots, m-1\}$, $t \mapsto p_m(t B_0(d))$ is non-increasing. At $t = m-1$, we have $\ell(m-1) = \ell m - \ell = \ell m - (rm + u) = (\ell - r - 1)m + (m - u)$ with $1 \le m-u \le m-1$, so $\lfloor \ell(m-1)/m \rfloor = \ell - r - 1 = d - r$ and therefore

$$p_m((m-1) B_0(d)) = d - (d - r) = r.$$

Hence $\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t B_0(d)) = r$. Finally, suppose $t \in \{1, \dots, m-1\}$ is any unit with $p_m(t B_0(d)) = r$, i.e., $\lfloor \ell t/m \rfloor = d - r = \ell - r - 1$. If $t < m/2$, then $2t \le m-1$, so for any $\ell \ge 2$ we have

$$(\ell - r - 1)m - \ell t \ge (\ell - r - 1)m - \frac{\ell(m-1)}{2} = \frac{(\ell - 2r - 2)m + \ell}{2}.$$

Since $\ell = rm + u$ with $m \ge 3$ and $u \ge 1$:
- if $r = 0$, then $\ell = d+1 \ge 2$, so $\ell - 2r - 2 = \ell - 2 \ge 0$ and $((\ell-2)m + \ell)/2 \ge \ell/2 \ge 1 > 0$;
- if $r \ge 1$, then $\ell = rm + u \ge 3r + 1 \ge 2r + 2$, so $\ell - 2r - 2 \ge 0$ and $((\ell - 2r - 2)m + \ell)/2 \ge \ell/2 > 0$.
In both cases $\ell t < (\ell - r - 1)m$, which forces $\lfloor \ell t/m \rfloor \le \ell - r - 2 < d - r$, a contradiction. Thus every unit $t$ with $p_m(t B_0(d)) = r$ satisfies $t > m/2$, so $p_m(tA) = 1$ by (1) and $p_m(tA) + p_m(t B_0(d)) = r + 1$. For all other units $t$, $p_m(t B_0(d)) \ge r + 1$ and $p_m(tA) \ge 0$, so $p_m(tA) + p_m(t B_0(d)) \ge r + 1$. $\square$

Next we show that whenever $(m,n,q)$ lies in the region $mq \ge n+2$ and $2q \le n+1$, one can pad $B_0(n-2s)$ with $s$ neutral pairs $(1, m-1)$ to hit the target filtration step $q$ exactly.

**Lemma 3.2 (Existence of an admissible padding index $s$).** *Let $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$ satisfy $mq \ge n+2$ and $2q \le n+1$. Define*

$$f(s) := s + 1 + \Bigl\lfloor \frac{n - 2s + 1}{m} \Bigr\rfloor \qquad \bigl(0 \le s \le s_{\max} := \lfloor (n-1)/2 \rfloor\bigr).$$

*Then there exists at least one integer $s \in \{0, 1, \dots, s_{\max}\}$ such that*

$$m \nmid (n - 2s + 1) \quad \text{and} \quad f(s) = q.$$

*Proof.* Set $\ell(s) := n - 2s + 1$. As $s$ increases from $0$ to $s_{\max} = \lfloor (n-1)/2 \rfloor$, $\ell(s)$ decreases in steps of $2$ from $\ell(0) = n+1$ down to $\ell(s_{\max}) \in \{2, 3\}$.

1. *Endpoint bounds:* At $s = 0$, the hypothesis $mq \ge n+2$ gives $\lfloor (n+1)/m \rfloor \le q - 1$, so

   $$f(0) = 1 + \Bigl\lfloor \frac{n+1}{m} \Bigr\rfloor \le q.$$

   At $s = s_{\max}$, we have $\ell(s_{\max}) = 2$ if $n = 2s_{\max} + 1$ is odd (so $q \le (n+1)/2 = s_{\max} + 1 \le f(s_{\max})$), and $\ell(s_{\max}) = 3$ if $n = 2s_{\max} + 2$ is even (so $2q \le n+1 = 2s_{\max} + 3$ implies $q \le s_{\max} + 1 \le f(s_{\max})$). Thus $f(0) \le q \le f(s_{\max})$.

2. *Step size of $f(s)$:* Since $m \ge 3$, incrementing $s$ to $s+1$ decreases $\ell(s)$ by $2 < m$, so $\lfloor \ell(s+1)/m \rfloor \in \{\lfloor \ell(s)/m \rfloor,\, \lfloor \ell(s)/m \rfloor - 1\}$. Therefore

   $$f(s+1) - f(s) = 1 + \Bigl\lfloor \frac{\ell(s) - 2}{m} \Bigr\rfloor - \Bigl\lfloor \frac{\ell(s)}{m} \Bigr\rfloor \in \{0, 1\}.$$

   Because $f(0) \le q \le f(s_{\max})$ and $f$ changes by $0$ or $+1$ at each unit step, the preimage $S_q := \{s \in \{0, \dots, s_{\max}\} : f(s) = q\}$ is a non-empty discrete interval.

3. *Avoiding multiples of $m$:* Suppose for some $s \in S_q$ that $m \mid \ell(s)$, say $\ell(s) = km$ with $k \ge 1$ (which implies $f(s) = s + 1 + k$). Since $\ell(s) = km \ge 3$ and $\ell(s_{\max}) \in \{2, 3\}$, either:
   - $s < s_{\max}$: then $\ell(s+1) = km - 2 = (k-1)m + (m-2)$ with $1 \le m-2 \le m-1$, so $m \nmid \ell(s+1)$ and
     $$f(s+1) = (s+1) + 1 + (k-1) = s + 1 + k = f(s) = q,$$
     meaning $s+1 \in S_q$ satisfies $m \nmid \ell(s+1)$; or
   - $s = s_{\max}$: then $\ell(s_{\max}) = km \in \{2, 3\}$ with $m \ge 3$ forces $m = 3$, $k = 1$, and $\ell(s_{\max}) = 3$, so $n = 2s_{\max} + 2$ is even and $f(s_{\max}) = s_{\max} + 2$. In that case, $2q \le n+1 = 2s_{\max} + 3$ gives $q \le s_{\max} + 1 < f(s_{\max})$, contradicting $s_{\max} \in S_q$.

Thus $S_q$ always contains at least one index $s$ with $m \nmid (n - 2s + 1)$. $\square$

### 3.3. Multiset invariance when $s$ is non-unique and proof of Theorem 1.2

A natural question highlighted during cross-checking is whether the witness construction and the permutation-orbit rank lower bound $\nu_x(m,n,q)$ depend on the choice of $s$ when more than one index $s \in \{0, \dots, s_{\max}\}$ satisfies the conditions of Lemma 3.2. The following proposition proves that at most two such indices can exist, characterizes the exact arithmetic condition under which two indices occur, and shows that the resulting witness tuples $B(s)$ have the exact same coordinate multiset.

**Proposition 3.3 (Characterization of non-unique $s$ and multiset invariance).** *Let $m \ge 3$, $n \ge 1$, and $q \in \mathbf{Z}$ satisfy $mq \ge n+2$ and $2q \le n+1$, and let*

$$S_q^{\mathrm{adm}} := \Bigl\{ s \in \{0, 1, \dots, \lfloor (n-1)/2 \rfloor\} : m \nmid (n - 2s + 1) \text{ and } s + 1 + \Bigl\lfloor \frac{n - 2s + 1}{m} \Bigr\rfloor = q \Bigr\}.$$

*Then:*
1. *The set $S_q^{\mathrm{adm}}$ has cardinality $1$ or $2$.*
2. *One has $|S_q^{\mathrm{adm}}| = 2$ if and only if there exists $s_1 \in \{0, \dots, \lfloor (n-1)/2 \rfloor - 1\}$ such that*
   $$n - 2s_1 + 1 = km + 1 \quad \text{for some integer } k \ge 1 \text{ with } q = s_1 + 1 + k,$$
   *in which case $S_q^{\mathrm{adm}} = \{s_1, s_2\}$ with $s_2 = s_1 + 1$.*
3. *Whenever $S_q^{\mathrm{adm}} = \{s_1, s_1 + 1\}$, the two witness tuples*
   $$B(s_1) = \bigl((m-1)^{(km+1)},\, 1,\, (1, m-1)^{(s_1)}\bigr) \quad \text{and} \quad B(s_1+1) = \bigl((m-1)^{(km-1)},\, m-1,\, (1, m-1)^{(s_1+1)}\bigr)$$
   *have the exact same coordinate multiset $\{(m-1)^{(km + 1 + s_1)},\, 1^{(s_1 + 1)}\}$, and therefore generate the exact same $\mathfrak{S}_{n+2}$-permutation orbit and the exact same lower bound $\nu_x(m,n,q)$.*

*Proof.* Write $\ell(s) := n - 2s + 1 = k_s m + u_s$ with $k_s = \lfloor \ell(s)/m \rfloor \ge 0$ and $0 \le u_s \le m-1$. By the proof of Lemma 3.2, $f(s+1) - f(s) = 0$ if and only if $\lfloor (\ell(s) - 2)/m \rfloor = k_s - 1$, which holds if and only if $u_s \in \{0, 1\}$ and $k_s \ge 1$.
- If $u_s = 0$, then $m \mid \ell(s)$, so $s \notin S_q^{\mathrm{adm}}$.
- If $u_s = 1$ and $k_s \ge 1$, then $\ell(s) = k_s m + 1$ is not divisible by $m$, and $\ell(s+1) = k_s m - 1 = (k_s - 1)m + (m - 1)$ has remainder $u_{s+1} = m - 1 \ge 2$ (since $m \ge 3$), which is also not divisible by $m$ and satisfies $f(s+1) = (s+1) + 1 + (k_s - 1) = s + 1 + k_s = f(s)$. Moreover, since $u_{s+1} = m - 1 \ge 2$, we have $f(s+2) = f(s+1) + 1 > q$, and similarly $u_{s-1} = 3$ (or $0$ if $m=3$), so no third index in $S_q^{\mathrm{adm}}$ can exist. This proves parts (1) and (2).

For part (3), suppose $S_q^{\mathrm{adm}} = \{s_1, s_1 + 1\}$ with $\ell(s_1) = km + 1$ ($k \ge 1$). Then $\langle \ell(s_1) \rangle_m = 1$, so

$$B(s_1) = \bigl((m-1)^{(km+1)},\, 1,\, (1, m-1)^{(s_1)}\bigr),$$

which consists of $(km + 1) + s_1 = km + s_1 + 1$ coordinates equal to $m-1$ and $1 + s_1 = s_1 + 1$ coordinates equal to $1$. On the other hand, for $s_2 = s_1 + 1$, we have $\ell(s_2) = km - 1 = (k-1)m + (m-1)$, so $\langle \ell(s_2) \rangle_m = m - 1$ and

$$B(s_2) = \bigl((m-1)^{(km-1)},\, m-1,\, (1, m-1)^{(s_1+1)}\bigr),$$

which consists of $(km - 1) + 1 + (s_1 + 1) = km + s_1 + 1$ coordinates equal to $m-1$ and $s_1 + 1$ coordinates equal to $1$. In both cases every coordinate of $B(s_i)$ belongs to $\{1, m-1\}$ with identical multiplicities $\mu_{m-1} = km + s_1 + 1$ and $\mu_1 = s_1 + 1$. Thus $B(s_1)$ and $B(s_2)$ differ only by a coordinate permutation in $\mathfrak{S}_{n+2}$. $\square$

We can now complete the proofs of Theorem 1.1 and Theorem 1.2.

*Proof of Theorems 1.1 and 1.2.* By Proposition 3.0, $\Delta_q(m,n) = 0$ whenever $q \le 0$, $2q > n+1$, or $mq \le n+1$. Conversely, assume $mq \ge n+2$ and $2q \le n+1$. By Lemma 3.2, we may choose $s \in S_q^{\mathrm{adm}}$, set $d := n - 2s \ge 1$ and $\ell := d + 1 = n - 2s + 1$, and form

$$A = (1, 1, m-2) \in A_{m,1}, \qquad B = B(s) = \bigl(B_0(d),\, (1, m-1)^{(s)}\bigr) \in A_{m,n}.$$

For every unit $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, each appended block $(1, m-1)$ transforms under multiplication by $t$ into $(\langle t \rangle_m, m - \langle t \rangle_m)$, whose two coordinates sum to $m$. Hence appending $s$ blocks $(1, m-1)$ adds exactly $s$ to $|t B_0(d)|_m$, so

$$p_m(t B(s)) = p_m(t B_0(d)) + s \qquad \bigl(\forall\, t \in (\mathbf{Z}/m\mathbf{Z})^\times\bigr).$$

By Lemma 3.1(3), with $r := \lfloor (d+1)/m \rfloor$, we obtain

$$\min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} p_m(t B(s)) = r + s = q - 1, \qquad \min_{t \in (\mathbf{Z}/m\mathbf{Z})^\times} \bigl(p_m(tA) + p_m(t B(s))\bigr) = r + 1 + s = q.$$

By Proposition 2.2(3), $(A, B(s)) \in E_q(m,n)$. In particular, $E_q(m,n) \ne \emptyset$ and $\Delta_q(m,n) \ne 0$, completing the proof of Theorem 1.1.

Next, because $p_m(\cdot)$ depends only on the coordinate multiset of a character tuple and multiplication by $t \in (\mathbf{Z}/m\mathbf{Z})^\times$ commutes with coordinate permutations $(\sigma, \tau) \in \mathfrak{S}_3 \times \mathfrak{S}_{n+2}$, every pair $(\sigma(A), \tau(B))$ also belongs to $E_q(m,n)$. Thus the entire subset

$$\mathcal{S}(A, B) := (\mathfrak{S}_3 \cdot A) \times (\mathfrak{S}_{n+2} \cdot B) \subseteq E_q(m,n)$$

lies in $E_q(m,n)$ and has cardinality $|\mathfrak{S}_3 \cdot A| \cdot |\mathfrak{S}_{n+2} \cdot B|$. Moreover, for each $(\alpha, \beta) \in \mathcal{S}(A, B)$ and each unit $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, the character $t\alpha$ has coordinate multiset $\{\langle t \rangle_m^{(2)}, \langle (m-2)t \rangle_m\}$. Since $\langle t \rangle_m = t$ is recovered as the unique residue appearing with multiplicity at least $2$ in $t\alpha$ (for $m=3$, $\varphi(3)=2$ and $t=1, 2$ give $(1,1,1)$ and $(2,2,2)$, which are already distinct), the map $t \mapsto t\alpha$ is injective on $(\mathbf{Z}/m\mathbf{Z})^\times$. Furthermore, if $(t\alpha, t\beta) = (\alpha', \beta')$ for some $(\alpha', \beta') \in \mathcal{S}(A, B)$ and $t \in (\mathbf{Z}/m\mathbf{Z})^\times$, then $t\alpha$ and $\alpha'$ must have the same coordinate multiset as $A = (1, 1, m-2)$, which forces $\langle t \rangle_m = 1$, i.e., $t = 1 \in (\mathbf{Z}/m\mathbf{Z})^\times$. Therefore, the $(\mathbf{Z}/m\mathbf{Z})^\times$-orbits of the elements of $\mathcal{S}(A, B)$ are pairwise disjoint in $E_q(m,n)$, and each orbit has cardinality $\varphi(m)$. Their union in $E_q(m,n)$ has cardinality

$$\nu_x(m,n,q) = \varphi(m) \cdot |\mathfrak{S}_3 \cdot A| \cdot |\mathfrak{S}_{n+2} \cdot B| = \varphi(m) \cdot c_A(m) \cdot \frac{(n+2)!}{\prod_{c=1}^{m-1} \mu_c(B)!}.$$

By Proposition 2.2(2), $\dim_{\mathbf{Q}} \Delta_q(m,n) = |E_q(m,n)| \ge \nu_x(m,n,q)$, and by Proposition 3.3 this lower bound is independent of the choice of $s \in S_q^{\mathrm{adm}}$. This completes the proof of Theorem 1.2. $\square$

### 3.4. Worked examples across the boundary

1. **The first nonzero fourfold-product case $(m,n,q) = (5,3,1)$:** For $n=3$ and $q=1$, the boundary inequality $mq \ge n+2 = 5$ shows that $\Delta_1(3,3) = \Delta_1(4,3) = 0$, whereas $\Delta_1(5,3) \ne 0$. At $(m,n,q) = (5,3,1)$, the unique admissible index in Lemma 3.2 is $s = 0$, giving $d = 3$, $\ell = 4$, $r = \lfloor 4/5 \rfloor = 0$, $u = 4$, and

   $$A = (1, 1, 3) \in A_{5,1}, \qquad B(0) = (4, 4, 4, 4, 4) \in A_{5,3}.$$

   For $t \in (\mathbf{Z}/5\mathbf{Z})^\times = \{1, 2, 3, 4\}$, we have $(p_5(tA))_{t=1}^4 = (0, 0, 1, 1)$ and $(p_5(tB))_{t=1}^4 = (3, 2, 1, 0)$, so $\min_t p_5(tB) = 0 = q-1$ (attained solely at $t=4$, where $p_5(4A) = 1$) and $(p_5(tA) + p_5(tB))_{t=1}^4 = (3, 2, 2, 1)$ has minimum $1 = q$ and maximum $3 = n+1-q$. Here $|\mathfrak{S}_3 \cdot A| = 3$, $|\mathfrak{S}_5 \cdot B| = 1$, and $\nu_x(5,3,1) = 4 \cdot 3 \cdot 1 = 12$, while the exact defect dimension is $\dim_{\mathbf{Q}} \Delta_1(5,3) = 24$ (see Table 1; the remaining $12$ dimensions come from the orbit of $B' = (2,2,2,2,2) = 3 \cdot B(0)$ paired with permutations of $(2,2,1)$).

2. **Two admissible values of $s$ and multiset invariance at $(m,n,q) = (3,3,2)$ and $(4,4,2)$:**
   - At $(m,n,q) = (3,3,2)$, we have $s_{\max} = 1$ and $\ell(0) = 4 = 1 \cdot 3 + 1 \equiv 1 \pmod 3$. By Proposition 3.3, both $s_1 = 0$ and $s_2 = 1$ belong to $S_2^{\mathrm{adm}}$:
     $$B(0) = (2, 2, 2, 2, 1) \quad \text{and} \quad B(1) = (2, 2, 2, 1, 2).$$
     Both have the coordinate multiset $\{2^{(4)}, 1^{(1)}\}$ of $\mathfrak{S}_5$-orbit size $5!/(4!1!) = 5$. Since $c_A(3) = 1$ and $\varphi(3) = 2$, Theorem 1.2 gives $\nu_x(3,3,2) = 2 \cdot 1 \cdot 5 = 10 = \dim_{\mathbf{Q}} \Delta_2(3,3)$, which is tight.
   - Similarly, at $(m,n,q) = (4,4,2)$, we have $\ell(0) = 5 = 1 \cdot 4 + 1 \equiv 1 \pmod 4$, so $S_2^{\mathrm{adm}} = \{0, 1\}$ with $B(0) = (3, 3, 3, 3, 3, 1)$ and $B(1) = (3, 3, 3, 3, 1, 3)$, both sharing the coordinate multiset $\{3^{(5)}, 1^{(1)}\}$ and giving $\nu_x(4,4,2) = 2 \cdot 3 \cdot 6 = 36$.

3. **Higher filtration step and tightness at $(m,n,q) = (3,7,3)$:** For $m=3$ and $n=7$, Theorem 1.1 predicts $\Delta_q(3,7) = 0$ for $q \in \{1, 2\}$ (since $3q \le 6 < 9 = n+2$) and $\Delta_q(3,7) \ne 0$ for $q \in \{3, 4\}$. At $q = 3$, the unique admissible index is $s = 0$ ($\ell = 8 = 2 \cdot 3 + 2$, $f(0) = 1 + 2 = 3$), giving $A = (1, 1, 1)$ and $B(0) = (2^{(9)})$, for which $\nu_x(3,7,3) = 2 \cdot 1 \cdot 1 = 2 = \dim_{\mathbf{Q}} \Delta_3(3,7)$ (Table 2).

---

## 4. Translation to the Borel–Moore homological level filtration

In [1] (Section 2, pp. 519–521) and [2] (Sections 2–4, pp. 224–228), Kang formulated the level filtration on Borel–Moore homology $H^{\mathrm{BM}}_k(Y, \mathbf{Q})$. For a smooth projective complex variety $Y$ of pure complex dimension $d_Y$, Borel–Moore homology coincides with singular homology $H_k(Y, \mathbf{Q})$, and Poincaré duality provides a canonical isomorphism of pure $\mathbf{Q}$-Hodge structures (up to Tate twist)

$$\mathrm{PD}_Y : H^{2d_Y - k}(Y, \mathbf{Q}) \xrightarrow{\;\sim\;} H^{\mathrm{BM}}_k(Y, \mathbf{Q}).$$

Under Kang's indexing convention [1] (equation (2.1), p. 521), the homological level filtration $\mathsf{F}^{\mathrm{BM}}_p H^{\mathrm{BM}}_k(Y, \mathbf{Q})$ is related to the cohomological level filtration $\mathsf{F}^q H^{2d_Y - k}(Y, \mathbf{Q})$ by

$$\mathsf{F}^{\mathrm{BM}}_p H^{\mathrm{BM}}_k(Y, \mathbf{Q}) = \mathrm{PD}_Y\Bigl(\mathsf{F}^{d_Y - p} H^{2d_Y - k}(Y, \mathbf{Q})\Bigr), \qquad q = d_Y - p.$$

On the product $Y = X_m^1 \times X_m^n$ of dimension $d_Y = n+1$ at middle homological degree $k = n+1 = d_Y$, let $H^{\mathrm{BM}}_{n+1,\mathrm{prim}}(X_m^1 \times X_m^n, \mathbf{Q}) := \mathrm{PD}_Y(H_m \otimes_{\mathbf{Q}} K_{m,n})$ be the primitive Künneth summand, and define the homological tensor-filtration defect at homological level $p \in \mathbf{Z}$ by

$$\Delta^{\mathrm{BM}}_p(m,n) := \frac{\mathsf{F}^{\mathrm{BM}}_p\bigl(H^{\mathrm{BM}}_1(X_m^1, \mathbf{Q}) \otimes_{\mathbf{Q}} H^{\mathrm{BM}}_{n,\mathrm{prim}}(X_m^n, \mathbf{Q})\bigr)}{\sum_{i+j=p} \mathsf{F}^{\mathrm{BM}}_i H^{\mathrm{BM}}_1(X_m^1, \mathbf{Q}) \otimes_{\mathbf{Q}} \mathsf{F}^{\mathrm{BM}}_j H^{\mathrm{BM}}_{n,\mathrm{prim}}(X_m^n, \mathbf{Q})}.$$

**Corollary 4.1 (Borel–Moore homological defect boundary).** *Let $m \ge 3$, $n \ge 1$, and $p \in \mathbf{Z}$, and set $q := n + 1 - p$. Under Poincaré duality on $X_m^1 \times X_m^n$, there is a canonical isomorphism $\Delta^{\mathrm{BM}}_p(m,n) \simeq \Delta_{n+1-p}(m,n)$. Consequently, $\Delta^{\mathrm{BM}}_p(m,n) \ne 0$ if and only if*

$$m(n + 1 - p) \ge n + 2 \quad \text{and} \quad 2p \ge n + 1,$$

*and whenever these two inequalities hold, $\dim_{\mathbf{Q}} \Delta^{\mathrm{BM}}_p(m,n) \ge \nu_x(m, n, n + 1 - p)$.*

*Proof.* For $X_m^1$ ($d_1 = 1$) and $X_m^n$ ($d_2 = n$) with $d_Y = d_1 + d_2 = n+1$, the Künneth compatibility of Poincaré duality identifies $\mathsf{F}^{\mathrm{BM}}_i H^{\mathrm{BM}}_1(X_m^1, \mathbf{Q})$ with $\mathsf{F}^{1-i} H_m$ and $\mathsf{F}^{\mathrm{BM}}_j H^{\mathrm{BM}}_{n,\mathrm{prim}}(X_m^n, \mathbf{Q})$ with $\mathsf{F}^{n-j} K_{m,n}$. As $(i, j)$ runs over pairs with $i + j = p$, the pair $(i', j') := (1 - i, n - j)$ runs over pairs with $i' + j' = n + 1 - p = q$. Thus $\Delta^{\mathrm{BM}}_p(m,n)$ is canonically isomorphic via $\mathrm{PD}_Y$ to $\Delta_q(m,n)$ with $q = n + 1 - p$, and Theorems 1.1 and 1.2 apply directly. $\square$

---

## 5. Finite computational checks and data availability

Although Theorems 1.1 and 1.2, Proposition 1.3, Proposition 3.3, and Corollary 4.1 are proved algebraically in Sections 2–4 for all parameters $(m,n,q)$, we accompany the paper with a self-contained, zero-dependency Python 3 verification package in `supplement/` that independently checks the character sets, orbit-level minimums, witness families, multiset invariance, and defect dimensions across finite parameter grids:

1. **Primary 82-layer census (`census.py`, `census.jsonl`, `census-summary.json`):** Using weak-composition histogram compression of character tuples in $A_{m,n}$, `census.py` evaluates all 82 pairs $(m,n)$ in the primary grid ($1 \le n \le 6$ with $2 \le m \le 12$, $n = 3$ with $13 \le m \le 19$, and $n = 8$ with $2 \le m \le 10$), covering 264 filtration cells $(m,n,q)$ across $1 \le q \le \lfloor (n+1)/2 \rfloor + 1$ (139 nonzero cells and 125 zero cells; 53 nonzero and 29 zero at $q = 1$). On every cell, the script verifies that $\Delta_q(m,n) > 0 \iff mq \ge n+2 \text{ and } 2q \le n+1$ and that $\dim_{\mathbf{Q}} \Delta_q(m,n) \ge \nu_x(m,n,q)$.
2. **Unit-by-unit verification of 17,534 explicit witnesses (`verify_witnesses.py`, `witness-records.jsonl.xz`, `verification.json`):** Across 17,534 nonzero parameter triples $(m,n,q)$ ($1 \le n \le 12$ with $n+2 \le m \le 257$ at $q=1$; $n = 3$ with $258 \le m \le 2001$ at $q=1$; and $3 \le n \le 30$, $2 \le q \le \lfloor (n+1)/2 \rfloor$, $3 \le m \le 65$ with $mq \ge n+2$), `verify_witnesses.py` constructs and independently verifies the explicit witness pair $(A, B(s)) \in E_q(m,n)$ unit-by-unit over $(\mathbf{Z}/m\mathbf{Z})^\times$, and cross-checks 15 pairs $(m,n)$ ($2 \le m \le 6$, $1 \le n \le 3$: 35 filtration cells) against direct uncompressed enumeration over $(\mathbf{Z}/m\mathbf{Z})^{n+2}$. The 17,534 witness records are archived losslessly in `witness-records.jsonl.xz` (208 KB compressed; 3,900,829 bytes uncompressed, SHA-256 `b5b9d0c8c4823442125a5d6cb9c33543cd2b5231e4ca07a5bd085cdabca5e03c`).
3. **Independent checker, $n=7$ extension, and fault injection (`independent_checker.py`, `independent-summary.json`):** Without importing `census.py` or `verify_witnesses.py`, `independent_checker.py` re-computes the 82 primary layers (264 cells) plus an out-of-grid extension at $n = 7$ for $2 \le m \le 10$ (9 layers, 45 cells: 25 nonzero and 20 zero), totaling 91 pairs $(m,n)$ and 309 filtration cells; cross-checks 24 pairs $(m,n)$ ($2 \le m \le 7$, $1 \le n \le 4$: 60 cells) by direct ordered-tuple enumeration; checks Lemma 3.1 on 3,309 pairs $(m,d)$ ($3 \le m \le 60$, $1 \le d \le 60$, $m \nmid (d+1)$); checks Lemma 3.2 and Proposition 3.3 across 235,315 triples $(m,n,q)$ ($3 \le m \le 100$, $1 \le n \le 100$, including all 7,240 triples with two admissible indices $s_1 < s_2$); verifies permutation-orbit disjointness on 74 nonzero parameter choices $(m,n,q,s)$ ($3 \le m \le 9$, $1 \le n \le 6$); verifies Proposition 1.3 across 7,040 even-$n$ unit checks; and runs 5 fault-injection self-tests.

Table 1 and Table 2 display representative rows from the primary census and from the $n = 7$ extension, respectively. Every script uses explicit `require(...)` checks active under `python3 -O` and reproduces all outputs in under 12 seconds via `python3 -O census.py && python3 -O verify_witnesses.py && python3 -O independent_checker.py`.

**Table 1.** Representative rows from the primary census grid, showing the ambient level-filtration dimension $|P_q(m,n)|$, the factorwise dimension $|D_q(m,n)|$, the exact defect dimension $\dim_{\mathbf{Q}} \Delta_q(m,n)$, and the permutation-orbit lower bound $\nu_x(m,n,q)$ from Theorem 1.2.

| $m$ | $n$ | $q$ | $|P_q(m,n)|$ | $|D_q(m,n)|$ | $\dim_{\mathbf{Q}} \Delta_q(m,n)$ | $\nu_x(m,n,q)$ | Regime / feature |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| 3 | 3 | 1 | 20 | 20 | 0 | 0 | Sub-threshold ($mq = 3 \le 4$) |
| 4 | 3 | 1 | 360 | 360 | 0 | 0 | Sub-threshold boundary ($mq = 4 = n+1$) |
| 5 | 3 | 1 | 2,424 | 2,400 | 24 | 12 | First nonzero degree for $(n,q)=(3,1)$ |
| 6 | 3 | 1 | 10,300 | 10,200 | 100 | 30 | Even degree ($m=6$, $n=3$, $q=1$) |
| 8 | 3 | 1 | 85,260 | 82,320 | 2,940 | 60 | Even degree ($m=8$, $n=3$, $q=1$) |
| 10 | 3 | 1 | 406,944 | 388,800 | 18,144 | 60 | Even degree ($m=10$, $n=3$, $q=1$) |
| 3 | 3 | 2 | 10 | 0 | 10 | 10 | Non-unique $s \in \{0,1\}$; bound tight |
| 4 | 5 | 2 | 3,234 | 3,192 | 42 | 42 | Higher step $q=2$; bound tight |
| 5 | 8 | 2 | 2,516,568 | 2,516,544 | 24 | 12 | Even $n=8$, step $q=2$ ($mq = 10 = n+2$) |
| 10 | 8 | 1 | 25,104,847,608 | 25,104,847,464 | 144 | 12 | Threshold $m = n+2 = 10$ at $q=1$ |

**Table 2.** Representative rows from the out-of-grid extension at dimension $n = 7$ ($2 \le m \le 10$, $1 \le q \le 5$).

| $m$ | $n$ | $q$ | $|P_q(m,n)|$ | $|D_q(m,n)|$ | $\dim_{\mathbf{Q}} \Delta_q(m,n)$ | $\nu_x(m,n,q)$ | Regime / feature |
| ---: | ---: | ---: | ---: | ---: | ---: | ---: | :--- |
| 3 | 7 | 2 | 340 | 340 | 0 | 0 | Sub-threshold ($mq = 6 \le 8 = n+1$) |
| 3 | 7 | 3 | 338 | 336 | 2 | 2 | Threshold $mq = 9 = n+2$; bound tight |
| 3 | 7 | 4 | 168 | 0 | 168 | 168 | Top step $2q = 8 = n+1$; bound tight |
| 4 | 7 | 3 | 28,584 | 27,648 | 936 | 432 | Unique $s = 1$ ($4 \mid \ell(0)=8$, $\ell(1)=6$) |
| 4 | 7 | 4 | 13,824 | 0 | 13,824 | 3,024 | Top step $q=4$ at $m=4$ |
| 5 | 7 | 2 | 628,920 | 628,704 | 216 | 108 | Threshold $mq = 10 \ge 9$ at $q=2$ |
| 5 | 7 | 3 | 567,360 | 508,032 | 59,328 | 432 | Interior cell $(m,n,q)=(5,7,3)$ |
| 5 | 7 | 4 | 127,008 | 0 | 127,008 | 6,048 | Top step $q=4$ at $m=5$ |
| 9 | 7 | 1 | 835,132,312 | 835,132,144 | 168 | 18 | Threshold $m = n+2 = 9$ at $q=1$ |
| 10 | 7 | 1 | 2,789,426,160 | 2,789,424,864 | 1,296 | 108 | Above threshold at $q=1$ ($m=10$) |

---

## References

[1] Su-Jeong Kang, *Refined Motivic Dimension*, Canadian Mathematical Bulletin **58** (2015), no. 3, 519–529. DOI: `10.4153/CMB-2015-018-4`.

[2] Su-Jeong Kang, *Refined motivic dimension of some Fermat varieties*, Bulletin of the Australian Mathematical Society **93** (2016), no. 2, 223–230. DOI: `10.1017/S0004972715001379`.

[3] Hongmin Li, *Residual Characters of Odd-Degree Fermat Fourfolds*, rStation `hodge_conjecture/104` v7 (2026). DOI: `10.5281/zenodo.24054302`.

[4] Tetsuji Shioda, *The Hodge Conjecture for Fermat Varieties*, Mathematische Annalen **245** (1979), no. 2, 175–184. DOI: `10.1007/BF01428804`.

[5] Tetsuji Shioda and Toshiyuki Katsura, *On Fermat varieties*, Tohoku Mathematical Journal (2) **31** (1979), no. 1, 97–115. DOI: `10.2748/tmj/1178229881`.

[6] Phillip A. Griffiths, *On the Periods of Certain Rational Integrals: I*, Annals of Mathematics (2) **90** (1969), no. 3, 460–495. DOI: `10.2307/1970746`.

[7] Phillip A. Griffiths, *On the Periods of Certain Rational Integrals: II*, Annals of Mathematics (2) **90** (1969), no. 3, 496–541. DOI: `10.2307/1970747`.

[8] Noboru Aoki, *Some new algebraic cycles on Fermat varieties*, Journal of the Mathematical Society of Japan **39** (1987), no. 3, 385–396. DOI: `10.2969/jmsj/03930385`.

[9] Pierre Deligne, *Cohomologie des intersections complètes*, in *Groupes de Monodromie en Géométrie Algébrique (SGA 7 II)*, Exposé XI, Lecture Notes in Mathematics, vol. 340, Springer, Berlin, 1973, pp. 39–61. DOI: `10.1007/BFb0060507`.

[10] Maximiliano Miranda, Hossein Movasati, Lucas Rufino, and Roberto Villaflor, *Lengths of Hodge characters in Fermat varieties*, arXiv preprint `arXiv:2609.27301v2` (2026). DOI: `10.48550/arXiv.2609.27301`.

[11] Gilberto Bini, Robert Laterveer, and Gianluca Pacienza, *Voisin's conjecture for zero-cycles on Calabi-Yau varieties and their mirrors*, Advances in Geometry **20** (2020), no. 1, 91–108. DOI: `10.1515/advgeom-2019-0008`.
