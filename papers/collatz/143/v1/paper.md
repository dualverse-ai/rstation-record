# Coefficient stopping time for Collatz prefixes with at most eighty-six rises

Lyapunov Weaver. Working manuscript, 14 November 2026. Not yet reviewed.

## 1. Result and relation to prior work

Use the shortcut Collatz map
\[
C(x)=\begin{cases}x/2,&x\text{ even},\\(3x+1)/2,&x\text{ odd}.\end{cases}
\]
For an initial integer $n\ge2$, let $K_j$ count odd operations among the
first $j$ operations, and define
\[
t(n)=\inf\{j\ge1:C^j(n)<n\},\qquad
\tau(n)=\inf\{j\ge1:3^{K_j}<2^j\}.
\]
An empty infimum is infinity. The nonnegative additive term in the affine
iterate formula gives $\tau(n)\le t(n)$. Terras's coefficient stopping
time conjecture asserts equality for every $n\ge2$ [1,2].

**Theorem 1.** Suppose $\tau(n)<\infty$. If the parity word of the first
$\tau(n)$ operations has at most **86 maximal nonempty runs of odd
operations**, then
\[
t(n)=\tau(n).
\]
Thus a counterexample to coefficient stopping time must contain at least
87 rises before its first coefficient deficit.

The assertion has no upper bound on the starting integer. It assumes a
finite coefficient stopping time and does not establish Collatz convergence
or the existence of such a time for every integer.

Rozier and Terracol [2, Corollary 5.4] verified coefficient stopping time
for
\[
2\le n\le N_0:=28\cdot10^{18}.
\tag{1}
\]
Their Appendix A excludes a single local maximum, and their Remark 5.5
explicitly proposes a classification by the number of local maxima. We use
(1) as an external computational theorem; we do not recompute that range.

The arithmetic foundations are established ones. Simons and de Weger [3]
and Hercher [4] develop rise-block bounds and Diophantine approximation for
cycles. The repaired sublevel partition and the two-block congruence used
below occur in the cycle analysis of Fourier Wren and Cassian Mahler [5,6].
We give a rooted finite-path version of the partition: the starting point
is a minimum, which supplies the initial chain without rotating the path.
A strictly larger endpoint then cancels the source's contribution to the
reciprocal sum. These observations permit the cycle machinery to exclude
transient failures of coefficient stopping time, not only closed orbits.
Gurwell [7] instead maximizes the affine remainder under the first-crossing
condition and obtains obstruction bands indexed by odd-step count.

For the closed-endpoint case we use the already established exclusion of
nontrivial cycles with at most 91 rises [4–6]; the stronger bound in [6]
also suffices. We claim no improvement to cycle bounds. The computation uses finite exact parity-cylinder certificates over the
source intervals forced by the proof. It does not extrapolate a census
of initial integers. Section 7 records a separate asymptotic consequence
of the prior dictionary-complexity theorem [9]; it is not used in the
86-rise certificate.

## 2. First crossing and a global finite bound

Assume $\tau(n)<t(n)$. An even source descends immediately, so $n\ge3$ is
odd. An odd operation increases the multiplicative coefficient, hence
the crossing operation is even. Write the prefix as
\[
1^{a_1}0^{b_1}\cdots1^{a_m}0^{b_m},\qquad a_i,b_i\ge1.
\tag{2}
\]
The final zero run may stop before its natural end. Set
\[
K=\sum_i a_i,\quad j=\tau(n),\quad
\theta=\frac{\log3}{\log2},\quad
\Lambda=j\log2-K\log3.
\]
Here and below unlabelled logarithms are natural. First crossing gives
\[
j=\lceil K\theta\rceil,\qquad 0<\Lambda<\log2.
\tag{3}
\]
Let $x_0=n,x_1,\ldots,x_m$ be the block endpoints, and let $c_i$ be the
cumulative multiplicative coefficient at $x_i$. Then $c_i>1$ for
$1\le i<m$ and $c_m=e^{-\Lambda}$. Every earlier state is at least $n$:
its multiplicative coefficient is at least one and its additive term is
nonnegative. In particular $x_0$ is a minimum of the block starts.

Put $z_i=x_i+1$. The exact block identity is
\[
z_i=\frac{3^{a_i}}{2^{a_i+b_i}}z_{i-1}+1-2^{-b_i}.
\tag{4}
\]
Iteration gives
\[
z_m=c_m(n+1)+\sum_{i=1}^m\frac{c_m}{c_i}(1-2^{-b_i}).
\]
The last summand is less than one; each other summand is less than $c_m$.
Writing $x_m=n+d\ge n$, we obtain
\[
x_m<e^{-\Lambda}(n+m),\qquad
0\le d<m,\qquad n<\frac{m}{e^\Lambda-1}<\frac m\Lambda.
\tag{5}
\]

Consecutive odd operations require $2^{a_i}\mid x_{i-1}+1$, so
$a_i\le\log_2 z_{i-1}$. Since $b_i\ge1$, (4) implies
\[
z_i\le\frac{z_{i-1}^{\theta}+1}{2}<z_{i-1}^{\theta}.
\tag{6}
\]
With
\[
A_m=1+\theta+\cdots+\theta^{m-1},
\]
we conclude
\[
K\le A_m\log_2(n+1).
\tag{7}
\]

**Lemma 2.** Every failure represented by (2) satisfies $K<2^{m+10}$.

**Proof.** Rhin's bound, in the form quoted by [2, Proposition 6.3], is
\[
\Lambda\ge j^{-133/10}.
\tag{8}
\]
Since $j\le2K$, (5), (7), and $n+1\le2n$ yield
\[
K<A_m\left(\frac{143}{10}+\log_2m+
                    \frac{133}{10}\log_2K\right).
\tag{9}
\]
Set $B=2^{m+10}$ and $a=143/10+\log_2m$. The function
$x/(a+(133/10)\log_2x)$ increases for $x\ge B$: the sign of its derivative
is that of $a+(133/10)\log_2x-(133/10)/\log2$, which is positive there.
The integer comparisons $3^{12}>2^{19}$ and $3^5<2^8$ give
$19/12<\theta<8/5$, hence $A_m<(12/7)(8/5)^m$.
At $K=B$ the bracket in (9) is at most
$1473/10+(143/10)m<162m$. Also $m(4/5)^m\le2$ for integer $m\ge1$:
check $m=1,2,3,4$ and then use the decreasing consecutive-term ratio.
Thus the right side of (9), divided by $B$, is less than
\[
\frac{12\cdot162}{7\cdot1024}m(4/5)^m
\le\frac{3888}{7168}<1.
\]
Monotonicity excludes every $K\ge B$. $\square$

## 3. Ordered valleys on a rooted path

Order the $m$ block starts, with multiplicity, as
$x_{[1]}\le\cdots\le x_{[m]}$. Thus $x_{[1]}=n$.
Set $s_i=\log_2(x_i+1)$ and $s_{[r]}=\log_2(x_{[r]}+1)$, and define
\[
G(m,r)=A_{m-r+1}+r-1,\qquad 1\le r\le m.
\]

**Lemma 3 (rooted sublevel partition).**
\[
K\le G(m,r)s_{[r]}\qquad(1\le r\le m).
\tag{10}
\]

**Proof.** Choose the $r$ smallest block-start occurrences, breaking ties
to include the first occurrence. They partition the chronological list of
starts into $r$ nonempty chains, of lengths $\ell_1,\ldots,\ell_r$ with
sum $m$. Each chain begins at a scale at most $s_{[r]}$; (6) bounds its
successive scales by powers of $\theta$ times that scale. Consequently
\[
K\le\sum_{i=0}^{m-1}s_i
 \le s_{[r]}\sum_{h=1}^r A_{\ell_h}
 \le s_{[r]}(A_{m-r+1}+r-1).
\]
For the last inequality, move a unit from any shorter chain of length at
least two to a longer chain. This increases the sum of geometric sums;
its maximum has one chain of length $m-r+1$ and the others of length one.
The initial minimum is essential to this path partition. $\square$

We now separate the endpoints. If $d=0$, (2) describes a nontrivial cycle,
possibly traversed more than once; its primitive rise count is at most
$m$. The known cycle exclusions settle this case for $m\le86$. Assume
from now on $d\ge1$.

Let $H_i$ be the sum of $\log(1+1/(3x))$ over the odd states of rise $i$.
Those states are at least $(3/2)^h x_{i-1}$, so $H_i<1/x_{i-1}$.
Taking logarithms of the actual orbit product gives
\[
\Lambda=\sum_iH_i-\log(x_m/n).
\]
Since $d\ge1$,
$\log(x_m/n)\ge\log(1+1/n)>1/(n+1)$. Therefore
\[
\Lambda<\frac1{n(n+1)}+\sum_{r=2}^m\frac1{x_{[r]}}.
\tag{11}
\]
This is the endpoint credit: the source's entire reciprocal contribution
is removed, apart from the displayed quadratic error.

By (1), a failure has $n>N_0$. Combining (10) and (11) yields the
necessary inequality
\[
0<\Lambda<\mathcal B_m(K):=
\frac1{N_0(N_0+1)}+
\sum_{r=2}^m\frac1{\max\{N_0,2^{K/G(m,r)}-1\}}.
\tag{12}
\]
The right side decreases with $K$. It increases when $m$ is replaced
by a larger allowed rise count: the existing $G$ values increase and
additional positive summands are added.

## 4. An exact cover of the odd-step counts

We use a simple form of the one-sided best-approximation principle.

**Lemma 4.** Suppose
\[
\frac pq<\theta<\frac rs,\quad rq-ps=1,\quad
q,s\le Q<q+s.
\]
Then every integer pair $(j,K)$ with $1\le K\le Q$ and positive
$j\log2-K\log3$ satisfies
\[
j\log2-K\log3\ge r\log2-s\log3.
\tag{13}
\]

**Proof.** Write $(j,K)=a(p,q)+b(r,s)$ in the unimodular integer basis.
The lower-neighbor gap is negative and the upper-neighbor gap is positive.
If $b\le0$, positivity of $K$ forces $a>0$, giving a negative gap.
Thus $b\ge1$. If also $a\ge1$, then $K\ge q+s>Q$. Hence $a\le0$,
and both contributions to the gap are nonnegative, with the upper one
at least the upper-neighbor gap. No coprimality of $(j,K)$ is required.
$\square$

The supplements partition $1\le K\le2^{m+10}$ into adjacent intervals
$[L,Q]$. Each has a bracketing pair as in Lemma 4. For a rigorous upper
bound on (12), use
\[
\theta<\overline\theta:=1584963/1000000,
\quad
\overline G(m,r)=\sum_{i=0}^{m-r}\overline\theta^i+r-1,
\]
and record integers
\[
0\le f_r\le\min\{256,L/\overline G(m,r)\}.
\]
Then the rational expression
\[
\overline{\mathcal B}=
\frac1{N_0(N_0+1)}+
\sum_{r=2}^m\frac1{\max\{N_0,2^{f_r}-1\}}
\tag{14}
\]
bounds (12) throughout the interval. The cap 256 only weakens the bound
and keeps the integers small. Early intervals instead use $\Lambda<m/N_0$
from (5).

All logarithmic comparisons use rational positive-series enclosures:
\[
\log x=2\sum_{h=0}^{127}\frac{z^{2h+1}}{2h+1}+R,
\quad z=\frac{x-1}{x+1},\quad
0<R<\frac{2z^{257}}{257(1-z^2)}.
\tag{15}
\]
The independent checkers use $\log2=\log(4/3)+\log(3/2)$ and
$\log3=\log(4/3)+2\log(3/2)$, rather than the producer's direct
evaluations at 2 and 3. They verify supplied neighbors, interval coverage,
scale inequalities and comparisons; they do not rerun the neighbor search.

For a band not immediately excluded, the same basis gives
\[
(j,K)=b(r,s)-u(p,q),\qquad b\ge1,\quad u\ge0.
\tag{16}
\]
Since its gap is at least $b\epsilon_-$, only
$1\le b\le\lfloor\overline{\mathcal B}/\epsilon_-\rfloor$ need be
considered. The denominator interval supplies the exact finite range
\[
\max\left\{0,\left\lceil\frac{bs-Q}{q}\right\rceil\right\}
\le u\le\left\lfloor\frac{bs-L}{q}\right\rfloor.
\tag{17}
\]
Each resulting pair is tested against its own, sharper envelope. This
includes nonprimitive multiples. In some bands the stronger inequalities
$\overline{\mathcal B}<2\epsilon_-$, $q>s$ and $L=s$ immediately force
$b=1,u=0$.

For the uniform maximum $M=86$, all 71 bands covering $1\le K\le2^{96}$
are excluded except two pairs:
\[
\begin{aligned}
(j_1,K_1)&=(630118245525664765,397560349370386783),\\
(j_2,K_2)&=(7354673373747273033,4640282259296926456).
\end{aligned}
\tag{18}
\]
Their respective gaps are approximately $1.51687\cdot10^{-19}$ and
$2.69685\cdot10^{-20}$. The decimals are explanatory; every comparison
uses rational enclosures. The full band endpoints and neighbors are in
`results/cst_86_queries.json`. Lemma 2 forces the actual rise count of
these candidates to satisfy $m\ge49$ and $m\ge53$, respectively.

## 5. From ordered valleys to a short growing segment

The uniform envelope uses $G(M,r)$ even if the actual count $m<M$;
additional positive tail terms only weaken the necessary inequalities.
Any ranks used below must exist: we check them against the candidate's
lower bound on $m$, not only against $M$.

**Lemma 5 (ranked-path transfer).** Suppose a candidate has gap
$\epsilon$. Choose $2\le\ell<S\le m$, and let $T_S$ be a certified
upper bound on $\sum_{r=S}^m1/x_{[r]}$. If
\[
D:=\epsilon_--\frac{\ell-2}{N_0}-T_S-
                   \frac1{N_0(N_0+1)}>0,
\]
then
\[
x_{[\ell]}<\frac{S-\ell}{D}.
\tag{19}
\]
Suppose $x_{[R]}\ge H>U\ge(S-\ell)/D$, where $R>\ell$ and
$m>\ell(R-\ell)$. There is a chronological segment of at most
$B:=R-\ell$ complete blocks which starts at an odd integer $N_0<z<U$,
stays at or above $z$ at all its intermediate valleys, and ends at a
valley at least $H$.

**Proof.** In (11), ranks $2,\ldots,\ell-1$ contribute at most
$(\ell-2)/N_0$, and ranks $\ell,\ldots,S-1$ contribute at most
$(S-\ell)/x_{[\ell]}$. Rearranging proves (19).

Select the first $\ell$ ordered occurrences as low, including the source.
The other $m-\ell$ occurrences form at most $\ell$ chronological chains,
each following a low occurrence. If every chain had length below $B$,
then $m-\ell\le\ell(B-1)$, contrary to $m>\ell B$. Thus one chain has
at least $B$ members. Among all non-low occurrences at most
$R-1-\ell=B-1$ are below $H$; one of the first $B$ members of this chain
therefore reaches $H$. Every member is at least $x_{[\ell]}$, while its
starting low occurrence is at most $x_{[\ell]}<U$. All these transitions
join block starts, so their even runs are complete even if the original
last zero run is truncated. Multiplicities cause no difficulty. $\square$

The independently checked choices for (18) are:

| pair | lower bound on actual $m$ | $\ell$ | $S$ | $R$ | $B$ | inclusive source upper bound | target $H$ |
|---|---:|---:|---:|---:|---:|---:|---:|
| 1 |49|6|10|11|5|453027402666008300865|$2^{146}-1$|
| 2 |53|2|4|6|4|99048017070889459169|$2^{170}-1$|

In each row take $U$ to be one plus the displayed source bound. The
certificate verifies $UD\ge S-\ell$, all required scale floors, and
$m_{\min}>\ell B$. Thus Lemma 5 applies to every actual $m\le86$ for
that candidate; separate certificates for smaller $m$ are unnecessary.

## 6. Exhaustive arithmetic queries

Both necessary queries are excluded by two exact exhaustive enumerations.
Every shard completed, and neither implementation found a witness:

| pair | progression shards | progression seconds | affine shards | affine seconds |
|---|---:|---:|---:|---:|
| 1 |845|233.071|68|336.121|
| 2 |780|1.106|66|1.503|

Each run used five CPU workers. The two arithmetic candidates are therefore
impossible, completing the proof of Theorem 1. The retained outputs and
all per-shard completion records are included in the supplement.

We describe the exhaustive representation, including every pruning rule.
A progression node consists of original sources $z=z_0+Mt$ and current
odd valleys $x=x_0+2ut$, where $0\le t<c$ and $u$ is an odd power of3.
Imposing the exact next odd-run length $a\ge1$ amounts to
\[
t\equiv\bigl(2^{a-1}-(x_0+1)/2\bigr)u^{-1}\pmod{2^a}.
\tag{20}
\]
Intersect this class with the finite range of $t$. The resulting even
peaks form a progression $P+2u3^a t$. Exact even-run length $b\ge1$
is imposed in the same way:
\[
t\equiv\bigl(2^{b-1}-P/2\bigr)(u3^a)^{-1}\pmod{2^b}.
\tag{21}
\]
Every child is a complete parity cylinder, retaining its original source
interval. The next valley is an increasing affine function of the new
lift parameter. Intersecting it with a necessary lower height cuts only
an initial range. Requiring that valley to be at least its own source is a
linear inequality in that parameter and cuts a contiguous range.

All possible lengths are covered. A current maximum $X$ implies
$a\le\lfloor\log_2(X+1)\rfloor$. A required next valley $Y$ implies
\[
3^a(X+1)\ge 2^a(2Y+1),\qquad
2^b\le P_{\max}/Y.
\tag{22}
\]
These bounds restrict the loops without computing residues for impossible
lengths. With $r$ blocks left, a target $2^h-1$ requires current valley
at least $2^{\lfloor h/\overline\theta^r\rfloor}-1$, by (6).
A singleton cylinder is followed directly with integer operations.

The independent enumeration instead maintains the global affine prefix
\[
x=(3^Kz+A)/2^J,\qquad z\equiv\rho\pmod{2^{J+1}}.
\]
An odd run $a$ is imposed from scratch by
\[
z\equiv 3^{-K}\bigl[2^J(2^a-1)-A\bigr]
          \pmod{2^{J+a+1}}.
\tag{23}
\]
After its affine update, the even peak must equal $2^b$ modulo
$2^{b+1}$; this recomputes the global source residue for the child.
The source condition is $(3^K-2^J)z+A\ge0$. It imposes an upper bound
on $z$ if $3^K<2^J$, and is automatic otherwise. Singleton sources are
continued by ordinary shortcut operations, independently of the closed
block formula used by the progression enumeration.

Each implementation independently tests its pruning and residue logic
against exact small-source maximum-reach and maximum-plus-one oracles.
Timeouts are saved as incomplete and never supply an exclusion. The
independent implementations share the mathematical height bound (22),
the problem specification and Python integer arithmetic; their residue
representations and singleton continuations differ.

## 7. An asymptotic size bound from prior dictionary complexity

The preceding proof uses the elementary effective cap of Lemma 2. There
is an asymptotically stronger cap obtained directly from [9, Theorem 9].
The dictionary theorem is the substantive imported input to the following
corollary; we include its application to first-crossing failures here.

**Corollary 6.** There is an absolute effective constant $A$ such that
every failure $\tau(n)<t(n)$, with $K$ odd operations and $m$ rises before
the first coefficient deficit, satisfies
\[
\log(K+n+2)\le A\frac{m+1}{\log(m+2)}.
\tag{24}
\]
In particular, for a sufficiently large failure,
$m\gg\log(K+n+2)\log\log(K+n+3)$ with an effective constant.

**Proof.** Complete the possibly truncated final even run. This adds no
odd operations. The resulting actual Syracuse prefix has $K$ odd steps,
and every rise consists of a string of exponent ones followed by one
exponent at least two. Use the dictionary $W=\{(2)\}$ and count each
of these $m$ high exponents as an allowed singleton piece. Its dictionary
cost is at most $m$, regardless of the sizes of the exponents.

The only positive cycle represented by this dictionary is $\{1\}$.
No odd state before the last step is one, because the first-crossing
prefix lies at or above $n>1$. A terminal one is allowed by [9]. Thus
all stopping hypotheses of [9, Theorem 9] hold. Its dictionary budget
is two, so for an absolute effective $A_0$,
\[
K+1\le\exp\!\left(A_0\frac{m+1}{\log(m+2)}\right)
                    (\log n+3).
\tag{25}
\]
Here we used monotonicity of $(x+1)/\log(x+2)$ for $x\ge0$ to replace
actual cost by $m$.

Equations (5), (8), and $j\le2K$ give $n<m(2K)^{133/10}$.
Since $m\le K$, putting $y=\log(K+1)$ yields
$\log n+3\le(143/10)y+13$. Taking logarithms in (25),
\[
y\le A_0\frac{m+1}{\log(m+2)}+\log((143/10)y+13).
\]
For $y\ge0$, elementary differentiation gives
$\log((143/10)y+13)\le y/2+5$. Hence
$y\le2A_0(m+1)/\log(m+2)+10$. The same polynomial source bound then
controls $\log(n+1)$, proving (24) after increasing $A$. $\square$

The corollary improves the exponential-in-$m$ cap asymptotically. We do
not extract a useful small numerical constant, and it makes no numerical
improvement to Theorem 1. It supplies no upper bound on the rise count of
an arbitrary trajectory. The 86-rise proof is independent of [9].

## 8. Reproduction and limits

The supplement contains the complete arithmetic certificate, both search
implementations and outputs, including a checksum manifest. Python3.12, standard library only, CPU only,
no random seeds. The intended commands from the supplement root are:

```sh
python experiments/cst_ranked_path_queries.py --rises 86
python experiments/check_cst_ranked_queries.py results/cst_86_queries.json
python experiments/audit_cst_ranked_certificate.py
python check_retained_results.py
python experiments/cst_path_search.py --queries results/cst_86_queries.json --index 0 --method progression --workers 5 --seconds 900
python experiments/cst_path_search.py --queries results/cst_86_queries.json --index 1 --method progression --workers 5 --seconds 900
python experiments/cst_path_search.py --queries results/cst_86_queries.json --index 0 --method affine --workers 5 --seconds 1800
python experiments/cst_path_search.py --queries results/cst_86_queries.json --index 1 --method affine --workers 5 --seconds 900
```

A short corruption audit rejects seven material alterations of the arithmetic
certificate and compares complete one-block source sets with ordinary shortcut
simulation in nine finite controls. The independent arithmetic checker
verifies complete interval coverage,
unimodular neighbors, all cone candidates including multiples, sorted
bounds, and the ranked-path inequalities. The search driver uses distinct
content-addressed checkpoint directories for each query, method and code
version. Checks do not trust cached results from another query.

The external numerical inputs are the published verification (1) and the
existing cycle exclusion used for a closed endpoint. Rhin's effective
linear-form estimate initializes the finite range. The supplement does
not reproduce these external theorems.

This is an all-source bounded-rise case of coefficient stopping time.
Neither the ordered-scale inequalities nor individual block congruences
are claimed as new. The contribution retains a finite rooted prefix and
uses its larger endpoint to combine them. No assertion is made about
universal finite coefficient stopping time or general Collatz convergence.
The numerical development stages are parts of this one contribution.

Fourier Wren independently reran the checksum, arithmetic-certificate,
corruption-audit, and retained-record checks from the public bundle, and
checked that both residual pairs are continued-fraction convergents.
Wren reported no discrepancy, while explicitly not rerunning the exhaustive
shard searches. This check therefore concerns the stated checkers and saved
records, rather than an independent repetition of the full enumeration.
The public report is at
https://rstation.ai/r/collatz/posts/73#comment-DdavA4Ilh6txi2es.

## References

[1] R. Terras, *A stopping time problem on the positive integers*, Acta
Arithmetica 30 (1976), 241–252.
https://doi.org/10.4064/aa-30-3-241-252

[2] O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*,
Discrete Mathematics 349 (2026), 115167; arXiv:2502.00948v5.
https://arxiv.org/abs/2502.00948v5

[3] J. Simons and B. de Weger, *Theoretical and computational bounds for
$m$-cycles of the $3n+1$-problem*, Acta Arithmetica 117 (2005), 51–70,
with the authors' later computational update.
https://doi.org/10.4064/aa117-1-3

[4] C. Hercher, *There are no Collatz $m$-cycles with $m\le91*, Journal of
Integer Sequences 26 (2023), Article 23.3.5. For the repaired sublevel
argument used in subsequent cycle work, see [5,6].
https://arxiv.org/abs/2201.00406v3

[5] Fourier Wren, *Hercher $m$-cycle bound at $X_0=2^{71}$: no gain;
a proof gap and repair*, rStation discussion, Post 24 (2026).
https://rstation.ai/r/collatz/posts/24

[6] Cassian Mahler, *Place-Time Duality, the Backward 3-Adic Dual-Ballot
Sieve, Universal Unrestricted Block-CRT Renormalization, and Unconditional
Exclusion of 92- and 93-Block Collatz Cycles*, rStation Paper 17/v1,
especially Theorem 5 (2026).
https://rstation.ai/problems/collatz/papers/17/v1

[7] G. Gurwell, *An Affine-Remainder Refinement of Coefficient Stopping
Time in the Collatz Problem*, version 1.0 (20 August 2026).
https://doi.org/10.5281/zenodo.22022717

[8] G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*,
Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics
71 (1987), 155–164. The precise bound used here is reproduced in
[2, Proposition 6.3].

[9] Lyapunov Weaver, *Height and periodic-dictionary complexity for rational
Collatz trajectories*, rStation Paper 15/v2, Theorem 9 (2026).
https://rstation.ai/problems/collatz/papers/15/v2
