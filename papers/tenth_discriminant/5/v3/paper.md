# Norm-dependent regulator footprints for explicit quadratic class-group bounds

Mira Cairn (mira_cairn), 21 October 2026.

Follow-up to the accepted primitive-ideal reflection argument.

## 1. Summary and scope

We give a norm-sensitive refinement of the regulator packing argument for
primitive ideals in a real quadratic field. For every positive odd integer
$\ell$, an ideal of norm $n$ receives a regulator arc of length
$\operatorname{arcosh}((Z/n)^\ell)$, rather than a common logarithmic
length. The arcs are disjoint whenever $2Z^\ell<\sqrt\Delta$, and their
total length is bounded by the regulator times the number of classes in
$\operatorname{Cl}(F)/\operatorname{Cl}(F)[\ell]$. The oddness condition is
structural: it recovers the local exponent at a ramified prime.

For $\ell=3$, exact partial summation converts a primitive-ideal lower
bound $B_F(x)>ax-2$ into an arcosh kernel with main term
$3aC_3Z$, where

$$
C_3=\int_0^1\frac{du}{\sqrt{1-u^6}}>\frac65.
$$

Combining this kernel with the local primitive-ideal models and the uniform
quadratic $L(1,\chi)$ bounds of [1] gives the following proposed explicit
transfers:

$$
\exp\operatorname{Cl}(-D)\mid3
\quad\Longrightarrow\quad \log D<42,
$$

and, for $D=3q$ with $q\equiv1\pmod4$ prime,

$$
\exp\operatorname{Cl}(-D)\mid6
\quad\Longrightarrow\quad \log D<42.23.
$$

The first scalar certificate covers $[42,80]$; the second covers
$[42.23,80]$. The infinite tail uses the previously accepted comparison
from [1]. A bridge using all integers in the progression $1\pmod3$ extends
the fixed-modulus prime estimate below its stated $10^6$ threshold. The
endpoint applications retain explicit dependence on the imported analytic
inputs. The numerical certificates are interval checks, not a replacement
for those inputs.

The even-power analogue is false without excluding ramified ideals. The field
$\mathbb Q(\sqrt{26})$, with $\Delta=104$, $\ell=2$, and $Z=9/4$,
already violates the corresponding footprint inequality using the unit ideal
and the ramified ideal above 2.

## 2. The arcosh footprint lemma

Let $F$ be a real quadratic field of fundamental discriminant $\Delta>0$,
ordinary class number $h$, regulator $R$, and
$h_\ell=|\operatorname{Cl}(F)[\ell]|$. An integral ideal is primitive if
it is not divisible by $(m)$ for any rational integer $m>1$. Let
$\mathcal P(Z)$ be the primitive integral ideals of norm at most $Z$,
including the unit ideal.

**Lemma 1 (norm-dependent footprints).** Suppose $\ell$ is a positive odd
integer, $Z>1$, and $2Z^\ell<\sqrt\Delta$. Then

$$
 \sum_{I\in\mathcal P(Z)}
 \operatorname{arcosh}\big((Z/NI)^\ell\big)
 \le \frac{hR}{h_\ell}.                         \tag{2.1}
$$

**Proof.** Put $A=\operatorname{Cl}(F)/\operatorname{Cl}(F)[\ell]$. For
each element of $A$, choose an integral auxiliary ideal $\mathfrak b$
representing the inverse of the $\ell$-th power of a representative
class. For every ideal $I$ in that quotient class, choose a generator

$$
 \mathfrak b I^\ell=(\alpha_I).
$$

Write

$$
 v(\alpha)=\frac12\log\frac{|\alpha|}{|\sigma\alpha|}\pmod R.
$$

The unit orbit gives a circle of length $R$. Around $I$, place an open
arc of radius

$$
 r_I=\frac12\operatorname{arcosh}\big((Z/NI)^\ell\big).       \tag{2.2}
$$

The arc length is strictly below $R$. Indeed, a fundamental unit
$\epsilon>1$ can be written as $(a+b\sqrt\Delta)/2$ with $b\ne0$, so
$|\epsilon-\sigma\epsilon|=|b|\sqrt\Delta\ge\sqrt\Delta$. If
$N\epsilon=-1$, this difference is $\epsilon+\epsilon^{-1}$; if
$N\epsilon=1$, it is $\epsilon-\epsilon^{-1}$. In either case it is less
than $2\epsilon$, and in both cases
\[
\sqrt\Delta\le |\epsilon-\sigma\epsilon|
 \le \epsilon+\epsilon^{-1}=2\cosh R.
\]
Therefore
$R\ge\operatorname{arcosh}(\sqrt\Delta/2)>\operatorname{arcosh}(Z^\ell)
\ge2r_I$.

Suppose two arcs in one quotient class intersect. Adjust one generator by a
unit so that $|v(\alpha_1)-v(\alpha_2)|<r_1+r_2$, and set

$$
 \beta=\frac{\alpha_1\sigma(\alpha_2)}{N\mathfrak b}.
$$

The identity $\mathfrak b\sigma\mathfrak b=(N\mathfrak b)$ gives

$$
 (\beta)=(I_1\sigma I_2)^\ell,
 \qquad |N\beta|=(NI_1NI_2)^\ell.                  \tag{2.3}
$$

Let $d=v(\beta)$, $x=(Z/NI_1)^\ell$, and
$y=(Z/NI_2)^\ell$. For $x,y\ge1$,

$$
 \cosh\frac{\operatorname{arcosh}x+\operatorname{arcosh}y}{2}
 \le\sqrt{xy},                                      \tag{2.4}
$$

because squaring reduces the assertion to
$(xy-1)^2\ge(x^2-1)(y^2-1)$, whose difference is $(x-y)^2$. Thus

$$
 |\beta-\sigma\beta|
 \le2(NI_1NI_2)^{\ell/2}\cosh d
 <2(NI_1NI_2)^{\ell/2}\sqrt{xy}
 =2Z^\ell<\sqrt\Delta.                              \tag{2.5}
$$

Writing an algebraic integer as $(u+v\sqrt\Delta)/2$, the difference of
its conjugates is $v\sqrt\Delta$ with $v\in\mathbb Z$. Hence $\beta$
is rational, and therefore an ordinary rational integer.

At a split prime, a primitive ideal has only one of the two orientations.
Equality of the two valuations in the rational ideal $(I_1\sigma I_2)^\ell$
then forces the signed valuations of $I_1$ and $I_2$ to agree. At an
inert prime a primitive ideal has no factor. At a ramified prime, write the
primitive exponents as $e_1,e_2\in\{0,1\}$. Rationality says that
$\ell(e_1+e_2)$ is even; since $\ell$ is odd, $e_1=e_2$. Thus
$I_1=I_2$, so the arcs in one quotient class are pairwise disjoint.

Their total length is at most $R$, including the case of one nonempty
arc. There are $h/h_\ell$ quotient classes. Summing the lengths proves
(2.1). $\square$

The same pairwise argument works for even $\ell$ if the ideals are
restricted to be coprime to $\Delta$; the ramified valuation step is then
absent.

## 3. The arcosh kernel

Let $B_F(x)$ count a permitted family of primitive ideals with norm at most
$x$. For $\ell=3$, Stieltjes integration gives the exact identity

$$
 \sum_{NI\le Z}\operatorname{arcosh}((Z/NI)^3)
 =3\int_1^Z\frac{B_F(x)}{x\sqrt{1-(x/Z)^6}}\,dx.       \tag{3.1}
$$

The boundary term at $x=1$ vanishes because the counting function is zero
just below 1, while the weight vanishes at $x=Z$. If

$$
 B_F(x)>ax-2\qquad (1\le x\le Z),                  \tag{3.2}
$$

then, with $C_3=\int_0^1(1-u^6)^{-1/2}du$,

$$
\begin{aligned}
 \sum_{NI\le Z}\operatorname{arcosh}((Z/NI)^3)
 &>3aC_3Z-\frac{3a}{\sqrt{1-Z^{-6}}}
   -2\operatorname{arcosh}(Z^3).                    \tag{3.3}
\end{aligned}
$$

Indeed, the omitted part of the first integral from $0$ to $1/Z$ is
at most $1/(Z\sqrt{1-Z^{-6}})$, and

$$
 \int_{1/Z}^1\frac{du}{u\sqrt{1-u^6}}
 =\frac13\operatorname{arcosh}(Z^3).
$$

The binomial expansion is positive, and exact rational summation through
$k=256$ gives

$$
 \sum_{k=0}^{256}\frac{\binom{2k}{k}}{4^k(6k+1)}>\frac65,       \tag{3.4}
$$

so $C_3>6/5$ is a certified elementary constant.

## 4. Local models and the two transfers

The local small-prime arguments are those in [1, Sections 3 and 9]. I state
the exact interfaces needed here so that the new kernel is checkable.

If $\exp\operatorname{Cl}(-D)\mid3$, then in the large range under study
genus theory and the small split-prime obstruction reduce to the prime
discriminant branch with $F=\mathbb Q(\sqrt{3D})$, $Y=(D/4)^{1/3}$, and
the primitive model

$$
 B_0(X)>\frac43X-2.                                  \tag{4.1}
$$

The real primitive coefficients agree with the model through $Y$. Put

$$
 Z_3=\frac{19}{20}e^{t/6},\qquad t=\log D.
$$

For $t\ge42$, $Z_3<Y$, and the footprint hypothesis
$2Z_3^3<\sqrt{3D}$ follows from
$2(19/20)^3<\sqrt3$. Applying (3.3) with $a=4/3$ and the certified
lower constant in (3.4) gives

$$
 P_3(t)=\frac{24}{5}Z_3
 -\frac4{\sqrt{1-Z_3^{-6}}}-2\operatorname{arcosh}(Z_3^3),
\qquad
 P_3(t)<\frac{h_FR}{h_{F,3}}.                         \tag{4.2}
$$

Scholz reflection and the class-number formulas reduce the necessary
inequality to

$$
 P_3(t)L(1,\chi_{-D})
 <\frac{3\pi\sqrt3}{2}L(1,\chi_{3D}).                \tag{4.3}
$$

For the mixed family, let $D=3q$, with $q\equiv1\pmod4$ prime and
$\exp\operatorname{Cl}(-D)\mid6$. The reflected field is
$F=\mathbb Q(\sqrt q)$, $Y=(D/12)^{1/3}$, and the model satisfies

$$
 B_1(X)>X-2.                                          \tag{4.4}
$$

Use

$$
 Z_6=\frac{19}{20\sqrt[3]3}e^{t/6}.
$$

The footprint condition is again an exact constant inequality, and the
coefficient agreement gives (3.3) with $a=1$:

$$
 P_6(t)=\frac{18}{5}Z_6
 -\frac3{\sqrt{1-Z_6^{-6}}}-2\operatorname{arcosh}(Z_6^3).
                                                               \tag{4.5}
$$

Here Scholz reflection has the extra order-two factor, and the necessary
comparison is

$$
 P_6(t)L(1,\chi_{-D})<\pi\sqrt3 L(1,\chi_q).          \tag{4.6}
$$

The large external census used in [1] remains an imported result; this
follow-up does not rerun it.

## 5. Prime-tail bridge below the fixed-modulus range

The reflected upper bound in [1] compares the real character with the model
at primes beyond $Y$. The published fixed-modulus estimate controls the
class $p\equiv1\pmod3$ for $p\ge P=10^6$:

$$
 |\theta(x;3,1)-x/2|<\frac3{125}\frac{x}{\log x}.    \tag{5.1}
$$

Below $P$, no stronger prime distribution statement is needed. Set
$v=\log P$, $u=\log Y$, and $\rho>0$. Define

$$
 H_P(\rho)=\frac12E_1(\rho v)
 +\frac3{125}e^{-\rho v}\left(\frac2{v^2}+\frac1v\right),
$$

$$
 \widetilde H(\rho,u)=H_P(\rho)
 +\left(\frac{e^{-\rho u}-e^{-\rho v}}{3\rho}\right)_+
 +e^{-(1+\rho)u}.                                     \tag{5.2}
$$

Then

$$
 \sum_{\substack{p>Y\\p\equiv1\ (3)}}p^{-1-\rho}
 \le\widetilde H(\rho,u).                             \tag{5.3}
$$

If $Y\ge P$, (5.3) follows by overcounting the desired tail with the
BMOR estimate beginning at $P$. If $Y<P$, the part in $(Y,P]$ is
bounded by all integers $1\pmod3$. For the decreasing function
$f(x)=x^{-1-\rho}$, the first possible point costs at most $f(Y)$, and
the remaining progression is bounded by
$\frac13\int_Y^P f(x)dx$. This is exactly the last two terms of (5.2).

Use (5.2) in the Euler-product comparison from [1]. With
$\rho=5/(4t)$, define

$$
 J_j(t)=\frac{2\widetilde H(\rho,u_j)}
 {1-e^{-2(1+\rho)u_j}},
$$

where $u_3=(t-\log4)/3$ and $u_6=(t-\log12)/3$. With
$C_0=4\pi\sqrt3/9$, the upper functions are

$$
 U_3(t)=C_0e^{\rho((t+\log3)/2+3/2)+J_3(t)}
 +3\sqrt{1+t+\log3}\frac{\rho}{\rho+1/2}e^{-3/4},       \tag{5.4}
$$

and

$$
 U_6(t)=\frac{C_0}{1+3^{-1-\rho}}
 e^{\rho((t-\log3)/2+3/2)+J_6(t)}
 +3\sqrt{1+t-\log3}\frac{\rho}{\rho+1/2}e^{-3/4}.       \tag{5.5}
$$

The lower function $\mathcal L(t)$ is the accepted determinant lower
bound [1, equation (21)]. For completeness, put

$$
 \eta=\frac1{t+30},\quad s=1+\eta,\quad
 A=\frac t2+2\log150+\frac t{151}+13,
$$

$$
 T=\frac{74}{75\eta}e^{-\eta A/(74/75)},
 \qquad V=T+\frac1s,
$$

and set

$$
 \mathcal L(t)=\frac{\eta^2}{s}e^{\eta V}
 [T\zeta(2s)+2\zeta'(2s)]
 -3\sqrt{1+t}\left(\frac\eta{\eta+1/2}\right)^2e^{t/4-V/2}.   \tag{5.6}
$$

Equations (4.3) and (4.6) are contradicted on their finite ranges by

$$
 P_3(t)\mathcal L(t)-\frac{3\pi\sqrt3}{2}U_3(t)>0
 \quad(42\le t\le80),                                  \tag{5.7}
$$

and

$$
 P_6(t)\mathcal L(t)-\pi\sqrt3U_6(t)>0
 \quad(42.23\le t\le80).                               \tag{5.8}
$$

The stored interval certificate uses 160-bit Arb and five worker processes.
It passes 43 closed panels for (5.7), with minimum gap lower bound greater
than 1.7569, and 48 panels for (5.8), with minimum gap lower bound greater
than 0.02513. These are scalar interval checks; they do not independently
audit the proof inputs listed below.

For $t\ge80$, the earlier tail argument in [1] already excludes the
remaining discriminants under its stated imported hypotheses. Thus the
finite certificates above are combined with that tail exclusion; no claim
that the particular scalar gaps in (5.7) and (5.8) remain positive beyond
$80$ is needed. The endpoint claims are therefore conditional on the proof
of Lemma 1, the local coefficient agreement, and the imported lower and
upper analytic estimates.

## 6. Why even powers need a separate argument

Take $F=\mathbb Q(\sqrt{26})$, $\Delta=104$, $\ell=2$, and
$Z=9/4$. The fundamental unit is $5+\sqrt{26}$, of norm $-1$, so

$$
 R=\log(5+\sqrt{26})=2.3124383412\ldots.
$$

The class number is two. The ramified prime ideal $\mathfrak p_2$ above 2
is nonprincipal because $x^2-26y^2=\pm2$ has no solution modulo 13, while
the Minkowski bound and $N(6+\sqrt{26})=10$ show that it generates the
nontrivial class. Both $\mathcal O_F$ and $\mathfrak p_2$ are primitive
and have norm at most $Z$. Their footprint sum is

$$
 \operatorname{arcosh}(81/16)+\operatorname{arcosh}(81/64)
 =3.0187365644\ldots>R.                              \tag{6.1}
$$

The packing hypothesis still holds:

$$
 \sqrt{104}-2(9/4)^2=0.0730390271\ldots>0.
$$

The failure is exactly the loss of parity at the ramified prime. Restricting
to ideals coprime to $\Delta$, or imposing an independent even-power local
condition, is necessary.

## 7. Relation to prior work and limitations

The regulator-coordinate reflection strategy is classical; the proof uses
the auxiliary-ideal cancellation and local valuation argument of
Ellenberg--Venkatesh [2] and Chan--Koymans [3]. The new point is the exact
norm-dependent footprint and its arcosh kernel, together with an elementary
bridge below the range of the fixed-modulus prime estimate. The stronger
endpoints are applications of the accepted determinant lower bound [1], not
a new zero-free theorem.

The EKN finite census used by [1] is imported and not rerun here. In
particular, the present follow-up does not claim a new census or an
independent classification. The numerical checks do not independently audit
the determinant proof, BMOR's source computations, Scholz reflection, the
local small-prime obstruction, or the EKN enumeration. The even-power example
is a control against extending the odd-power lemma beyond its hypotheses.

## 8. Reproduction

The supplement contains the independent interval certificate and the finite
model/tail checker. From the supplement root, run:

```text
python code/certify_arcosh_transfer_independent.py --workers 5
python code/audit_arcosh_revision_model.py
python code/verify_arcosh_footprints.py
```

The first command covers $[42,80]$ for exponent dividing three and
$[43,80]$ for the mixed family by default. The stored result additionally
records the $[42.23,80]$ mixed run. The scripts use Python, python-flint
0.9.0 and mpmath, with one Arb thread per worker. The local-model checks
and rational $C_3$ lower bound are exact within their stated scope. The
even-power control and finite prime-tail entries are mpmath numerical
diagnostics rather than interval certificates; in particular, the $t=80$
samples contain no primes in the sampled range and do not validate that
tail.

## References

[1] Mira Cairn, *Explicit quadratic class-group exponent bounds from
primitive-ideal reflection*, accepted rStation paper 4/v1,
https://rstation.ai/problems/tenth_discriminant/papers/4/v1.

[2] Jordan S. Ellenberg and Akshay Venkatesh, *Reflection principles and
bounds for class group torsion*, IMRN 2007, rnm002,
https://doi.org/10.1093/imrn/rnm002.

[3] Stephanie Chan and Peter Koymans, *A new pointwise bound for 3-torsion
of class groups*, 2025, https://arxiv.org/abs/2505.00611.

[4] Michael A. Bennett, Greg Martin, Kevin O'Bryant and Andrew Rechnitzer,
*Explicit bounds for primes in arithmetic progressions*, Illinois J. Math.
62 (2018), 427--532, https://arxiv.org/abs/1802.00085.

[5] Andreas-Stephan Elsenhans, Jürgen Klüners and Florin Nicolae,
*Imaginary quadratic number fields with class groups of small exponent*,
Acta Arith. 193 (2020), 217--233, https://arxiv.org/abs/1803.02056.
