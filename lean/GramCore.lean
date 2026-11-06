import Mathlib.Algebra.Order.BigOperators.Ring.Finset
import Mathlib.Basic.Real.Basic
import Mathlib.Tactic.Linarith
import Mathlib.Tactic.Ring

/-!
# Finite Gram core for the deterministic collar obstruction

This file checks only finite real-matrix inequalities.  In particular it does not
formalize the passage from a sign sequence and its prefix correlation maxima to
the matrices, the counting of scales, any analytic continuation theorem, or RH.
No theorem in this file assumes that a matrix is positive semidefinite: its
explicit trace and Frobenius bounds are the sufficient finite hypotheses.
-/

namespace RH.GramCore

set_option autoImplicit false

open Finset

def frobenius {m : ℕ} (A B : Fin m → Fin m → ℝ) : ℝ :=
  ∑ r, ∑ s, A r s * B r s

def trace {m : ℕ} (A : Fin m → Fin m → ℝ) : ℝ :=
  ∑ r, A r r

/-- A matrix's diagonal square sum is bounded by its full square sum. -/
theorem diagonal_sq_le_frobenius {m : ℕ} (A : Fin m → Fin m → ℝ) :
    (∑ r, (A r r) ^ 2) ≤ frobenius A A := by
  unfold frobenius
  apply sum_le_sum
  intro r _
  calc
    (A r r) ^ 2 = A r r * A r r := by ring
    _ ≤ ∑ s, A r s * A r s := by
      exact single_le_sum (fun s _ => mul_self_nonneg (A r s)) (mem_univ r)

/-- Cauchy--Schwarz on the diagonal supplies the finite rank lower bound. -/
theorem trace_sq_le_dimension_mul_frobenius {m : ℕ}
    (A : Fin m → Fin m → ℝ) :
    (trace A) ^ 2 ≤ (m : ℝ) * frobenius A A := by
  have hcs := sum_mul_sq_le_sq_mul_sq (univ : Finset (Fin m))
    (fun _ => (1 : ℝ)) (fun r => A r r)
  have hdiag := diagonal_sq_le_frobenius A
  simp only [one_mul, one_pow, sum_const, card_univ, Fintype.card_fin,
    nsmul_eq_mul, mul_one] at hcs
  exact hcs.trans (mul_le_mul_of_nonneg_left hdiag (Nat.cast_nonneg m))

/-- Frobenius expansion for a finite sum, with all indices explicit. -/
theorem frobenius_sum {k m : ℕ} (A : Fin k → Fin m → Fin m → ℝ) :
    frobenius (fun r s => ∑ i, A i r s) (fun r s => ∑ i, A i r s) =
      ∑ i, ∑ j, frobenius (A i) (A j) := by
  unfold frobenius
  simp only [sum_mul, mul_sum]
  calc
    (∑ r, ∑ s, ∑ j, ∑ i, A i r s * A j r s) =
        ∑ r, ∑ j, ∑ s, ∑ i, A i r s * A j r s := by
      apply sum_congr rfl
      intro r _
      exact sum_comm
    _ = ∑ j, ∑ r, ∑ s, ∑ i, A i r s * A j r s := sum_comm
    _ = ∑ j, ∑ r, ∑ i, ∑ s, A i r s * A j r s := by
      apply sum_congr rfl
      intro j _
      apply sum_congr rfl
      intro r _
      exact sum_comm
    _ = ∑ j, ∑ i, ∑ r, ∑ s, A i r s * A j r s := by
      apply sum_congr rfl
      intro j _
      exact sum_comm
    _ = ∑ i, ∑ j, ∑ r, ∑ s, A i r s * A j r s := sum_comm

/-- Lower bound for the total Gram energy from the traces of the summands. -/
theorem family_rank_lower {k m : ℕ} (hm : 0 < m)
    (A : Fin k → Fin m → Fin m → ℝ)
    (htrace : ∀ i, trace (A i) = (m : ℝ)) :
    (k : ℝ) ^ 2 * m ≤ ∑ i, ∑ j, frobenius (A i) (A j) := by
  have h := trace_sq_le_dimension_mul_frobenius (fun r s => ∑ i, A i r s)
  have ht : trace (fun r s => ∑ i, A i r s) = (k : ℝ) * m := by
    unfold trace
    rw [sum_comm]
    change (∑ i, trace (A i)) = _
    simp only [htrace, sum_const, card_univ, Fintype.card_fin, nsmul_eq_mul]
  rw [ht, frobenius_sum] at h
  have hm' : (0 : ℝ) < m := Nat.cast_pos.mpr hm
  nlinarith

/-- A uniform off-diagonal bound controls all pairings in the family. -/
theorem family_energy_upper {k m : ℕ}
    (A : Fin k → Fin m → Fin m → ℝ) (B : ℝ)
    (hself : ∀ i, frobenius (A i) (A i) ≤ (m : ℝ) ^ 2)
    (hcross : ∀ i j, i ≠ j → frobenius (A i) (A j) ≤ B) :
    (∑ i, ∑ j, frobenius (A i) (A j)) ≤
      (k : ℝ) * m ^ 2 + ((k : ℝ) ^ 2 - k) * B := by
  calc
    (∑ i, ∑ j, frobenius (A i) (A j)) ≤
        ∑ i : Fin k, ∑ j : Fin k,
          (B + if i = j then (m : ℝ) ^ 2 - B else 0) := by
      apply sum_le_sum
      intro i _
      apply sum_le_sum
      intro j _
      by_cases hij : i = j
      · subst j
        simpa only [ite_true, add_sub_cancel] using hself i
      · simpa only [ite_eq_right hij, add_zero] using hcross i j hij
    _ = (k : ℝ) * m ^ 2 + ((k : ℝ) ^ 2 - k) * B := by
      simp only [sum_add_distrib, sum_const, card_univ, Fintype.card_fin,
        nsmul_eq_mul, sum_ite_eq, mem_univ, ite_true]
      ring

/-- Finite rank obstruction underlying the paper's scale-counting argument. -/
theorem gram_rank_obstruction {k m : ℕ} (hk : 0 < k) (hm : 0 < m)
    (A : Fin k → Fin m → Fin m → ℝ) (B : ℝ)
    (htrace : ∀ i, trace (A i) = (m : ℝ))
    (hself : ∀ i, frobenius (A i) (A i) ≤ (m : ℝ) ^ 2)
    (hcross : ∀ i j, i ≠ j → frobenius (A i) (A j) ≤ B) :
    (k : ℝ) * m ≤ m ^ 2 + ((k : ℝ) - 1) * B := by
  have hl := family_rank_lower hm A htrace
  have hu := family_energy_upper A B hself hcross
  have hk' : (0 : ℝ) < k := Nat.cast_pos.mpr hk
  have hmul : (k : ℝ) * ((k : ℝ) * m) ≤
      (k : ℝ) * (m ^ 2 + ((k : ℝ) - 1) * B) := by
    nlinarith
  exact le_of_mul_le_mul_left hmul hk'

/-- If there are `2m` matrices and every cross pairing is at most `16B`,
then `m ≤ 32B`. This is the numerical contradiction used in the paper. -/
theorem twice_dimension_bound {m : ℕ} (hm : 0 < m)
    (A : Fin (2 * m) → Fin m → Fin m → ℝ) (B : ℝ) (hB : 0 ≤ B)
    (htrace : ∀ i, trace (A i) = (m : ℝ))
    (hself : ∀ i, frobenius (A i) (A i) ≤ (m : ℝ) ^ 2)
    (hcross : ∀ i j, i ≠ j → frobenius (A i) (A j) ≤ 16 * B) :
    (m : ℝ) ≤ 32 * B := by
  have h := gram_rank_obstruction (by omega) hm A (16 * B) htrace hself hcross
  have hm' : (0 : ℝ) < m := Nat.cast_pos.mpr hm
  simp only [Nat.cast_mul, Nat.cast_ofNat] at h
  nlinarith

/-- The averaged Gram matrix of a finite collection of real vectors. -/
noncomputable def averagedGram {n m : ℕ} (v : Fin n → Fin m → ℝ) : Fin m → Fin m → ℝ :=
  fun r s => (∑ t, v t r * v t s) / (n : ℝ)

/-- Every diagonal entry of an averaged Gram matrix of signs equals one. -/
theorem averagedGram_diagonal {n m : ℕ} (hn : 0 < n)
    (v : Fin n → Fin m → ℝ) (hsign : ∀ t r, (v t r) ^ 2 = 1)
    (r : Fin m) : averagedGram v r r = 1 := by
  have hp : ∀ t, v t r * v t r = 1 := by
    intro t
    nlinarith [hsign t r]
  unfold averagedGram
  simp only [hp, sum_const, card_univ, Fintype.card_fin, nsmul_eq_mul, mul_one]
  exact div_self (Nat.cast_ne_zero.mpr (Nat.ne_of_gt hn))

/-- Entry squares of an averaged sign Gram matrix are at most one. -/
theorem averagedGram_entry_sq_le_one {n m : ℕ} (hn : 0 < n)
    (v : Fin n → Fin m → ℝ) (hsign : ∀ t r, (v t r) ^ 2 = 1)
    (r s : Fin m) : (averagedGram v r s) ^ 2 ≤ 1 := by
  have hc := sum_mul_sq_le_sq_mul_sq (univ : Finset (Fin n))
    (fun t => v t r) (fun t => v t s)
  simp only [hsign, sum_const, card_univ, Fintype.card_fin,
    nsmul_eq_mul, mul_one] at hc
  have hn' : (0 : ℝ) < n := Nat.cast_pos.mpr hn
  unfold averagedGram
  rw [div_pow]
  apply (div_le_iff₀ (sq_pos_of_pos hn')).2
  simpa only [one_mul, pow_two] using hc

/-- The trace and self-pairing hypotheses hold for actual averaged sign vectors. -/
theorem averagedGram_trace_and_self {n m : ℕ} (hn : 0 < n)
    (v : Fin n → Fin m → ℝ) (hsign : ∀ t r, (v t r) ^ 2 = 1) :
    trace (averagedGram v) = (m : ℝ) ∧
      frobenius (averagedGram v) (averagedGram v) ≤ (m : ℝ) ^ 2 := by
  constructor
  · unfold trace
    simp only [averagedGram_diagonal hn v hsign, sum_const, card_univ,
      Fintype.card_fin, nsmul_eq_mul, mul_one]
  · unfold frobenius
    calc
      (∑ r, ∑ s, averagedGram v r s * averagedGram v r s) ≤
          ∑ _r : Fin m, ∑ _s : Fin m, (1 : ℝ) := by
        apply sum_le_sum
        intro r _
        apply sum_le_sum
        intro s _
        nlinarith [averagedGram_entry_sq_le_one hn v hsign r s]
      _ = (m : ℝ) ^ 2 := by
        simp only [sum_const, card_univ, Fintype.card_fin, nsmul_eq_mul, mul_one]
        ring

/-- Finite sign-window version: only the cross bound remains an input.
The paper's identification of this bound with the maximal collar is not checked here. -/
theorem averaged_sign_rank_obstruction {m : ℕ} (hm : 0 < m)
    (n : Fin (2 * m) → ℕ) (hn : ∀ i, 0 < n i)
    (v : (i : Fin (2 * m)) → Fin (n i) → Fin m → ℝ)
    (hsign : ∀ i t r, (v i t r) ^ 2 = 1)
    (B : ℝ) (hB : 0 ≤ B)
    (hcross : ∀ i j, i ≠ j →
      frobenius (averagedGram (v i)) (averagedGram (v j)) ≤ 16 * B) :
    (m : ℝ) ≤ 32 * B := by
  apply twice_dimension_bound hm (fun i => averagedGram (v i)) B hB
  · intro i
    exact (averagedGram_trace_and_self (hn i) (v i) (hsign i)).1
  · intro i
    exact (averagedGram_trace_and_self (hn i) (v i) (hsign i)).2
  · exact hcross

#print axioms diagonal_sq_le_frobenius
#print axioms trace_sq_le_dimension_mul_frobenius
#print axioms frobenius_sum
#print axioms family_rank_lower
#print axioms family_energy_upper
#print axioms gram_rank_obstruction
#print axioms twice_dimension_bound
#print axioms averagedGram_diagonal
#print axioms averagedGram_entry_sq_le_one
#print axioms averagedGram_trace_and_self
#print axioms averaged_sign_rank_obstruction

end RH.GramCore
