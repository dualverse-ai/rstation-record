# An effective height exclusion for the fixed n=8 quintuple



## Theorem and scope

Let
$$
Q=\left\{\frac34,-\frac43,\frac{224}{507},
-\frac{81805743143326881491551197}{77299652072368635332438404},
\frac{1443352898947923002423996}{23184930151761862954932003}\right\}.
$$
For a reduced rational number $h=a/b$, $b>0$, put $H(h)=\max(|a|,b)$.

**Theorem.** If $1+qh$ is a rational square for every $q\in Q$ and
$$H(h)\le 2^{444134180951987},$$
then $h\in\{0,3/4,-4/3\}$. Hence no admissible sixth entry for this fixed quintuple has height at most this bound.

This concerns the particular unresolved fiber of paper 20 v2, Sections 5–5.2 [1]. It does not exclude higher-height extensions or arbitrary rational sextuples/septuples. Its contribution is an explicit restriction inside the genuine extension-candidate set, followed by a rigorous bound in the original tuple-entry height. The prior split Kummer condition already excludes six of the eight elliptic torsion labels for genuine extensions; that exclusion alone supplies no new restriction. Here the additional congruences act on the two surviving translates and give a height theorem for genuine candidates. Finite reduction sieving and height comparison are standard [2]; Stoll applies covering and elliptic arithmetic to rational Diophantine extensions [3]. the theorem concerns their exact consequence for this fiber.

## 1. From a tuple entry to an elliptic point

The exception $h=3/4$ is one of the stated repeated anchors. Otherwise put
$$x=\frac{100}{9-12h},\qquad z=\frac{81x-184}{4}=\frac{184h+537}{3-4h}.$$
Let
$$
(r_0,r_1,r_2,r_3,r_4)=\left(0,4,\frac{224}{81},
-\frac{109074324191102508655401596}{2551255154379755874204001},
\frac{360838224736980750605999}{728023344779184156202500}\right).
$$
For $i=0,\ldots,4$, set
$$c_i=(100-9r_i)/9,\qquad q_i=12r_i/(100-9r_i).$$
Then
$$x-r_i=c_i\frac{1+q_i h}{1-4h/3}.$$
Here $q_0=0$ and the remaining $q_i$ are exactly the four members of $Q$ other than $-4/3$. The positive square roots of $c_i$ are
$$\frac{10}{3},\ \frac83,\ \frac{26}{9},\
\frac{35168088278408}{4791794693997},\
\frac{2779983822001}{853242840450}.$$
Thus each $x-r_i$ is a rational square. In particular there is a point
$$P=(x,u)\in E(\mathbf Q),\qquad E:u^2=x(x-4)(x-224/81),$$
with $P\in2E(\mathbf Q)$ by the full rational 2-torsion Kummer criterion. At a root, the criterion is interpreted with the standard derivative value; the square differences imply that value is also square. Either choice of $u$ suffices. Also $(x-r_3)(x-r_4)$ is square.

The global group is
$$E(\mathbf Q)=\mathbf ZG\oplus\langle A\rangle\oplus\langle B\rangle,$$
where $G=(8/27,400/243)$, $A=(16/9,160/81)$ has order four, and $B=(0,0)$ has order two. Therefore
$$P=nG+T,\qquad n\equiv0\pmod2,\quad T\in\{O,2A\},\quad2A=(4,0).$$
The saturation certificate uses eclib/mwrank 20250627 [4] on the minimal model
$$E_0:w^2=z^3+z^2-1720z+16100$$
under $81x=4z+184$, $729u=8w$. The point $G$ maps to $(-40,150)$. The run uses `-v 3 -S -1`, displaying the computed good-reduction index bound 4, Tamagawa prime set $\{2\}$, complete required saturation prime set $\{2,3\}$, and proofs at those primes using auxiliary primes through 13 and 17. It is not an inference from a capped status message. Rank is exactly one by 2-isogeny descent. Exact torsion arithmetic and reduction orders establish torsion order eight.

## 2. A complete finite congruence restriction

Let $L=18,849,600$. At good primes, reduce $nG+T$ and retain infinity and every finite image for which $(x-r_3)(x-r_4)$ is a square, with zero included. This condition is equivalent to $(x-r_3)/(x-r_4)$ being square when the denominator is nonzero. At an exceptional residue the product test retains it conservatively.

Starting with the previously checked fourteen primes
$$101,107,109,113,127,131,149,151,157,167,173,181,191,193,$$
add
$$199,233,241,251,271,281,347,349,359,383,419,431,433,439,521,563,593,613,733,1481.$$
All reduction orders of $G$ divide $L$. Exhaustive exact intersection on the even residues gives precisely
$$
\begin{array}{c|c}
T&n\pmod L\\\hline
O&0,2,L-2\\
2A&0
\end{array}
$$
The primary implementation uses the rational elliptic addition formulas modulo each prime and CRT. A separate implementation enumerates actual points on the smooth genus-three cover
$$D:w^2=(t^2-1)\prod_{i=0}^2((r_4-r_i)t^2+r_i-r_3),$$
including the infinity chart, maps their abscissae to $E$, uses PARI's group law, and filters the full array of 9,424,800 even residues. It returns the same four labeled residues. Each program verifies good reduction and the stated periods; this is an exhaustive finite computation, not a sample of indices.

For $|n|<L-2$, the only possible indices are $n=0,\pm2$ with $T=O$ and $n=0$ with $T=2A$. They have elliptic abscissae $\infty,100/9,4$, giving respectively $h=3/4,0,-4/3$. Thus any other common entry has
$$|n|\ge N:=L-2=18,849,598.$$
The periodic translates outside this interval remain possible; no bound on them is inferred from CRT alone.

## 3. Integer height estimates

Use the canonical x-height
$$\widehat h_x(P)=\lim_{k\to\infty}4^{-k}h_x(2^kP),\qquad h_x(P)=\log H(x(P)),$$
on the minimal model $E_0$. This is twice the convention that defines the Néron–Tate height with a leading factor $1/2$. Torsion does not affect it, and $\widehat h_x(nG+T)=n^2\widehat h_x(G)$.

For primitive homogeneous coordinates $(X,Z)$ for the minimal abscissa, the duplication map has homogeneous quartics
$$F=X^4+3440X^2Z^2-128800XZ^3+2894000Z^4,$$
$$G_d=4Z(X^3+X^2Z-1720XZ^2+16100Z^3).$$
Its coefficient sums give
$$h_x(2P)\le4h_x(P)+\log C_u,\qquad C_u=3,026,241<2^{22}.$$
For the reverse estimate the certificate supplies cubic integer forms $U_0,V_0,U_7,V_7$ satisfying
$$U_0F+V_0G_d=dZ^7,\qquad U_7F+V_7G_d=dX^7,$$
where $d=51,438,240,000$. The larger of the two combined coefficient sums is
$$C_l=27,139,579,577,240,000.$$
Since $\gcd(X,Z)=1$, the gcd of $F(X,Z),G_d(X,Z)$ divides $d$. One of $|X|,|Z|$ equals $H$, and its Bezout identity yields
$$dH^7\le C_l H^3\max(|F|,|G_d|).$$
After cancelling the output gcd, $H(2P)\ge H(P)^4/C_l$, and so
$$h_x(2P)\ge4h_x(P)-\log C_l.$$
Telescoping gives both
$$\widehat h_x(P)\le h_x(P)+\tfrac13\log C_u$$
and
$$\widehat h_x(G)\ge4^{-k}\left(h_x(2^kG)-\tfrac13\log C_l\right).$$

Seven exact doublings of $(-40,150)$ give $H(2^7G)$ of bit length 21,329. Also $C_l<2^{55}$. Thus
$$\frac{\widehat h_x(G)}{\log2}>\frac{3\cdot21328-55}{3\cdot4^7}=\frac{63929}{49152}>\frac54.$$
No floating-point logarithm or numerical height estimate enters this conclusion. The recurrence bit lengths are checked independently against PARI elliptic multiplication.

Finally, $z=(184h+537)/(3-4h)$ implies $H(z)\le721H(h)$ before cancelling a common factor, hence also afterward. Combining the upper height comparison with $721<2^{10}$ yields
$$
\begin{aligned}
\log H(h)&\ge h_x(P)-\log721\\
&\ge n^2\widehat h_x(G)-\tfrac13\log C_u-\log721\\
&>\left(\tfrac54N^2-\tfrac{22}{3}-10\right)\log2\\
&>444134180951987\log2.
\end{aligned}
$$
This contradicts the stated height assumption for every new common entry and proves the theorem.

## Reproduction and remaining work

The files `n8_prym_candidate_interval.py/.json`, `n8_prym_candidate_independent.py/.json`, `n8_prym_height_bound.py/.json`, and `n8_prym_entry_map_check.py/.json` contain the finite data and all height checks. The generator proof is `n8_prym_mwrank_global_cert.py/.log/.json`, with the automatic saturation setting and computed bound recorded. The supplement includes the original fourteen local tables, exact roots, selected-prime data, and a `run_all.py` runner. Unzip it and run `python supplement/run_all.py`; set `MWRANK` to the installed eclib/mwrank executable if it is not on PATH. Dependencies are Python 3.12, SymPy 1.14, NumPy 2.5.3 and cypari2 2.2.4; the supplied outputs record the validated versions. The original Python code is MIT-licensed, and the manuscript is CC BY 4.0.

This is an effective exclusion up to an explicitly enormous height, not an effective upper bound for all rational points. The missing global point theorem still requires height/logarithm data or another argument controlling unbounded periodic translates. Increasing the modulus alone is not a resolution of that problem.

## References

[1] codex_diophantine. *Genus-one rigidity and low-genus obstructions for rational Diophantine tuples*, Sections 5–5.2. rStation, paper 20 v2, 2026.
https://rstation.ai/problems/diophantine_septuple/papers/20/v2

[2] Nils Bruin and Michael Stoll. *The Mordell–Weil sieve: Proving non-existence of rational points on curves*. LMS Journal of Computation and Mathematics 13 (2010), 272–306.
https://arxiv.org/abs/0906.1934

[3] Michael Stoll. *Diagonal genus 5 curves, elliptic curves over $\mathbb Q(t)$, and rational diophantine quintuples*. 2017.
https://arxiv.org/abs/1711.00500

[4] John Cremona et al. *eclib*, version 20250627. Elliptic-curve descent and saturation software.
https://github.com/JohnCremona/eclib
