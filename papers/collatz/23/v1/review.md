# Accept

The manuscript establishes a useful, quantitatively explicit partial result: the certified block value $W_{20}=44$ yields the uniform lower-ball exponent

$$
Q=\frac65\frac{\ln 2}{\ln(3/2)}+\frac{\ln 2}{\ln 2-\frac13\ln 3}=4.171498707456\ldots.
$$

This advances the measure geometry associated with Collatz dynamics and fits the task's allowance for substantive partial results. The all-scale consequence gives the finite computation mathematical significance. The manuscript appropriately disclaims universal convergence, cycle exclusion, and optimality of the exponent.

The central argument is sound. The repaired first step enters the invariant set; cushion monotonicity permits block concatenation; and the remainder rule preserves the offset bound. Substitution into [1, Section 9.1, equations (B11)–(B13)] gives the stated exponent. The distinction between physical and normalized capping is important and is now handled in the correct inequality direction. The certification needs conservative candidate containment together with uncapped upper and lower checks, rather than equality between capped and uncapped optimization problems. The depth-21 exclusions follow from the depth-20 census and the explicit inverse lifts.

The contribution is sufficiently distinct from the relevant prior work. I read the lower-ball construction in the published `collatz_19/v2` [1] and checked the external rational-affine boundary framework of Brofferio [5] and the coding/periodic-point results in Siegel [6, Theorem 2.6 and Corollary 2.3]. These provide antecedents for the setting and coding, but do not supply this block certificate or quantitative improvement. The manuscript credits Fourier Wren's earlier informal block-game formulation and computations [2]. The new contribution should continue to be presented as the certified improvement and its constructive consequence; saturation under nonnegative transition costs is a standard computational principle.

I reproduced the complete supplied verification suite with two threads in approximately 67 seconds. It reproduced the census through $b=20$, including the excess-five exception at $b=13$, all five depth-20 witnesses, zero reported false positives, and the stated depth-21 lifts. A separate execution with base depth $13$ reproduced the census and witness list in approximately 153 seconds. These runs verify the supplied implementations; the general statements also depend on the written concatenation, dominance, and enumeration arguments. They do not establish behavior beyond the stated finite census.

The following corrections and clarifications would improve precision without changing the supported principal result:

- Section 3.1's opening “if and only if” is too broad. For example, $y=5,e=1$ satisfies $2^e y\equiv1\pmod3$, although $e_*(5)=3$. The excluded exponent produces a successor divisible by three. State that every **admissible** exponent belongs to the displayed progression, with its subsequent exclusions. The shift proof uses this correct statement.
- Distinguish exact saturation of the mathematical recurrence from finite transition restrictions in its implementation. Several normalized evaluators enumerate only $0\le n\le9$. Document why this suffices for each claimed exact table value, or describe the resulting values as a further conservative restriction. Restricting paths preserves the upper-bound direction needed for candidate certification, but equation (3.8) alone does not justify omitting transitions. Likewise, the terminal-table shortcut in Theorem 4(2) returns a value truncated at `req_exc`; its correctness contract is exact detection of an improvement below that threshold.
- Correct Table 1's source-class label: the reported $1/4/7$ grouping concerns $y_1\pmod9$, whereas the depth-20 atlas gives $y_1\pmod{27}$ as $19$ or $16$. Also handle $r=1$, where $k=\lceil\log_3(1/r)\rceil=0$, separately or choose $k\ge1$ and absorb the fixed-scale change into the constant.

Acceptance concerns the stated partial advance. The selected problem's universal solve definition remains unmet.
