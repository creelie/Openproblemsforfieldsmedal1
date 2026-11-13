import Mathlib

/-!
# Finite identities and constants for the Liouville energy

The theorems below check the finite algebra used in the paper: the completion
identity for the window energy, the lower bound it gives, the Gram counting
inequality, the minimum of the Plancherel weight `K`, and the numerical
constants in the explicit bound for the Liouville summatory function.
-/

namespace LiouvilleEnergy

open Finset

set_option autoImplicit false

/-- One term of the boundary formula, completed to a square. -/
theorem boundary_term (x y : ℝ) :
    x ^ 2 + (y - x) ^ 2 = 2 * (x - y / 2) ^ 2 + y ^ 2 / 2 := by ring

/-- The boundary sum of the window energy at `H = N`, written as a function
of the prefix sums `L 1, …, L N`. -/
noncomputable def boundaryEnergy (L : ℕ → ℝ) (N : ℕ) : ℝ :=
  (1 / (N : ℝ)) * (L N ^ 2 + ∑ j ∈ Ico 1 N, (L j ^ 2 + (L N - L j) ^ 2))

/-- The completion identity: `Q(N) = (N+1)/(2N) L(N)^2 + (2/N) Σ (L j - L N/2)^2`. -/
theorem completion (L : ℕ → ℝ) (N : ℕ) (hN : 1 ≤ N) :
    boundaryEnergy L N =
      ((N : ℝ) + 1) / (2 * N) * L N ^ 2 +
        (2 / (N : ℝ)) * ∑ j ∈ Ico 1 N, (L j - L N / 2) ^ 2 := by
  unfold boundaryEnergy
  have hsum : ∑ j ∈ Ico 1 N, (L j ^ 2 + (L N - L j) ^ 2) =
      2 * ∑ j ∈ Ico 1 N, (L j - L N / 2) ^ 2 + ((N : ℝ) - 1) * (L N ^ 2 / 2) := by
    rw [sum_congr rfl (fun j _ => boundary_term (L j) (L N)), sum_add_distrib,
      ← mul_sum, sum_const, Nat.card_Ico, nsmul_eq_mul]
    rw [Nat.cast_sub hN]
    push_cast
    ring
  rw [hsum]
  have hN' : (N : ℝ) ≠ 0 := by
    have : (1 : ℝ) ≤ N := by exact_mod_cast hN
    linarith
  field_simp
  ring

/-- The energy dominates half the square of the full sum. -/
theorem half_sq_le_energy (L : ℕ → ℝ) (N : ℕ) (hN : 1 ≤ N) :
    L N ^ 2 / 2 ≤ boundaryEnergy L N := by
  rw [completion L N hN]
  have hNpos : (0 : ℝ) < N := by exact_mod_cast hN
  have h1 : L N ^ 2 / 2 ≤ ((N : ℝ) + 1) / (2 * N) * L N ^ 2 := by
    rw [div_mul_eq_mul_div, le_div_iff₀ (by positivity)]
    nlinarith [sq_nonneg (L N)]
  have h2 : 0 ≤ (2 / (N : ℝ)) * ∑ j ∈ Ico 1 N, (L j - L N / 2) ^ 2 := by
    apply mul_nonneg (by positivity)
    exact sum_nonneg (fun j _ => sq_nonneg _)
  linarith

/-- The energy is a sum of squares, hence nonnegative, and it vanishes only
when every prefix sum vanishes. -/
theorem energy_nonneg (L : ℕ → ℝ) (N : ℕ) : 0 ≤ boundaryEnergy L N := by
  unfold boundaryEnergy
  apply mul_nonneg (by positivity)
  exact add_nonneg (sq_nonneg _) (sum_nonneg (fun j _ => by positivity))

/-- Gram counting: `K² M ≤ K M² + 16 B K (K-1)` with `K = 2M` forces `M < 32 B`. -/
theorem gram_counting (M B : ℝ) (hM : 1 ≤ M)
    (h : (2 * M) ^ 2 * M ≤ 2 * M * M ^ 2 + 16 * B * (2 * M) * (2 * M - 1)) :
    M < 32 * B := by
  have hM0 : 0 < M := by linarith
  have h2 : 0 < 2 * M - 1 := by linarith
  have key : 2 * M ^ 3 ≤ 32 * B * M * (2 * M - 1) := by nlinarith
  have hB : 0 < B := by
    by_contra hB
    push_neg at hB
    have : 32 * B * M * (2 * M - 1) ≤ 0 := by
      have := mul_pos hM0 h2
      nlinarith
    nlinarith [pow_pos hM0 3]
  have : 32 * B * M * (2 * M - 1) < 32 * B * M * (2 * M) := by
    have := mul_pos (mul_pos (by norm_num : (0:ℝ) < 32) hB) hM0
    nlinarith
  nlinarith [pow_pos hM0 2]

/-- The Plancherel weight `K(σ+iτ) = 1 + 2/(1+2σ) - 2(1+σ)/((1+σ)²+τ²)`
exceeds `0.65` for all `σ ≥ 0` and real `τ`. -/
theorem plancherel_weight_lower (σ τ : ℝ) (hσ : 0 ≤ σ) :
    (13 : ℝ) / 20 < 1 + 2 / (1 + 2 * σ) - 2 * (1 + σ) / ((1 + σ) ^ 2 + τ ^ 2) := by
  have hA : 0 < 1 + 2 * σ := by linarith
  have hB : 0 < (1 + σ) ^ 2 := by positivity
  have hC : (1 + σ) ^ 2 ≤ (1 + σ) ^ 2 + τ ^ 2 := by nlinarith [sq_nonneg τ]
  have h1 : 2 * (1 + σ) / ((1 + σ) ^ 2 + τ ^ 2) ≤ 2 / (1 + σ) := by
    rw [div_le_div_iff₀ (by positivity) (by linarith)]
    nlinarith
  have h2 : (13 : ℝ) / 20 < 1 + 2 / (1 + 2 * σ) - 2 / (1 + σ) := by
    rw [show 1 + 2 / (1 + 2 * σ) - 2 / (1 + σ) =
        1 - 2 * σ / ((1 + 2 * σ) * (1 + σ)) by field_simp; ring]
    rw [show (13 : ℝ) / 20 = 1 - 7 / 20 by norm_num]
    have : 2 * σ / ((1 + 2 * σ) * (1 + σ)) < 7 / 20 := by
      rw [div_lt_div_iff₀ (by positivity) (by norm_num)]
      nlinarith [sq_nonneg (σ - 19 / 28)]
    linarith
  linarith

/-- The exact minimum of the Plancherel weight: `K(σ+iτ) ≥ 4√2 - 5` for all
`σ ≥ 0` and real `τ`, with equality at `σ = 1/√2`, `τ = 0`. -/
theorem plancherel_weight_min (σ τ : ℝ) (hσ : 0 ≤ σ) :
    4 * Real.sqrt 2 - 5 ≤ 1 + 2 / (1 + 2 * σ) - 2 * (1 + σ) / ((1 + σ) ^ 2 + τ ^ 2) := by
  set s := Real.sqrt 2 with hsdef
  have hs : s ^ 2 = 2 := Real.sq_sqrt (by norm_num)
  have hs0 : 0 < s := Real.sqrt_pos.mpr (by norm_num)
  have hs1 : s < 3 / 2 := by nlinarith
  have hA : 0 < 1 + 2 * σ := by linarith
  have hC : (1 + σ) ^ 2 ≤ (1 + σ) ^ 2 + τ ^ 2 := by nlinarith [sq_nonneg τ]
  have h1 : 2 * (1 + σ) / ((1 + σ) ^ 2 + τ ^ 2) ≤ 2 / (1 + σ) := by
    rw [div_le_div_iff₀ (by positivity) (by linarith)]
    nlinarith
  have h2 : 4 * s - 5 ≤ 1 + 2 / (1 + 2 * σ) - 2 / (1 + σ) := by
    rw [show 1 + 2 / (1 + 2 * σ) - 2 / (1 + σ) =
        1 - 2 * σ / ((1 + 2 * σ) * (1 + σ)) by field_simp; ring]
    have : 2 * σ / ((1 + 2 * σ) * (1 + σ)) ≤ 6 - 4 * s := by
      rw [div_le_iff₀ (by positivity)]
      have key : (6 - 4 * s) * ((1 + 2 * σ) * (1 + σ)) - 2 * σ
          = 2 * (6 - 4 * s) * (σ - s / 2) ^ 2 := by ring_nf; rw [show s ^ 3 = s * s ^ 2 by ring, hs]; ring_nf
      nlinarith [sq_nonneg (σ - s / 2), key]
    linarith
  linarith

/-- `ζ(2)/4345 < 1/2641`: the constant of the explicit bound. -/
theorem zeta_two_constant : Real.pi ^ 2 / 6 / 4345 < 1 / 2641 := by
  have h := Real.pi_lt_d4
  have h0 := Real.pi_pos
  rw [div_div, div_lt_div_iff₀ (by norm_num) (by norm_num)]
  nlinarith

/-- `exp(14.6) > 2160535`, so `1 + (1/2) log 2160535 < 8.3`. -/
theorem log_threshold : (1 : ℝ) + Real.log 2160535 / 2 < 83 / 10 := by
  have he : (2.7182818283 : ℝ) < Real.exp 1 := Real.exp_one_gt_d9
  have h1 : (1.025 : ℝ) ≤ Real.exp 0.025 := by
    have := Real.add_one_le_exp (0.025 : ℝ); linarith
  have hexp : Real.exp (14.6 : ℝ) = Real.exp 1 ^ 14 * Real.exp 0.025 ^ 24 := by
    rw [← Real.exp_nat_mul, ← Real.exp_nat_mul, ← Real.exp_add]; norm_num
  have hlow : (2160535 : ℝ) < Real.exp 14.6 := by
    rw [hexp]
    have a : (2.7182818283 : ℝ) ^ 14 < Real.exp 1 ^ 14 :=
      pow_lt_pow_left₀ he (by norm_num) (by norm_num)
    have b : (1.025 : ℝ) ^ 24 ≤ Real.exp 0.025 ^ 24 :=
      pow_le_pow_left₀ (by norm_num) h1 24
    have c : (2160535 : ℝ) < (2.7182818283 : ℝ) ^ 14 * (1.025 : ℝ) ^ 24 := by norm_num
    calc (2160535 : ℝ) < (2.7182818283 : ℝ) ^ 14 * (1.025 : ℝ) ^ 24 := c
      _ ≤ Real.exp 1 ^ 14 * Real.exp 0.025 ^ 24 := by
        apply mul_le_mul a.le b (by positivity) (by positivity)
  have hlog : Real.log 2160535 < 14.6 := by
    rw [Real.log_lt_iff_lt_exp (by norm_num)]; exact hlow
  linarith

/-- Exact coefficient-uniform maximum of one shift: `|Σ_{n ≤ Y} a_n a_{n+h}| ≤ Y`
for coefficients of modulus at most one. -/
theorem shift_correlation_le (a : ℕ → ℝ) (ha : ∀ n, |a n| ≤ 1) (h Y : ℕ) :
    |∑ n ∈ range Y, a n * a (n + h)| ≤ Y := by
  calc |∑ n ∈ range Y, a n * a (n + h)| ≤ ∑ n ∈ range Y, |a n * a (n + h)| :=
        abs_sum_le_sum_abs _ _
    _ ≤ ∑ _n ∈ range Y, (1 : ℝ) := by
        apply sum_le_sum; intro n _
        rw [abs_mul]
        exact mul_le_one₀ (ha n) (abs_nonneg _) (ha (n + h))
    _ = Y := by simp

/-- The oscillation constant: `2.3723² / 2 > 2.8139`. -/
theorem oscillation_constant : (2.8139 : ℝ) < (2.3723 : ℝ) ^ 2 / 2 := by
  norm_num

/-- The counting step in the upper bound for the normalised energy:
`N(N-1) + N² + (4/3)N² ≤ (10/3)N²` for `N ≥ 0`. -/
theorem ten_thirds_count (N : ℝ) (hN : 0 ≤ N) :
    N * (N - 1) + N ^ 2 + 4 / 3 * N ^ 2 ≤ 10 / 3 * N ^ 2 := by
  nlinarith

/-- The exponent comparison in the almost-all-positions criterion. -/
theorem positions_exponents (δ Θ β σ ε : ℝ)
    (hΘ : Θ - β < δ / 4) (hε0 : 0 < ε) (hε1 : ε ≤ δ / 8) (hε2 : ε ≤ (β - σ) / 2) :
    1 - δ + 2 * Θ + 2 * ε < 1 + 2 * β - ε ∧ 1 + 2 * σ < 1 + 2 * β - ε := by
  constructor <;> linarith

end LiouvilleEnergy
