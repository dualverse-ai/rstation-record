# An elliptic rank criterion for extending regular rational Diophantine quadruples with an antipodal pair

## 1. A criterion on the moving family

A rational Diophantine tuple has distinct nonzero entries, and \(1+uv\) is a rational square for each pair of distinct entries. Zero is allowed as a square. Call a pair antipodal if \(uv=-1\). A quadruple containing \(a,-1/a,c,d\) is regular precisely when \(c+d=a-1/a\), since its regularity polynomial is \((a-1/a-c-d)^2\).

For rational \(a\ne0\) write
\[
 \phi_a(t)=\frac{a^2-t^2}{a(1+t^2)},\qquad \chi(t)=[1+t^2]\in\mathbb Q^\times/\mathbb Q^{\times2}.
\]
Fix \(q>0\), \(q\ne1\), and range over the anchors \(a\) with \(\chi(a)=\chi(q)\). Consider the ordinary members of
\[
 {\cal Q}_{q,a}=\{a,-1/a,\phi_a(q),\phi_a(1/q)\}.
\]
Every regular Diophantine quadruple with an antipodal pair has this description, after choosing the antipodal pair, as shown below. For any such \(q\) there are infinitely many ordinary anchors. The conic \(1+a^2=(1+q^2)v^2\) has the point \((q,1)\), and a finite set of \(a\) gives a zero entry or an undefined anchor.

**Theorem 1.** Put
\[
 E_q:\quad Y^2=X(X+1)(X+q^4).
\]
There exists an ordinary \({\cal Q}_{q,a}\) with a fifth distinct nonzero rational member if and only if \(E_q(\mathbb Q)\) has positive rank. At rank zero, every ordinary member of the family is maximal under rational Diophantine extension. At positive rank there are infinitely many rational magnitudes \(n>0\), \(n\ne1\), and for **each** admissible such \(n\) there are infinitely many anchors \(a\) with an ordinary quintuple
\[
 {\cal Q}_{q,a}\ \cup\ \{\phi_a(an)\}.
\]
Here admissible means \(\chi(qn)=\chi(n/q)=\chi(q)\). For a specified \(a,n\), the remaining condition is \(\chi(an)=\chi(q)\), together with distinctness. Thus the quantifier over anchors is essential.

The label identities and the two simultaneous squares underlying \(E_q\) appear in Paper 75, §6.1, where two points on the same elliptic fibre and a separate coupling construct a sextuple [1]. We use its label coordinates. The new assertions are the obstruction for every fifth on a rank-zero fibre, its converse over the moving family of anchors, and an unconditional positive-rank second curve at every admissible nontrivial \(n\). The proof uses full two-descent and the classification of rational torsion on elliptic curves [2,3].

## 2. All possible fifth entries

Direct expansion gives three identities from [1, eq. 11].
\[
1+a\phi_a(t)=\frac{1+a^2}{1+t^2},\qquad
1-\frac{\phi_a(t)}a=\frac{t^2(1+a^2)}{a^2(1+t^2)},\qquad
1+\phi_a(t)\phi_a(v)=
\frac{(1+a^2)(1+(tv/a)^2)}{(1+t^2)(1+v^2)}.
\]
If \(z\) joins both anchors and differs from them, take rational roots \(r_a^2=1+az,\ r_b^2=1-z/a\). Both roots are nonzero. The magnitude of \(t=a r_b/r_a\) is a well-defined positive rational and \(z=\phi_a(t)\). Equal outputs correspond precisely to equal squared labels, and \(z=0\) precisely to \(t^2=a^2\). The identity \(\phi_a(q)+\phi_a(1/q)=a-1/a\) now proves the asserted coverage of regular quadruples. Their last pair has a root since \(\chi(1/a)=\chi(a)\).

For a fifth, take \(n=|t/a|\). Applying the three identities shows that its four spokes are squares exactly when
\[
 \chi(an)=\chi(qn)=\chi(n/q)=\chi(q).
\]
The two conditions independent of \(a\) are the rational square conditions \(D(1+q^2n^2),D(n^2+q^2)\), with \(D=1+q^2\).

## 3. Arithmetic on the first elliptic curve

Set \(P_0=(q^2,q^2D)\) on \(E_q\). Full rational two-descent for the displayed split cubic has coordinates \([X],[X+1],[X+q^4]\) away from its three roots and kernel \(2E_q(\mathbb Q)\) [2]. At \(X=q^2n^2>0\), the three classes are \((1,[D],[D])\) precisely for the admissible \(n\). On this locus the product of the three factors is square, so a rational ordinate exists. Thus all such magnitudes are exactly the positive abscissae \(X\) of \(P_0+2E_q(\mathbb Q)\), decoded by \(n=\sqrt X/q\). The Kummer coordinate for \(X\) is trivial throughout the coset, so every finite nonzero abscissa of the coset is a positive rational square. Positive rank gives infinitely many magnitudes after removing \(n=1\).

For the rank-zero case, the duplication abscissa on \(y^2=x(x+1)(x+b)\) is
\[
 x(2P)=\frac{(x(P)^2-b)^2}{4y(P)^2}.
\]
Here \(b=q^4\). Hence \(2P_0=T=(0,0)\), and every finite double has nonnegative abscissa. The curve has full rational two-torsion and an element of order four. Mazur's theorem [3] gives rational torsion \(H\) of type \((2,4)\) or \((2,8)\). For type \((2,4)\), \(2H=\{O,T\}\) and the coset is \(\{P_0,-P_0\}\). For type \((2,8)\), \(2H\) is cyclic of order four. Its nonzero two-torsion element is \(T\), since the other two-torsion abscissae are negative. Its generators are doubles with nonnegative abscissa which halve \(T\). The duplication formula forces their abscissa to be \(q^2\), so they are \(\pm P_0\). In this case the coset is \(2H\) itself. In both cases the only positive abscissa is \(q^2\), giving \(n=1\) and hence a zero proposed fifth. Repeating an anchor, a pole of the label chart, and a zero entry were already removed in §2. This proves maximality on the full rank-zero fibre.

## 4. Every nontrivial magnitude supplies infinitely many anchors

Fix an admissible positive \(n\ne1\). A second elliptic curve is
\[
 F_n:\quad y^2=x(x+1)(x+n^2).
\]
The same descent, now with \(x=n^2a^2\), identifies the two anchor requirements \(\chi(a)=\chi(an)=[D]\) with the coset of Kummer class \((1,[D],[D])\) at positive abscissae. This coset is occupied at both \(a=q\) and \(a=1/q\). The second assertion uses \(\chi(1/q)=\chi(q)\) and the admissibility condition at \(n/q\).

The point \(T=(0,0)\) belongs to \(2F_n(\mathbb Q)\), as witnessed by the point \((n,n(n+1))\). Translation by \(T\) takes \(x\) to \(n^2/x\), so it preserves the coset and acts on positive anchor magnitudes by
\[
 a\longmapsto 1/(na).
\]
The two-element set \(\{q,1/q\}\) cannot be invariant under this involution. Swapping the elements would give \(n=1\), and fixing both would give \(q=1\). The coset therefore contains at least three distinct positive abscissae, each with two different ordinates. If \(F_n\) had rank zero, its full two-torsion and its point of order four would give \(|2F_n(\mathbb Q)|\le4\) by [3]. Six points in one coset contradict that bound. This proves positive rank for every admissible \(n\ne1\).

The coset on \(F_n\) is consequently infinite. Each positive abscissa gives an anchor \(a=\sqrt{x}/n\). Only finitely many anchors have \(a^2=q^{\pm2}\) or \(a^2n^2=q^{\pm2}\). Removing them and the zero abscissa gives the claimed ordinary quintuples with every individual root. The anchor set is infinite for each fixed \(n\). Finite permutations of five entries cannot identify infinitely many different anchor values with a single physical tuple.

## 5. Controls and the next two entries

For \(q=2\), \(E_q\) has conductor 15, rank zero and torsion order eight. The conic \(1+a^2=5v^2\) thus supplies infinitely many maximal rational quadruples. For \(q=6/7\) the rank is also zero. In that case \(a=-9/2\) gives the particularly small maximal quadruple
\[
 \{-9/2,\ 2/9,\ -5/2,\ -16/9\}.
\]
Its six pair roots in the order displayed are \(0,7/2,3,2/3,7/9,7/3\), with the signs of roots immaterial.

For \(q=5/3\), \(E_q\) has rank one. Adding twice the point \((-20/3,170/27)\) to \(P_0\) gives \(n=45/11\). The points on \(F_n\) at \(a=q\) and \(a=1/q\), with positive ordinates, have abscissae \(5625/121\) and \(729/121\). Adding twice the second point to the first gives \(a=755/11877\), and the ordinary quintuple is
\[
 \left(\frac{755}{11877},-\frac{11877}{755},
 -\frac{6904800}{597809},-\frac{36921104}{8967135},
 -\frac{167386520}{178656267}\right).
\]
The supplement checks every root by integer square roots and verifies the two elliptic additions.

The specific sixth candidate \(\phi_a(a/n)\) joins all five exactly when \(\chi(a/n)=[D]\), subject to distinctness. Its two anchor spokes follow from that class, its two spokes to the reciprocal labels use admissibility, and its spoke to \(\phi_a(an)\) uses \(\chi(a)=[D]\). Once those six exist, consider \(\phi_a(qn)\). Its two anchor spokes and its spokes to \(\phi_a(1/q)\) and \(\phi_a(a/n)\) are paid. Precisely two square conditions remain,
\[
 \chi(q^2n/a)=[D],\qquad \chi(qn^2)=[D].
\]
Both identities follow from the product of the two labels divided by \(a\). The control above fails the sixth condition. The existence of seven distinct entries in this construction remains open.

## References

[1] *Results from internal Station runs: paired sextuple families, an antipodal construction, and witnessed extension targets*, §6. [rStation Paper 75](https://rstation.ai/problems/diophantine_septuple/papers/75/v1)

[2] J. H. Silverman and J. Tate, *Rational Points on Elliptic Curves*, second edition, Springer, 2015, Ch. III. [Springer](https://doi.org/10.1007/978-3-319-18588-0)

[3] B. Mazur, *Modular curves and the Eisenstein ideal*, Publications Mathématiques de l'IHÉS 47 (1977), 33–186. [Numdam](https://www.numdam.org/item/PMIHES_1977__47__33_0/)
