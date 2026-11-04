# Fourth moments and zero density for quartic Hecke characters ordered by conductor

## 1. Results and previous work

Let $\mathcal F_4(Q)$ be the distinct primitive finite-order Hecke
characters over $\mathbb Q(i)$ whose orders divide four and whose
conductor norms are at most $Q$. They have trivial infinity type.
All local characters at the prime above two are included. In a
Dirichlet polynomial, character values retain their zeros at primes
of the conductor. A fixed omission of the prime above two is permitted.

**Theorem 1.** For every fixed $H\ge1$ and $\epsilon>0$,

$$
 \sum_{\chi\in\mathcal F_4(Q)}
       |L(1/2+it,\chi)|^4
       \ll_{H,\epsilon}Q^{13/9+\epsilon},\qquad |t|\le H.
 \tag{1}
$$

The theorem includes the full quartic family ordered by conductor,
not just squarefree quartic presentations. The character with
presentation $ab^2d^3$, where $a,b,d$ are pairwise coprime and squarefree,
has odd conductor $abd$. Replacing conductor ordering by the norm of
that presentation would discard information used in the proof.

There is a zero-density application. For a nonprincipal primitive
character define

$$
 N(\sigma,T;\chi)=\#\{\rho:L(\rho,\chi)=0,
                \ \Re\rho\ge\sigma,\ |\Im\rho|\le T\},
 \tag{2}
$$

with multiplicity. The principal function is treated by the same
zero count after excluding its pole.

**Theorem 2.** For every fixed $3/4<\sigma<1$ and $\epsilon>0$ there
is $h=h(\sigma,\epsilon)>0$ such that

$$
 \sum_{\chi\in\mathcal F_4(Q)}N(\sigma,Q^h;\chi)
       \ll_{\sigma,\epsilon}Q^{E_4(\sigma)+\epsilon}.
 \tag{3}
$$

The continuous decreasing function $E_4$ is given explicitly in
Section 7. In particular,

$$
 E_4(4/5)=\frac{32}{39},\qquad
 E_4(5/6)=\frac35,\qquad
 E_4(17/20)=\frac{12}{23},\qquad
 E_4(7/8)=\frac25.
 \tag{4}
$$

The positive height power is chosen after the requested losses and
all fixed differentiation orders. No uniform positive height power
is asserted as $\sigma$ approaches an endpoint.

We start with the inverse-pair estimate [1, equation (20)], which
already follows from the older squarefree sieve [2], and the quadratic
large sieve [3]. The sharper quartic Proposition 4 of [1] is not
needed here. Together these inputs give
an ordinary common-coefficient mean of size

$$
                         Q+Q^{2/3}L
 \tag{5}
$$

for centrally normalized polynomials of length $L$. The associated
central second moment is $Q^{7/6+\epsilon}$. We treat these as baseline
consequences, not separate new results.

Our additional step keeps all three quartic conductor components
through a distinct-character Gram argument. For a smooth ordinary
Gram matrix of length $Z$ we prove

$$
 \sup_{\alpha\in\mathcal F_4(Q)}
       \sum_{\substack{\beta\in\mathcal F_4(Q)\\\beta\ne\alpha}}
            |G_{\alpha,\beta}(Z)|^2
       \ll_\epsilon(QZ)^\epsilon(QZ+Q^{8/3}).
 \tag{6}
$$

The ratio of two characters retains a zero mask at each canceled
prime. After primitive Poisson summation, the fixed character in the
ratio is a common frequency coefficient. The residual family remains
ordered by conductor, so (5) applies. Hilbert duality then gives large
values, (1), and a finite restricted-row iteration used in (3).

The Gram and restricted-row methods were developed for cubic conductor
pairs in [4]. We credit that method and recompute its arithmetic input
for the full quartic family. The new assertions are (6) and the quartic
applications, rather than Poisson summation, Hilbert duality or iteration
as general techniques. De Faveri [5, Section 1.2] distinguishes natural
and conductor ordering and proves the tight cubic conductor second
moment. His natural-index zero-density theorem does not give (3).
Gao and Zhao [6, Theorem 1.3] prove a $Q^{7/6+\epsilon}$ second moment
for rational quartic Dirichlet characters and a different mean for
rationally indexed Gaussian Hecke characters. Neither is the complete
Gaussian conductor family here. Corrigan [7, Theorem 2.3] likewise
concerns rational Dirichlet characters. The scalar zero detector and
common-factor selection come from [8, Sections 4--5.2]; their hypotheses
are checked directly for the present conductor family.

Liu [9, main theorem and Theorem 17.1] states a zero-free half-plane
$\Re s>B_\flat=0.874886647039964\ldots$ for every finite-order Hecke
character over every number field. It therefore covers this family.
Our density proof does not use that result. In comparison with it,
Theorem 2 supplies zero-count information in $3/4<\sigma\le B_\flat$;
for $\sigma>B_\flat$ the zero count already vanishes by [9]. In
particular the benchmark at $7/8$ compares the two density methods
within this paper and is not an improvement over the zero information
in [9]. The benchmark at $5/6$ lies below that zero-free boundary.

For the same family as (1), applying (5) directly to the square of
a central approximate functional equation gives only
$Q^{5/3+\epsilon}$. At $\sigma=5/6$, the usual second-moment zero
detector with (5) gives exponent $7/8$, compared with $3/5$ in (3).
Section 8 supplies that comparison. We do not claim optimality among
all possible combinations of prior estimates. These are family moment
and zero-density results; they do not give a new zero-free half-plane
for an individual function or resolve the Riemann hypothesis.

## 2. The conductor family and a common polynomial mean

Write $\mathcal O=\mathbb Z[i]$ and $\lambda=1+i$. Unless specified
otherwise, an ideal index is nonzero, integral and prime to $\lambda$.
We identify it with its unique primary generator, congruent to one
modulo $\lambda^3$. Norms are ideal norms. For an odd prime ideal
$\mathfrak p$, its residue field contains $\mu_4$, and its multiplicative
characters of order dividing four are the powers of the quartic residue
character. We write $\chi_a$ for the usual quartic ideal family, keeping
its fixed dyadic factors when reciprocity is applied.

At an odd prime, a character of order dividing four is trivial on
principal units, whose finite quotients are $p$-groups. Its conductor
exponent is therefore at most one. At $\lambda$, the local logarithm
is an isomorphism on $1+\lambda^3\mathcal O_\lambda$, and multiplication
by four maps $\lambda^3\mathcal O_\lambda$ onto
$\lambda^7\mathcal O_\lambda$. Hence

$$
 (1+\lambda^3\mathcal O_\lambda)^4
       =1+\lambda^7\mathcal O_\lambda.
 \tag{7}
$$

Every local character of order dividing four is trivial on the right
side. Its dyadic conductor exponent is bounded by seven.

The local units decompose as
$\mathcal O_\lambda^\times=\mu_4\times(1+\lambda^3\mathcal O_\lambda)$.
Thus a prescribed order-dividing-four character on the global units
extends to a dyadic character of that order: use its prescribed value
on $\mu_4$ and the trivial character on the second factor. In
particular, the unit compatibility below can always be enforced by
one of a fixed finite collection of dyadic adjustments.

Since $\mathbb Q(i)$ has class number one, an actual finite-order Hecke
character is determined by its finite residue characters, subject to
triviality on global units. Its odd local exponents split uniquely into
three coprime squarefree ideals $a,b,d$, on which those exponents are
$1,2,3$. On primary generators its good part is
$\chi_a\chi_b^2\overline{\chi_d}$, up to fixed dyadic phases. The
remaining local data belong to the finite set in (7). Unit compatibility
selects a subset of that set. Conversely these compatible choices give
the actual characters. In positive upper bounds we may enlarge the
compatible subset. Distinct choices of odd exponents have distinct odd
characters; within each such choice we count distinct dyadic characters
only. This classification also appears in [10, Section 4.4.2] for the
unramified-at-two subfamily. Conjugation interchanges $a,d$ and leaves
$b$ unchanged.

The following estimates allow bounded fixed ray factors. A growing
character or a deletion may also occur as a **common coefficient** of
the inner polynomial; no conductor-dependent constant is then invoked.
Let $\tau(n)^A$ be any fixed divisor bound on coefficients.

**Lemma 3.** Let

$$
 P_\chi(L)=L^{-1/2}\sum_n b_n\chi(n)W(Nn/L),
       \qquad |b_n|\le\tau(n)^A,
 \tag{8}
$$

where $W$ is smooth with compact support in $(0,\infty)$ and common
to the family. The inner ideals are ordinary. Then

$$
 \sum_{\chi\in\mathcal F_4(Q)}|P_\chi(L)|^2
       \ll_{\epsilon,A,W}(QL)^\epsilon(Q+Q^{2/3}L).
 \tag{9}
$$

The same assertion holds for a family of common profiles separated
against a measure of bounded weighted $L^1$ mass, with the corresponding
fixed profile seminorms. Character restrictions may be imposed before
the positive sum.

*Proof.* First restrict the inner ideals to squarefree $n\asymp L$
and use arbitrary coefficients $\ell_n$. Partition $Na,Nb,Nd$ into
dyads $A,B,D$, and put $R=ABD$, $P=AD$. Separate the fixed reciprocity
packets. Fixing $b$ and absorbing its quadratic character into $\ell_n$,
[1, equation (20)] gives

$$
 \sum_{a,b,d}\left|\sum_n\ell_n
                    \chi_a(n)\chi_b(n)^2\overline{\chi_d(n)}\right|^2
       \ll (RL)^\epsilon
                  (R+R P^{-1/2}L)\sum_n|\ell_n|^2.
 \tag{10}
$$

The inverse-pair estimate permits ordinary outer ideals, so enlarging
the original coprime squarefree outer subset is legitimate at this
positive stage. All zeros and the fixed $b$ twist remain in the inner
coefficients. Independently, fix $a,d$ and use the number-field quadratic
sieve [3] in $b$. It gives

$$
                     (RL)^\epsilon(R+PL)\sum_n|\ell_n|^2.
 \tag{11}
$$

If $P\le R^{2/3}$ use (11); otherwise use (10). Thus each rectangle
has bound

$$
                  (RL)^\epsilon(R+R^{2/3}L)\|\ell\|_2^2.
 \tag{12}
$$

All finite dyadic and reciprocity packets cost constants. The complete
conductor is a fixed dyadic multiple of $abd$, so summing its dyads and
the logarithmically many rectangles proves the squarefree-inner form
with $Q$ in place of $R$.

For ordinary inner ideals write uniquely $n=e^2f$, $f$ squarefree;
no condition $(e,f)=1$ is imposed. Put $L_e=L/(Ne)^2$. The $e$ daughter
of (8) has the outside factor $(Ne)^{-1}\chi(e^2)$ and common
coefficients $b_{e^2f}$ at length $L_e$. Character multiplication, with
its zero values, is valid without coprimality. The diagonal factor
$\chi(e^2)$ has modulus at most one. Minkowski and (12) give

$$
 \left(\sum_\chi|P_\chi(L)|^2\right)^{1/2}
 \ll (QL)^\epsilon\sum_{Ne\ll\sqrt L}\frac1{Ne}
                  \sqrt{Q+Q^{2/3}L/(Ne)^2}
 \ll (QL)^{2\epsilon}\sqrt{Q+Q^{2/3}L}.
 \tag{13}
$$

The two sums have weights $(Ne)^{-1}$ and $(Ne)^{-2}$, respectively,
and cost at most a logarithm. Empty subunit daughters contribute zero;
bounded endpoint ranges are absorbed into fixed constants. Rechoose
$\epsilon$. The profile assertion follows by Minkowski once more.
$\square$

Equation (9) is a bounded-common-coefficient statement. We do not assert
an unrestricted ordinary-column operator norm with the same unweighted
coefficient mass. This distinction is essential in the applications.

## 3. Primitive overlap sectors and the Gram estimate

Fix a nonnegative radial smooth profile $V$ of compact support in
$(0,\infty)$, and set

$$
 G_{\alpha,\beta}(Z)=\sum_n V(Nn/Z)
                         \alpha(n)\overline{\beta(n)}.
 \tag{14}
$$

The sum is over ordinary odd ideals. A fixed smooth majorant may replace
$V$ when a product support is being estimated. The diagonal is $O_V(Z)$.

**Lemma 4.** For $Q,Z\ge1$, (6) holds, uniformly in
$\alpha\in\mathcal F_4(Q)$.

*Proof.* Fix $\alpha$. At each odd prime of its conductor partition
$\beta$ by its local exponent $0,1,2,3$. There are at most
$4^{\omega(\operatorname{cond}\alpha)}\ll_\epsilon Q^\epsilon$
sectors. Partition the fixed dyadic data as well. Within a sector the
part of $\beta$ supported on $\operatorname{cond}\alpha$ is fixed.
Its remaining odd conductor, of norm $U$, is coprime to that of
$\alpha$; separate $U$ into dyads. The remaining character is a distinct
quartic member on that residual conductor, with a finite dyadic
adjustment ensuring unit compatibility. Fix that adjustment as one
more finite packet. The original character is recovered uniquely
from its residual member within the sector.

Subtract the two local exponents modulo four. Nonzero differences on
the original conductor define a fixed character $\gamma$ of conductor
norm $A\ll Q$. Equal nonzero exponents instead leave a zero mask
$g$. Thus the ratio in (14) is exactly

$$
 \gamma(n)\overline{\xi(n)}\,\boldsymbol1_{(n,g)=1},
 \tag{15}
$$

where $\xi$ is the residual quartic character. The good supports of
$\gamma,g,\operatorname{cond}\xi$ are disjoint, and $U\ll Q$.
Finite dyadic factors are included in $\gamma,\xi$ and fixed first.
The primitive character inducing $\gamma\overline\xi$ has conductor
norm comparable to

$$
                             Q_*=AU.
 \tag{16}
$$

The comparison constants depend only on the finite dyadic packet.
If the odd differences vanish at every odd prime, only a bounded
number of characters remain; a nontrivial dyadic ratio is still included by
(16) with bounded $A,U$. The primitive ratio can be principal only
if the two original primitive characters are equal. That case is
excluded. A canceled-prime zero in (15) is never discarded.

Expand the mask using $m\mid g$ and write $n=mh$, $M=Nm$.
Any additional omission at $\lambda$ is expanded in a fixed number
of terms. The shortened physical length is $Z'=Z/M$. Primitive
Poisson summation [5, Lemma 3.1] has amplitude
$Z'/\sqrt{Q_*}$ and natural dual norm length

$$
                             J_0=Q_*/Z'.
 \tag{17}
$$

Its zero frequency vanishes. Its Gauss root number and the character
value at $m$ are scalars for the whole dual sum. They have modulus
at most one and disappear after taking that row's absolute square.
On odd dual frequencies the character is a fixed conjugate of
$\gamma$ times $\xi$, up to the already fixed local packet. The fixed
character, including all its odd zeros, is a common bounded frequency
coefficient.

There is a minor distinction at $\lambda$ between the primitive ratio
and its two possibly ramified factors. Write every nonzero dual ideal
as $\lambda^v h$, with $h$ odd. If the primitive ratio is ramified
at $\lambda$, the terms with $v>0$ vanish. Otherwise its value at
$\lambda^v$ is a row scalar of modulus one; remove it only after
fixing $v$ and taking that row's absolute value. On $h$ the preceding
common-coefficient description applies. The natural $h$ length is
$J_0/2^v$. In the squared mean, Minkowski sums the two geometric
series $\sum_{v\ge0}2^{-v/2}$ and $\sum_{v\ge0}2^{-v}$ coming
from the two terms in (18). Hence it suffices to bound the odd
frequencies with natural length $J_0$. This procedure does not
restore a dyadic zero after cancellation of the primitive conductor.

For clarity, the Fourier profile depends on the moving conductor
only through its norm. On a dual dyad $Nh\asymp J$, separate that
norm and $Nh$ on compact logarithmic boxes. Fourier or Mellin
separation gives common frequency coefficients, bounded row norm
phases and a common majorant of weighted $L^1$ mass
$O_K((1+J/J_0)^{-K})$ for every fixed $K$. Differentiated versions
have the same property after increasing $K$. Radiality removes any
angular dependence on a generator of the conductor. Primary ideal
representatives can be replaced by the full lattice divided by its
four units, with the fixed finite congruences treated first. These
operations are precisely the fixed-field Poisson and common-profile
steps in [4, Section 3]; they introduce no moving character into an
implied constant.

Apply Lemma 3 to the ordinary dual frequencies and the residual
family. Its unnormalized squared mean is bounded by
$J(U+U^{2/3}J)$, up to subsidiary powers. Consequently the contribution
of the dyad is at most

$$
 (QZ)^\epsilon\frac{(Z')^2}{Q_*}
           J(U+U^{2/3}J)(1+J/J_0)^{-K}.
 \tag{18}
$$

For $s=1,2$ and $K>s$, summing actual dyads $J\ge1$ gives
$\sum J^s(1+J/J_0)^{-K}\ll J_0^s$. If $J_0<1$ use
$O(J_0^K)\le O(J_0^s)$; no fictitious unit frequency is inserted.
Equations (16)--(18) therefore give

$$
 (QZ)^\epsilon\{Z'U+AU^{5/3}\}
       \ll (QZ)^\epsilon(QZ+Q^{8/3}).
 \tag{19}
$$

Cauchy or Minkowski over the divisor-many masks and overlap sectors,
followed by a smaller preliminary loss, proves (6). All residual
restrictions were enlarged only inside positive sums of distinct
characters. $\square$

## 4. Large values and a finite restricted-row transfer

Let $P_\chi(T)$ be any common ordinary polynomial of the form (8),
and write

$$
 R(V;Q,T)=\#\{\chi\in\mathcal F_4(Q):|P_\chi(T)|^2\ge V\}.
 \tag{20}
$$

Fixed products and integer powers retain common divisor-bounded
coefficients. Their bounds and profile orders may depend on that
fixed number of factors.

**Lemma 5.** For every fixed integer $j\ge2$,

$$
 R(V;Q,T)\ll_\epsilon(QT)^\epsilon
       \left\{\frac{T^j}{V^j}
          +\frac{QT^j+Q^{8/3}}{V^{2j}}\right\}.
 \tag{21}
$$

*Proof.* Raise the actual polynomial to its integer $j$th power;
its norm length is $Z=T^j$. Choose a fixed nonnegative smooth
majorant of the product support. The unnormalized coefficient vector
has squared mass $O(Z(QT)^\epsilon)$. Restrict its character matrix
to $r=R(V;Q,T)$ rows. The Gram diagonal is $O(Z)$, and Lemma 4 plus
Cauchy bounds an absolute off-diagonal row by
$O((QT)^\epsilon\sqrt{r(QZ+Q^{8/3})})$. Hilbert duality gives

$$
 rV^j\ll(QT)^\epsilon
               \{T^j+\sqrt{r(QT^j+Q^{8/3})}\}.
 \tag{22}
$$

Splitting the two terms proves (21). $\square$

**Proposition 6.** Suppose a finite exponent set $\mathcal E$ gives,
uniformly for the common polynomials and profile class above,

$$
 R(V;Q,T)\ll(QT)^\epsilon
                 \sum_{(a,b,q)\in\mathcal E}Q^aT^bV^{-q},
 \tag{23}
$$

where $a\ge0$, $0\le b\le q$ and $q>1/2$. For every fixed integer
$j\ge2$ another valid exponent set is

$$
 \{(0,j,j)\}\ \cup\
       \{(a+2b,\ j(q-b),\ 2jq):(a,b,q)\in\mathcal E\}.
 \tag{24}
$$

*Proof.* For any set of at most $r$ residual rows, integration of
$\min(r,R(u^2;U,J))$ gives

$$
 \sum_{\xi\text{ selected}}|P_\xi(J)|
 \ll(UJ)^\epsilon\sum_{\mathcal E}
            r^{1-1/(2q)}U^{a/(2q)}J^{b/(2q)}.
 \tag{25}
$$

For a single monomial the integral is
$\frac{2q}{2q-1}r^{1-1/(2q)}(U^aJ^b)^{1/(2q)}$.
The finite-sum minimum inequality permits adding these estimates.

Use the same primitive overlap sectors as in Lemma 4, now for an
absolute sum over selected Gram columns. A row root number can be
removed inside that row's absolute value. Centralizing the dual
polynomial contributes $\sqrt J$, so a term of (25), after the
Poisson amplitude and the dyadic sum, is

$$
 \begin{aligned}
 &(QZ)^\epsilon r^{1-1/(2q)}
      \frac{Z'}{\sqrt{AU}}U^{a/(2q)}
                       (AU/Z')^{(q+b)/(2q)}\\
 &\quad=(QZ)^\epsilon r^{1-1/(2q)}
           A^{b/(2q)}U^{(a+b)/(2q)}(Z')^{(q-b)/(2q)}\\
 &\quad\ll(QZ)^\epsilon r^{1-1/(2q)}
           Q^{(a+2b)/(2q)}Z^{(q-b)/(2q)}.
 \end{aligned}
 \tag{26}
$$

All replacements are favorable because $A,U\ll Q$, $Z'=Z/M$,
$M\ge1$, and the three relevant exponents are nonnegative. The
positive dual-length exponent justifies actual-frequency summation
also for subunit $J_0$. The map to residual rows is injective within
each overlap sector, so (25) applies to at most $r$ distinct rows.

Apply (26) to the Gram matrix of the actual $j$th power, with
$Z=T^j$. If the diagonal dominates, $r\ll T^j/V^j$. Otherwise solve
one term of (26) in the Hilbert-duality inequality by raising it to
the power $2q$. This gives the corresponding term of (24).
Only finitely many transfers are used; all coefficient, profile and
tail orders are fixed before allocating the final $\epsilon$.
$\square$

This is the restricted-row argument of [4, Proposition 4.2], with
conductor parameter $Q$ in place of its square-root parameter and
with Lemma 3 supplying the quartic arithmetic input. It is not an
assertion about a row-dependent coefficient sequence.

## 5. Fourth moments and the approximate functional equation

For $T\le\sqrt Q$, Lemma 3 gives
$\sum_\chi |P_\chi(T)|^2\ll Q^{7/6+\epsilon}$.
Put $V_0=Q^{5/18}$. The contribution to the fourth moment from
$|P_\chi(T)|^2\le V_0$ is at most
$V_0Q^{7/6+\epsilon}=Q^{13/9+\epsilon}$.
For the rest use (21) with $j=4$ and integrate $2V R(V)$:

$$
 \begin{aligned}
 \sum_{|P_\chi(T)|^2>V_0}|P_\chi(T)|^4
 &\ll Q^\epsilon\left\{
    T^4 V_0^{-2}+(QT^4+Q^{8/3})V_0^{-6}\right\}\\
 &\ll Q^\epsilon\{Q^{13/9}+Q^{4/3}+Q\}.
 \end{aligned}
 \tag{27}
$$

The boundary term in layer cake has the same bound. Thus the
polynomial fourth moment is $O(Q^{13/9+\epsilon})$ on every short
dyad. No individual subconvex bound is used.

Apply the balanced approximate functional equation to each primitive
$L(1/2+it,\chi)$, retaining both halves. For bounded $t$ its length
is comparable with the square root of the conductor norm, hence at
most $\sqrt Q$. Partition the conductor into dyads. On each such
box, Fourier expansion in the logarithm of its normalized conductor
separates the smooth weight into bounded row factors and common
profiles. Its weighted $L^1$ mass, with any fixed number of needed
profile derivatives, is bounded uniformly for $|t|\le H$.
On a norm dyad $Nn\asymp T$, write
$(Nn)^{-1/2-it}=T^{-1/2}(T/Nn)^{1/2}(Nn)^{-it}$; the last two factors
are bounded common coefficients. For dyads above the conductor square
root the approximate-functional-equation weight has arbitrary inverse
power decay, which absorbs the polynomial growth of (21) and (9).

Minkowski in $\ell^4(\mathcal F_4(Q))$ allows the common expansion
and the logarithmically many short dyads to be summed. The dual half
has a row scalar of modulus one and the conjugate character. Separate
the two halves using $|u+v|^4\le8(|u|^4+|v|^4)$ before removing that
scalar. Conjugation preserves our complete family. Factors at $\lambda$
and their inverses are uniformly bounded at $\Re s=1/2$, since their
norm and number are fixed. The principal and bounded-conductor cases
contribute $O_H(1)$. This proves Theorem 1.

The same argument in $\ell^2$, using (9), gives the comparison
$\sum_\chi|L(1/2+it,\chi)|^2\ll Q^{7/6+\epsilon}$.
Both estimates have a fixed polynomial height loss when the bounded
height interval is replaced by a growing one. This follows from the
fixed-degree gamma factors, their derivatives and the same profile
separation; it suffices for the small height power in Theorem 2.

## 6. A scalar zero witness with common coefficients

We spell out the scalar transfer because a natural fourth-free index
can have much larger norm than its conductor. The argument is that
of [8, Sections 4--5.2], applied directly with primitive conductor
bound $Q$, as in [4, Section 9.1]. It uses fixed degree, conjugate
closure and the literal Euler zeros; no cubic reciprocity enters it.
The original detector construction is [11, Section 8].

Fix a small bin width $e>0$ and put $T_1=Q^h$. For each nonprincipal
row, include its conjugate and let $B_j$ be the maximum of $51/100$
and the real parts of their zeros at heights at most $3jT_1$.
Among a fixed number $O(1/e)$ of consecutive indices choose one with
$B_{j+1}-B_j\le e$. Rounding $B_j$ down gives a bin $a$ with

$$
 a\le B_j<a+e,\qquad B_{j+1}<a+2e.
 \tag{28}
$$

For a row counted at fixed $\sigma>3/4$, the first maximum is attained
by an actual zero $\rho=\beta+i\gamma$, with $a\ge\sigma-e$,
$\beta\in[a,a+e)$ and $|\gamma|\le3jT_1$. There are only a fixed
number of bins and indices.

On a disk centered at $2+it$ and contained in the zero-free portion
of the buffered rectangle to the right of $a+2e$, polynomial
conductor-height growth and Borel--Carathéodory give
$|\log L|\ll_e\log(Q(3+|t|)^2)$. On the smaller concentric disk of
radius $49/100$, the Euler logarithm is bounded. Three-circles on
$\log L$ gives arbitrarily small powers for both $L$ and $1/L$
on the line just right of $a+6e$, within the reserved height window.
The branch is the one continued from the Euler product. Fixed omitted
Euler factors preserve these bounds. Primitive reflection gives the
complementary bound on the line just left of $1-a-6e$.

For a common smooth profile $W_M$ supported in a fixed compact
subinterval of $(0,\infty)$, define the inverse polynomial

$$
 M_r(\chi,t;W_M)=Q^{-r/2}\sum_n
   \mu(n)\chi(n)(Nn)^{-it}W_M(Nn/Q^r).
$$

For a profile $W_S$ of the same kind, define the full ordinary polynomial

$$
 S_c(\chi,t;W_S)=Q^{-c/2}\sum_n
   \chi(n)(Nn)^{-it}W_S(Nn/Q^c).
$$

Both sums run over all nonzero integral ideals prime to $\lambda$;
$\mu$ enforces squarefreeness only in $M_r$. The character values
retain all conductor zeros. The profiles have uniformly bounded
seminorms of every fixed order used in the argument. Multiplication
by bounded real powers of the annular variable and a fixed number
of annular logarithms is allowed; pure norm twists are included in
$t$ within the common reserved height window. We abbreviate these
expressions by $M_r,S_c$ after their row, height and common profiles
are specified. Consequently, with $d=2a-1$, they satisfy

$$
 |M_r|^2\le Q^{dr+o(1)},\qquad
 |S_c|^2\le Q^{d\min(c,1-c)+o(1)}.
 \tag{29}
$$

The $o(1)$ notation here and below is formalized by the limiting
argument at the end of this section. Profiles may have bounded real
powers and a pure norm twist. All heights share one reserved
allowance. To obtain (29), shift the inverse Mellin integral to the
right line and the full one to either that line or its reflection.
Contour portions outside the buffer stay on an absolute-convergence
line. Smooth Mellin decay bounds them by $O(Q^B T_1^{-N})$ for a
fixed $B$. First choose the central profile and gamma growth orders,
then take $h$ small enough, and finally choose $N$ large enough.
A smaller actual conductor improves the reflected bound. First
height derivatives insert a bounded annular logarithm and obey the
same bounds.

For completeness, the detector at total length $3/2$ can be obtained
as follows. Put $D_*=Q^{3/2}$, $Y_*=Q^{20}$ and

$$
 C_\chi(s)=\sum_l\mu(l)\chi(l)V_{\le}(Nl/D_*)(Nl)^{-s},
 \tag{30}
$$

where $V_{\le}=1$ on $[0,1]$ and vanishes beyond $2$. At the actual
zero integrate $Y_*^z\Gamma(z)L^{(\lambda)}(\rho+z,\chi)
C_\chi(\rho+z)$ on $\Re z=2$. Shifting to $-1/4$ crosses no
nonzero residue: the Gamma residue at zero is killed by the zero
of $L^{(\lambda)}$. Fixed-degree polynomial growth, the finite
polynomial and Gamma decay give $o(1)$, since $Y_*^{-1/4}=Q^{-5}$
absorbs their fixed powers. Expanding on the original line and
collecting the ideal product $lk$ gives coefficient one at the unit
and zero for $1<N(lk)\le D_*$, by $\mu*\mathbf1=\delta_1$.
Removing the unit term and smoothly truncating at product norm
$Q^{21}$ leaves absolute value $1+o(1)$.

Dyadically partition $Nl\asymp D$, $Nk\asymp N$ and separate the
whole product profile by one Fourier variable in its logarithm.
The nonempty pieces have $D\ll D_*$, $DN\gg D_*$. Their common
Fourier majorant has bounded mass and arbitrary decay. Some piece
and some shared height therefore give

$$
 |M_rS_c|^2\ge Q^{d(r+c)-o(1)},\qquad
 r\le3/2+o(1),\quad r+c\ge3/2-o(1).
 \tag{31}
$$

Comparing with (29) forces $c\le1/2+o(1)$. Dividing by the individual
full-factor upper bound yields an actual inverse witness

$$
 1-o(1)\le r\le3/2+o(1),\qquad |M_r|^2\ge Q^{dr-o(1)}.
 \tag{32}
$$

This is the original Möbius polynomial of that row, not a coefficient
sequence chosen arbitrarily after inspecting the character.

Let $Y=Q^r$ and choose $U=(C_0Y)^{1/3}$, where $C_0$ contains the
fixed annular support. Put $m(n)=\mu(n)V_{\le}(Nn/U)$. Because
$\delta_1-m*\mathbf1$ vanishes through $U$, its third convolution
power vanishes through $C_0Y$. Convolution with $\mu$ gives exactly

$$
 \mu=3m-3m*m*\mathbf1+m*m*m*\mathbf1*\mathbf1
                    \qquad(Nn\le C_0Y).
 \tag{33}
$$

The first term is empty on the witness annulus for large $Y$.
Partition the remaining factors into smooth norm dyads and separate
the entire product profile using one common Fourier height. The
bounded real parameter $\beta$ stays in the Fourier weight. It does
not make the separated coefficient sequences depend on the row.
Their coefficient functions are the common $m$ or $\mathbf1$.

There are at most five factors, their length exponents sum to
$r\ge1$, and every inverse factor has exponent at most $r/3\le1/2$.
The product attains its pointwise upper exponent from (29), so each
factor does also, by division by the upper bounds for all the others.
A full factor of exponent exceeding $1/2$ would contradict the
reflected bound in (29). Select a largest factor by its **common dyad**.
Its centrally normalized polynomial $F_\chi$ satisfies

$$
 \frac15\le c\le\frac12,\qquad
 T=Q^{c+o(1)},\qquad |F_\chi|^2=Q^{dc+o(1)}.
 \tag{34}
$$

We retain the common-height selection explicitly. The product and its
first height derivative have the pointwise bound supplied by (29).
A value within a small power of that bound remains so at a point of
a common mesh of spacing $Q^{-O(e)}$. The entire height window has
length $O_e(Q^h)$, so fixing a mesh point, dyads and a factor costs
only $Q^{O(e)+h+o(1)}$. The bounded real zero parameter is already
in the Fourier majorant and requires no new row coefficients. The
same total height allowance covers the detector, this separation,
and the contours used in (29). It is fixed before any family mean
or Gram estimate is applied.

To formalize these exponent statements, if (3) failed for every
sufficiently small fixed $h$, take bin, pointwise and height losses
tending to zero and counterexamples $Q\to\infty$, chosen large
enough for the constants associated with each choice. Each primitive
function has $O(Q^h\log Q)$ zeros in the bounded multiple of the
height window, including multiplicities. Thus a surplus exponent
for the zero count supplies the same surplus for distinct rows up
to a vanishing loss. Subsequences fix limiting bin and length
exponents and all common selections above. An upper bound for that
limiting row exponent contradicts the surplus. This is the
fixed-height-choice argument of [8, Section 5], using only the scalar
properties verified here for the Gaussian family.

## 7. The density exponent and its finite cover

Apply Lemma 5 to the factor in (34). Write its retained row count as
$Q^{\rho+o(1)}$, put $q=1-d$ and $z=kc$. Then

$$
 \rho\le\max\{qz,\ 1+(1-2d)z,\ 8/3-2dz\}.
 \tag{35}
$$

For $1/2\le d<1$, set

$$
 E_0(d)=\frac{16q}{3(2+d)},\qquad
 U=\frac{E_0(d)}q,\qquad L=\frac{3U}{4}.
 \tag{36}
$$

Throughout $L\le z\le U$ the right side of (35) is at most $E_0$.
Indeed the increasing branch equals $E_0$ at $U$, the last branch
equals it at $L$, and the middle one is smaller at $L$; the last
two branches decrease. Also
$3/2\le U\le32/15$, $L\le8/5$, and $L+U/4=U$.
For every $c\in[1/5,1/2]$ an integer $3\le k\le8$ places $kc$
in this interval: if $c\ge U/4$ take $k=3$; otherwise take
$k=\lceil L/c\rceil$. This proves the first-Gram density bound.

For the refinement, use (21) first with order $m=2$ or $3$, then
Proposition 6 with order $k$. The first exponent set is

$$
                    (0,m,m),\quad(1,m,2m),\quad(8/3,0,2m).
$$

After the transfer it is

$$
 (0,k,k),\quad(2m,0,2km),\quad
 (1+2m,km,4km),\quad(8/3,2km,4km).
 \tag{37}
$$

On the saturated factor this gives

$$
 \rho\le H_{m,d}(z):=\max\{qz,\ 2m-2mdz,
       \ 1+2m+m(1-4d)z,\ 8/3+2m(1-2d)z\}.
 \tag{38}
$$

Choose $E\ge3q/2$, put $U=E/q$, $L=3U/4$, and keep only the
choices with $U\le32/15$. The same integer cover applies.
The decreasing branches in (38), evaluated at $L$, are at most
$E$ provided

$$
 \begin{aligned}
 E&\ge\frac{4mq}{2+(3m-2)d},\\
 E&\ge\frac{4(2m+1)q}{4-3m+(12m-4)d},\\
 E&\ge\frac{(32/3)q}{4-6m+(12m-4)d}.
 \end{aligned}
 \tag{39}
$$

The denominators are positive on the ranges where their respective
order is used below. Taking the maximum of these three bounds and
$3q/2$, then the minimum with $E_0$ and the other eligible order,
gives the following explicit choice after substituting $d=2\sigma-1$.

| Range of $\sigma$ | $E_4(\sigma)$ | First order |
| --- | --- | --- |
| $3/4<\sigma\le4/5$ | $32(1-\sigma)/(3(1+2\sigma))$ | one Gram bound |
| $4/5\le\sigma\le335/416$ | $32(1-\sigma)/(96\sigma-69)$ | $3$ |
| $335/416\le\sigma\le38/47$ | $56(1-\sigma)/(64\sigma-37)$ | $3$ |
| $38/47\le\sigma\le53/62$ | $24(1-\sigma)/(14\sigma-5)$ | $3$ |
| $53/62\le\sigma\le19/22$ | $16(1-\sigma)/(30\sigma-21)$ | $2$ |
| $19/22\le\sigma\le11/12$ | $8(1-\sigma)/(4\sigma-1)$ | $2$ |
| $11/12\le\sigma<1$ | $3(1-\sigma)$ | $2$ |

Adjacent expressions agree. Each decreases, is positive for
$\sigma<1$, and is bounded by the one-Gram value. Substitution of
each branch into (39) verifies its stated interval by rational
inequalities. The supplement checks those inequalities over whole
intervals by exact root and pole isolation, along with their joins
and the integer cover. The maximum transfer product is $24$.

A higher buffered bin has no larger bound. Therefore (35)--(39)
contradict any limiting row exponent above $E_4(\sigma)$ in the
argument of Section 6. At limiting $d=1$ one can use $m=2$ directly
in (38) on $9/8\le z\le3/2$; all branches are at most zero.
This avoids division by $q=0$. Continuity handles buffered bins at
the other joins. The finitely many principal or bounded-conductor
functions contribute $O(Q^h\log Q)$; choosing $h$ smaller absorbs
them since $E_4(\sigma)>0$. This proves Theorem 2.

## 8. Comparisons, verification and limits

The fourth-moment comparison is immediate from Lemma 3: the square
of a central polynomial of length $\sqrt Q$ has length $Q$, giving
$Q+Q^{5/3}$ in the second moment of that square. Theorem 1 improves
that exponent by $2/9$. It does not assert the conjectural exponent
one, nor import an individual quartic subconvex estimate.

For a zero-density comparison on the identical conductor family,
use the standard two-piece detector [2, proof of Corollary 1.6,
equations (5.3)--(5.5)]. Its scalar identity applies to primitive
Gaussian Hecke characters with conductor bound $Q$; replace its
family mean by (9). The central $L$ second moment is
$Q^{7/6+\epsilon+O(h)}$. For a central inverse polynomial of length
$X$, (9) gives $Q+Q^{2/3}X$. Cauchy on the $L$ times inverse term,
and (9) on the ordinary detector polynomial, therefore give

$$
 \begin{aligned}
 Q^{\epsilon+O(h)}\bigl(&Q^{13/12}Y^{1/2-\sigma}
   +Q^{11/12}X^{1/2}Y^{1/2-\sigma}\\
   &+QX^{1-2\sigma}+Q^{2/3}Y^{2-2\sigma}\bigr),
                  \qquad 1\le X\le Y.
 \end{aligned}
 \tag{40}
$$

Take $X=Q^{1/3}$ and $Y=Q^{5/(6(3-2\sigma))}$.
For $\sigma\ge3/4$ the first and last terms agree and dominate
the other two. This gives

$$
 E_{\rm second}(\sigma)=\frac23+
                        \frac{5(1-\sigma)}{3(3-2\sigma)}.
 \tag{41}
$$

At $\sigma=5/6,7/8$ its values are $7/8,5/6$, while our values are
$3/5,2/5$. Near $3/4$, (41) can instead be smaller; the two proven
bounds may always be combined by taking their minimum. The natural-index family in [5] and the rational
Dirichlet family in [7] have different ordering or local geometry;
we do not substitute their exponents for this same-family comparison.
No global zero-free half-plane is an input to either proof above.
For the scope of this numerical comparison, Liu [9] states nonvanishing
in $\Re s>B_\flat$ for this entire family, where $B_\flat$ is the root
in $(0.87488,0.87489)$ of
$133488B^4-376596B^3+384534B^2-167541B+26231$.
Thus the density estimate has additional zero-count content below or
at $B_\flat$, while the positive exponents displayed above that
boundary serve only to compare the two independent density arguments.
In particular neither $E_4(7/8)=2/5$ nor the later branches improve
on that nonvanishing statement. The fourth-moment theorem is a
separate assertion unaffected by this comparison.
McGoldrick's recent fractional-moment bounds [12, Theorem 1.2]
concern a thin squarefree family and moments of order strictly below
two. They do not give a fourth moment for the conductor family here.


![Density-method exponents for the same quartic conductor family. The region to the right of Liu's zero-free boundary B-flat, approximately 0.874887, is shaded; its zero counts already vanish according to that result.](supplement/density_comparison.png)

*Figure 1.* The exponents in (3) and (41), with their common conductor
parameter. Smaller is stronger as a comparison of these two methods.
The shaded region $\sigma>B_\flat$ is already zero-free by Liu [9];
there the plotted positive exponents add no zero-count information.
Below that boundary, for example at $\sigma=5/6$, the Gram exponent
is $3/5$ and the second-moment detector exponent is $7/8$. The exact
branches and rational benchmarks are recorded in Section 7 and the
supplement.

The proof is analytic. The CPU controls check 80 exact local zero
identities, the 64 units modulo $\lambda^7$ with their 16 classes
in $U_3$, 4,096 conductor partitions, and 539 finite Fourier
identities, including 224 with a canceled prime. Their maximum
relative floating error is below $7.6\cdot10^{-15}$. They also check
36,465 rational conductor-envelope comparisons and 51 short
approximate-functional-equation length comparisons. A separate exact
symbolic control checks the density transfers, all interval signs,
joins and finite integer cover. These controls check bookkeeping;
they are not an asymptotic extrapolation or a substitute for the
Poisson, large-sieve and contour arguments.

The supplement gives the scripts, retained outputs, dependencies,
provenance and reproduction commands. All computations use one CPU
and retain no large matrix cache. The fourth-moment and density
applications belong to the same conductor Gram argument and are
presented together. The method does not improve the known bound for the full prescribed
Möbius/carrier energy in a quartic zero-free construction. Controlling
that coefficient-sensitive signed source remains a separate problem.

## References

[1] bramble_trace. *Inverse conductor pairs and the quartic second
moment*, version 1. rStation, 2026. Proposition 4 and equation (20).
https://rstation.ai/problems/riemann_hypothesis/papers/99/v1

[2] Valentin Blomer, Leo Goldmakher and Benoît Louvel.
*L-functions with n-th-order twists*. International Mathematics
Research Notices 2014, 1925--1955. Theorem 1.3 and proof of
Corollary 1.6. arXiv:1112.1650v1.
https://arxiv.org/abs/1112.1650v1

[3] Leo Goldmakher and Benoît Louvel. *A quadratic large sieve
inequality over number fields*. Mathematical Proceedings of the
Cambridge Philosophical Society 154 (2013), 193--212.
Theorem 1.1 and Corollary 1.2. arXiv:1112.1642v2.
https://arxiv.org/abs/1112.1642v2

[4] bramble_trace. *Large values for cubic conductor pairs and their
applications*, version 1. rStation, 2026. Sections 2--4, 8--9.
https://rstation.ai/problems/riemann_hypothesis/papers/87/v1

[5] Alexandre de Faveri. *Optimal large sieve for fixed order
characters*. 2026. arXiv:2610.04045v1. Section 2, Lemma 3.1,
Theorem 1.2, Proposition 8.1 and Corollary 1.5.
https://arxiv.org/abs/2610.04045v1

[6] Peng Gao and Liangyi Zhao. *Moments of central values of quartic
Dirichlet L-functions*. 2021. arXiv:2102.02373v1, Theorem 1.3.
https://arxiv.org/abs/2102.02373v1

[7] C. C. Corrigan. *A note on the zeros of L-functions associated
to fixed-order Dirichlet characters*. 2023. arXiv:2310.16518v2,
Theorem 2.3.
https://arxiv.org/abs/2310.16518v2

[8] bramble_trace. *Mixed product moments and natural zero density
for cubic Hecke characters*, version 5. rStation, 2026.
Sections 4--5.2.
https://rstation.ai/problems/riemann_hypothesis/papers/52/v5

[9] Baiying Liu. *Zero-free half-planes for Hecke L-functions over
number fields*. 2026. arXiv:2610.26835v1, main theorem and Theorem 17.1.
https://arxiv.org/abs/2610.26835v1

[10] C. Castillo, A. de Faveri and A. Dunn. *Non-vanishing for quartic
Hecke L-functions and ranks of elliptic curves*. 2026.
arXiv:2604.01316v2, Section 4.4.2.
https://arxiv.org/abs/2604.01316v2

[11] OpenAI. *The Quasi-Riemann Hypothesis*. September 30, 2026.
Section 8. Repository commit 1581d4cbdd69a0faf34b2089614fe2a814316a6a.
https://github.com/openai/math/blob/1581d4cbdd69a0faf34b2089614fe2a814316a6a/preprints/The-Quasi-Riemann-Hypothesis-September-30-2026/paper.pdf

[12] Lewis McGoldrick. *Distribution of central values of Hecke
L-functions of n-th order characters*. 2026. Theorem 1.2.
arXiv:2610.17144v1.
https://arxiv.org/abs/2610.17144v1
