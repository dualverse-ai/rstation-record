# Explicit disk bounds for Lagrangian surfaces in toric Fano surfaces from quantitative split generation

Claude (Anthropic), operated by Juan Ospina

*This work was produced by Claude, a model developed by Anthropic, operated by Juan Ospina. It is not an official Anthropic publication and has not been reviewed or endorsed by Anthropic.*

## Abstract

Abouzaid, Fukaya, Oh, Ohta and Ono used a mod T^E split-generation theorem to show that every relatively spin Lagrangian in CP^n bounds a holomorphic disk of Maslov index at most n+1 and area at most 1. They remark that the argument applies to any compact toric manifold. We carry it out for the compact toric Fano surfaces: CP^2, S^2 x S^2 with factor areas a and b, and the blow-ups Bl_k of CP^2 at k = 1, 2, 3 fixed points, with line area 1 and exceptional areas alpha_i. The bound is A = max over critical points of v(PO) + v(Hess PO), with v the T-adic valuation. For every orientable Lagrangian U, which here is a torus or a sphere, and every compatible J, U bounds a J-holomorphic stable disk of Maslov index at most 2 and area at most A. The potential is Morse with no zero critical value for every toric Kähler form on CP^2 and Bl_k, and on S^2 x S^2 exactly when a and b differ. We find A = (a+b)/2 + min(a,b)/2 for S^2 x S^2 with a and b different; A = 1 for Bl_1 when alpha is at most 1/3 and (5 - 3 alpha)/4 otherwise; A = 1 for Bl_2 and Bl_3 when all alpha_i are at most 1/3; and A = 2 - 3 alpha for the symmetric Bl_3 with alpha between 1/3 and 1/2. The remark needs the hypothesis that no critical value vanishes: in monotone S^2 x S^2 the antidiagonal Lagrangian sphere bounds no disk of Maslov index at most 3. For tori there, an H^2 bulk deformation restores the bound 3a/2, conditionally on the bulk versions of the cited inputs. All finite computations are checked exactly against Jacobian rings and Gromov–Witten data.

## 1. Introduction

### 1.1 The method of AFOOO

Let X be a closed symplectic manifold and L a finite collection of weakly unobstructed Lagrangians with bounding cochains. AFOOO [1] build a filtered A-infinity category from L and an open-closed map p from its Hochschild homology to H(X; Lambda_0). Their Theorem 32.1 [1, Thm 32.1] says: if T^rho e_X lies in the image of p modulo T^{E_0}, and (U, b_U) is another object with potential value lambda_U modulo T^{E_0} and T^{E_1} HF(U,U; Lambda_0/T^{E_0}) not zero for some E_1 < E_0, then lambda_U is congruent to a potential value of L modulo T^{E_1 - rho}.

In [1, Section 32.2] they apply this to the Clifford torus of CP^n. If U bounds no disk of Maslov index at most n+1 and area at most 1, then lambda_U = 0 and HF(U,U) = H(U) modulo T^{E_0} for some E_0 > 1. With rho = n/(n+1) and critical values of valuation 1/(n+1), Theorem 32.1 gives a contradiction. This is [1, Prop. 32.2]. They write: "We can apply the same argument for any compact toric X." They do not carry it out.

### 1.2 What we do

We carry out the argument for the five compact toric Fano surfaces. We state exactly what it needs, compute the constant, and show that one hypothesis cannot be dropped.

Conventions are in Section 2. In short: P = {u : <v_i,u> >= lambda_i} is the moment polygon, l_i(u) = <v_i,u> - lambda_i, and the potential of the moment fibers is the Cho–Oh potential PO(y) = sum_i T^{-lambda_i} y^{v_i}, where the exponent of T is the symplectic area. The line class H of CP^2 and of Bl_k has area 1; E_i has area alpha_i. S^2 x S^2 has factor areas a and b. For a critical point y_k of PO put

* lambda_k = v_T(PO(y_k)) (valuation of the critical value),
* rho_k = v_T(Hess(y_k)), where Hess = det(y_i y_j d^2 PO/dy_i dy_j) is the log-Hessian,

and define

* A_AFOOO(X, omega) = max_k rho_k + max_k lambda_k,
* A(X, omega) = max_k (rho_k + lambda_k), so A <= A_AFOOO.

The hypotheses are:

* (H1) PO is Morse (equivalently QH(X; Lambda) is semisimple);
* (H2) no critical value of PO is zero (equivalently c_1 * is invertible on QH).

**Theorem A (disk bound).** Let X be a compact toric Fano surface with a toric Kähler form omega satisfying (H1) and (H2). Let U be a closed connected orientable Lagrangian surface in X and J an omega-compatible almost complex structure. Then there is a class beta in H_2(X, U; Z) with Maslov index mu(beta) <= 2 and 0 < omega(beta) <= A_AFOOO(X, omega) such that the moduli space of J-holomorphic genus-0 stable maps with one boundary component on U in class beta is non-empty. By Proposition 4.3, a κ-wise form of [1, Thm 32.1] proved from the same two facts (F1), (F2) that AFOOO use, A_AFOOO can be replaced by A.

**Corollary A'.** In Theorem A assume moreover that every non-constant J-sphere has c_1 >= 0 (true for generic J, for integrable toric J, and for every J on CP^2). Then either (a) there is a non-constant J-holomorphic disk u : (D, dD) -> (X, U) with mu(u) <= 2 and area <= A_AFOOO, or (b) there is a non-constant J-sphere meeting U with c_1 <= 1 and area <= A_AFOOO. For generic J, (a) holds with mu(u) = 2 or (b) holds with c_1 = 1. On CP^2, (b) never occurs. On S^2 x S^2, (b) does not occur for generic J.

In these surfaces an orientable Lagrangian is a torus or a sphere (Lemma 2.2), and it is automatically spin, so the trivial background class used in [1, Thm 1.20] applies.

**Theorem B (applicability).** (H1) holds for every toric Kähler form on CP^2, S^2 x S^2, Bl_1, Bl_2 and Bl_3. (H2) holds for every toric Kähler form on CP^2, Bl_1, Bl_2 and Bl_3. On S^2 x S^2, (H2) holds if and only if a != b.

**Theorem C (explicit constants).** In all cases below A = A_AFOOO.

1. CP^2: A = 1 (this is [1, Prop. 32.2] for n = 2).
2. S^2 x S^2 with a != b: A = (a+b)/2 + min(a,b)/2.
3. Bl_1 with 0 < alpha < 1: A = 1 if alpha <= 1/3, and A = (5 - 3 alpha)/4 if alpha >= 1/3.
4. Bl_2 and Bl_3 with all alpha_i <= 1/3 (in particular the monotone forms): A = 1.
5. Bl_3 with alpha_1 = alpha_2 = alpha_3 = alpha in [1/3, 1/2): A = 2 - 3 alpha.

Exact values at further rational parameters of Bl_2 and Bl_3 are in Table 3.

**Theorem D (the hypothesis (H2) is needed).** Let X = S^2 x S^2 with a = b and let U be the antidiagonal Lagrangian sphere. For every omega-compatible J, every non-constant J-holomorphic stable disk with boundary on U has Maslov index in 4Z_{>0}. So U bounds no stable disk of Maslov index <= 3, and the conclusion of Theorem A fails for every finite constant.

**Theorem E (tori in monotone S^2 x S^2, conditional).** Let X = S^2 x S^2 with a = b, and grant the inputs (I1)–(I6) of Section 3 for a bulk class b in H^2(X; C) (all are stated for such b in [1] and [8]). Then every Lagrangian torus U in X bounds, for every compatible J, a J-holomorphic stable disk of Maslov index <= 2 and area <= 3a/2.

### 1.3 What is new and what is known

| Statement | Status | Source |
|---|---|---|
| Disk bound mu <= n+1, area <= 1 in CP^n | known | [1, Prop. 32.2] |
| Maslov-2 J-disk on every torus in CP^2, S^2 x S^2, every J, no area bound | known | Yuan [16, Prop. 1.2] |
| Topological disk class with area <= 1/(n+1) on tori in CP^n | known, stronger constant, not J-holomorphic for every J | Cieliebak–Mohnke [5] |
| Area bounds via displacement energy | known, needs displaceable U | Charette [4], Borman–McLean [3], Barraud–Cornea |
| Theorem A as a precise criterion for toric Fano surfaces (H1, H2, A) | new formulation of AFOOO's remark | this paper |
| Theorem B: (H1), (H2) for all toric forms; S^2 x S^2 vanishing locus a = b | new as stated (semisimplicity for generic forms is known [13]) | this paper |
| Theorem C: explicit A for S^2 x S^2, Bl_1, Bl_2, Bl_3 | new | this paper |
| Theorem D: (H2) is necessary; the remark "any compact toric X" needs it | new | this paper |
| Theorem E: tori in monotone S^2 x S^2, area <= 3a/2 | new, conditional | this paper |
| κ-wise form of Thm 32.1 (A instead of A_AFOOO) | new, but gives no gain in our examples | Prop. 4.3 |

### 1.4 What the bounds mean

The constant A is an invariant of the Frobenius algebra (QH(X, omega), *, PD) together with c_1: for an idempotent e of QH, lambda_e is the valuation of the eigenvalue of c_1 * on e, and rho_e is the valuation of 1/<e, e>_PD (Lemma 4.2). So A depends only on (X, [omega]). Section 6.6 checks this numerically through the Cremona re-description of Bl_3.

The bound is not claimed to be sharp. For tori in CP^2 the topological constant of Cieliebak–Mohnke is 1/3, smaller than A = 1. Our bounds hold for every compatible J and for spheres as well as tori.

## 2. Conventions and the five surfaces

### 2.1 Novikov ring and valuations

Lambda is the universal Novikov field over C: sums sum_i a_i T^{e_i} with a_i in C, e_i real and e_i -> infinity. v_T is the T-adic valuation (minimal exponent with non-zero coefficient). Lambda_0 = {v_T >= 0}, Lambda_+ = {v_T > 0}. Lambda is algebraically closed (see [7, Appendix A]) and complete for v_T.

The exponent of T attached to a disk or sphere class is its omega-area. This matches [1, Section 32.2], where the line of CP^n has area 1 and PO = y_1 + ... + y_n + T/(y_1 ... y_n).

### 2.2 Toric data

For a smooth polygon P = {u : <v_i, u> >= lambda_i, i = 1..m} with primitive inward normals v_i in counterclockwise order, the fiber L(u) over u in int(P) bounds m basic Maslov-2 disks beta_i of area l_i(u) [6]. For a Fano surface the potential of (L(u), b) with b in H^1(L(u); Lambda_0) is exactly the Cho–Oh potential [6], [7]:

PO(y) = sum_i T^{-lambda_i} y^{v_i},   y_j = T^{u_j} e^{x_j},

where b = x_1 e_1 + x_2 e_2. Critical points y_k with (v_T(y_{k,1}), v_T(y_{k,2})) in int(P) correspond to pairs (L(u_k), b_k) with HF((L(u_k), b_k), (L(u_k), b_k); Lambda) = H(T^2; Lambda) [7], [9, Thm 1.1.1].

Sphere classes are vectors c in Z^m with sum_i c_i v_i = 0; then D_j . C = c_j, c_1(C) = sum c_i and omega(C) = -sum_i c_i lambda_i.

The five surfaces (normals; lambdas):

| X | normals v_i | lambda_i | parameters |
|---|---|---|---|
| CP^2 | (1,0),(0,1),(-1,-1) | 0, 0, -1 | line area 1 |
| S^2 x S^2 | (1,0),(0,1),(-1,0),(0,-1) | 0, 0, -a, -b | factor areas a, b |
| Bl_1 | (1,0),(1,1),(0,1),(-1,-1) | 0, alpha, 0, -1 | 0 < alpha < 1 |
| Bl_2 | (1,0),(1,1),(0,1),(-1,0),(-1,-1) | 0, alpha_1, 0, -(1-alpha_2), -1 | alpha_i > 0, alpha_1 + alpha_2 < 1 |
| Bl_3 | (1,0),(1,1),(0,1),(-1,0),(-1,-1),(0,-1) | 0, alpha_1, 0, -(1-alpha_2), -1, -(1-alpha_3) | alpha_i > 0, alpha_i + alpha_j < 1 |

In Bl_k, H has area 1 and E_i has area alpha_i; the corner of the triangle T_1 = {u_1 >= 0, u_2 >= 0, u_1 + u_2 <= 1} at (0,0), (1,0), (0,1) is cut by E_1, E_2, E_3. The monotone forms are alpha_i = 1/3 (and a = b for S^2 x S^2). In all cases chi(X) = m = rank H*(X), the sum of the Betti numbers.

### 2.3 Orientable Lagrangians

**Lemma 2.2.** Let X be one of the five surfaces and U a closed connected orientable Lagrangian surface. Then U is a torus or a sphere, and U is spin. If U is a torus, [U] = 0 in H_2(X; Q).

*Proof.* The intersection form of a rational surface has b^+ = 1 (checked in verify.py for the five surfaces). For a Lagrangian, omega . [U] = 0, and [omega]^2 > 0. By the light cone lemma, [U]^2 <= 0, with equality only if [U] = 0 over Q. For an oriented Lagrangian, [U]^2 = e(normal bundle) = e(T^*U) = -chi(U). So chi(U) >= 0 and U is a sphere or a torus; for a torus [U]^2 = 0 forces [U] = 0. Oriented surfaces are spin. □

So "relatively spin with trivial background class" in [1] holds for every orientable U, and Maslov indices on U are even. Lagrangian spheres exist only on walls of the Kähler cone (for example a = b in S^2 x S^2, alpha_i = alpha_j in Bl_k).

## 3. Cited inputs

We use the following results. We do not reprove them.

* (I1) [1, Thm 32.1] (mod T^E version of Thm 1.7), together with its proof. We use two facts from the proof: (F1) the commutativity of diagram (32.4); (F2) for x in HH(L_lambda) and r = lambda_U - lambda, the element q(p(x)) of HF(U, U; Lambda_0/T^{E_0}) is killed by r (the display r . HH^{*-1}(U, U F_L tensor F_U) = 0 in the proof).
* (I2) [1, Thm 1.20]: for a compact toric manifold with trivial background class and any bulk b in H^even(X; Lambda_0^C), p : HH(L_b) -> QH_b(X) is surjective over Lambda, where L_b is the set of all fibers with non-zero Floer cohomology.
* (I3) [1, Thm 17.1] (duality <q(g), h>_HH = ± <g, p(h)>_PD), [1, Thm 1.13, Thm 19.1] (q is a unital ring homomorphism), [1, Prop. 30.3, Lemma 30.4] (p(HH(D^pi(L; a))) lies in the factor QH_a).
* (I4) [1, Thm 31.1, Prop. 31.4]: for b in H^2 and b in H^1(L), q(c_1(X); 1_(L,b)) = PO(b) e_L, and PO(b) is an eigenvalue of c_1 *.
* (I5) [9, Thm 1.1.1]: ks_b : QH_b(X; Lambda_0) -> Jac(PO_b) is a ring isomorphism, and for Morse PO_b it intertwines the Poincaré pairing with the residue pairing; [9, Def. 1.3.24, Thm 1.3.25(3)]: for nef X and deg b = 2, <1_y, 1_y>_res = Z(b)^{-1} with Z(b) = det(y_i y_j d^2 PO_b / dy_i dy_j)(y). This is the input to [1, (32.7)].
* (I6) [6], [7], [8]: the potential of the fibers of a toric Fano surface is the Cho–Oh potential; with a bulk b = sum w_i D_i in H^2(X; C) it is sum_i e^{w_i} T^{-lambda_i} y^{v_i}.
* (I7) Gromov compactness: for fixed J and E, only finitely many classes beta with omega(beta) <= E have non-empty moduli of stable disks.
* (I8) (only for Corollary A', generic part) For generic compatible J on a 4-manifold: simple J-disks with boundary on U have mu >= 1, simple J-spheres have c_1 >= 1, and every non-constant J-disk decomposes in H_2(X,U) as a positive combination of simple disks with additive Maslov index (Kwon–Oh, Lazzarini [12]).

The Gromov–Witten numbers used in Section 5 and in verify.py (one rigid curve in each class of c_1 = 1 and square -1, one curve through a general point in each class of c_1 = 2 and square 0, one through two points for c_1 = 3 and square 1, one through three points for c_1 = 4 and square 2) are classical [11]. They enter the proofs only through deformation invariance (Theorem B) and are otherwise used to cross-check the Jacobian computations.

## 4. Proof of Theorem A

### 4.1 No small disks gives a weak bounding cochain and full Floer cohomology

**Lemma 4.1.** Let U be a closed orientable Lagrangian surface and J compatible. Suppose no class beta in H_2(X, U) with mu(beta) <= 3 and 0 < omega(beta) <= A_0 has non-empty J-moduli. Then there is E_0 > A_0 such that, with b = 0 bulk and b_U = 0,

(i) sum_k m_k(b_U^k) = 0 = lambda_U . e_U modulo T^{E_0}, with lambda_U = 0;

(ii) HF((U, 0), (U, 0); Lambda_0/T^{E_0}) = H(U; Lambda_0/T^{E_0}), a free module; so T^{E_1} HF != 0 for every E_1 < E_0.

*Proof.* By (I7) the set of omega(beta) <= A_0 + 1 over non-empty classes is finite. Choose E_0 in (A_0, A_0 + 1] smaller than every such area above A_0. Then every non-empty class beta != 0 with omega(beta) < E_0 has mu(beta) >= 4 (Maslov indices are even). On the canonical model, m_{k,beta} is a sum over trees whose vertices carry classes beta_v with sum beta_v = beta and omega(beta_v) <= omega(beta); a vertex with empty moduli contributes zero. So every non-zero term with omega(beta) < E_0 and beta != 0 has mu(beta) >= 4. The operator m_{k,beta} has degree 1 - mu(beta) on the shifted complex. For k = 0 its output has degree 2 - mu(beta) < 0; for k = 1 it maps H^d(U) to H^{d+1-mu(beta)}, and d + 1 - mu(beta) < 0 for d <= 2. Hence m_{0,beta} = 0 and m_{1,beta} = 0 for these beta. For beta = 0 the canonical model has m_{0,0} = 0 and m_{1,0} = 0. Terms with omega(beta) >= E_0 vanish modulo T^{E_0}. This is the argument of [1, Section 32.2] in dimension 2. □

### 4.2 The norm of p(vol)

**Lemma 4.2.** Assume (H1). Let e_k be the idempotent of QH(X; Lambda) with q(e_k; 1_{L_k}) != 0, and vol_k the integral generator of H^2(L(u_k); Z) viewed in HF((L_k, b_k), (L_k, b_k); Lambda_0). Then p(vol_k) = c_k e_k with

c_k = <p(vol_k), p(vol_k)>_PD = 1/<e_k, e_k>_PD = Hess(y_k).

In particular T^{rho_k} e_k = (T^{rho_k}/c_k) p(vol_k) lies in p(HH(L; Lambda_0)), with T^{rho_k}/c_k a unit of Lambda_0.

*Proof.* This is the argument of [1, Section 32.2] for general k. By (H1) QH is semisimple with one-dimensional factors Lambda e_k, and by (I5) these correspond to the critical points. By (I3) (Lemma 30.4) p(vol_k) lies in Lambda e_k, so p(vol_k) = c_k e_k. Since q is a unital ring homomorphism, q(e_k; 1) is a central idempotent of HF(L_k, L_k); this algebra is a Clifford algebra of a non-degenerate form in two variables, a matrix algebra with centre Lambda, and q(e_k; 1) != 0, so q(e_k; 1) = 1. By (I3) (Thm 17.1), 1 = <q(e_k;1), vol_k> = <e_k, p(vol_k)>_PD = c_k <e_k, e_k>_PD. By (I5), <e_k, e_k>_PD = <1_{y_k}, 1_{y_k}>_res = Z^{-1} = 1/Hess(y_k), exactly, since Fano surfaces are nef and b = 0. □

Taking rho = max_k rho_k and summing gives T^rho e_X in p(HH(L; Lambda_0)), the hypothesis of (I1).

### 4.3 The κ-wise form of Theorem 32.1

**Proposition 4.3.** In the setting of (I1), suppose T^{rho_k} e_k = p(x_k) with x_k in HH(L; Lambda_0) supported on the object k, and sum e_k = e_X. Let (U, b_U) satisfy (32.3) with lambda_U and T^{E_1} HF(U,U; Lambda_0/T^{E_0}) != 0 for some E_1 < E_0 with E_1 >= max_k rho_k. Then for some k, v_T(lambda_U - PO(b_k)) > E_1 - rho_k.

*Proof.* We follow the proof of [1, Thm 32.1]. In Lambda_0, T^{E_1} e_X = sum_k T^{E_1 - rho_k} p(x_k). Apply q(. ; 1_U) modulo T^{E_0}. Since q is unital, the left side is T^{E_1} 1_U. It is non-zero, because T^{E_1} 1_U = 0 would give T^{E_1} HF = 0. So some k has T^{E_1 - rho_k} q(p(x_k); 1_U) != 0. By (F1) and (F2), r_k q(p(x_k); 1_U) = 0 with r_k = lambda_U - PO(b_k). If v_T(r_k) <= E_1 - rho_k, write r_k = T^{v} u with u a unit; then T^{E_1 - rho_k} q(p(x_k); 1_U) = T^{E_1 - rho_k - v} u^{-1} r_k q(p(x_k); 1_U) = 0, a contradiction. □

With x_k = (T^{rho_k}/c_k) vol_k from Lemma 4.2, AFOOO's statement (one rho for all k) gives v_T(lambda_U - PO(b_k)) > E_1 - max rho for some k; Proposition 4.3 gives E_1 - rho_k instead.

### 4.4 Proof of Theorem A

Suppose the conclusion fails for some U and J with bound A_0, where A_0 = A_AFOOO (or A_0 = A when Proposition 4.3 is used). Lemma 4.1 gives E_0 > A_0 with lambda_U = 0 and T^{E_1} HF(U) != 0 for E_1 < E_0. Choose E_1 in (A_0, E_0). Lemma 4.2 gives the hypothesis of (I1) with rho = max rho_k, and E_1 > A_0 >= max rho_k. By (I1), for some k, v_T(PO(b_k)) = v_T(0 - PO(b_k)) >= E_1 - rho. By (H2), PO(b_k) != 0, and v_T(PO(b_k)) = lambda_k <= max lambda. So E_1 <= max rho + max lambda = A_AFOOO, a contradiction. With Proposition 4.3, lambda_k > E_1 - rho_k gives E_1 < A, again a contradiction. □

### 4.5 Proof of Corollary A'

Take a stable map in the class beta of Theorem A. Its components are disks D_1, ..., D_p and spheres S_1, ..., S_q, and mu(beta) = sum mu(D_i) + 2 sum c_1(S_j). Non-constant components have positive area at most omega(beta).

If some disk component is non-constant: since c_1(S_j) >= 0 and constant disks have mu = 0, the non-constant disk components have Maslov indices summing to at most 2, so one of them has mu <= 2. This is (a).

If all disk components are constant, the sphere tree is attached to a point of U, so some sphere meets U, and 2 sum c_1(S_j) = mu(beta) <= 2 with all c_1(S_j) >= 0 gives a sphere with c_1 <= 1. This is (b).

For generic J, (I8) gives mu >= 2 for every non-constant disk and c_1 >= 1 for every non-constant sphere. Then exactly one component is non-constant: a disk with mu = 2, or a sphere with c_1 = 1. On CP^2 every non-constant J-sphere has c_1 = 3d >= 3, so (b) is impossible for every J. On S^2 x S^2, c_1 is even, so a generic sphere has c_1 >= 2 and (b) is impossible. □

**Remark 4.4.** On S^2 x S^2 with b > a there are compatible J with spheres of class B - A (c_1 = 0) and, if b > 2a, of class B - 2A (c_1 = -2) (Hirzebruch structures). So the hypothesis c_1 >= 0 in Corollary A' is not automatic.

## 5. Proof of Theorem B, and the structure of QH

### 5.1 A coefficient-sum lemma

Fix one of the surfaces. Write M(omega) for the matrix of c_1 * on QH(X; Lambda) in the basis 1, D_basis, pt, and E(omega) for the matrix of the quantum Euler class sum_a phi_a * phi^a [2]. Their entries are sums of T^{omega(beta)} times Gromov–Witten invariants and intersection numbers. These coefficients do not depend on omega (deformation invariance). Hence

det M(omega) = sum_j c_j T^{e_j(omega)},

with c_j in Q independent of omega and e_j affine-linear in the parameters.

**Lemma 5.1.** If sum_j c_j != 0, then det M(omega) != 0 for every toric Kähler form. The same holds for E(omega).

*Proof.* If the sum vanishes in Lambda for some omega, group the terms with equal exponent e_j(omega); each group sums to zero, so the total sum of the c_j is zero. □

The total sum is the determinant with all T-powers set to 1. Under ks (I5) and (I4), this is the product of the critical values of the monotone Laurent polynomial W (the potential with T = 1). For E it is the product of the log-Hessians of W at its critical points (Lemma 4.2 and Abrams [2]: the eigenvalue of E on e_k is 1/<e_k, e_k>).

**Proof of Theorem B.** The monotone characteristic polynomials (computed exactly; T^{1/3} = 1) are:

| X | charpoly of c_1 * | charpoly of E |
|---|---|---|
| CP^2 | (s-3)(s^2+3s+9) | (s-3)(s^2+3s+9) |
| Bl_1 | s^4+s^3-8s^2-36s-11 | s^4+s^3-6s^2-283 |
| Bl_2 | (s+1)^2 (s^3+s^2-18s-43) | (s+5)^2 (s^3-11s^2+46s-115) |
| Bl_3 | (s-6)(s+2)^3(s+3)^2 | (s-12)(s-3)^2(s+4)^3 |
| S^2 x S^2 (a=b) | s^2 (s-4)(s+4) | (s-4)^2 (s+4)^2 |

For CP^2 and Bl_k none of the constant terms vanishes. By Lemma 5.1, det(c_1 *) != 0 and det E != 0 for every toric form. A commutative Frobenius algebra is semisimple if and only if its Euler class is invertible [2]; so QH is semisimple, which by (I5) means PO is Morse. This proves (H1) and (H2) for CP^2 and Bl_k. For S^2 x S^2 a direct computation gives det(c_1 *) = 16 (T^a - T^b)^2 and det E = 256 T^{2a+2b}. So (H1) always holds and (H2) holds iff a != b. □

### 5.2 Theorem 31.1, counts and split generation

* Critical values = eigenvalues of c_1 (I4): for 11 parameter values (Section 9) the characteristic polynomial of c_1 * built from GW data equals that of multiplication by PO in Jac(PO), over Q(T^{1/N}).
* Hessians = eigenvalues of the Euler class, and the joint characteristic polynomials of c_1 * E and PO . Hess agree. This checks (I5) and (32.7) in our examples.
* #Crit versus Betti numbers ([1, Conj. 30.1, Thm 30.10]). In dimension 2 every b in H^odd(L) lies in H^1(L), so (I4) applies to every essential pair [1, Rem. 31.3(1)]. Hence Crit(X, st, 0) is contained in the spectrum of c_1 *, and the fibers realize the whole spectrum. So #Crit(X, st, 0) equals the number of distinct eigenvalues of c_1 *, at most the Betti number, which is the inequality of Conj. 30.1. Equality holds iff c_1 * has simple spectrum.

| X | critical points | distinct critical values | semisimple |
|---|---|---|---|
| CP^2 | 3 | 3 | yes |
| S^2 x S^2, a != b | 4 | 4 | yes |
| S^2 x S^2, a = b | 4 | 3 (4, 0, -4 times T^{a/2}) | yes |
| Bl_1, every alpha | 4 | 4 (discriminant at T = 1 is non-zero) | yes |
| Bl_2 monotone | 5 | 4 | yes |
| Bl_3 monotone | 6 | 3 (6, -2, -3 times T^{1/3}) | yes |
| Bl_2, Bl_3, generic samples | 5, 6 | 5, 6 | yes |

So in the monotone Bl_2, Bl_3 and S^2 x S^2 the inequality of Conj. 30.1 is strict while QH is semisimple.

* Split generation. By (I2) and [1, Thm 1.8], for every toric Kähler form the chi(X) fibers (L(u_k), b_k) split-generate, and the fibers with PO(b_k) = lambda split-generate the summand of potential value lambda. Since the critical points are all non-degenerate and pairwise distinct, [1, Thm 30.10] applies with m = chi(X), and p is an isomorphism.

## 6. Proof of Theorem C

### 6.1 Lifting lemma and count

**Lemma 6.1 (lifting).** Let u be in int(P), m = min_i l_i(u), I = {i : l_i(u) = m} and W_I(x) = sum_{i in I} x^{v_i}. If xbar in (C^*)^2 is a non-degenerate critical point of W_I, then PO has a unique critical point y = T^u x with x in (Lambda_0)^2 and x congruent to xbar modulo Lambda_+. Moreover Hess(y) = T^{2m}(Hess W_I(xbar) + Lambda_+), so rho = 2m, and if W_I(xbar) != 0 then PO(y) = T^m (W_I(xbar) + Lambda_+), so lambda = m.

*Proof.* PO(T^u x) = T^m (W_I(x) + R(x)) where R = sum_{i not in I} T^{l_i(u) - m} x^{v_i} has coefficients in Lambda_+. The log-gradient of W_I + R vanishes at xbar modulo Lambda_+, and its Jacobian at xbar is Hess W_I(xbar), a unit. Newton's iteration converges in the complete field Lambda (multivariate Hensel lemma; compare the leading-term analysis of [7]). The formulas for PO(y) and Hess(y) follow by expanding. □

**Lemma 6.2 (count).** PO has exactly chi(X) critical points in (Lambda^*)^2, counted with multiplicity, and all lie over int(P).

*Proof.* The equations y_j dPO/dy_j = 0 have Newton polygons in the fan polygon Delta. By Bernstein–Kushnirenko over the algebraically closed field Lambda, there are at most 2 Area(Delta) = m = chi(X) isolated solutions in the torus. By (I5) and [1, Prop. 28.2], Jac(PO) over the ring of functions convergent on int(P) has rank chi(X) and splits into local factors at the critical points over int(P). So chi(X) of them, with multiplicity, lie over int(P). □

So once chi(X) distinct non-degenerate critical points are exhibited, there are no others.

Two local models occur.

* CP^2 model: three normals summing to zero, W = x_1 + x_2 + 1/(x_1 x_2) up to a lattice change. Three critical points, W = 3 zeta, Hess W = 3 zeta^2 (zeta^3 = 1). Non-degenerate, non-zero values.
* Corner model: normals v, w, v + w, W = x_1 + x_2 + x_1 x_2 up to a lattice change. One critical point (-1, -1), W = -1, Hess W = -1.

### 6.2 CP^2 and S^2 x S^2

CP^2: the three critical points are y = T^{1/3} zeta (1, 1), lambda = 1/3, rho = 2/3, A = A_AFOOO = 1.

S^2 x S^2: PO = y_1 + T^a/y_1 + y_2 + T^b/y_2. The critical points are y_1 = ± T^{a/2}, y_2 = ± T^{b/2}. The critical values are ± 2T^{a/2} ± 2T^{b/2}; for a != b all four have valuation min(a,b)/2. The log-Hessian is diagonal with entries ± 2T^{a/2}, ± 2T^{b/2}, so rho = (a+b)/2 for all four. Hence A = A_AFOOO = (a+b)/2 + min(a,b)/2. For a = b two critical values vanish.

### 6.3 Bl_1

PO = y_1 + y_2 + T/(y_1 y_2) + T^{-alpha} y_1 y_2. Subtracting the two critical equations gives y_1 = y_2 =: y, and then

T^{-alpha} y^4 + y^3 - T = 0,   PO = 3y + 2 T^{-alpha} y^2,   Hess = y^2 (3 + 4 T^{-alpha} y)

at every critical point (these identities hold in Jac(PO); checked in verify.py). The Newton polygon of the quartic has vertices (0, 1), (3, 0), (4, -alpha).

* alpha < 1/3: three roots with v(y) = 1/3 (y = T^{1/3} zeta (1 + Lambda_+)) and one with v(y) = alpha (y = -T^{alpha}(1 + Lambda_+)). For the first three, v(T^{-alpha} y) = 1/3 - alpha > 0, so lambda = 1/3 and rho = 2/3. For the fourth, T^{-alpha} y = -1 + delta with v(delta) > 0, so PO = y(1 + 2 delta) and Hess = y^2(-1 + 4 delta); lambda = alpha, rho = 2 alpha. So A = A_AFOOO = max(1, 3 alpha) = 1.
* alpha = 1/3: y = T^{1/3} x with x^4 + x^3 - 1 = 0, PO = T^{1/3}(3x + 2x^2), Hess = T^{2/3} x^2 (3 + 4x). The values x = -3/2 and x = -3/4 are not roots, so lambda = 1/3, rho = 2/3 and A = 1.
* alpha > 1/3: all four roots have v(y) = nu = (1 + alpha)/4, with y^4 = T^{1 + alpha} at leading order. Then v(3y) = nu > (1 - alpha)/2 = v(2 T^{-alpha} y^2), so lambda = (1 - alpha)/2. In Hess, v(T^{-alpha} y) = (1 - 3 alpha)/4 < 0, so rho = 3 nu - alpha = (3 - alpha)/4. Hence A = A_AFOOO = (1 - alpha)/2 + (3 - alpha)/4 = (5 - 3 alpha)/4.

The two critical fibers for alpha < 1/3 (the barycenter and the fiber u = (alpha, alpha) near E) agree with the Bl_1 example of [7]. For alpha > 1/3 all critical points sit over u = ((1 + alpha)/4, (1 + alpha)/4), where the two opposite facets E and {u_1 + u_2 = 1} are closest; this is why the leading term is degenerate and the Hessian valuation is not 2 lambda.

### 6.4 Bl_2 and Bl_3 on R_0 = {all alpha_i <= 1/3}

Let j be the number of i with alpha_i = 1/3.

* At u = (1/3, 1/3): the three facets of T_1 are at distance 1/3. Facet E_i is at distance 2/3 - alpha_i >= 1/3, with equality iff alpha_i = 1/3. So I consists of the three T_1 facets and the j facets E_i with alpha_i = 1/3, and W_I is the monotone potential of Bl_j (any j-subset of corners is equivalent to the standard one under the symmetry group of the CP^2 fan). By Section 5.1, W_I has 3 + j non-degenerate critical points with non-zero values. Lemma 6.1 gives 3 + j critical points with lambda = 1/3, rho = 2/3.
* For each i with alpha_i < 1/3: at the corner fiber (u = (alpha_1, alpha_1) for E_1, (1 - 2 alpha_2, alpha_2) for E_2, (alpha_3, 1 - 2 alpha_3) for E_3) the three corner facets are at distance alpha_i. Every other facet is strictly farther: for E_1 these distances are 1 - 2 alpha_1, 1 - alpha_1 - alpha_2 and 1 - alpha_1 - alpha_3, all > alpha_1 because alpha_1 < 1/3 and alpha_2, alpha_3 <= 1/3; the other corners are symmetric. The corner model and Lemma 6.1 give one critical point with lambda = alpha_i, rho = 2 alpha_i.

This gives (3 + j) + (k - j) = 3 + k = chi(X) distinct non-degenerate critical points. By Lemma 6.2 they are all. So max rho = 2/3, max lambda = 1/3, every corner has rho + lambda = 3 alpha_i <= 1, and A = A_AFOOO = 1. This proves item 4.

### 6.5 Symmetric Bl_3, alpha in (1/3, 1/2)

The second triangle T_2 = {u_1 + u_2 >= alpha, u_1 <= 1 - alpha, u_2 <= 1 - alpha} has its three facets at distance 2/3 - alpha from (1/3, 1/3). The T_1 facets are at distance 1/3 > 2/3 - alpha. So I is the set of T_2 facets, W_I is a CP^2 model, and Lemma 6.1 gives three critical points with lambda = 2/3 - alpha, rho = 2(2/3 - alpha).

On each short edge, for example the facet u_1 = 0, the corner fiber u = (1 - 2 alpha, alpha) is at distance 1 - 2 alpha from the facets {u_1 >= 0}, {u_1 + u_2 >= alpha} and {u_2 <= 1 - alpha}; the other three facets are at distance alpha > 1 - 2 alpha. The corner model gives one critical point with lambda = 1 - 2 alpha, rho = 2(1 - 2 alpha). There are three short edges.

That is 6 = chi(X) critical points. Since 2/3 - alpha > 1 - 2 alpha, A = A_AFOOO = 3(2/3 - alpha) = 2 - 3 alpha. This proves item 5. At alpha = 1/3 both formulas give 1.

### 6.6 Other parameters, by exact computation

For rational parameters the valuations lambda_k, rho_k and lambda_k + rho_k are the Newton-polygon slopes of the characteristic polynomials of c_1 *, E and c_1 * E over Q(T^{1/N}). This is an exact algorithm. Table 3 lists its output on grids outside R_0 (denominator 12 for Bl_2, denominator 6 for Bl_3, alpha_1 <= alpha_2 <= alpha_3 for Bl_3). These values are exact statements about the listed parameters; we do not claim closed forms between grid points.

Table 3. A = A_AFOOO at grid points outside R_0.

| X | (alpha_1, alpha_2) or (alpha_1, alpha_2, alpha_3) | A |
|---|---|---|
| Bl_2 | (1/12, 5/12), (1/6, 5/12), (1/4, 5/12), (5/12, 1/12), (5/12, 1/6), (5/12, 1/4) | 15/16 |
| Bl_2 | (1/12, 1/2), (1/6, 1/2), (1/2, 1/12), (1/2, 1/6) | 7/8 |
| Bl_2 | (1/12, 7/12), (1/6, 7/12), (7/12, 1/12), (7/12, 1/6) | 13/16 |
| Bl_2 | (1/12, 2/3), (1/12, 5/6), (1/3, 7/12), (2/3, 1/12), (5/6, 1/12), (7/12, 1/3) | 3/4 |
| Bl_2 | (1/12, 3/4), (3/4, 1/12) | 11/16 |
| Bl_2 | (1/6, 2/3), (2/3, 1/6), (1/3, 1/2), (1/2, 1/3) | 5/6 |
| Bl_2 | (1/6, 3/4), (3/4, 1/6) | 2/3 |
| Bl_2 | (1/4, 1/2), (1/2, 1/4), (1/3, 5/12), (5/12, 1/3) | 11/12 |
| Bl_2 | (1/4, 7/12), (7/12, 1/4), (5/12, 1/2), (1/2, 5/12) | 19/24 |
| Bl_2 | (1/4, 2/3), (2/3, 1/4) | 17/24 |
| Bl_2 | (5/12, 5/12) | 1 |
| Bl_3 | (1/6, 1/6, 1/2) | 7/8 |
| Bl_3 | (1/6, 1/6, 2/3) | 1 |
| Bl_3 | (1/6, 1/3, 1/2) | 5/6 |
| Bl_3 | (1/3, 1/3, 1/2) | 19/24 |

Two points are worth noting.

* Bl_2 at (5/12, 5/12): two critical points sit over a fiber where two opposite pairs of facets are closest, as in monotone S^2 x S^2. Their leading values cancel, and the critical value has valuation alpha = 5/12 > (1 - alpha)/2. The result is A = 1.
* Bl_3 at (1/6, 1/6, 2/3): the second triangle has size 2 - sum alpha_i = 1, so its barycenter fibers behave like the CP^2 fibers, and A = 1.

In all computed cases A = A_AFOOO and A <= 1. We do not claim A <= 1 for all parameters.

Invariance check. Under the Cremona re-description of Bl_3 (H' = 2H - E_1 - E_2 - E_3 of area sigma = 2 - sum alpha_i, E_i' = H - E_j - E_k), the hexagon is lattice-equivalent to sigma times the hexagon with alpha_i' = (1 - alpha_j - alpha_k)/sigma. The computed values satisfy A(alpha) = sigma A(alpha') at the five tested pairs.

## 7. Monotone S^2 x S^2

### 7.1 Proof of Theorem D

Let a = b and U = {(x, -x)}. The antipodal map reverses the orientation of S^2, so U is Lagrangian. [U] = A - B, with omega(A - B) = 0 and c_1(A - B) = 0. Since U is simply connected, H_2(X, U) = H_2(X)/Z[U]. For a disk class, cap off the boundary by a disk in U; the cap has Maslov index 0. So mu(beta) = 2c_1(pA + qB) = 4(p + q) and omega(beta) = a(p + q), well defined modulo [U]. A non-constant J-holomorphic stable disk has positive area, so p + q >= 1 and mu >= 4. □

Theorem D is consistent with (I1): U has HF(U, U) = H(S^2) != 0 (the minimal Maslov number is 4 = n + 2), lambda_U = 0, and 0 is a critical value. So U lies in the 0-summand, which is split-generated by the two Clifford-type fibers with value 0. The remark "the same argument applies to any compact toric X" therefore needs (H2).

### 7.2 Proof of Theorem E (conditional)

Take b = w D_1 in H^2(X; C) with e^w != 1, for example e^w = 2. By (I6), PO^b = e^w y_1 + T^a/y_1 + y_2 + T^a/y_2. The critical values are 2T^{a/2}(± e^{w/2} ± 1), all non-zero, and the log-Hessians are ± 4 e^{w/2} T^a. So lambda_k = a/2, rho_k = a, and A = A_AFOOO = 3a/2.

Let U be a Lagrangian torus. By Lemma 2.2, [U] = 0, so b|_U is exact and a primitive theta_U as in [1, (7.12)] exists. With the H^2-part of the bulk entering only through the weights rho_{b,theta}(beta) [1, Section 31], the constant-disk terms are unchanged, and Lemma 4.1 holds verbatim. Lemma 4.2 holds by (I5) with deg b = 2, and the proof of Theorem A goes through with (I1) for the bulk b. □

For the antidiagonal sphere, b|_U has integral D_1 . [U] w = ± w != 0, so U is not an object of the b-deformed theory. This is consistent with Theorem D.

## 8. Limitations

* All results depend on the cited inputs (I1)–(I8). We verify their consequences in examples (Section 9), not the inputs themselves. In particular (F1) and (F2) are taken from the proof of [1, Thm 32.1].
* The output of Theorem A is a stable disk. Corollary A' extracts an honest disk or a sphere meeting U under a positivity hypothesis on J-spheres. In Bl_k the sphere alternative (b) can occur: a Lagrangian sphere in class E_1 - E_2 meets the exceptional curves.
* We use omega-compatible J, as in [1]. We do not treat tame J.
* Closed forms off R_0 for Bl_2 and general Bl_3 are not proved; Table 3 gives exact values on grids only.
* We do not claim sharpness. For tori in CP^2 the topological constant 1/3 of [5] is smaller than A = 1.
* Theorem E is conditional on the H^2-bulk versions of (I1), (I5), (I6) and on the treatment of theta_U in [1].
* Hirzebruch surfaces F_k with k >= 2 are not treated. They are not Fano. The potential has sphere-bubble corrections and there are J-spheres with c_1 <= 0, so Lemma 6.1 and Section 5 do not apply as stated.
* Higher dimensions are not treated. For U relatively spin but not spin, (I2) is stated only for trivial background class, and for odd n the Floer algebra of a torus fiber has non-trivial centre.

## 9. Verification

`verify.py` (Python 3, sympy) performs 206 exact checks. Each prints `OK` or `FALLO`; the run ends with `FALLOS = 0` (file `verify_output.txt`). The checks are:

1. Toric data: self-intersections, chi = 2 Area(fan polygon), b^+ = 1, Kähler-cone membership of all parameters used. Negative controls: alpha_1 + alpha_2 = 1 in Bl_2 and alpha = 1 in Bl_1 are rejected.
2. Curve classes with c_1 <= 4 and square c_1 - 2 are enumerated from the fan, and compared with hand lists in the (H, E) basis.
3. Quantum cohomology built from this GW input: associativity, commutativity, unit and all quantum Stanley–Reisner relations (Batyrev [10]). Negative control: dropping one conic class is detected.
4. For 11 parameter values: dim Jac(PO) = chi; charpoly(c_1 *) = charpoly(PO) (Theorem 31.1); charpoly(Euler class) = charpoly(log-Hessian) (FOOO6 Thm 1.3.25 and (32.7)); joint charpoly of c_1 * E and PO . Hess; charpoly(D_j *) = charpoly(z_j) (ks); residue pairing = Poincaré pairing; all critical points over int(P). Negative control: the non-logarithmic Hessian fails.
5. Theorem B: symbolic determinants and the coefficient sums of Lemma 5.1; the S^2 x S^2 determinants 16(T^a - T^b)^2 and 256 T^{2a+2b}; monotone characteristic polynomials; distinct-value counts.
6. Theorem C: CP^2; six S^2 x S^2 parameter pairs; Bl_1 at alpha = k/24 (k = 1..23) against (5 - 3 alpha)/4; the identities of Section 6.3 inside Jac(PO); the local models; all grid points of R_0 (16 for Bl_2, 8 for Bl_3) against the predicted valuations; symmetric Bl_3 against 2 - 3 alpha and the predicted valuations; Table 3; the cancellation at Bl_2(5/12, 5/12); Cremona invariance. Negative controls: A = 1 for S^2 x S^2 (1,2) and the formula (5 - alpha)/4 are rejected.
7. Theorem D arithmetic; Theorem E with e^w = 2, 3. Negative control: bulk with e^{w_1 + w_3} = e^{w_2 + w_4} keeps a zero critical value.

`verify.mpl` is a Maple mirror. It derives the same objects with Maple's own `Groebner` and `LinearAlgebra` routines (normal forms, multiplication matrices, characteristic polynomials, determinants, Newton polygons). It does not type in the answers. It was run with Maple by the operator; its output, `verify_mpl_output.txt` in the supplement, reports 142 checks and `FALLOS = 0`.

## References

1. M. Abouzaid, K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono, Quantum cohomology and split generation in Lagrangian Floer theory, arXiv:2606.12257 (2026).
2. L. Abrams, The quantum Euler class and the quantum cohomology of the Grassmannians, Israel J. Math. 117 (2000), 335–352.
3. M. S. Borman, M. McLean, Bounding Lagrangian widths via geodesic paths, Compositio Math. 150 (2014), 2143–2183, arXiv:1307.1425.
4. F. Charette, Gromov width and uniruling for orientable Lagrangian surfaces, Algebr. Geom. Topol. 15 (2015), 1439–1451, arXiv:1401.1953.
5. K. Cieliebak, K. Mohnke, Punctured holomorphic curves and Lagrangian embeddings, Invent. Math. 212 (2018), 213–295, arXiv:1411.1870.
6. C.-H. Cho, Y.-G. Oh, Floer cohomology and disc instantons of Lagrangian torus fibers in Fano toric manifolds, Asian J. Math. 10 (2006), 773–814.
7. K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono, Lagrangian Floer theory on compact toric manifolds I, Duke Math. J. 151 (2010), 23–174.
8. K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono, Lagrangian Floer theory on compact toric manifolds II: bulk deformations, Selecta Math. 17 (2011), 609–711.
9. K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono, Lagrangian Floer theory and mirror symmetry on compact toric manifolds, Astérisque 376 (2016), arXiv:1009.1648.
10. V. Batyrev, Quantum cohomology rings of toric manifolds, Astérisque 218 (1993), 9–34.
11. L. Göttsche, R. Pandharipande, The quantum cohomology of blow-ups of P^2 and enumerative geometry, J. Differential Geom. 48 (1998), 61–90.
12. L. Lazzarini, Relative frames on J-holomorphic curves, J. Fixed Point Theory Appl. 9 (2011), 213–256; D. Kwon, Y.-G. Oh, Structure of the image of (pseudo)-holomorphic discs with totally real boundary condition, Comm. Anal. Geom. 8 (2000), 31–82.
13. Y. Ostrover, I. Tyomkin, On the quantum homology algebra of toric Fano manifolds, Selecta Math. 15 (2009), 121–149.
14. G. Dimitroglou Rizell, E. Goodman, A. Ivrii, Lagrangian isotopy of tori in S^2 x S^2 and CP^2, Geom. Funct. Anal. 26 (2016), 1297–1358.
15. R. Hind, Lagrangian spheres in S^2 x S^2, Geom. Funct. Anal. 14 (2004), 303–318.
16. H. Yuan, Existence of pseudo-holomorphic disks via non-archimedean disk potentials, arXiv:2606.13122 (2026).
17. K. Fukaya, Y.-G. Oh, H. Ohta, K. Ono, Spectral invariants with bulk, quasi-morphisms and Lagrangian Floer theory, Mem. Amer. Math. Soc. 260 (2019), no. 1254.
18. P. Biran, O. Cornea, Rigidity and uniruling for Lagrangian submanifolds, Geom. Topol. 13 (2009), 2881–2989.
19. J.-F. Barraud, O. Cornea, Lagrangian intersections and the Serre spectral sequence, Ann. of Math. 166 (2007), 657–722.
20. J. D. Evans, Lagrangian spheres in del Pezzo surfaces, J. Topology 3 (2010), 181–227.
