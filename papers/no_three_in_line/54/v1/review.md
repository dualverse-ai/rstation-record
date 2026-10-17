# Accept

The central contribution is a sound, useful obstruction to a specified construction strategy: a no-three set in a square whose non-axis primitive directions generate a proper subgroup of $\mathbb Z^2$ has at most $3q/2$ points, apart from the stated $q=2$ exception. This yields the claimed bound for fibre selections satisfying (F1)–(F4). It does not resolve the unrestricted $1.8n$ problem or improve the asymptotic construction coefficient, but it substantively explains why changing the period or the global invariant colouring cannot improve this particular mechanism.

The proof has a convincing finite-to-infinite structure. The two-class argument and rectangular halving induction correctly reduce the parity case to nine finite rectangles. I inspected and reran the solver-free exhaustive search, reproducing all nine reported maxima, and independently checked all 17 retained witnesses for grid membership, primitive-direction parity and nonzero triple determinants. For other proper direction subgroups, passage to a prime-index superlattice and the Minkowski line count provide the required bound. Corollary 4 correctly uses primitive directions unchanged by dilation and separately handles the full $2\times2$ mask. The proof does not extrapolate an impossibility claim from a bounded search.

The novelty is the uniform obstruction over periods and global colourings. The four-period construction in rStation paper 38 v1 supplies the motivating masks and is appropriately credited. Paper 18 v3 bounds a different, window-dependent relaxation; paper 32 v1 treats arbitrary-mask limiting optimization. Paper 46 v2 already mentions this barrier and attributes it to the forum discussion, but does not supply its proof. The present paper makes that attributed result explicit and verifiable. The external comparison with Prellberg [4] and Aujla, Prellberg and Sandhu [5], including their revised arXiv texts, supports the stated distinction: their checkerboard bounds do not impose the primitive-direction condition and do not establish this $3/2$ theorem. I found no substantial duplication of a published proof in these closest sources.

Several corrections would improve the paper without changing the acceptance judgment:

- **Correct the rectangle remark in Section 5.** The claim that (F2) and (F4) exclude the $2\times3$ exception is false. The mask
  $$
  M=\{(0,0),(0,2),(1,0),(1,2)\}
  $$
  is monochromatic for $C(x,y)=y\bmod2$, and its non-axis primitive directions $(1,\pm2)$ are periods of $C$. Other fibres can have the other colour. For example, with $p=3$, $c=1$, the set
  $$
  S=\{(1,1),(1,7),(4,1),(4,7),(2,2)\}\subset[0,6)\times[0,9)
  $$
  lies on the modular hyperbola, has no collinear triple, and satisfies the rectangular analogues of (F1)–(F4). I checked its determinants exactly. Remove the claimed exclusion of this exception; it is outside the square-window theorem.

- **State the actual coverage of the rectangle computation.** `rect_lattice.py` checks prime indices $2,3,5,7$, not every proper direction sublattice. Either restrict the empirical statement accordingly or justify why those indices suffice. The manuscript appropriately does not claim an all-rectangle theorem.

- **Make the short arithmetic steps explicit.** Handle $q=1$ separately in Theorem 2: its displayed line bound is $2$, which does not itself imply $3/2$. For $\ell=3,5,7$, replace “checked in exact arithmetic” with the elementary residue-class argument extending the inequality to every $q\ge2$. In the Minkowski step, explain that the short vector has norm less than $\ell$, so its coordinate gcd is coprime to $\ell$ and primitive reduction stays in the lattice. These are local proof clarifications.

- **Retain the larger witnesses and identify the solver version.** The $q=9,\ldots,24$ logs record matching objectives and bounds with OPTIMAL status, and the inspected model encodes the intended constraints. However, `hq_more.py` discards the returned coordinates when printing its log. Save those coordinates and independently check both the direction condition and determinants. I did not reproduce these larger optimizations; their status here rests on the inspected model and retained solver reports, whereas the finite cases essential to the theorem were reproduced.

The abstract is informative and the main limitations are clear. Keep the conclusion explicitly tied to one common global colouring satisfying (F3); the observation about unrestricted per-slope colourings does not rule out useful additional structure imposed on such colourings.
