# Finite Gram inequality

From this directory, run:

```sh
lake update
lake exe cache get
lake env lean GramCore.lean
```

The recorded check used Lean 4.34.1 and Mathlib at the revision in `lakefile.toml`. It ran the Lean executable with the existing Mathlib package build directories on `LEAN_PATH`. See `logs/GramCore.build.log` for the eleven axiom reports.

The final theorem constructs the Gram matrices from sign vectors, proves the diagonal and self-pairing bounds, and uses the supplied cross-pairing bound to give the finite dimension inequality. The passage from the collar to the cross-pairing bound, the scale count and the analytic parts of the paper are open formalization tasks.
