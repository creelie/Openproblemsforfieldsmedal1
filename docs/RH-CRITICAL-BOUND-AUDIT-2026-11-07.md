# The critical Liouville energy bound in version 2.6.0

The bound required to prove RH has not been established. This revision does not prove RH, GRH or a new zero-free half-plane.

## Target

For the actual Liouville function, let B(X)=sum lambda(n) exp(-n/X). The required estimate is the local mean square H_B(X)=O_epsilon(X^(1+epsilon)), for every positive epsilon and all X at least one. Section 12.1 explains both directions of its equivalence to RH. The signed correlation upper estimate needed to prove it remains open.

## Proved addition

Section 12 contains a quantitative approximation theorem for completely multiplicative comparison functions. These functions agree exactly with Liouville on a prescribed finite prime prefix, preserve every logarithmic summatory and additive-twist saving, and approximate every prescribed finite normalized Abel jet to arbitrary precision. Each fixed comparison function nevertheless retains a pole at a chosen real beta between one half and one, and its critical local energy estimate fails.

The proof supplies an explicit upper bound for the logarithm of the relative Euler product, a zero-free disk estimate derived directly from Euler summation, a Cauchy derivative estimate, and a dyadic Mellin argument proving local-energy failure. The cutoff formula is explicit. For beta=3/4, r=1/8 and P=2^320, the first four normalized Abel derivatives differ from Liouville's by less than 10^-6. The exact-rational checker certifies the constants, not an infinite-scale computation.

The exact leading Abel coefficient remains rigid and singles out Liouville. The comparison functions have a strictly different coefficient. Therefore the new theorem does not disprove RH or show that the desired estimate for Liouville is false. It proves a precise limitation of replacing an exact arithmetic identity with finite-precision local data.

## Verification and scope

An independent mathematical review checked the new proof, constants and quantifiers. The source ZIP includes anc/abel-jet-bounds.py, mapped from checks/abel-jet-bounds.py in the repository. No new Lean formalization has been produced. No independent literature-priority or journal-acceptance claim is made. The AI use declaration identifies the new section and the assistance used.
