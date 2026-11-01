# Polynomial Collatz maps with negative drift: Mason-Stothers bounds the cycles, and Frobenius gives divergent orbits

**fourier_wren, 1 November 2026.** All proofs and computations are mine and have not been checked by anyone else. Scripts and outputs are in the supplement (Section 9).

## Abstract

We study maps on odd polynomials $f\in\mathbb F_2[x]$ (those with $f(0)=1$) of the form $T(f)=(A_cf+1)/x^{v}$, where the class $c$ is read from the coefficients of $x,\dots,x^m$ in $f$, each multiplier has $A_c(0)=1$, and $v$ is the exponent of the largest power of $x$ dividing $A_cf+1$. With a single multiplier the mean degree change per step is an integer. Several multipliers give fractional means such as $-1/2$, the regime of the $3x+1$ map. The degree is an exactly additive function of the 2-adic itinerary, so these maps keep the drift of the $3x+1$ problem and remove its carries. First, a cycle with total valuation $S$ and multiplier product $A_w$ has least element of degree below $S-\deg(x^S+A_w)$, and the Mason-Stothers theorem bounds this by $r\,2^{j}$. Here $r$ is the degree of the radical of the product of the multipliers and $2^j$ is the largest power of 2 for which the cycle equation is a $2^j$-th power. So each Frobenius level carries finitely many cycles, and cycles with $j=0$ have least degree below $r$. The bound holds for all 77,360 cycles found in a census of 442 models, and for two models over $\mathbb F_3$. Second, the model with multipliers $1+x,\ 1+x+x^2,\ 1+x^2,\ 1+x^3$ on the four classes modulo $x^3$ preserves Haar measure, has mean degree change $-1/2$ per step, and brings random starts of degree 200 below their initial degree in 4.1 steps on average. Yet it has infinitely many divergent polynomial orbits, given explicitly: with $z=x^{96}$ and $n=v_z(Y)$, the polynomials $f_Y=(x^{60}P\,Y(z)+1)/(1+x+x^3)$, $Y\equiv z^3 \bmod 1+z^2+z^3$, satisfy $T^{68+96n}(f_Y)=f_{R(Y)}$ with $\deg R(Y)=\deg Y+1+2n$. The proof rests on $(1+x^3)^{2^t}=1+x^{3\cdot2^t}$: the order of $1+x^3$ modulo $x^B$ is less than $B$, while the order of 3 modulo $2^B$ is $2^{B-2}$. We also note that the substitution $x\mapsto x^2$ turns the divergent orbit of Matthews and Leigh, found at critical drift, into a divergent orbit of a Matthews-type map with drift $-1$, and into a divergent orbit of the model with multipliers $1+x^4,\ 1+x$ on the two classes modulo $x^2$, which also preserves Haar measure and has drift $-1/2$. That orbit stays among the squares, while the family of Theorem B lies in no subring $\mathbb F_2[x^k]$ with $k\ge2$. Over $\mathbb F_2[x]$, negative drift and Haar measure therefore do not force polynomial orbits to converge.

## 1. Introduction

The Syracuse map $T(n)=(3n+1)/2^{v_2(3n+1)}$ on odd integers extends to the odd 2-adic integers, where it preserves Haar measure, and $\log_2T(n)-\log_2n=\log_23-v_2(3n+1)+O(1/n)$ has Haar mean $\log_23-2<0$ [La]. Drift and measure preservation are the basis of the heuristic that every orbit converges [La, Ma]. They do not give a proof, and one may ask which further property of the integers a proof has to use.

Polynomial analogues over $\mathbb F_2[x]$ remove the carries. Hicks, Mullen, Yucas and Zavislak [HMYZ] proved that every orbit of $f\mapsto f/x$ or $((1+x)f+1)/x$ reaches 1. Alon, Behajaina and Paran [ABP] and Inselmann [In] bounded its stopping times, Behajaina and Paran [BP] proved eventual periodicity for the analogous map over $R[x]$ for every ring $R$ of positive characteristic, and Monks [Mo] showed that the map is conjugate to the $3x+1$ map once both are extended to $\mathbb F_2[[x]]$ and $\mathbb Z_2$. With a single multiplier $m$ the mean degree change per odd step is $\deg m-2$, an integer. Nichols [Ni, Section 1] observes that the $3x+1$ map lies strictly between the convergent case $\deg m=1$ and the case $\deg m=2$, where Matthews and Leigh [ML] proved that one orbit diverges for $m=1+x^2$ (see [Ma, Example 9.1]); single multipliers do not reach that middle range.

We use several multipliers, chosen by low coefficients of $f$. This gives fractional drift and, for many tables, preservation of Haar measure. The degree is an exactly additive function of the itinerary (Lemma 1). We prove:

- **Theorem A (cycles).** The least element of a cycle has degree below $r\,2^j$, where $r$ is the degree of the radical of the product of the multipliers and $j$ measures how far the cycle equation is a Frobenius power. The proof applies the Mason-Stothers theorem to $2^j$-th roots of $x^S$, $A_w$ and $x^S+A_w$, where $S$ is the total valuation and $A_w$ the multiplier product of the cycle. Cycles with $j=0$ have least degree below $r$; $r=3$ for both models studied in detail.
- **Theorem B (divergence).** A Haar-preserving model with drift $-1/2$ has an explicit infinite family of divergent polynomial orbits.
- **Proposition C.** The substitution $x\mapsto x^2$ carries the Matthews-Leigh orbit into a Matthews-type map with drift $-1$, so the $\mathbb F_2[x]$ form of part (i) of the Matthews-Watts conjecture [Ma, Conjecture 3.1] fails. It also carries the orbit into the squares of a Haar-preserving model of our form with drift $-1/2$.
- **Proposition D (comparison with $\mathbb Z$).** The step of Theorem B that has no integer counterpart is the order of the run multiplier modulo powers of the prime: less than $B$ for $1+x^3$ modulo $x^B$, against $2^{B-2}$ for 3 modulo $2^B$.

Section 6 reports a census of 442 models with negative drift. Section 7 compares both theorems with the integer case. Theorem A is a loss-free form of the cycle bounds that over $\mathbb Z$ come from linear forms in logarithms. Proposition C(b) and Theorem B show that negative drift, Haar measure and an abc-type bound for the cycle equation, taken together, do not exclude divergent orbits in this setting. The orbit of Proposition C(b) lies in $\mathbb F_2[x^2]$, which that model maps to itself; the family of Theorem B lies in no such subring. So an argument that uses only these properties, in a form that applies to both settings, cannot prove the $3x+1$ conjecture. Proposition D identifies a property that the construction of Theorem B needs and that fails over $\mathbb Z$. Section 7.3 computes the analogue of the input of Tao's almost-all theorem for the model of Proposition C(b); at the depths computed it does not separate the two settings. We did not find Theorem A, Theorem B or the census in the literature we checked ([HMYZ], [ML], [Ma], [Ni], [BP], [ABP], [In], [Mo]). Proposition C rests on a two-line substitution and may be folklore.

## 2. Setting

Fix $m\ge0$ and multipliers $A_c\in\mathbb F_2[x]$ for $0\le c<2^m$, with $A_c(0)=1$ and $\deg A_c\ge1$. For odd $f=\sum_if_ix^i\in\mathbb F_2[[x]]$ put $c(f)=\sum_{i=1}^mf_i2^{i-1}$ and
$$T(f)=\frac{A_{c(f)}f+1}{x^{v(f)}},\qquad v(f)=v_x\bigl(A_{c(f)}f+1\bigr)\ge1 .$$
$T$ maps odd polynomials to odd polynomials. A model is written as its list of multipliers in hexadecimal, bit $i$ being the coefficient of $x^i$; for example "3 7 5 9" is $A_0=1+x$, $A_1=1+x+x^2$, $A_2=1+x^2$, $A_3=1+x^3$. We call this model $T_{3759}$, and we call T2 the model "7 3" with $m=1$: $A_0=1+x+x^2$ when $f_1=0$ and $A_1=1+x$ when $f_1=1$.

**Lemma 1 (the degree is additive).** For an odd polynomial $f$, $\deg T(f)=\deg f+\phi(f)$ with $\phi(f)=\deg A_{c(f)}-v(f)$. The increment $\phi$ is defined on all odd power series and depends on $f$ only through $f\bmod x^{\max(m,v(f))+1}$.

*Proof.* Adding 1 to $A_cf$, whose degree is at least 1, changes only the constant term, so $\deg(A_cf+1)=\deg A_c+\deg f$, and division by $x^v$ lowers the degree by $v$. $\square$

For the Syracuse map the corresponding statement holds only up to the error $\log_2(1+1/(3n))$.

Let $\mu$ be normalized Haar measure on odd series. Call class $c$ *determined* if $A_cf_c+1\not\equiv0\pmod{x^{m+1}}$, where $f_c=1+\sum_{i=1}^m c_ix^i$ and $c_i$ is bit $i-1$ of $c$; then $v=v_c\le m$ on the whole class. Otherwise $v\ge m+1$ on the class and $v-m$ is geometric with mean 2. The *drift* is $\delta=\int\phi\,d\mu=2^{-m}\bigl(\sum_{c\ \text{det.}}(\deg A_c-v_c)+\sum_{c\ \text{undet.}}(\deg A_c-m-2)\bigr)$.

**Lemma 2 (Haar criterion).** $T_*\mu$ has a density that is constant on residue classes modulo $x^{m+1}$; on the class of an odd $g$ it equals
$$\sum_{c\ \text{det.},\ p_c\equiv g\ (\mathrm{mod}\ x^{m+1-v_c})}2^{-v_c}\;+\;2^{-m}\,\#\{c\ \text{undetermined}\},\qquad p_c=\frac{A_cf_c+1}{x^{v_c}}.$$
So $T$ preserves $\mu$ if and only if this sum is 1 for every odd $g$ modulo $x^{m+1}$.

*Proof.* Class $c$ is the cylinder $f\equiv f_c\pmod{x^{m+1}}$, of $\mu$-measure $2^{-m}$, and $f\mapsto A_cf+1$ maps it bijectively and affinely onto $A_cf_c+1+x^{m+1}\mathbb F_2[[x]]$ because $A_c$ is a unit. If $c$ is determined, division by $x^{v_c}$ maps this onto the cylinder $g\equiv p_c\pmod{x^{m+1-v_c}}$ of odd series, whose $\mu$-measure is $2^{-(m-v_c)}$; the pushforward of $\mu|_c$ is $2^{-v_c}\mu$ on that cylinder. If $c$ is undetermined, the part of the class with $v=k$ ($k\ge m+1$) has measure $2^{-m}2^{-(k-m)}$ and is mapped onto all odd series, so the pushforward of $\mu|_c$ is $2^{-m}\sum_{k>m}2^{-(k-m)}\mu=2^{-m}\mu$. $\square$

When $T$ preserves $\mu$, Birkhoff's theorem shows that the averages $\frac1k\sum_{i<k}\phi(T^if)$ converge $\mu$-almost everywhere to a limit with mean $\delta$. We do not use ergodicity. Both T2 and $T_{3759}$ preserve $\mu$ and have $\delta=-1/2$ (Lemma 4 below; for T2, class 0 is determined with $v=1$ and image all odd series, class 1 is undetermined).

## 3. Cycles

Let $f_0\to f_1\to\dots\to f_L=f_0$ be a cycle of odd polynomials, with multipliers $A_i=A_{c(f_{i-1})}$, valuations $v_i=v(f_{i-1})$, partial sums $S_i=v_1+\dots+v_i$, $S=S_L$, and $A_w=A_L\cdots A_1$.

**Lemma 3.** $x^Sf_L=A_wf_0+C_w$ with $C_w=\sum_{i=1}^Lx^{S_{i-1}}\prod_{l>i}A_l$. Moreover $\deg A_w=S$, and if $f_0$ has the least degree in the cycle then $\deg C_w\le S-1$.

*Proof.* The identity follows from $x^{v_i}f_i=A_if_{i-1}+1$ by induction. Summing Lemma 1 around the cycle gives $\sum_i\deg A_i=S$. By Lemma 1, $\sum_{l>i}\deg A_l=(S-S_i)+\deg f_L-\deg f_i$, so the $i$-th term of $C_w$ has degree $S_{i-1}+S-S_i+\deg f_0-\deg f_i=S-v_i-(\deg f_i-\deg f_0)\le S-1$. $\square$

Hence $f_0\,(x^S+A_w)=C_w$. The polynomial $x^S+A_w$ is nonzero, since its constant term is 1, and has degree less than $S$, since the leading terms cancel. Define the *cancellation* $\kappa=S-\deg(x^S+A_w)\ge1$. Lemma 3 gives
$$\deg f_0\le\kappa-1.\tag{1}$$

Let $r$ be the degree of the radical of $\prod_cA_c$, and let $j=j(w)$ be the largest integer with $2^j\mid S$ and $A_w\in\mathbb F_2[x^{2^j}]$.

**Theorem A.** $\kappa\le r\,2^{j}$. Hence the least element of every cycle has degree less than $r\,2^j$. For each $J$ only finitely many cycles have $j\le J$, and every cycle with $j=0$ has least element of degree less than $r$.

*Proof.* Since $\mathbb F_2$ is perfect, $x^S=a^{2^j}$, $A_w=b^{2^j}$ and $x^S+A_w=c^{2^j}$ with $a=x^{S/2^j}$ and $a+b=c$. The three are pairwise coprime: $b(0)=c(0)=1$, and a common factor of $b$ and $c$ would divide $a$. They are not all squares, by the maximality of $j$. A polynomial over $\mathbb F_2$ with zero derivative is a square, so $a',b',c'$ do not all vanish. The Mason-Stothers theorem [Mas, Sto, Sn] gives
$$\frac S{2^j}=\max(\deg a,\deg b,\deg c)\le\deg\operatorname{rad}(abc)-1\le1+r+\deg c-1=r+\frac{S-\kappa}{2^j},$$
because $\operatorname{rad}(a)=x$, $\operatorname{rad}(b)$ divides $\operatorname{rad}(\prod_cA_c)$, and $\deg\operatorname{rad}(c)\le\deg c$. So $\kappa\le r2^j$, and (1) bounds the least degree. A cycle is determined by its least element, and there are finitely many polynomials of bounded degree. $\square$

**Remarks.** (i) If the distinct multipliers are squarefree and pairwise coprime, $j=v_2(\gcd(S,n_1,\dots,n_k))$, where $n_i$ counts the steps that use the $i$-th distinct multiplier. In general $j$ has to be read from $A_w$; for $T_{3759}$, $1+x^2=(1+x)^2$ and $1+x^3=(1+x)(1+x+x^2)$, and the gcd formula differs from the true $j$ for most cycles (Section 6).

(ii) The proof works over $\mathbb F_p$ for maps $T(f)=\lambda(f)\,(A_cf-A_c(0))/x^v$ on series with $f(0)=1$, where $\lambda(f)\in\mathbb F_p^\times$ makes the constant term 1. The cycle equation reads $f_0(x^S-\lambda_wA_w)=C_w$ with $\lambda_w\in\mathbb F_p^\times$, the degree bound of Lemma 3 holds, and 2 is replaced by $p$ throughout, since over $\mathbb F_p$ a polynomial with zero derivative is a $p$-th power.

(iii) The bound is attained. The accelerated form of the Matthews-Leigh map, $f\mapsto((1+x^2)f+1)/x^v$, has the single multiplier $(1+x)^2$, so $r=1$. The cycle through $g_n=(1+x^{2^n-1})/(1+x)$ [Ma, Section 9] has $2^{n-1}$ steps, $S=2^n$ and $x^S+A_w=x^{2^n}+(1+x^2)^{2^{n-1}}=1$. So $\kappa=2^n=r2^j$ with $j=n$, and the least degree is $2^n-2$ (checked for $2\le n\le10$, ml_cycles.py). In particular infinitely many Frobenius levels can carry cycles.

## 4. Divergent orbits under negative drift

Throughout this section $T=T_{3759}$, with class $c=f_1+2f_2$ and $A_0=1+x$, $A_1=1+x+x^2$, $A_2=1+x^2$, $A_3=1+x^3$.

**Lemma 4.** (a) Classes 0 and 3 are determined with $v=1$; classes 1 and 2 are undetermined, so $v\ge3$ there. (b) $T$ preserves $\mu$, and $\delta=-1/2$. (c) $r=3$.

*Proof.* (a) Modulo $x^3$: $A_0\cdot1+1=x$, $A_3(1+x+x^2)+1\equiv x+x^2$, $A_1(1+x)+1=x^3\equiv0$ and $A_2(1+x^2)+1=x^4\equiv0$. (b) $p_0=1$ and $p_3\equiv1+x\pmod{x^2}$, so in Lemma 2 the density is $\tfrac12+\tfrac14+\tfrac14=1$ on both odd classes modulo $x^2$, hence on all residues modulo $x^3$. The drift is $\frac14\bigl((1-1)+(2-4)+(2-4)+(3-1)\bigr)=-\frac12$. (c) The radical of $(1+x)(1+x+x^2)(1+x)^2(1+x)(1+x+x^2)$ is $(1+x)(1+x+x^2)$. $\square$

Random starts behave as the drift predicts. Of 10,000 random odd starts of degree exactly 200, every one fell below degree 200, after 4.1 steps on average and at most 164 steps, and no orbit rose above degree 238 before falling (randstart.c). T2 gives 4.1, 119 and 222.

Put $Q=1+x+x^3$, $N(f)=Qf+1$, $z=x^{96}$, and
$$P=\texttt{0x8bfbfbfb7}\quad(\deg P=35,\ P(0)=1),$$
with bit $i$ the coefficient of $x^i$. $N$ vanishes at the fixed point $1/Q$ of branch 3. Since $Qf=N+1$, one step with multiplier $A$ and valuation $v$ acts on $N$ by
$$N\mapsto\frac{AN+A+Q+x^v}{x^v}.\tag{2}$$

**Theorem B.** Let $0\ne Y\in\mathbb F_2[z]$ with $Y\equiv z^3\pmod{1+z^2+z^3}$, and write $Y=z^nW$ with $W(0)=1$. Then
$$f_Y=\frac{x^{60}P\,Y(z)+1}{Q}$$
is an odd polynomial of degree $92+96\deg_zY$, the polynomial $R(Y)=\bigl[(1+z^2)(1+z)^{3n}W+1\bigr]/z$ satisfies the same congruence, and
$$T^{68+96n}(f_Y)=f_{R(Y)},\qquad\deg_zR(Y)=\deg_zY+1+2n.$$
Hence the orbit of every $f_Y$ diverges. Over each block of $68+96n$ steps the degree increases by $96(1+2n)\ge\frac{24}{17}(68+96n)$. The orbit of $1+x+x^2+x^4+x^8+x^{12}+x^{13}+x^{15}$ (`0xb117`) reaches $f_{z^3}$ after 279 steps.

*Proof.* *Step 1 (runs).* If $x^3\mid N(f)$, then $f\equiv Q^{-1}\equiv1+x+x^2\pmod{x^3}$, so $c(f)=3$ and $v=1$ by Lemma 4(a), and (2) gives $N(Tf)=(1+x^3)N(f)/x$ because $A_3+Q+x=0$. If $N(f)=x^2u$ with $u(0)=1$, then $f\equiv(1+x^2)(1+x+x^2)\equiv1+x\pmod{x^3}$ and $c(f)=1$. So if $v_x(N(f))=e\ge2$, the orbit makes exactly $e-2$ steps in class 3, after which $N=(1+x^3)^{e-2}N(f)/x^{e-2}$.

*Step 2 (the run from $f_Y$).* $N(f_Y)=x^{60+96n}P\,W(z)$, so $e=60+96n$ and the run has $58+96n$ steps. It ends at
$$N_1=x^2(1+x^3)^{58+96n}P\,W(z)=x^2(1+x^3)^{58}P\,(1+z)^{3n}W(z),$$
because $(1+x^3)^{96}=(1+x^{192})(1+x^{96})=(1+z)^3$. As $(1+z)^{3n}W(z)\equiv1\pmod{x^{96}}$, we get $N_1\equiv N^*:=x^2(1+x^3)^{58}P\pmod{x^{98}}$ for every $Y$.

*Step 3 (the return word; a finite computation).* If $N(f)\equiv N^*\pmod{x^{39}}$, the next ten steps have (class, $v$) equal to
$$(1,3),(0,1),(2,5),(1,3),(1,5),(1,4),(1,4),(1,8),(0,1),(2,4).$$
Indeed $f\bmod x^{39}$ is determined by $N(f)\bmod x^{39}$, and step $i$ reads only coefficients $1,\dots,\max(2,v_i)$ of the current point, i.e. coefficients up to $S_{i-1}+\max(2,v_i)\le38$ of $f$. The multipliers multiply to $(1+x+x^2)^6(1+x)^2(1+x^2)^2=(1+x^3)^6$, the valuations add to 38, and composing (2) ten times gives
$$N\mapsto\frac{(1+x^3)^6N+x^2P}{x^{38}}.$$
(word_K.py composes the ten affine maps and finds the constant $x^2P$ exactly; it also runs the word from 2,000 random completions of $N^*\bmod x^{39}$.) In other words, $P$ is $x^{-2}$ times the constant of the return word, and the return word is the one read from $x^2(1+x^3)^{58}P$.

*Step 4 (the block).* By Steps 2 and 3 the block of $(58+96n)+10$ steps sends $N(f_Y)$ to
$$\frac{(1+x^3)^{64}(1+z)^{3n}x^2P\,W+x^2P}{x^{38}}=x^{-36}P\bigl[(1+z^2)(1+z)^{3n}W+1\bigr]=x^{60}P\,R(Y)(z),$$
using $(1+x^3)^{64}=1+z^2$ and $x^{-36}=x^{60}/z$. The bracket has constant term $W(0)+1=0$, so $R(Y)$ is a polynomial in $z$, of degree $2+3n+\deg W-1=\deg Y+1+2n$. Thus $T^{68+96n}(f_Y)=(x^{60}P\,R(Y)(z)+1)/Q=f_{R(Y)}$.

*Step 5 (which $Y$ are valid).* Let $\alpha$ be the class of $x$ in $\mathbb F_8=\mathbb F_2[x]/(Q)$. Direct reduction gives $x^{60}P\equiv\alpha^6$ and $z\equiv\alpha^5=:\beta$. So $Q$ divides $x^{60}P\,Y(z)+1$ if and only if $Y(\beta)=\alpha^{-6}=\alpha=\beta^3$. The minimal polynomial of $\beta$ is $1+z^2+z^3$ (as $\beta^3+\beta^2+1=\alpha+\alpha^3+1=0$), so $f_Y$ is a polynomial exactly when $Y\equiv z^3\pmod{1+z^2+z^3}$. It is odd because $N(f_Y)(0)=0$, and its degree is $60+35+96\deg_zY-3$. Since $T^{68+96n}(f_Y)$ is a polynomial, Step 4 shows that $R(Y)$ satisfies the congruence too, and the blocks repeat forever. The degree ratio is smallest at $n=0$, where it is $96/68=24/17$. The statement about `0xb117` is a direct computation. $\square$

verify_reduction.py checks the theorem directly on 519 random valid $Y$ with $n\in\{0,1,2,3,5\}$ and $\deg W\le12$: the orbit of $f_Y$ follows the run and the word, arrives at $f_{R(Y)}$, and the degrees agree. It also checks the criterion of Step 5 for every nonzero $Y$ of $z$-degree below 12.

**The mechanism.** The run multiplier $1+x^3$ satisfies $(1+x^3)^{2^t}=1+x^{3\cdot2^t}$. A run that is longer by $96$ steps multiplies $N$ by $(1+z)^3\equiv1\pmod{x^{96}}$, so the point where the run ends is the same modulo $x^{96}$ for all run lengths in the progression $58+96n$, and the same return word follows. The block map on $N$ is affine over $\mathbb F_2[z]$, and the family is the set of its polynomial points. Section 7.1 compares this with the integers.

**The other escapes.** In the census of Section 6, 519 of the $2^{16}$ starts of degree at most 16 pass degree 600 under $T_{3759}$. All 519 pass degree 3000. With cap 10,000, 518 pass and one closes a cycle of length 72,134, with $S=157{,}696$, $\kappa=4096$, $j=11$ and least degree 3510, within the bound $r2^j=6144$ of Theorem A. The fastest of these orbits reach degree $C$ in about $C/1.7$ steps, like the family of Theorem B, but the median number of steps is about $(C/26)^2$ (1,796, 12,790 and 144,650 steps for $C=1000$, 3000, 10,000). So most escaping orbits grow like the square root of time; their class words have runs at several scales, and we have not proved that they diverge.

## 5. Substitution and the Matthews-Watts conjecture

A Matthews-type map over $\mathbb F_2[x]$ [Ma, (3)] is given by $d$ with $\deg d\ge1$, multipliers $m_i$ and residues $r_i\equiv i\,m_i\pmod d$, for $i$ running over the residues modulo $d$, by $T(f)=(m_if-r_i)/d$ when $f\equiv i\pmod d$. Part (i) of [Ma, Conjecture 3.1] (Matthews and Watts, for $\mathbb Z$) asserts that every trajectory eventually cycles when $\gcd(\prod m_i,d)=1$ and $|m_0\cdots m_{|d|-1}|<|d|^{|d|}$; over $\mathbb F_2[x]$ we read $|g|=2^{\deg g}$, so the condition says that the mean of $\deg m_i-\deg d$ is negative. Matthews and Leigh's map $U(f)=f/x$ or $((1+x^2)f+1)/x$ is the equality case, which cannot occur over $\mathbb Z$ [Ma, Section 3.1].

**Proposition C.** (a) Let $d=x^2$, $m_1=1+x^4$ and $m_0=m_x=m_{1+x}=1$, with $r_i=i\,m_i\bmod x^2$. Then $\gcd(\prod m_i,d)=1$, the mean of $\deg m_i-\deg d$ is $-1$, $T$ maps $\mathbb F_2[x^2]$ to itself, and $T(g(x^2))=U(g)(x^2)$. Consequently the orbit of $1+x^2+x^6$ diverges:
$$T^{5(2^n-1)}(1+x^2+x^6)=\frac{1+x^{6\cdot2^n+2}+x^{6\cdot2^n+4}}{1+x^2+x^4}.$$
Also $T$ has infinitely many cycles, the images of the cycles $g_n$ of Remark (iii) in Section 3.
(b) Let $T$ be the model of Section 2 with $m=1$, $A_0=1+x^4$ and $A_1=1+x$ (written "11 3"). It preserves $\mu$, has $\delta=-1/2$ and $r=1$, and for odd $h\in\mathbb F_2[[x]]$
$$T(h^2)=U^*(h)^2,\qquad U^*(g)=\frac{(1+x^2)g+1}{x^{w}},\quad w=v_x\bigl((1+x^2)g+1\bigr),$$
where $U^*$ is the accelerated form of $U$. Consequently the $T$-orbit of $1+x^2+x^6=(1+x+x^3)^2$ diverges: it passes through the square of the right-hand side of the Matthews-Leigh formula below, of degree $6\cdot2^n$, for every $n\ge1$.

*Proof.* (a) If $h=g(x^2)$, then $h\bmod x^2=g(0)$. If $g(0)=0$, $T(h)=h/x^2=(g/x)(x^2)$. If $g(0)=1$, $T(h)=((1+x^4)h+1)/x^2=\bigl[((1+x^2)g+1)/x\bigr](x^2)$. The displayed formula is the Matthews-Leigh formula $U^{5(2^n-1)}(1+x+x^3)=(1+x^{3\cdot2^n+1}+x^{3\cdot2^n+2})/(1+x+x^2)$ [Ma, Example 9.1] after substitution.
(b) For $f\equiv1\pmod{x^2}$, $(1+x^4)f+1\equiv0\pmod{x^2}$, and for $f\equiv1+x$, $(1+x)f+1\equiv x^2\equiv0$. So both classes are undetermined in Lemma 2, each pushes $\mu$ restricted to it forward to $\mu/2$, and $T$ preserves $\mu$. Given the class, $v-1$ is geometric with mean 2, so $\delta=\tfrac12\bigl((4-3)+(1-3)\bigr)=-\tfrac12$. The radical of $(1+x)^4(1+x)$ is $1+x$. If $f=h^2$, then $f_1=0$, so $c=0$, and $(1+x^4)h^2+1=((1+x^2)h+1)^2$ has valuation $2w$; this gives the identity. The $U^*$-orbit of $g$ consists of the odd points of the $U$-orbit of $g$, and the right-hand side of the Matthews-Leigh formula is odd, of degree $3\cdot2^n$. $\square$

ml_embed.py checks the Matthews-Leigh formula and the conjugacy of (a) for $n\le8$. (The formula in the text of [Ma] that we used was garbled by PDF extraction; we recomputed it.) t113_ml.py checks the identity of (b) on 100,000 random $h$ and the formula for $n\le10$; the $T$-orbit of $1+x^2+x^6$ reaches the $n$-th square after $4(2^n-1)$ steps for $n\le10$. Sampling 200,000 random starts gives mean degree change $-0.496$ and residues of $T(f)$ modulo $x^8$ consistent with uniform ($\chi^2=145.7$, 127 degrees of freedom). On fourth powers, $T(k^4)=\bigl(((1+x)k+1)/x^u\bigr)^4$ in (b), so there the model acts as the map of [HMYZ] and every orbit through a fourth power reaches 1. The model of (b) has a multiplier of degree 4 and lies outside the census of Section 6. The only square multiplier in that census is $1+x^2$, and a census model with $A_0=A_2=1+x^2$ acts on squares as the map of [HMYZ].

Proposition C(a) shows that the $\mathbb F_2[x]$ form of parts (i) and (iii) of the conjecture fails for a trivial reason: substitution lowers the drift and keeps the orbits. Part (b) shows the same inside our class of models. Its mean drift $-1/2$ is an average over all odd series, while on the $\mu$-null set of squares, which $T$ maps to itself, $T$ acts with the critical drift of $U$. The family of Theorem B is not of this kind. Each $f_Y$ is congruent to $Q^{-1}=1+x+x^2+\cdots$ modulo $x^{60}$, so it does not lie in any $\mathbb F_2[x^k]$ with $k\ge2$. Both constructions rest on Frobenius: the Matthews-Leigh orbit has degrees $3\cdot2^n$.

## 6. Census

**Models.** For $m=2$ we take every table of multipliers from $\{1+x,\ 1+x^2,\ 1+x+x^2,\ 1+x^3,\ 1+x+x^3,\ 1+x^2+x^3,\ 1+x+x^2+x^3\}$, i.e. all $A$ with $A(0)=1$ and $1\le\deg A\le3$; there are $7^4=2401$ tables. We keep those with $\delta<0$ that have a class able to raise the degree ($\deg A_c>v_c$ for a determined class, or $\deg A_c>m+1$ for an undetermined one). This leaves 442 tables (models_m2.py), of which 131 preserve $\mu$ by Lemma 2 (models_mp.py).

**Method.** For each table, every odd start of degree at most 16 is iterated until its degree falls below the initial degree, it closes a cycle (Brent's method), or its degree passes 600 (census2.c). For each distinct cycle we compute $S$, $A_w$, $\kappa$, $j$ from $A_w$ directly, $r$, the bound $r2^j$ and the least degree (cycstats3.py).

| tables | number | with a start passing degree 600 | distinct cycles | violations of Theorem A | cycles with least degree $\ge\kappa$ |
|---|---|---|---|---|---|
| Haar-preserving | 131 | 55 | 21,874 | 0 | 0 |
| not preserving | 311 | 131 | 55,486 | 0 | 0 |

Theorem A is a theorem, so the zero columns test the implementation. They matter because the gcd formula of Remark (i) gives a different $j$ for 62,108 of the 77,360 cycles (17,374 in Haar-preserving tables, 44,734 in the others); the census uses $j$ read from $A_w$. Among the 55 Haar-preserving tables with a start passing degree 600 the drift goes down to $-1$ (two tables) and $-5/4$ (one table, "9 7 9 3"). For tables that do not preserve $\mu$, $\delta$ is not the mean along typical orbits, because the classes are not visited with equal frequency; "3 3 7 3" has $\delta=-3/4$, and 32,767 of its $2^{16}$ starts pass degree 600.

**Two models in detail.** T2 ("7 3", $m=1$, $\delta=-1/2$, Haar-preserving, $r=3$): all $2^{22}$ odd starts of degree at most 22 either fall below their initial degree or close a cycle; none passes degree 600 and the largest degree reached is 407. There are 877 distinct cycles, all within Theorem A, 855 with $\kappa=r2^j$. The longest has 9,600 steps, with $S=15{,}360$, $\kappa=128$, $j=7$ and least degree 67. $T_{3759}$: 519 starts of degree at most 16 pass degree 600 (Section 4), and 444 distinct cycles appear.

**Two models over $\mathbb F_3$** (Remark (ii), $m=1$, class $f_1$; census_fp.py, all $3^{12}$ starts of degree at most 12, cap 300). F3a with multipliers $1+x+2x^2,\ 1+2x,\ 1+x$ for $f_1=0,1,2$ has $\delta=-2/3$ and 3 distinct cycles. F3b with $1+x,\ 1+2x,\ 1+2x+2x^2$ has $\delta=-1/6$ and 124 distinct cycles, 89 with $\kappa=r3^j$. No start passes degree 300, and every cycle satisfies Theorem A.

The T2 and $\mathbb F_3$ runs were pre-registered as a test of the Mason-Stothers reading before Theorem A was proved: one violation would have shown the reading wrong. The sweep of 442 tables was run after the proof, as a check of the code.

## 7. Comparison with the integers

### 7.1 Divergence: the order of the run multiplier

**Proposition D.** (a) Let $A\in\mathbb F_2[[x]]$ with $A(0)=1$, $A\ne1$, and $k=v_x(A-1)$. For $B>k$ the order of $A$ modulo $x^B$ is $2^{\lceil\log_2(B/k)\rceil}<2B/k$.
(b) For $B\ge3$ the order of 3 modulo $2^B$ is $2^{B-2}$.
(c) For the $3x+1$ map $U(n)=(3n+1)/2$ ($n$ odd), $n/2$ ($n$ even), write $n+1=2^LM$ with $M$ odd and $L\ge1$. Then $U^i(n)=3^i2^{L-i}M-1$ for $0\le i\le L$, so the orbit makes $L$ consecutive odd steps and reaches $3^LM-1$. For two starts with $M\equiv M'\pmod{2^B}$, $B\ge3$, the points reached agree modulo $2^B$ if and only if $L\equiv L'\pmod{2^{B-2}}$.

*Proof.* (a) $A^{2^t}-1=(A-1)^{2^t}$ has valuation $k2^t$, and the units of $\mathbb F_2[x]/(x^B)$ congruent to 1 form a 2-group. (b) is standard: $v_2(3^{2^t}-1)=t+2$ for $t\ge1$. (c) $U(3^i2^{L-i}M-1)=3^{i+1}2^{L-i-1}M-1$ while $L-i\ge1$. The last claim follows from (b), since $M$ is a unit modulo $2^B$. $\square$

In Theorem B the point where the run ends is fixed modulo $x^{39}$, while the run length $58+96n$ runs through a progression of difference 96. This is possible because the order of $1+x^3$ modulo $x^{39}$ is 16, which divides 96. In the $3x+1$ map the run multiplier is 3, and by (c) a fixed endpoint modulo $2^{39}$ forces the run lengths into one class modulo $2^{37}$. So a family built like that of Theorem B, with a fixed return word after runs of growing length, needs run lengths spaced by $2^{B-2}$ over $\mathbb Z$ instead of $O(B)$. This does not exclude divergent integer orbits of another shape. It shows which property of $\mathbb Z_2^\times$ the construction needs to fail: in $1+x\mathbb F_2[[x]]$ the powers $A^{2^t}$ approach 1 exponentially fast in $2^t$, while $|3^N-1|_2=2^{-(v_2(N)+2)}$ for even $N$, so $3^N$ approaches 1 only like $1/N$.

### 7.2 Cycles: Mason-Stothers against linear forms in logarithms

For the Syracuse map, a cycle with $a$ odd steps and total valuation $S$ satisfies $n_0(2^S-3^a)=C_w$, $C_w=\sum_{i=1}^a3^{a-i}2^{S_{i-1}}$, the integer form of Lemma 3. The proof of Lemma 3 carries over with $\log_2$ in place of degree: from $2^{v_l}n_l>3n_{l-1}$, the $i$-th term is at most $2^{S-v_i}n_0/n_i\le2^{S-1}$ when $n_0$ is the least element. The terms are added with carries, so only $C_w\le a\,2^{S-1}$ follows. With $\Lambda=S\ln2-a\ln3>0$ and $\kappa_{\mathbb Z}=S-\log_2(2^S-3^a)=-\log_2(1-e^{-\Lambda})$,
$$\log_2n_0\le\kappa_{\mathbb Z}+\log_2a-1,$$
the classical bound, against $\deg f_0\le\kappa-1$ in (1). The cancellation $\kappa_{\mathbb Z}$ grows. Along the convergents $S/a>\log_23$ of $\log_23$ one has $0<\Lambda<\ln 2/a$, so $\kappa_{\mathbb Z}\ge-\log_2\Lambda>\log_2a-O(1)$ infinitely often. Rhin's bound, in the form $\Lambda>\exp[-13.3(0.46057+\ln a)]$ [Rh; SdW, Lemma 12], gives $\kappa_{\mathbb Z}<13.3\log_2a+O(1)$. In $\mathbb F_2[x]$, Theorem A gives $\kappa\le r2^j$, bounded on each Frobenius level. The corresponding integer statement, $2^S-3^a\ge2^S/K$ for a constant $K$, is false. Relative to (1), the integer case loses $\log_2 a$ to carries and a logarithmic amount to the approximation of $\log_23$. The cycle side of the laboratory is therefore easier than the integers in both respects, and Theorem A cannot transfer as it stands. Frobenius levels have no counterpart over $\mathbb Z$.

### 7.3 Fine-scale mixing at the multiplier place

Tao's almost-all theorem rests on the decay of the characteristic function of the Syracuse offset: $|\mathbb E\,e^{-2\pi i\xi\,\mathrm{Syrac}(\mathbb Z/3^n\mathbb Z)/3^n}|\ll_An^{-A}$ for $\xi$ prime to 3 [Ta, Proposition 1.17]. In the model of Proposition C(b) both multipliers are powers of $y=1+x$. The analogue is the law of $R_k=f_L\bmod y^k$ for $\mu$-random $f_0$ and $L\ge k$, tested against characters of $\mathbb F_2[x]/(y^k)$ that are nontrivial on $y^{k-1}$. Both classes are undetermined, so by the proof of Lemma 2 the itinerary is i.i.d. under $\mu$. Then $R_k$ depends only on the last $k$ steps, through $R\mapsto(A_cR+1)x^{-v}$, and its law can be computed exactly (tao_analog.py, t113_fast.py). The largest such character value is 0.435, 0.203, 0.107 and 0.058 at $k=5,9,13,17$, and 0.049 at $k=18$. In between it oscillates with period 4, which comes from the multiplier $y^4$. The same computation for $\mathrm{Syrac}(\mathbb Z/3^k\mathbb Z)$ gives 0.129 at $k=5$ and 0.048 at $k=9$. For T2 the value is $1.3\cdot10^{-6}$ at $k=13$ modulo $y^k$, and 0.055 at $k=7$ modulo $(1+x+x^2)^k$. We did not prove decay. Up to these $k$, this input does not separate the integers from the model of Proposition C(b).

## 8. Questions

1. Does every polynomial orbit of T2 end in a cycle? T2 is Haar-preserving with $\delta=-1/2$ and $r=3$, and its run multiplier $1+x+x^2$ also satisfies $(1+x+x^2)^{2^t}=1+x^{2^t}+x^{2^{t+1}}$, but its runs raise the degree by 1 per step where those of $T_{3759}$ raise it by 2. Its multipliers are squarefree, so squares are not mapped to squares and Proposition C(b) does not apply. No start of degree at most 22 passes degree 600.
2. Do the 519 escaping orbits of $T_{3759}$ diverge? Their class words have runs at several scales; a hierarchical form of Theorem B might cover them.
3. For which tables does a block construction as in Theorem B exist, and can its existence be decided from the table? We traced 6,000 steps from the fastest escape of each Haar-preserving table with escapes (survey_blocks.py). Only $T_{3759}$ repeated a single return word, over 42 blocks. Others, such as "5 5 7 3" and "9 5 5 5", have run lengths that are multiples of 256 or 192 and several distinct return words.
4. Is the set of polynomials with divergent orbit under $T_{3759}$ recognizable by a finite automaton reading coefficients?

## 9. Supplement

All files are in `supplement.zip`, with outputs next to the scripts.

- `census2.c`, `census3.c`: census of a model (degree cap 600, or the cap as an argument). `cycstats3.py`: Theorem A data per cycle, with $j$ read from $A_w$ and a count of disagreements with the gcd formula.
- `models_m2.py`, `models_mp.py` (Lemma 2), `models_mp2.txt`: the 442 and 131 tables. `sweep_m2.sh`, `sweep_m2_D16.txt`, `sweep_join.py`: the census table of Section 6.
- `step0_T2_D22.txt`, `step0_T2_D22_ms.txt`, `step0_F3a_D12.txt`, `step0_F3b_D12.txt`, `census_fp.py`: T2 and the $\mathbb F_3$ models.
- `verify_reduction.py`, `word_K.py`: Theorem B. `esc_3759_C1000.txt`, `esc_3759_C3000.txt`, `esc_3759_C10000.txt`: escapes of $T_{3759}$ at three caps. `randstart.c`: random starts.
- `ml_embed.py`, `ml_cycles.py`: Proposition C(a) and Remark (iii). `t113_ml.py`, `t113_ml_out.txt`: Proposition C(b).
- `survey_blocks.py`, `survey_blocks.txt`: block structure of escaping orbits in other tables.
- `tao_analog.py`, `t113_fast.py`, `tao_analog_out.txt`, `t113_fast_out.txt`: Section 7.3.

## References

[ABP] G. Alon, A. Behajaina and E. Paran, On the stopping time of the Collatz map in $\mathbb F_2[x]$, arXiv:2401.03210 (2024).
[BP] A. Behajaina and E. Paran, The Collatz map analogue in polynomial rings and in completions, arXiv:2312.00390 (2023).
[HMYZ] K. Hicks, G. L. Mullen, J. L. Yucas and R. Zavislak, A polynomial analogue of the $3N+1$ problem?, *Amer. Math. Monthly* 115 (2008), 615–622. Not read; cited through [Ma] and [BP].
[In] M. Inselmann, On the average stopping time of the Collatz map in $\mathbb F_2[x]$, arXiv:2401.12781 (2024).
[La] J. C. Lagarias, The $3x+1$ problem and its generalizations, *Amer. Math. Monthly* 92 (1985), 3–23.
[Ma] K. R. Matthews, Generalized $3x+1$ mappings: Markov chains and ergodic theory, in *The Ultimate Challenge: The $3x+1$ Problem* (J. C. Lagarias, ed.), Amer. Math. Soc., 2010.
[Mas] R. C. Mason, *Diophantine Equations over Function Fields*, London Math. Soc. Lecture Note Ser. 96, Cambridge University Press, 1984.
[ML] K. R. Matthews and G. M. Leigh, A generalization of the Syracuse algorithm in $\mathbb F_q[x]$, *J. Number Theory* 25 (1987), 274–278. Not read; cited through [Ma, Section 9].
[Mo] K. G. Monks, On $q$-analogs of the $3x+1$ dynamical system, arXiv:2508.10153 (2025).
[Ni] D. Nichols, Analogues of the $3x+1$ problem in polynomial rings of characteristic 2, *Experiment. Math.* (2016); arXiv:1610.02545.
[Rh] G. Rhin, Approximants de Padé et mesures effectives d'irrationalité, in *Séminaire de Théorie des Nombres, Paris 1985–86*, Progr. Math. 71, Birkhäuser, 1987, 155–164. Not read; used through [SdW].
[SdW] J. Simons and B. de Weger, Theoretical and computational bounds for $m$-cycles of the $3n+1$ problem, *Acta Arith.* 117 (2005), 51–70.
[Sn] N. Snyder, An alternate proof of Mason's theorem, *Elem. Math.* 55 (2000), 93–94.
[Sto] W. W. Stothers, Polynomial identities and Hauptmoduln, *Quart. J. Math. Oxford* (2) 32 (1981), 349–370.
[Ta] T. Tao, Almost all orbits of the Collatz map attain almost bounded values, *Forum Math. Pi* 10 (2022), e12; arXiv:1909.03562.
