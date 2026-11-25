# Sparse and spaced clocks of Collatz coefficient contractions without descent

## Abstract

For the shortcut Collatz map and an original start \(n\ge2\), retain date zero and all strict coefficient records before the first drop below \(n\). Over all starts, the set \(G\) of odd-count increments between consecutive retained dates meets every translated interval of \(M\) integers in \(O(M^\rho)\) places for some \(\rho<0.949956\). The proof sums deficits along each simple prefix and over the eligible phases of each primitive cycle, including cycles reached from transients. Each increment has at least 17 odd departures and 27 shortcut steps. Distinct sizes are separated by at least 12 odd departures and 19 steps. With fixed signed weights, sums of \(k\) increments occupy \(O(M^{1-(1-\rho)^k})\) integer positions in such intervals.

Below \(q=72{,}057{,}431{,}991\) odd departures, every contraction before descent has \(q\ge6{,}586{,}818{,}670\), \(n\le135{,}961{,}155{,}471{,}034{,}881{,}034\), and one of 25 candidate pairs. Weighted parity windows and early-ancestor exclusions give 14 pairs under either of Roosendaal's published delay premises. The respective bounds on successive records on one trajectory are 13, 11 and 11.

After a contraction in this band, the fresh coefficient clock and the first descent below \(n\) agree through \(630{,}138{,}896\) steps, and through \(10{,}439{,}860{,}590\) at the least pair. The general restart comparison at strict records and simple contractions holds through 26 steps and eventually through \(\lfloor n^{2/165}\rfloor\) steps. The normalized affine remainder has uniform asymptotic savings \(1/2052\) at first failures and \(1/284\) at arbitrary contractions on simple prefixes.

## 1. The first crossing and its affine remainder

Let \(T(n)=n/2\) for even \(n\) and \(T(n)=(3n+1)/2\) for odd \(n\). Write \(x_t=T^t(n)\), and let \(q_t\) count the odd departures at dates strictly below \(t\). The multiplicative coefficient is \(3^{q_t}/2^t\). Let \(j\) be the first positive date at which this coefficient is below one, assuming such a date exists. A failure means \(x_j\ge n\). The nonnegative additive correction implies \(x_t\ge n\) at every \(t<j\), so for \(n\ge2\) a failure is exactly a discrepancy between the first physical descent and the coefficient stopping time of Terras [1]. The case \(q_j=0\) is an immediate even descent. The start 1 has \(j=2,\ q_j=1,\ x_j=1\) and is included in the small controls.

Write \(q=q_j\ge1\) and \(\theta=\log_2 3\). Index odd departures by \(i=0,\ldots,q-1\), with dates \(t_i\), and set
\[
b_i=\lfloor i\theta\rfloor,\qquad d_i=b_i-t_i,\qquad
W_i=\sum_{a<i}\frac{2^{t_a}}{3^a},\qquad W=W_q .
\]
At \(t_i\) the coefficient is \(3^i/2^{t_i}\ge1\), so \(d_i\ge0\). Call an odd departure *on time* when \(d_i=0\), and *early* when \(d_i>0\). The crossing step is even, since an odd step increases the coefficient. Hence \(j-1\le q\theta<j\) and \(j=\lceil q\theta\rceil\). The affine expansion gives
\[
x_{t_i}=\frac{3^i}{2^{t_i}}\left(n+\frac{W_i}{3}\right),\qquad
x_j=\frac{3^q}{2^j}\left(n+\frac{W}{3}\right).
\tag{1}
\]
Indeed, an odd step at \(t_i\) adds \(1/2\) at its arrival date, which divided by the new coefficient is \(2^{t_i}/3^{i+1}\). For a failure, (1) is equivalent to
\[
3n(2^{j-q\theta}-1)\le W .
\tag{2}
\]
Each summand of \(W\) is at most one. At an on-time departure, (1) also gives
\[
x_{t_i}<2(n+i/3)\le2(n+q/3).
\tag{3}
\]

Gurwell [2, Theorem 3.1, pp. 4–5, and Corollary 3.3, p. 5, equations (12)–(14)] maximizes the remainder over first-crossing parity words. The resulting rotation sum and the exact loss along the given trajectory are
\[
S_q=\sum_{i<q}2^{-\{i\theta\}},\qquad
S_q-W=\sum_{i<q}2^{-\{i\theta\}}(1-2^{-d_i}).
\tag{4}
\]
For \(d_i>0\) the loss is strictly greater than \(1/4\), since \(\{i\theta\}<1\). The arguments below force a positive fraction of such terms.

## 2. A uniform saving with repeated states

**Theorem 1.** There is a function \(\varepsilon(q)\to0\), independent of the starting integer, such that every failure in §1 satisfies
\[
\frac{W}{q}\le\frac{1}{2\ln 2}-\frac{1}{2052}+\varepsilon(q).
\]

**Height and repeat multiplicity.** Bondareva, Luchin and Salikhov [10, Theorem 1, p. 18] prove \(|h_1\ln 2+h_2\ln 3+h|>H^{-4.116201}\) for integer coefficients with \(H=\max(|h_1|,|h_2|)\) sufficiently large. We use the linear-form bound with \(h=0\), \(h_1=p\), and \(h_2=-v\). Take \(\nu=33/8>4.116201\). There is an absolute \(c>0\) such that for \(v\ge1\) and \(p-v\theta>0\),
\[
p-v\theta\ge c v^{-\nu}.
\tag{5}
\]
When \(p-v\theta<1\), one has \(p<v\theta+1\), so the coefficient height is \(O(v)\). The finitely many smaller coefficient heights give nonzero forms by unique factorization and can be absorbed by decreasing \(c\). Differences at least one also satisfy (5) with \(c\le1\). From \(W\le q\), (2), and \(2^u-1\ge u\ln2\) for \(u>0\), it follows that \(n=O(q^{1+\nu})=O(q^{41/8})\), with an absolute implied constant. By (3) the same height bound holds at every on-time departure.

Fix an odd state \(y\) with more than one occurrence on time. Determinism makes \(y\) periodic, even if its first occurrence follows a transient. Let its least period consist of \(p\) shortcut steps and \(v\ge1\) odd departures. Applying the affine formula to one lap gives \(y=3^vy/2^p+B\) for \(B>0\). Thus \(\Delta=p-v\theta>0\). Consecutive visits to \(y\) are exactly one least period apart. At the \(m\)-th return from any fixed visit, the base-two logarithm of the original prefix coefficient has decreased by \(m\Delta\). An odd departure is on time precisely when this logarithm lies in \([0,1)\), so at most \(1+1/\Delta\) visits can qualify, including the initial visit if it qualifies. The odd indices of visits are spaced by \(v\), so at most \(1+q/v\) visits can lie in the whole segment. By (5) the multiplicity of a state among on-time departures is at most
\[
1+\min(q/v,c^{-1}v^\nu)=O(q^{33/41}).
\tag{6}
\]
For \(v\le q^{8/41}\) use the second term and for \(v>q^{8/41}\) use the first. A state with a single occurrence already satisfies the same estimate.

On the shortcut orbit \(1\to2\to1\) the lap multiplier is \(3/4\), with \(p=2\) and \(v=1\). At most three visits to 1 can have coefficient in \([1,2)\), since \((3/4)^3<1/2\). From the actual start 1 only its initial odd departure qualifies and its next visit is the crossing endpoint. A control with inherited factor \(243/128\) gives three consecutive qualifying factors under the lap recurrence. This inherited factor tests the recurrence independently of the original source. A failure with \(n\ge2\) cannot visit 1 through \(j\), by the physical floor \(x_t\ge n\).

**Few windows with few early dates.** Set \(K=\lceil(26/5)\log_2 q\rceil\), \(\delta=1/512\) and \(r=\lfloor\delta K\rfloor\). Since \(26/5>41/8\), for all sufficiently large \(q\) one has \(K\le q\) and all on-time states are below \(2^K\). A window consists of \(K\) consecutive odd departures and is counted as cheap if it starts at \(d_i=0\) and has at most \(r\) early dates. At such a start, with \(\phi=\{i\theta\}\), its relative dates are
\[
u_k=\lfloor k\theta+\phi\rfloor-d_{i+k},\qquad 0\le k<K .
\tag{7}
\]
Compare its first \(K\) shortcut departure bits with those given by the ideal dates \(s_k=\lfloor k\theta+\phi\rfloor\). An early date moves one odd bit and changes at most two positions in \([0,K)\), including when a date moves across the right boundary. The actual dates are strictly increasing nonnegative integers starting at zero. Thus any later odd departure beyond the \(K\) dates of the window is at a relative date at least \(K\). This also holds for the ideal dates, since \(\theta>1\). There are at most \(K\) ideal words in the comparison. The \(K-1\) floors with \(1\le k<K\) each have one jump as \(\phi\) ranges over \([0,1)\), and the value at a jump belongs to the cell on its right.

A parity word of \(K\) shortcut steps fixes one residue modulo \(2^K\), as proved in §3. Each residue provides at most one positive integer below \(2^K\). The number of possible distinct cheap starts is therefore bounded by
\[
K\sum_{m=0}^{2r}\binom Km\le K\,2^{KH_2(1/256)},
\tag{8}
\]
where \(H_2(x)=-x\log_2x-(1-x)\log_2(1-x)\). For the inequality, set \(a=1/256\) and use \((a+(1-a))^K=1\). For \(m\le aK\) each weight \(a^m(1-a)^{K-m}\) is at least \(2^{-KH_2(a)}\). Since \(-(1-a)\ln(1-a)\le a\) and \(\ln2>2/3\) by the first term of its atanh series,
\[
\frac{26}{5}H_2(1/256)
\le\frac{26}{5}\frac{8+\log_2 e}{256}
<\frac{26}{5}\frac{8+3/2}{256}
=\frac{247}{1280}<\frac{8}{41}.
\]
Multiplying (8) by (6) gives \(O((\log q)q^{33/41+(26/5)H_2(1/256)})=o(q)\) cheap windows, with constants independent of the path.

Let \(E\) be the number of early departures. Among the \(q-K+1\) windows, at most \(E\) start early. Apart from these and the cheap windows, each contains at least \(r+1\) early departures. Each early departure belongs to at most \(K\) windows. Hence
\[
q-K+1\le E+o(q)+\frac{KE}{r+1},
\qquad
\frac{E}{q}\ge\frac{1}{513}-o(1).
\tag{9}
\]
The rotation by \(\theta\) is irrational by unique factorization. Equidistribution and Riemann integrability of \(2^{-u}\) on \([0,1]\) give \(S_q/q\to\int_0^1 2^{-u}\,du=1/(2\ln2)\). Subtracting \(E/(4q)\) using (4) proves Theorem 1. The argument permits both simple paths and periodic tails. The existence of a failure for \(n\ge2\) remains open.

## 3. The finite cap in Gurwell's first band

**Theorem 2.** Put \(q_0=6{,}586{,}818{,}670\) and \(q_1=72{,}057{,}431{,}991\). Every failure with \(q_0\le q<q_1\) has
\[
n\le148{,}206{,}287{,}903{,}343{,}593{,}263 .
\]

Gurwell [2, Theorem 6.4, p. 10, equations (43)–(44)] gives the initial ceiling
\[
M=156{,}453{,}180{,}306{,}966{,}943{,}984<2^{71}.
\]
Bařina [5, §6, Table 10] reports convergence verified through \(2^{71}\). If two states at dates below \(j\) coincide, the intervening orbit is a period. Its states are all at least \(n>1\), contradicting eventual arrival at 1. Thus the states used in the windows are distinct. By (3), all on-time starts satisfy the strict uniform height cap
\[
H=2(M+q_1/3)=312{,}906{,}360{,}661{,}972{,}175{,}962<2^{69}.
\]

**Residues and phases.** A word with odd departure dates \(u_0,\ldots,u_{b-1}\) in \([0,L)\) requires the residue
\[
y\equiv-\sum_{\ell=0}^{b-1} 2^{u_\ell}3^{-\ell-1}\pmod{2^L}.
\tag{10}
\]
This follows from the divisibility of the affine numerator by \(2^L\). For completeness, each word is realized by one class. Starts congruent modulo \(2^L\) follow the same word, since under a common first \(a\) steps their difference remains divisible by \(2^{L-a}\). Two starts with the same word have images differing by \(3^b(y-y')/2^L\), which is integral and forces \(y\equiv y'\pmod{2^L}\). The \(2^L\) classes thus exhaust the \(2^L\) words. For \(K\) odd dates ending at \(u_{K-1}\), use \(L=u_{K-1}+1\) to include the last odd bit.

In the coordinate \(z=2^\phi\in[1,2)\), the ideal date \(s_k\) increases at \(z=2^{\lfloor k\theta\rfloor+1}/3^k\) for each \(k>0\). These are distinct rational cuts by unique factorization, and the floor \(\lfloor k\theta\rfloor\) is the bit length of \(3^k\) minus one. Every complete phase cell includes its left endpoint and excludes its right endpoint.

**Weighted window count.** Fix \(K\) and \(r\). Within each phase use (7) with initial offset zero and at most \(r\) positive offsets. For ideal successive gap \(g=s_{k+1}-s_k\), strict increase requires exactly
\[
0\le d'\le d+g-1
\]
for adjacent offsets \(d,d'\). A dynamic program starts with one count at \((e,d)=(0,0)\) and adds the current count to \((e+\mathbf1_{d'>0},d')\) for each allowed \(d'\) within budget. A terminal entry with offset \(d\) is weighted by \(\lceil H/2^{s_{K-1}-d+1}\rceil\), an upper bound on the number of positive representatives below \(H\) of a class from (10). Sum all weighted entries across phases and budgets through \(r\) to get \(C\). Since the starts are distinct on the path, the sum bounds the number of cheap windows even if some starts are counted for several phases.

The same charging argument as (9) gives
\[
\frac{E}{q}\ge\frac{r+1}{K+r+1}\left(1-\frac{K-1+C}{q}\right).
\tag{11}
\]
For the fixed height cap this increases in \(q\). The replay sweeps \(1\le K\le120\), \(0\le r\le24\), maximizing the bound at \(q_0\), and independently recounts the selected parameters phase by phase. It gives
\[
K=44,\qquad r=8,\qquad C=687{,}259{,}638,\qquad
\frac{E}{q}\ge \eta=\frac{53{,}096{,}030{,}901}{349{,}101{,}389{,}510}.
\]

**Exact ceiling.** Gurwell [2, Theorem 6.2, p. 9, equation (41)] gives \(S_q\le \mu q+138\) in this band, with \(\mu=1/(2\ln2)\). This rotation estimate uses Denjoy–Koksma for consecutive blocks of convergent length, each with error at most the circular total variation \(1\). The Ostrowski digit bounds cap the number of blocks by the sum \(138\) of the first 23 partial quotients of \(\theta-1\), since its 23rd convergent denominator exceeds \(q_1\). The replay checks the partial-quotient sum and denominator by rational enclosures.

Let \(p_0=10{,}439{,}860{,}591\). The fractions
\[
\frac{103{,}768{,}467{,}013}{65{,}470{,}613{,}321}<\theta<\frac{p_0}{q_0}
\]
have determinant one, and the denominator sum is \(q_1\). If \(a/b\) is strictly between the two fractions \(l/m\) and \(p_0/q_0\), the positive integers \(am-bl\) and \(bp_0-aq_0\) give \(b=(am-bl)q_0+(bp_0-aq_0)m\ge q_1\). Hence \(j/q=\lceil q\theta\rceil/q\ge p_0/q_0\) in the band, as in Gurwell [2, Lemma 6.1, pp. 8–9, equations (37)–(38)]. Set \(\lambda=p_0\ln2/q_0-\ln3>0\). Then \(2^{j-q\theta}-1\ge e^{q\lambda}-1\ge q\lambda\). By (2), (4) and (11),
\[
n\le \frac{\mu+138/q_0-\eta/4}{3\lambda}.
\tag{12}
\]
Enclose each \(\ln a\) for \(a=2,3\) by taking the odd powers through 191 in \(2\sum_{k\ {\rm odd}}x^k/k\) with \(x=(a-1)/(a+1)\). The positive tail is at most \(2x^{193}/(193(1-x^2))\). Propagating the rational bounds in (12) and rounding outwards gives the interval
\[
[148206287903343593263.446427,\quad148206287903343593263.446428].
\]
Its floor proves Theorem 2 and excludes an additional \(8{,}246{,}892{,}403{,}623{,}350{,}721\) integer starts within the band.

### Exact census of candidate pairs

Rozier and Terracol [4, Corollary 5.4] give the least eligible start \(N=28{,}000{,}000{,}000{,}000{,}000{,}001\). For a pair \((q,j)\), put \(D=j\ln2-q\ln3>0\), \(G(q)=\mu q+138\), and \(B(q)=9(q-687{,}259{,}681)/53\), the lower bound on \(E\) from (11). Given an upper envelope \(U(q)\) for \(W\), (2) requires \(3N(e^D-1)\le U(q)\). This is exactly the condition for the resulting source interval \([N,U(q)/(3(e^D-1))]\) to contain an integer. The test at \(j=\lceil q\theta\rceil\) gives 30 pairs for \(U=G(q)\) and 28 for each of \(U=G(q)-\eta q/4,\ G(q)-B(q)/4,\ G(q)-\lceil B(q)\rceil/4\), with identical sets for the three sliding bounds. Every passing pair has strictly positive margin even with \(\mu q-138\) replacing \(G(q)\). Each exclusion already fails at \(\mu q+138\), so using the exact \(S_q\) gives the same decisions. A passing pair certifies feasibility for the source interval test. A physical failure also requires a trajectory that realizes the pair and satisfies (2) with its own \(W\).

The two excluded pairs \((q,j)\) are \((47{,}300{,}450{,}827,\ 74{,}969{,}440{,}828)\) and \((60{,}871{,}661{,}546,\ 96{,}479{,}300{,}907)\). The full 30-row table with all four flags is in the supplement as census/candidates.csv. [Candidate table archive](supplement.zip)

**Determinant-one traversal.** Retain \(l/m\) and \(p_0/q_0\) from §3 and set \(D_0=p_0\ln2-q_0\ln3\). The integer coordinates \(a=mj-lq\) and \(v=q_0j-p_0q\) give \((j,q)=a(p_0,q_0)-v(l,m)\). By the Farey bound \(v\ge0\), and \(D=(qD_0+v\ln2)/q_0\). Since \(e^D-1\ge D\), any pair passing the Gurwell test satisfies
\[
0\le v\le\frac{q_0G(q)/(3N)-qD_0}{\ln2}.
\]
Use the upper rational bound on \(\mu\) and lower bounds on \(D_0,\ln2\) from the log series above. For a passing pair the numerator is nonnegative. The resulting affine upper bound is maximized at \(q_0\) or \(q_1-1\), and the floor of that maximum is 4. For each \(v=0,\ldots,4\), enumerate \(a\) from \(\lceil(q_0+vm)/q_0\rceil\) through \(\lceil(q_1+vm)/q_0\rceil-1\). There are 50 pairs, each certified to have \(0<D<\ln2\), which forces \(j=\lceil q\theta\rceil\). The replay filters them with rational enclosures of \(e^D-1\) using its degree-12 series and a geometric tail.

**Floor-sum traversal.** Write \(A_-\) for the lower bound on \(\ln2\), \(B_+\) for the upper bound on \(\ln3\), and \(\theta_-,\mu_+\) for the lower and upper bounds on \(\theta,\mu\), respectively. Every pair passing the Gurwell test lies in
\[
\theta_-q<j\le \frac{B_++\mu_+/(3N)}{A_-}q+\frac{138}{3NA_-}.
\]
For any subinterval of \(q\), the number of lattice points is the difference of the floor sums of the two lines. For \(F(s,m,a,b)=\sum_{i=0}^{s-1}\lfloor(ai+b)/m\rfloor\), first extract the integer quotients of \(a,b\) by \(m\). With the remainders \(0\le a,b<m\), write \(as+b=mh+r\). If \(h=0\), the reduced sum is zero. Otherwise counting the indices reaching each level \(1\le k\le h\) gives \(s-\lceil(mk-b)/a\rceil\) at level \(k\). Summing yields \(F(h,a,m,r)\), with strictly smaller modulus. Bisection prunes zero-count intervals and recovers the 30 strip points. This traversal tests \(D\le\ln(1+U(q)/(3N))\) with rational log bounds and agrees pair for pair with the first traversal for every envelope.

### Every contraction before descent below the band cutoff

**Finite clock theorem.** Suppose the supplied trajectory from \(n\ge2\) has \(x_a\ge n\) for \(0\le a\le t\) and \(D_t=t\ln2-q_t\ln3>0\), with \(q=q_t<q_1\). Then \(q\ge q_0\), \(t=\lceil q\theta\rceil\), and \(n\le135{,}961{,}155{,}471{,}034{,}881{,}034\). There are at most 25 candidate pairs \((q,t)=kU+vS\), where \(U=(q_0,p_0)\), \(S=(397{,}573{,}379,630{,}138{,}897)\), and \(k\) ranges up to 10 from \(1,3,6,9\) at \(v=0,1,2,3\), respectively. Under either Roosendaal delay premise in §3 the final list has 14 pairs, \(kU\) for \(1\le k\le10\) and \(kU+S\) for \(7\le k\le10\). Distinct pairs in each list differ by at least \(397{,}573{,}379\) odd departures and \(630{,}138{,}897\) shortcut steps.

**Preliminary list.** The first coefficient contraction at \(j\le t\) also occurs before descent, so \(n\ge N\). Multiplying the step ratios gives
\[
0<D_t\le\sum_{a<t,\ x_a\ {\rm odd}}\ln(1+1/(3x_a))<q/(3n)\le q/(3N)<\ln2.
\]
Here \(q>0\), so \(t=\lceil q\theta\rceil\). Call \(1\le i<q_1\) exceptional when \(0<\lceil i\theta\rceil\ln2-i\ln3\le i/(3N)\). Apply the determinant-one coordinates above with \(D\le q/(3N)\). They give \(0\le v\le q(q_0/(3N)-D_0)/\ln2\). The rational upper bound at \(q=q_0\) is in \([0,1)\). For \(0<q<q_0\), it would force \(v=0\) and hence \(q=a q_0\), an impossibility. The maximum upper bound for \(q<q_1\) has floor 7. The corresponding coordinate box contains 87 pairs, of which 43 satisfy the exceptional test. The floor-sum traversal in the rational strip for \(D\le q/(3N)\) independently returns the same 43, all with strict upper margin.

In particular \(q_j\in[q_0,q_1)\), so Theorem 2 gives the preliminary source cap \(M'=148{,}206{,}287{,}903{,}343{,}593{,}263\). Since \(M'<2^{71}\), Bařina's convergence range makes the whole prefix through \(t\) simple. A repeated state there would trap it on a cycle with every state at least \(n>1\). For each odd departure at \(t_i<t\), define \(d_i\) as in §1. If \(d_i<0\), that departure date is itself a contraction before descent, with odd count \(i\). Thus \(i\) is exceptional, and \(t_i=\lceil i\theta\rceil\) gives \(d_i=-1\). At most \(s=43\) departures are late in this sense, each adding less than one to the ideal sum in (4). For every partial sum \(W_i\le i+s\), so each on-time state is below \(2(M'+(q_1+s)/3)<H\), with the height cap \(H\) of §3. The same weighted count \(C=687{,}259{,}638\) therefore applies to windows anchored on time with no late departures and at most eight early ones.

Discard at most \(44s=1{,}892\) windows that contain a late departure. Charging the remaining windows as in (11) gives
\[
E\ge B_s(q)=\frac{9(q-687{,}259{,}681-44s)}{53},\qquad
W\le\mu q+138+s-B_s(q)/4 .
\]
Rounding \(B_s(q)\) up is also valid. The rotation estimate holds for every \(1\le q<q_1\) by the partial-quotient argument of §3. For each source floor \(N_*\), test \(3N_*(e^{D_t}-1)\le\mu q+138+s-B_s(q)/4\). The unrounded envelope gives an outer bound \(D_t\le A q+B\) via \(e^{D_t}-1\ge D_t\), using the upper rational endpoint for \(\mu\). In the determinant-one traversal this gives \(v\le(q_0(Aq+B)-q D_{0,-})/(\ln2)_-\). In the floor-sum traversal it gives the strip \(\theta_-q<t\le((\ln3)_++A)q/(\ln2)_-+B/(\ln2)_-\). The exact exponential and logarithmic filters agree for \(s=0\) and \(s=43\) and both rounding choices. Every surviving pair passes even with the lower rotation bound \(\mu q-138\). This verifies the same lists for the exact \(S_q\) in these necessary tests.

Write \(U=(q_0,p_0)\) and \(S=(10q_0-m,10p_0-l)=(397{,}573{,}379,630{,}138{,}897)\) in \((q,t)\) order. The baseline list is \(kU+vS\), with \(k\) ranging up to 10 from \(1,3,5,8,10\) at \(v=0,1,2,3,4\), respectively. Both coordinates strictly increase in \(q\)-order. The smallest consecutive gaps are precisely the coordinates of \(S\), attained in the list at \(6U,6U+S\). The last pair is \((67{,}458{,}480{,}216,106{,}919{,}161{,}498)\). Its distances to \(q_1\) and \(\lceil q_1\theta\rceil=114{,}208{,}327{,}604\) are \(4{,}598{,}951{,}775\) and \(7{,}289{,}166{,}106\), both larger than the corresponding gap. Consequently, given a contraction before descent below the cutoff on a supplied trajectory, a later coefficient contraction whose odd-count gap or shortcut-date gap is strictly smaller than the corresponding minimum has physical descent below the original \(n\) by that date. The gap minima describe the arithmetic list of candidates. \(\square\)

### Bounds from published ordinary-delay coverage

Write \(D_{\rm ord}(n)\) for the first arrival at 1 in ordinary Collatz steps, counting an odd step and its following halving separately. On a supplied contraction before descent at \(t\), the trajectory has avoided 1 through the first \(t+q_t\) ordinary steps, including the inserted states \(3x_a+1\). Since \(t\ge p_0>2480\) in the band, published coverage with \(D_{\rm ord}\le2480\) excludes the covered starts. For a first crossing one also has \(j\le D_{\rm ord}(n)\) on every orbit reaching 1, since the affine correction is nonnegative and the coefficient at arrival at 1 is at most \(1/n<1\).

Roosendaal [11] defines a confirmed strict delay record to mean that all smaller starts had smaller delay. His last listed confirmed start \(R=46{,}645{,}791{,}847{,}966{,}786{,}687\) has directly replayed delay 2480. The record premise thus bounds the delay by 2480 through \(R\). Independently, the class table declares complete coverage of 2,428 positive-delay class minima up to \(L=48{,}500{,}000{,}000{,}000{,}000{,}000\), with greatest delay 2480. The September 28, 2026 progress entry records completion through block 48,500 in units of \(10^{12}\). A larger delay at any start strictly below \(L\) would have a class minimum below \(L\) and hence a row. The endpoint \(L\) has directly replayed ordinary delay 381 and both shortcut stopping times equal to one. The two conditional source floors are therefore \(R+1\) and \(L+1\), respectively. The supplement verifies the archived declarations, listed trajectories, and endpoints. The exhaustiveness of each search is the corresponding published premise.

| Source coverage premise | Last excluded start | First-crossing Gurwell test | First-crossing uniform sliding | First-crossing \(q\)-dependent sliding | All protected dates before weighted bounds | All protected dates after fixed-width count | Final |
| --- | ---: | ---: | ---: | ---: | ---: | ---: | ---: |
| Rozier–Terracol baseline | 28,000,000,000,000,000,000 | 30 | 28 | 28 | 28 | 25 | 25 |
| Roosendaal confirmed strict record | 46,645,791,847,966,786,687 | 18 | 17 | 17 | 17 | 15 | 14 |
| Roosendaal complete class table and direct endpoint | 48,500,000,000,000,000,000 | 17 | 17 | 15 | 15 | 14 | 14 |

For either higher floor, the Gurwell test has determinant-one bound \(v\le2\). Both traversals give the same decisions and the replay also projects the baseline first-crossing rows through the corresponding integer source caps. Before the weighted bounds, the strict-record list is \(\{kU:1\le k\le10\}\cup\{kU+S:5\le k\le10\}\cup\{10U+2S\}\) and the class-table list is
\[
\{kU:1\le k\le10\}\ \cup\ \{kU+S:6\le k\le10\}.
\]
The all-dates sliding-window test gives these same lists under the respective coverage premises. The supplement's census/delay_floor.csv records the first-crossing comparison before the weighted sieve. [Supplement](supplement.zip)

### Weighted exclusion of \(6U+S\)

Take \((q,t)=6U+S=(39{,}918{,}485{,}399,63{,}269{,}302{,}443)\) and assume the complete delay-class premise, giving the floor \(N_c=48{,}500{,}000{,}000{,}000{,}000{,}001\). Retain the simple protected path and the bound of 43 offsets equal to \(-1\) from the finite clock theorem's proof. Write \(z_i=3^i/2^{b_i}\) and
\[
\mathcal L=\sum_{i<q,\ d_i\ge0}z_i^{-1}(1-2^{-d_i}),\qquad \Delta=D_t .
\]
The affine inequality and the rotation estimate give
\[
3n(e^\Delta-1)\le W\le\mu q+138+43-\mathcal L .
\]
The sliding-window bound \(\mathcal L\ge\lceil B_{43}(q)\rceil/4\) gives the initial pair-specific cap \(H_1=54{,}286{,}747{,}694{,}955{,}263{,}713\). Given any improved lower bound on \(\mathcal L\), use an upper rational bound on \(\mu\) and a lower bound on \(e^\Delta-1\) and take the floor of the resulting upper bound on \(n\). A smaller cap tightens the state intervals in the next count.

Fix \(K\), discard windows containing a negative offset, and retain at least \(A=q-K+1-43K\) windows. For each level \(D=0,1,2,3\), the anchor is the first offset \(a=d_i\le D\) in a retained window. Let \(e\) be the number of departures preceding the anchor. The loss of a window without an anchor is at least \(K(1-2^{-(D+1)})/2\). Partition the anchor phase \(z=z_i\) into left-closed cells \([\alpha,\beta)\) as in §3. On a cell \(s_j=\lfloor\log_2(3^j z)\rfloor\) is constant for \(0\le j<K\). The suffix departure with offset \(d_{i+j}\) contributes at least \(2^{s_j}(1-2^{-d_{i+j}})/(3^j\beta)\). For a preceding departure \(i-h\) the rotation weight satisfies
\[
z_{i-h}^{-1}=\frac{3^h}{z}2^{\lfloor\log_2(z/3^h)\rfloor}
\ \ge\ 
\max\!\left(\frac12,\frac{3^h}{\beta}2^{\lfloor\log_2(\alpha/3^h)\rfloor}\right).
\]
The lower endpoint bounds the floor even across a rotation discontinuity. Multiply the sum of these preceding weights for \(1\le h\le e\) by \(1-2^{-(D+1)}\), since all preceding offsets exceed \(D\). Scale by \(P=512\) and round down this preceding charge and each suffix charge.

For \(m=K-e\) suffix departures, the relative dates \(u_j=s_j+a-d_{i+j}\) start at zero. Their increase is equivalent to the transition \(0\le d_{i+j+1}\le d_{i+j}+s_{j+1}-s_j-1\). A dynamic program counts suffixes by current offset and rounded suffix charge, starting from offset \(a\) and its own charge. It adds the preceding charge at each possible suffix length. With current source cap \(H_p\), the anchor state is in the closed interval
\[
[\,2^a\alpha N_c,\ 2^a\beta(H_p+(q+43)/3)\,]
\]
by the affine formula and \(0\le W_i\le q+43\). If the interval contains \(w\) integers, the suffix residue (10) permits at most \(\lceil w/2^{u_{m-1}+1}\rceil\) of them. For a fixed \(e\) the distinct anchor state identifies at most one window, since it fixes its own date and hence the starting index \(i-e\). Summing the capacities over phases, suffixes, anchors and \(e\) bounds the number of windows in each rounded charge range.

Let \(C_D(b)\) be the capacity for charges at most \(b\), capped at \(A\). At and above the rounded threshold for a window without an anchor, use \(C_D(b)=A\). At least \(A-\min_D C_D(b)\) retained windows have scaled loss at least \(b+1\). This uses integer rounded charges that bound the actual scaled losses from below. The capped value gives zero contribution whenever the count reaches \(A\), even if more than \(A\) windows were retained. Sum these deficits over \(0\le b<\lceil4PK/25\rceil\) and divide by \(PK\), since each nonnegative offset is charged by at most \(K\) windows. All capacities use integer arithmetic, with saturation at \(A\). The rational intervals for logarithms and the exponential are those of the all-dates census.

| Pass | Input source cap | \(K\) | Sum of deficits | Implied source cap |
| ---: | ---: | ---: | ---: | ---: |
| 1 | 54,286,747,694,955,263,713 | 41 | 90,097,553,847,199 | 49,031,048,841,040,449,812 |
| 2 | 49,031,048,841,040,449,812 | 39 | 90,552,417,920,377 | 48,545,038,756,635,321,770 |
| 3 | 48,545,038,756,635,321,770 | 39 | 92,552,361,574,527 | 48,344,622,364,946,686,546 |

The third cap is below \(N_c\), excluding \(6U+S\) for every protected contraction, including a first crossing, under the class-table premise. The final conditional list is
\[
\{kU:1\le k\le10\}\ \cup\ \{kU+S:7\le k\le10\}.
\]
The \(7U,7U+S\) pair of candidates still attains both minimum coordinate gaps. The replay uses phase-dependent bounds, checks literal parity counts and native trajectories, and reproduces all three passes at \(K=39,41\). [Supplement](supplement.zip)

### Fixed original-source widths for all pairs

For any one original source \(n\) and any phase cell \([\alpha,\beta)\), the anchor interval in the preceding proof has endpoints \(2^a\alpha n\) and \(2^a\beta(n+(q+43)/3)\). If \(n\le H_p\) and \(q\le Q\), the interval contains at most
\[
w=1+\left\lfloor 2^a\bigl((\beta-\alpha)H_p+\beta(Q+43)/3\bigr)\right\rfloor
\]
integers. Indeed, subtract the two endpoints at the same \(n\) and take the floor of the resulting length, plus one. The interval may move with \(n\). A residue class modulo \(2^m\) has at most \(\lceil w/2^m\rceil\) representatives in any such translate. On the fixed trajectory this bounds the capacity for the suffix through its last odd departure, with \(m\) equal to the last relative date plus one. All windows in the charging argument come from that trajectory, so the bound holds uniformly in the original source without taking a union of its possible translated intervals.

Use the same phase charges and suffix recurrence, with these widths in place of the earlier source-floor intervals. A single count can serve a group of pairs by taking \(H_p\) and \(Q\) to be the respective maxima of the input caps and odd counts in the group. Clip each cumulative capacity at \(A(Q)=Q-K+1-43K\). For a pair with odd count \(q\le Q\), sum \(\max(0,A(q)-\min_D C_D(b))\) over \(0\le b<\lceil PK/5\rceil\), where \(A(q)=q-K+1-43K\). Clipping at the larger \(A(Q)\) preserves every positive contribution to this sum. Dividing by \(PK\) bounds \(\mathcal L\) below, and the affine inequality updates each pair's cap using its own \(q,\Delta\). Each pass keeps the stronger of the previous cap and the new cap.

The certificate starts from the rounded \(B_{43}\) bounds at all 28 preliminary baseline pairs. It first uses \(K=43\) at scale \(P=512\) on the full group. It then uses \(K=41\) at scale 512 and \(K=39,41\) at scale 1024 on \(6U+S,7U+S\), followed by \(K=39\) at scale 1024 on \(6U+S\) alone. Finally it uses \(K=41\) at scale 1024 on the pure multiples. The replay compares every updated cap to each of the three source floors. The caps use the inherited first-band bounds independently of the Roosendaal delay premises. The largest cap over all 28 pairs is the pure-multiple cap \(135{,}961{,}155{,}471{,}034{,}881{,}034\) at \(U\). At \(6U+S\) the fixed-width cap is \(48{,}310{,}943{,}696{,}040{,}412{,}182\), which is below the complete delay-class floor. The translated-interval replay supplies a separate exclusion at that floor using its own two-file exact counter. [Supplement](supplement.zip)

### Covered ancestors and the strict-record floor

Suppose ordinary first-hit delays are at most \(B\) through a covered start \(L\). On the original protected prefix through \(t\), consider \(x_s>2\) with \(t-s\ge B\). A positive ancestor \(a\le L\) reaching \(x_s\) before its first 1 would have to follow the same protected suffix by determinism. If it arrives at ordinary time \(r\), the ordinary endpoint occurs at \(r+t-s+q_t-q_s\), with every state on that suffix above 1. Its first hit of 1 is therefore later than \(B\), a contradiction. An arrival after the first 1 would put \(x_s\) on the ordinary \(1,4,2\) cycle, whose future also contradicts protection through \(t\) in this application. The transfer uses the physical floor \(n\) of the original trajectory. The timing controls compute the delay cap 237 through 4,096 and check the short protected prefix \(4097\to6146\). Its endpoint can be reached from 2,427 in five shortcut steps or nine ordinary steps, illustrating the need for the remaining-time condition.

In the strict-record calculation use \(L=46{,}645{,}791{,}847{,}966{,}786{,}687\) and \(B=2480\). Leave the last 2,481 odd departures outside the count. Every retained successor of an observed odd-to-odd edge has at least 2,480 remaining shortcut steps. If an edge has \(3x+1=2^v y\), take \(m=\lfloor(v-1)/2\rfloor\). Since \(x\equiv(4^m-1)/3\pmod{4^m}\), \(a=(x-(4^m-1)/3)/4^m\) is an integer. It satisfies \(3a+1=2^{v-2m}y\ge2\) with an even right-hand side, so \(a\) is positive and odd and its next odd state is \(y\). The early-ancestor bound requires \(a>L\), or
\[
x>4^mL+(4^m-1)/3 .
\]
At suffix position \(j\) with offset \(d\), the upper bound on \(x\) in the cell is \(2^d\beta\,3^j 2^{-s_j}(H_p+(q+43)/3)\). The worker rounds up the bound at \(d=0\), multiplies by \(2^d\), and omits a transition when this upper bound is at most the sibling threshold. It counts \(q-2481-K+1-43K\) windows by the same capacity argument.

For \(6U+S\) the one-pass sibling certificate starts from \(48{,}450{,}007{,}253{,}875{,}036{,}124\). The replay derives this cap with both ancestor filters off, using a shared fixed-width count for \(6U+S,7U+S\) at \(K=39\) and scale 256 starting from the rounded \(B_{43}\) caps. The strict-record pass uses \(K=39\), scale 256 and depth zero, with the direct sibling test. Its deficit sum is \(56{,}711{,}011{,}490{,}910\), yielding \(n\le46{,}253{,}252{,}327{,}428{,}858{,}256<L+1\). This excludes the last extra strict-record pair and gives the same 14 pairs as under the complete delay-class premise. [Supplement](supplement.zip)

## 4. Disjoint phase windows

Direct enumeration with (10) gives two comparison bounds. For all-on-time words of 49 odd dates, the minimum positive start over the 49 phase cells is \(338{,}019{,}242{,}168{,}217{,}300{,}075>H\). For 48 odd dates it is \(285{,}203{,}735{,}579{,}433{,}346{,}939<H\). The latter number is also the 49-date minimum when the last odd bit is omitted. This comparison checks the terminal-bit convention. With the coarser height cap \(2^{69}\), 52 dates suffice. Every complete block of 49 odd dates therefore loses at least \(1/4\).

For a 51-date block with at most two early departures, discard the \(\ell\) leading early dates and anchor the remaining dates at the first on-time departure. Here \(0\le\ell\le2\). Starting from offset zero, the transition \(d'\le d+g-1\le d+1\) limits every suffix offset to \(2-\ell\). In each phase enumerate positions and offsets within that budget, retain strictly increasing dates \(u_k=s_k-d_k\), and apply (10) through the last odd bit. If the least positive start is below \(H\), the suffix loss has infimum
\[
\frac{1}{z_{\rm right}}\sum_{k:\,d_k>0}\frac{2^{s_k}-2^{u_k}}{3^k}.
\]
This follows from (4) because each absolute weight is \(2^{s_k}/(3^kz)\) at the corresponding relative date. For \(\ell=0,1,2\), the replay checks respectively \(24{,}088,\ 1{,}483,\ 49\) phase and offset arrays with increasing dates. The numbers surviving the height test are \(4,0,0\), and the smallest suffix infimum is \(98{,}415/131{,}072>3/4\). Three or more early dates already cost more than \(3/4\). Every complete 51-date block therefore loses at least \(3/4\). For 50 dates and no leading early departures, a surviving phase and offset array has infimum \(2{,}236{,}003{,}291/3{,}099{,}363{,}912<3/4\), a control on this finite-word test.

For a disjoint block length \(L\) with loss \(c\), (4) gives
\[
W\le\mu q+138-c\lfloor q/L\rfloor
\le(\mu-c/L)q+138+c(L-1)/L.
\]
For \(a,b>0\) the quotient \((a q+b)/(3(e^{\lambda q}-1))\) decreases for \(q>0\). Its derivative has the sign of \(a(e^{\lambda q}(1-\lambda q)-1)-b\lambda e^{\lambda q}<0\). The resulting bound is maximal at \(q_0\). For \(D=\lambda q_0\) the replay brackets \(e^D-1\) using \(D+D^2/2+D^3/6\) and the same polynomial plus \(D^4/(24(1-D/5))\). These bounds follow from the positive power series and a geometric tail for \(0<D<1\). The replay recovers Gurwell's ceiling at \(c=0\) and gives the following comparisons.

| Window argument | Source ceiling |
| --- | ---: |
| Gurwell's rotation envelope | 156,453,180,306,966,943,984 |
| Disjoint blocks of 49 dates | 155,346,597,889,829,751,901 |
| Disjoint blocks of 51 dates | 153,263,619,223,245,858,200 |
| Sliding windows of 44 dates, up to eight early | 148,206,287,903,343,593,263 |

## 5. Separation of the odd counts at physical failures

Let \(\mathcal F\) consist of the distinct odd counts of first coefficient contractions which fail to give descent, over all positive integers \(n\ge2\). We also consider a contraction at any date \(t\), provided \(x_i\ge n\) for every \(0\le i\le t\). Call this a *contraction before descent*. For either kind of contraction, the first coefficient crossing occurs at or before \(t\) and fails. Rozier and Terracol [4, Corollary 5.4] therefore give \(n>2.8\cdot10^{19}>2^{64}\).

**Theorem 3.** Distinct members of \(\mathcal F\) differ by at least 12, and their shortcut dates differ by at least 19. As \(q\) tends to infinity in \(\mathcal F\), \(\delta_q=\lceil q\theta\rceil-q\theta\) tends to zero. In particular, each fixed positive difference occurs between only finitely many pairs in \(\mathcal F\).

For contractions before descent at arbitrary dates, two prefixes with odd counts differing by 1 through 11 force a repeated state on one of the supplied prefixes. That prefix contains a positive cycle above 1. Conversely, starting at the minimum of any such cycle supplies contractions before descent with every sufficiently large odd count.

**Proof.** Put \(g_t=3^{q_t}/2^t\). The physical identity for any interval of dates is
\[
 \ln\frac{x_b}{x_a}-\ln\frac{g_b}{g_a}
 =R_{a,b},\qquad
 R_{a,b}=\sum_{\substack{a\le i<b\\x_i\ {\rm odd}}}
                    \ln(1+1/(3x_i)).
 \tag{13}
\]
On a simple prefix, meaning that all states through its endpoint are distinct, \(x_t\ge n\) gives \(0<-\ln g_t\le R_{0,t}\) at a contraction before descent. Lemma 2 of [8] bounds the positive log correction of any simple shortcut list above \(2^{64}\) by
\[
 H=50666894410409296445627628396/10^{30}.
 \tag{14}
\]
There is also a bound depending on the start. Write \(d=H_2(\log_3 2)\), and let \(\eta_0<d\) be the exponent in [9, (P2), (P3), (P5)]. Fix \(\rho\) with \(\max(\eta_0,13/14)<\rho<d\), possible since \(d=0.9499555\ldots\). The reciprocal tail in (P3), taken at exponent 1, gives \(R_{0,t}\ll n^{\rho-1}\) by \(\ln(1+1/(3x))\le 1/(3x)\). All constants are uniform in the orbit and the terminal date.

At a first crossing \(j\), suppose some state in \(x_0,\ldots,x_j\) repeats. For any repeated pair with indices \(a<b\le j\), the least period \(p\) from \(a\) divides \(b-a\), so \(j-p\ge a\) and \(x_{j-p}=x_j\). The last \(p\) departures are distinct. For \(v\) odd departures on that lap, (13) gives
\[
 0<-\ln g_j
   = (p\ln 2-v\ln 3)-\ln g_{j-p}
   \le p\ln 2-v\ln 3 =R_{j-p,j}.
 \tag{15}
\]
Here \(g_{j-p}\ge1\) includes \(j-p=0\). The lap lies above \(n\), so (P3) applies with each state counted once. For (14), open the lap at the repeated endpoint and charge its last edge. The last edge of a first crossing is even, with zero cost. Thus \(-\ln g_j\le H\) and \(-\ln g_j\ll n^{\rho-1}\) in the repeated case as well.

For any simple contraction before descent, and for every first failure, the natural-log deficit \(D=t\ln 2-q\ln 3\) now belongs to \((0,H]\). Since \(H/\ln2=0.0730968773\ldots<1\), the date is \(t=\lceil q\theta\rceil\). Two such deficits differ by strictly less than \(H\). Checking the nearest integer to \(h\theta\) for each \(1\le h\le11\) gives
\[
 \min_{1\le h\le11,\,k\in\mathbb Z}|k\ln2-h\ln3|
    =\ln(256/243)>H.
 \tag{16}
\]
At \(h=12\) the nearest integer is 19 and \(\ln(3^{12}/2^{19})<H\). For \(h\ge12\) the dates differ by at least \(\lfloor12\theta\rfloor=19\). Equation (16) proves both the first-failure spacing and the repeat assertion for two supplied paths. If a positive cycle has minimum \(m>1\), start at \(m\). Every index stays above or equal to \(m\), and each full lap multiplies the coefficient by \(e^{-R}<1\). There are finitely many phases, so all sufficiently late dates are contractions. Since each odd departure increases the count by one, every sufficiently large odd count occurs.

Finally, each source has at most one first crossing. Any fixed finite set of sources supplies finitely many elements of \(\mathcal F\). By (13) and (15), all remaining deficits are at most \(C n^{\rho-1}\). This proves \(\delta_q\to0\) along \(\mathcal F\). If \(q,q+h\in\mathcal F\), then \(\|h\theta\|\le|\delta_q-\delta_{q+h}|\), where \(\|\cdot\|\) is distance to the nearest integer. For fixed \(h>0\) the left side is positive, proving the last finiteness assertion. \(\square\)

The independent numerical check compares the two integer dates bracketing \(h\theta\) for each \(h=1,\ldots,12\), using exact ratios of powers before enclosing their logarithms. It finds the minimum in (16) at \((h,k)=(5,8)\) and checks the two arithmetic band points \((q,j)=(17,27),(29,46)\). The band thus permits gaps 12 and 19 at the arithmetic level. Native checks include the trajectory from 7, whose date-8 endpoint has recovered above the start after an earlier descent, and a scan of starts 2 through 20,000 to their first 1. A modified odd branch \((3x+5)/2\) supplies explicit lap controls for (15), including a first contraction after earlier repeats. [Clock-gap replay in the supplement](supplement.zip)

**A coefficient threshold for a completed cycle.** Let \(s(n)\) be the first physical descent and \(u(n)\) the first date with \(g_t\le19/20\), assigning \(+\infty\) when the corresponding event never occurs. Then \(s(n)\le u(n)\) for every \(n\ge2\) if and only if there is no nontrivial positive cycle. In fact, if \(u(n)<s(n)\), the finite prefix through \(u(n)\) already contains such a cycle. Otherwise it would be a simple contraction before descent, giving \(-\ln g_{u(n)}\le H\) by (13)–(14). But \(\ln(20/19)>2/39>H\), by the first term of the positive odd-power logarithm series. The converse follows by starting at a nontrivial cycle minimum. The existence of a finite \(u(n)\) for every starting integer is a separate question.

**Restarting the coefficient at a record.** Set \(g_0=1\). Let \(t>0\) be a contraction before descent at which \(g_t\) is strictly smaller than every earlier coefficient, and put \(y=x_t\). The first visit below the original \(n\) and the first coefficient contraction calculated afresh from \(y\) agree in occurrence and first date through **26** additional shortcut steps. The conclusion also holds at any contraction before descent on a simple initial prefix. For all sufficiently large \(n\) the same conclusions hold through \(L=\lfloor n^{2/165}\rfloor\) further steps.

Let \(f\) be the first fresh contraction, allowing \(f=\infty\). At every earlier date the nonnegative affine correction from \(y\) keeps the state at least \(y\ge n\). It suffices to rule out a fresh contraction in the stated window whose endpoint also stays at or above \(n\). Write its local natural-log deficit as \(D'=\ln(g_t/g_{t+f})>0\). If the prefix through \(t\) is simple, (13)–(14) bound its correction by \(H\), and each of the next \(f\) departures contributes at most \(1/(3n)\). A protected endpoint \(x_{t+f}\ge n\) would give \(D'\le-\ln g_{t+f}\le H+f/(3n)\).

If a repeat occurs on the prefix through \(t\) and \(t\) was a strict coefficient record, write \(r\) for the cycle entry date and \(p\) for the least period. Then \(r+p\le t\), so the last primitive lap starts at \(t+f-p\ge r\) and all its states are at least \(n\). Every date before \(t+f\) has coefficient at least \(g_t\), including dates after \(t\), since \(f\) is the first fresh contraction. Therefore
\[
 D'\le\ln(g_{t+f-p}/g_{t+f})=R_{t+f-p,t+f}\le H .
\]
For (14), the closing step of this lap is even, as it is the step of the fresh contraction. This comparison is uniform in the number of previous laps.

For \(1\le\ell\le26\), \(0\le h\le\ell\), the smallest ratio \(2^\ell/3^h\) strictly above one is \(256/243\), attained at \((\ell,h)=(8,5)\). The replay compares the integer powers for all positive forms in this range. Its logarithm exceeds \(H+1/1000\), as follows from the first positive term \(26/499\) of the odd-power logarithm series. Since \(n>2.8\cdot10^{19}\), a fresh contraction in the 26 steps would exceed both allowable bounds on \(D'\). At \((\ell,h)=(27,17)\), the ratio is \(134217728/129140163\), with log strictly between zero and \(H\).

For the growing horizon, (P3) bounds the initial simple correction or the last primitive lap by \(C n^{\rho-1}\) as in Theorem 3. Since \(\rho<d<19/20\), for \(L=\lfloor n^{2/165}\rfloor\) one has \(C n^{\rho-1}+L/(3n)=o(n^{-1/20})\). For \(1\le\ell\le L,\ 0\le h\le\ell\), the two-sided estimate from [10] gives \(\lvert\ell\ln2-h\ln3\rvert\gg L^{-33/8}\ge n^{-1/20}\). The contradiction for a fresh contraction proves the claim with the original floor intact. The eventual threshold inherits the ineffectivity of (P3).

### Explicit restart horizons in the first band

On a supplied trajectory contracting before descent at \(t\) in the first band, the first fresh coefficient contraction from \(y=x_t\) and the first subsequent hit below the original \(n\) agree through the next \(630{,}138{,}896\) shortcut steps. At the least pair \((q,t)=(q_0,p_0)\), they agree through the next \(10{,}439{,}860{,}590\) steps. Agreement through a horizon means that the first dates are equal if either occurs by the horizon, and otherwise both exceed it.

For this proof use vectors in (date, odd count) order, and set \(D(\ell,h)=\ell\ln2-h\ln3\). If \(P_+,P_-\) have positive dates, determinant of absolute value one and deficits of opposite signs, write \((\ell,h)=aP_++bP_-\) in integer coordinates. For \(0<\ell\) less than the sum of their dates, the coefficients cannot both be positive or both be nonpositive. Thus a positive deficit requires \(a\ge1,b\le0\) and is at least \(D(P_+)\). A negative deficit requires \(a\le0,b\ge1\) and is at most \(D(P_-)\).

Take \(P_+=(272{,}500{,}658,171{,}928{,}773)\) and \(P_-=(357{,}638{,}239,225{,}644{,}606)\). Their sum is \(S'=(630{,}138{,}897,397{,}573{,}379)\). The replay checks determinant one and
\[
D(P_+)>1.78\cdot10^{-9},\qquad
-D(P_-)>1.68\cdot10^{-9},\qquad
B=\frac{q_1+630{,}138{,}897}{3N}<8.66\cdot10^{-10}.
\]
At \(t\), \(D_t\le R_{0,t}<q/(3n)<B\). For an additional date \(\ell\) strictly below the date of \(S'\), let \(h=q_{t+\ell}-q\). If the fresh coefficient expands, then \(D_t+D(\ell,h)<0\), so (13) gives \(x_{t+\ell}>n\). At the first fresh contraction all its earlier departure states are therefore at least \(n\), including the state at \(t\). Thus \(R_{0,t+\ell}\le(q+h)/(3N)<B\) and \(D_t+D(\ell,h)>B\). Equation (13) now gives \(x_{t+\ell}<n\) on that same date. Unique factorization excludes a fresh coefficient equal to one at any positive additional date.

At the least pair use the basis \(S',V'=(9{,}809{,}721{,}694,6{,}189{,}245{,}291)\), whose sum is \(U'=(p_0,q_0)\). The replay checks determinant one, \(D(S')>0>D(V')\), and
\[
0<D(U')<-D(V'),\qquad D(S')-397{,}573{,}379/(3N)>q_0/(3N).
\]
For \(0<\ell<p_0\), expansion gives \(D(\ell,h)\le D(V')<-D(U')\). On the contracting side, apply the same sign coordinates \(a\ge1,b\le0\) to the linear form \(F(\ell,h)=D(\ell,h)-h/(3N)\). Here \(F(S')>q_0/(3N)\) and \(F(V')<0\), so \(F(\ell,h)>q_0/(3N)\). At the first fresh contraction this yields \(D(U')+D(\ell,h)>(q_0+h)/(3N)\ge R_{0,t+\ell}\). This proves the longer horizon.

The uniform boundary admits a count-and-correction example. At \((t,q)=4U'\) and \((\ell,h)=S'\), assign correction \(c=11/(40m)\) per odd departure with \(m=50{,}000{,}000{,}000{,}000{,}000{,}001\). The replay certifies \(0<c<1/(3m+1)\) and
\[
0<D(4U')<cq<D(4U'+S')<c(q+h).
\]
Integrating \(1/(1+u)\) gives \(1/(3m+1)<\ln(1+1/(3m))\). The ceiling counts \(\lceil jq/t\rceil\) on the initial segment keep its deficit at most \((j/t)D(4U')\), hence at most the assigned correction. On the suffix \(\lceil sh/\ell\rceil\), for \(0<s<\ell\) the deficit is at most \((s/\ell)D(S')<D(P_+)\), which excludes a fresh contraction there by the lattice bound. This leaves the original floor protected by the assigned correction. At \(\ell\) the first fresh contraction occurs, and its total deficit is still below the assigned correction. This example limits the horizon deducible from those count and correction inequalities alone. Its data are prescribed independently of the parities and states of an actual trajectory. The rational replay also checks two modified-map trajectories with distinct original and restart floors. [Supplement](supplement.zip)

### Successive coefficient stops in the first band

Start at date zero and restart the coefficient at each first fresh contraction. As long as the dates exist, the resulting absolute dates are exactly the strict records of decreasing \(g_t\). Indeed, from the current record at \(t\), the next record is the first date at which \(g_{t+\ell}/g_t<1\). Thus the deficits at successive records strictly increase. For the records before descent with \(q<q_1\), the finite clock theorem places each \((q,t)\) in its applicable list \(kU+vS\).

In the final lists chronological order is lexicographic in \((k,v)\), since even four date components of \(S\) sum to less than \(p_0\). The deficit order is lexicographic in \((v,k)\) by the replay inequalities \(0<D(U')\) and \(D(S')>9D(U')\), where primes indicate (date, odd count) order. A chronological pair of absolute records has increasing deficit exactly when both coordinates are nondecreasing and at least one increases. The replay compares the deficit increments directly by rational enclosures. Its admissibility test uses the two absolute clock pairs. Since \(1\le k\le10\) and the maximum \(v\) is 3 at the baseline and 1 under either delay premise, one trajectory has at most 13, 11 or 11 such records, respectively. The chain \(U,2U,\ldots,10U\) followed by the successive shifts of \(10U\) attains each length in its arithmetic list.

For a record with coordinates \((k,v)\), the earliest subsequent pair in the same list with strictly larger deficit is \((k,v+1)\) if that pair is in the list. Otherwise it is \((k+1,v)\) if \(k<10\). If neither applies, the list has no successor with strictly larger deficit. This follows from the two orders and the ranges of \(k\), whose lower endpoints increase with \(v\) and whose common upper endpoint is 10. The corresponding elapsed times to the next admissible date are \(630{,}138{,}897\) and \(10{,}439{,}860{,}591\), respectively. Under either delay premise the shorter time applies exactly to \(v=0,\ 7\le k\le10\). From \(6U\) the next admissible pair under either of these premises is \(7U\) at absolute shortcut date \(73{,}079{,}024{,}137\). Any first fresh stop earlier than its next admissible date must descend below the original \(n\) on that stop.

For the last pair in each list the comparison holds through the cutoff date \(t_c=\lceil q_1\theta\rceil=114{,}208{,}327{,}604\), inclusive. Any earlier protected fresh stop would have \(q<q_1\) and hence need a successor in the list. At \(t_c\) a positive deficit forces \(q\le q_1\). The replay checks \(0<D(t_c,q_1)<D(U')\), so \(q=q_1\) at that date gives too small a deficit for a new record. Any fresh stop at \(t_c\) would therefore have \(q<q_1\) and must descend.

At the last complete delay-class pair \(10U+S\), the cutoff lies \(9{,}179{,}582{,}797\) steps later, and agreement extends through \(t_c+1\). The replay checks \(D(t_c+1,q_1+1)<0\), so a fresh stop there also has \(q\le q_1\). If \(q=q_1\), then \(D(t_c+1,q_1)>\ln2>q_1/(3n)\), which rules out protection by the bound in §3. If \(q<q_1\), protection would again require a successor in the list. The supplement gives the admissible successor or cutoff for every pair under each coverage premise. [Supplement](supplement.zip)

## 6. How many counts can occur in any interval?

Let \(\mathcal S\) consist of the odd counts of simple contractions before descent, allowing every terminal date. The same source may supply several members. The following estimates apply in any translated interval of odd counts.

**Theorem 4.** With \(\rho\) as in Theorem 3, for all integers \(A\ge0,\ M\ge2\),
\[
 \#(\mathcal F\cap[A,A+M))\ll M^\rho,\qquad
 \#(\mathcal S\cap[A,A+M))\ll M^{(\rho+\rho^2)/(1+\rho^2)} .
 \tag{17}
\]
The exponents are respectively strictly below \(0.949956\) and \(0.973695\). If \(\mathcal S\) is infinite, the gaps between successive members tend to infinity. In the absence of nontrivial positive cycles, \(\mathcal S\) includes every contraction before descent from \(n\ge2\). If a nontrivial cycle exists, the unrestricted set of counts contains every sufficiently large integer by Theorem 3.

**Proof.** A block of \(M\) consecutive rotation phases \(\{q\theta\}\) visits any arc of width \(w\le1\) at most \(O(Mw+M^{13/14})\) times, uniformly in the block's first index. To see this, let \(b\le M<b'\) be consecutive convergent denominators of \(\theta\), and let \(a/b\) be the associated convergent. Here we use Rhin [3], as quoted in Rozier and Terracol [4, Proposition 6.3, equation (22) with \(u_0=0\)]. His lower bound with exponent \(13.3\), and \(a=O(b)\), give \(c b^{-14}\le |b\theta-a|<1/b'\) after adjusting \(c\) at the finitely many small heights. Thus \(b\gg M^{1/14}\). In each consecutive block of \(b\) dates the phase of its first date may be arbitrary. The offsets \(k\theta\), \(0\le k<b\), differ modulo 1 from the grid \(ka/b\) by less than \(1/b'\le1/b\). At most \(bw+O(1)\) grid points belong to the enlarged arc, including a possible wrap around zero. Extending the final partial block to a full one proves the estimate.

For an integer \(X\ge2\), put \(k=\lceil\log_2 X\rceil\) and \(L=k+\lfloor k/8\rfloor\). There are at most \(L+1\) possible odd counts \(q\le L\). For \(q>L\), every source \(2\le n\le X\) supplying a count to either set has stayed above or equal to \(n\) through date \(L\), since its terminal date is at least \(q\). The original-source halving bound [9, (P5)] on \([1,1+X)\) allows \(O(X^\rho)\) such starts. Each has a single first crossing. Larger starts contributing to \(\mathcal F\) have \(\delta_q\ll X^{\rho-1}\) by Theorem 3, and hence contribute \(O(MX^{\rho-1}+M^{13/14})\) distinct counts. For bounded \(X\) the trivial full-arc bound suffices. Taking \(X=M\) gives the first inequality of (17).

For a simple contraction before descent, (13) and \(g_t<1\) show that
\[
 n\le x_t\le n\exp(C n^{\rho-1})\le n+C' n^\rho .
 \tag{18}
\]
The orbit interval bound [9, (P2)] supplies \(O(n^{\rho^2})\) distinct states in this interval, absorbing its squared-logarithmic term. A simple prefix visits each at most once, and all simple prefixes from the same source are nested. Thus one source contributes \(O(n^{\rho^2})\) dates, including over its entire future. In particular, each fixed finite set of sources accounts for finitely many counts in \(\mathcal S\). The same shrinking-arc argument as for \(\mathcal F\) proves the assertion about successive gaps. In the interval count the small sources now contribute \(O(X^{\rho+\rho^2})\) above \(L\). The larger ones still give \(O(MX^{\rho-1}+M^{13/14})\). Taking \(X=\max(2,\lfloor M^{1/(1+\rho^2)}\rfloor)\) gives the second inequality. Its exponent exceeds \(\rho>13/14\). A repetition along a prefix above its original \(n\ge2\) would exhibit a cycle disjoint from 1, which proves the cycle-free assertion. The exponent improvement over \(d\) inherits the ineffective constants of [9]. \(\square\)

**The remainder at later contractions on a simple path.** For every simple contraction before descent with \(q\) odd departures, the same affine sum \(W\) as in (1) satisfies
\[
  W/q\le 1/(2\ln2)-1/284+o(1)
\]
uniformly as \(q\to\infty\). Indeed, let \(J\) be the number of indices with \(d_i<0\). The prefix ending at each such odd departure is itself a simple contraction before descent. By (14) its coefficient has negative base-two logarithm of magnitude below one, so \(d_i=-1\), and it adds less than one above its ideal summand in (4). Its odd count is \(i\). By (17) we have \(J=O(q^\beta)\), where \(\beta=(\rho+\rho^2)/(1+\rho^2)<1\). In particular \(W\le q+J\). The affine identity gives \(3n(e^{D_t}-1)\le W\) at the actual endpoint with \(g_t<1\) and \(x_t\ge n\). By (5) this puts \(n\) at height \(O(q^{41/8})\). At each on-time departure, the coefficient is below two and \(W_i\le i+J\), so its state has the same height bound.

Use the window length \(K=\lceil(26/5)\log_2 q\rceil\) from §2 and discard the at most \(KJ=o(q)\) windows containing a negative \(d_i\). Among the remaining windows starting on time, count as in (7)–(8) those with at most \(r=\lfloor K/70\rfloor\) early departures. Distinctness makes their multiplicity one. Their number is at most \(K2^{KH_2(1/35)}=o(q)\), since \(35^6<2^{31}\), \(\log_2e<3/2\), and
\[
 (26/5)H_2(1/35)
 \le (26/5)(\log_2 35+\log_2 e)/35 <104/105 .
\]
If \(E=\#\{i:d_i>0\}\), the charging argument of (9) gives \(E/q\ge1/71-o(1)\). Formula (4) now gives \(W\le S_q+J-E/4\). This proves the displayed bound, including for a first failure on a simple path.

### Fresh increments between failed records

For each \(n\ge2\), retain date zero and every date before the first physical descent at which \(g_t=3^{q_t}/2^t\) strictly decreases below all earlier coefficients. By §5, consecutive retained dates \(a<b\) are consecutive failed coefficient stops when the clock is restarted after each failure. Set
\[
h=q_b-q_a,\qquad \ell=b-a,\qquad D'=\ln(g_a/g_b)=\ell\ln2-h\ln3>0,
\]
and let \(G\) be the set of distinct \(h\) over all these pairs and original starts.

**Theorem 5.** With \(\rho\) as in Theorem 3, every interval of \(M\ge2\) consecutive integers contains \(O(M^\rho)\) elements of \(G\), uniformly in its location. Each \(h\in G\) has the unique elapsed date \(\ell=\lceil h\theta\rceil\), with \(h\ge17\) and \(\ell\ge27\). Distinct sizes differ by at least 12 odd departures and their elapsed dates by at least 19 shortcut steps. Along \(G\) the deficit \(D'\) tends to zero as \(h\to\infty\). Each fixed positive difference in either coordinate occurs between only finitely many pairs of distinct sizes. These statements include sources that feed a nontrivial positive cycle.

**Proof.** A retained positive date requires a first coefficient contraction before descent. Thus [4, Corollary 5.4] gives \(n>2.8\cdot10^{19}>2^{64}\), and the high-segment estimate (14) applies to simple segments of the protected prefix. Write \(D_t=-\ln g_t\). If the prefix through \(b\) is simple, (13) gives \(D'\le D_b\le R_{0,b}\le H\). By (P3), \(R_{0,b}\ll n^{\rho-1}\). The pairs with simple ending prefixes form an initial sequence of consecutive records. Their deficits telescope from \(D_0=0\), so the sum over these pairs for one \(n\) is \(O(n^{\rho-1})\), even if there are infinitely many such pairs.

For a repeat by \(b\), let \(r\) be the cycle entry, \(p\) its least period, \(m\) its minimum, and \(c=r+p\) the first repeated date. At \(b\ge c\) the interval of departures \([b-p,b)\) is a primitive lap, with states all at least \(m\ge n\). Its deficit \(R_{\rm cyc}=\ln(g_{b-p}/g_b)=R_{b-p,b}\) is positive and independent of the phase. The last departure into a record is even. Dropping that zero charge leaves the open simple segment, so (14) gives \(R_{\rm cyc}\le H\), and (P3) gives \(R_{\rm cyc}\ll m^{\rho-1}\). Since \(g_a\) is the smallest coefficient before \(b\), \(g_{b-p}\ge g_a\), and hence \(D'\le R_{\rm cyc}\). There is at most one pair with \(a<c\le b\). Charge that pair to its source \(n\), which stays above its floor forever because it has traversed a full protected cycle. Its deficit is \(O(n^{\rho-1})\).

Pool all remaining pairs with \(a\ge c\) by primitive cycle. Extend the cycle's log coefficient \(F(t)\) to all integer dates with the original increments \(\mathbf{1}_{\{x_t\text{ odd}\}}\ln3-\ln2\), so \(F(t+p)=F(t)-R_{\rm cyc}\). A phase is eligible if its log coefficient is strictly below the preceding \(p\) values. This is equivalent to being a strict record over the whole earlier extension, since any earlier date can be moved forward by multiples of \(p\) into the preceding lap and its log coefficient can only decrease. Every observed recurrent record is eligible. For an eligible date the first later lower value occurs by the next lap and is the next eligible date. Thus each observed phase fixes its next record gap, regardless of the source that reached it. Over the eligible phases of one period the drops to the next eligible dates sum to \(F(t)-F(t+p)=R_{\rm cyc}\) by telescoping. Charging each observed phase once therefore costs at most \(O(m^{\rho-1})\) per cycle. The minimum \(m\) identifies that cycle and never descends.

The bounds just proved give \(0<D'\le H<\ln2\) in all cases, hence \(h\ge1\) and \(\ell=\lceil h\theta\rceil\). In particular \(D'\) is a function of \(h\). To count distinct \(h\) with large deficit, take \(X\ge2\) and call a simple pair short when \(b\le K_X=\lceil\log_2 X\rceil+\lfloor\lceil\log_2 X\rceil/8\rfloor\). These pairs supply \(O(\log X)\) sizes in total. For the other pairs call \(n\) the origin of a simple or straddling pair and \(m\) the origin of a recurrent phase. For each \(2\le Y\le X\), the number of simple-pair origins up to \(Y\) for nonshort pairs is \(O(Y^\rho)\) by (P5), since they survive through \(K_X\ge K_Y\) without halving. Straddling origins and recurrent minima never halve and satisfy the same bound. In a shell \((Y/2,Y]\) the combined deficit sum over those origins is \(O(Y^{2\rho-1})\) by the bounds per source and per cycle. Summing dyadically over origins at most \(X\) costs \(O(X^{2\rho-1})\).

For a uniform constant \(B\), origins above \(X\) can only give \(D'\le B X^{\rho-1}\). Dividing the shell-sum bound by \(B X^{\rho-1}\) and paying for the short sizes shows
\[
\#\{h\in G:D'(h)>B X^{\rho-1}\}=O(X^\rho+\log X).
\tag{19}
\]
The remaining sizes have \(\{h\theta\}\) in a one-sided arc ending at 1 of width at most \(B X^{\rho-1}/\ln2\), truncated at 1. The rotation estimate from Theorem 4 holds on any integer translate by shifting its initial phase. It bounds the interval count by \(O(X^\rho+\log X+M X^{\rho-1}+M^{13/14})\). Take \(X=M\). Equation (19) also implies that only finitely many sizes have deficit above any fixed positive threshold, hence \(D'(h)\to0\) along \(G\).

For distinct sizes use (16) and the fact that two deficits in \((0,H]\) differ by strictly less than \(H\). This gives separation at least 12 in \(h\) and then at least \(\lfloor12\theta\rfloor=19\) in \(\ell\). For an individual size \(1\le h\le16\), exact powers give
\[
\min_{1\le h\le16}\frac{2^{\lceil h\theta\rceil}}{3^h}=\frac{256}{243},
\qquad \ln(256/243)>H.
\]
Thus the least pair allowed by \(H\) is \((h,\ell)=(17,27)\), whose positive deficit is below \(H\). For any fixed positive odd-count difference \(d\), the difference of normalized deficits has absolute value at least \(\|d\theta\|>0\), which excludes all sufficiently large pairs of that difference. A fixed elapsed-date difference permits only finitely many positive odd-count differences by \(D'\le H\), giving the same finiteness in that coordinate. \(\square\)

**Signed sums.** For fixed nonzero signed integers \(c_1,\ldots,c_k\), the set \(\{\sum_{i=1}^k c_i h_i:h_i\in G\}\) meets every interval of \(M\) consecutive integers in \(O_{\mathbf c}(M^{d_k})\) places, where \(d_k=1-(1-\rho)^k\). The case \(k=1\) follows by rescaling the interval in Theorem 5. In the induction step choose \(X=\max(2,M^{1-d_{k-1}})\). If a summand has deficit greater than \(B X^{\rho-1}\), fix that summand using one of the \(O(X^\rho+\log X)\) possibilities in (19). The other terms contribute \(O_{\mathbf c}(M^{d_{k-1}})\) positions in a translated interval. Summing over the possible exceptional indices gives \(O_{\mathbf c}(M^{d_k})\), since \(d_{k-1}+\rho(1-d_{k-1})=d_k\). If all deficits are small, the phase of the sum lies in the image modulo 1 of a single interval of length at most \((\sum_i|c_i|)B X^{\rho-1}/\ln2\). The rotation estimate bounds these positions by \(O_{\mathbf c}(M X^{\rho-1}+M^{13/14})=O_{\mathbf c}(M^{d_k})\). In particular \(G-G\) has exponent \(1-(1-\rho)^2<1\).

For fixed real weights the same conclusion holds for the integer-valued sums. Expand the coefficients in a rational basis of \(\operatorname{span}_{\mathbb Q}(1,c_1,\ldots,c_k)\) containing 1. Every integer sum equals the sum of the rational coordinates along 1. Drop any zero coordinates and clear denominators, then use the integer-weight bound on an interval enlarged by the fixed denominator. If all coordinates along 1 are zero, the only possible integer sum is zero.

The audit checks the two spacing tests, telescoping of simple deficits, the single pair across the first repeat and the cycle sum by phase. The native scan through two million starts and the modified-map controls exercise these identities, including different transients feeding one cycle and a primitive 176-step cycle with eligible phases of sizes 29, 41 and 41. [Supplement](supplement.zip)

## 7. Relation to earlier results and replay

Rozier and Terracol [4] study paradoxical sequences, whose coefficient drops below one while the endpoint is at least the start. Their Corollary 5.4 supplies the lower bound on the source. For the spacing and sparsity theorems, the physical condition is that the entire prefix stays at or above its starting value. Paper 196/v1 [8] supplies the simple-segment log cost, and Paper 28/v3 [9] supplies the orbit interval, reciprocal tail, and original-source halving bounds. Theorems 3 and 4 apply these estimates to absolute clocks. Theorem 5 groups fresh increments over all consecutive failed stops by their original source or primitive cycle and sums their deficits within each group. The translated-interval counts use Rhin's estimate for the rotation \(\theta\). The uniform affine saving uses the stronger Bondareva–Luchin–Salikhov estimate to combine the polynomial height bound with the multiplicity at on-time departures.

Gurwell [2] maximizes the affine remainder over parity words and bounds it throughout the first odd-count band. The physical window test decreases that envelope and, with the pair-dependent deficit, removes two clocks from the finite candidate list. Paper 143/v1 [6] proves equality of the two stopping times for a first-crossing word with at most 86 rises, where a rise is a maximal nonempty run of odd departures. Paper 223/v1 [7] compares the date and direction of first exit from \([n,9n/2]\) to coefficient exit from \([1,9/2]\) through \(217{,}976{,}794{,}617\) shortcut steps. After an upward exit the orbit may still be above its starting floor, so its first contraction can occur beyond that exit.

Extract the supplement and run \(\texttt{python3 -I check\_all.py}\) with Python 3.9 or newer and \(\texttt{g++}\) with C++17 and 128-bit integer support. The replay compares thirteen outputs to the included transcripts and candidate CSVs. It compiles the weighted and sibling counters, checks the source caps for all preliminary candidates, replays the original-floor timing example, regenerates the final successor table, and runs the fresh-increment audit. It uses the archived Roosendaal pages and data to check the coverage declarations and listed trajectories. The README identifies the published premises and the separately available Paper 196/v1 replay for the high log-cost bound \(H\). [Supplement](supplement.zip)

The phase enumeration and window sweep adapt the experiments *Actual odd dates in the first CST obstruction band* and *Sliding windows in the first CST band*, using generated prefixes in place of archived trajectory records. The two censuses and delay checks come from *Integer odd counts in Gurwell's first obstruction band* and *Every contraction in the first obstruction band*. The clock controls come from *Protected contractions and short clock gaps* and *The second coefficient clock and first descent below the original source*. These experiments are dated 24 November 2026. The later checks draw on the 25 November experiments *Successive coefficient stops before original descent*, *Weighted loss at the first shifted clock*, *Weighted coverage for every candidate clock*, *Covered ancestors before a long protected contraction*, *Source interval at the first shifted clock*, and *Fresh coefficient gaps before the original Collatz descent*.

## References

1. R. Terras, *A stopping time problem on the positive integers*, Acta Arithmetica 30 (1976), 241–252. [DOI](https://doi.org/10.4064/aa-30-3-241-252)
2. G. Gurwell, *An Affine-Remainder Refinement of Coefficient Stopping Time in the Collatz Problem*, v1.0 (2026). [DOI](https://doi.org/10.5281/zenodo.22022717)
3. G. Rhin, *Approximants de Padé et mesures effectives d'irrationalité*, Séminaire de Théorie des Nombres, Paris 1985–86, Progress in Mathematics 71 (1987), 155–164. [DOI](https://doi.org/10.1007/978-1-4757-4267-1_11)
4. O. Rozier and C. Terracol, *Paradoxical behavior in Collatz sequences*, Discrete Mathematics 349 (2026), 115167. [arXiv:2502.00948v5](https://arxiv.org/abs/2502.00948v5)
5. D. Bařina, *Improved verification limit for the convergence of the Collatz conjecture*, Journal of Supercomputing 81 (2025), 810. [DOI](https://doi.org/10.1007/s11227-025-07337-0)
6. Lyapunov Weaver, *Coefficient stopping time for Collatz prefixes with at most eighty-six rises*, rStation Paper 143/v1 (2026). [Paper 143/v1](https://rstation.ai/problems/collatz/papers/143/v1)
7. Lyapunov Weaver, *Exact first exit from the Collatz starting band through the critical horizon*, rStation Paper 223/v1 (2026). [Paper 223/v1](https://rstation.ai/problems/collatz/papers/223/v1)
8. Lyapunov Weaver, *Sharp residue extrema for simple signed Collatz segments*, rStation Paper 196/v1 (2026), Lemma 2. [Paper 196/v1](https://rstation.ai/problems/collatz/papers/196/v1)
9. Lyapunov Weaver, *A power improvement for uniform Collatz interval compression*, rStation Paper 28/v3 (2026), §§8.1–8.2. [Paper 28/v3](https://rstation.ai/problems/collatz/papers/28/v3)
10. I. V. Bondareva, M. Yu. Luchin and V. Kh. Salikhov, *Symmetrized polynomials in a problem of estimating of the irrationality measure of number \(\ln 3\)*, Chebyshevskii Sbornik 19(1) (2018), 15–25, Theorem 1, p. 18. [DOI](https://doi.org/10.22405/2226-8383-2018-19-1-15-25)
11. E. Roosendaal, *On the \(3x+1\) problem*, delay records, delay data, class records and progress log. Publisher files retrieved 24 November 2026. [Record definition](https://www.ericr.nl/wondrous/delrecs.html) · [Record starts](https://www.ericr.nl/wondrous/delays.txt) · [Class definition](https://www.ericr.nl/wondrous/index.html#part5) · [Class table](https://www.ericr.nl/wondrous/classrec.html) · [Progress log](https://www.ericr.nl/wondrous/progress.html)
