# Polybrutus 61D: Exact 66-point Euclidean metric and a fifty-fivefold ideal graph mode

**Gabriel St-Pierre** - Independent researcher
**21 November 2026**
**Exact mathematical preprint / reproducible synthetic case study**
**AI disclosure:** OpenAI ChatGPT (Astra) materially assisted two independently implemented exact rational verifiers, mathematical manuscript and controlled publication. AI is not the human scientific author.

## Abstract

We construct one exact labelled synthetic Euclidean squared-distance metric on 66 norm-one points through a conservative orthogonal unit-vector extension of the original immutable Polybrutus D60 [1]. All 2080 predecessor labelled squared distances remain unchanged; 65 new squared distances each equal 2R², producing 2145 unordered labelled pairs. The centered exact rational Euclidean Gram is PSD with rank 61, proving minimum affine Euclidean realization dimension 61 for this specified metric. For a separately freely stipulated ideal equal-scalar-mass weighted complete graph with w_ij=1/d_ij², rational Laplacian eigenspace ranks yield eigenvalue 33 multiplicity 55 and 65/2 multiplicity 4. Two independently implemented rational programs verify all 2145 pair labels, all 2080 authentic inherited parent labels, centered Gram rank, ideal graph nullities, and frozen full parent scientific source. No physical discovery or empirical measurement is claimed.

## 1. Immutable immediate parent and exact distance conservation

The sole direct scientific predecessor is St-Pierre, Polybrutus D60 [1], DOI 10.5281/zenodo.24431598, scientific frozen Git tag Topbrutus/polybrutus-d60@v0.1.0 at real peeled commit 245cfbf39a9d79dea6bd701c151f89ba75920dbc. Its **entire original Git scientific source ZIP** is preserved byte-identically at prior/d60/frozen_scientific_tag_v0.1.0.zip, size 3849904 bytes with 32 entries and ZIP CRC PASS, SHA256 90f87e839256bd095eb599a70c2fbbf05cf3e53ce39b18bfe18fcf2aa83a0eda. All earlier original scientific source archives remain nested unchanged. The original D60 deterministic certificate is copied byte-identically at prior/d60/results/certificate_d60.json, SHA256 9728ea783514a7be5132b6ee535402d06cddeb5455cbd25b0778dfaf59b1760c. Both independent checkers authenticate source ZIP SHA/CRC, certificate bytes and all 2080 old labelled pairs.

Let p_i (i=1,...,65) be parent norm-one vectors and embed them by q_i=(p_i,0) into larger Euclidean coordinates. Append new perpendicular norm-one q_66. Then each old labelled squared distance remains unchanged, ||q_i-q_j||²=||p_i-p_j||². All 65 new squared distances satisfy ||q_66-q_i||²=2R². Thus C(66,2)=2145=2080+65 exact labelled unordered pairs. This is a constructed synthetic metric, not evidence for new physical spacetime dimensions.

## 2. Rational Gram PSD, exact affine rank and labelled histogram

Construct Gram G over rationals as an orthogonal sum of the seven canonical norm-one point Gram (rank 3), a centered regular five-point unit simplex with mutual inner products -1/4 (rank 4), and 54 independent perpendicular norm-one axes (rank 54). Hence G=XXᵀ is PSD with unit diagonal and rank 3+4+54=61. Define D_ii=0, D_ij=2-2G_ij and H=I-11ᵀ/66. The centered Euclidean Gram B=-(HDH)/2=HGH is PSD of exact rank 61. The inherited canonical antipodal pair puts the origin in the affine hull; the minimum affine Euclidean realization dimension for this metric is therefore 61, using 62 coordinate storage.

At R=1, exhaustive normalized histogram k=4d²/R² is 4:6, 7:2, 8:2114, 9:3, 10:10, 12:6, 13:2, 16:2, totaling 2145 unordered labelled pairs. Their exact sum of squared distances is 17207/4. Both programs verify all 2080 parent pair values by their exact original labels; histogram equality alone would not be an adequate conservation proof.

## 3. Separately specified ideal graph and rational spectral eigenspaces

We stipulate unit scalar masses and symmetric positive complete-graph edge weights w_ij=1/d_ij². The new perpendicular norm-one vertex joins all 65 old vertices with edge weight 1/2. The ideal Laplacian block is L61=[[L60+I65/2,-1_65/2],[-1_65ᵀ/2,65/2]]. Its characteristic polynomial satisfies chi66(z)=z(z-33)chi65(z-1/2)/(z-1/2). With the inherited seven-point core factor f6(z)=chiP7(z)/z, the chosen-model expression is chi66(z)=z(z-33)^55(z-65/2)^4*f6(z-59/2).

Independent exact rational rank-nullity for this Laplacian establishes eigenvalue 33 multiplicity 55 and 65/2 multiplicity 4. These are mathematically dimensionless eigenmodes of a freely chosen ideal graph, not measured acoustic or electromagnetic hertz, particles, or physical extra dimensions.

## 4. Two independent implementations and adversarial negative controls

Primary src/verify_d61.py constructs exact Gram G with SymPy, exhausts all 2145 labelled squared distances, independently authenticates parent complete ZIP SHA256/CRC and byte-identical original certificate, compares all 2080 inherited D60 labels, and computes centered Gram and ideal graph eigenspace ranks. Independent tests/independent_d61.py uses separate Python fractions.Fraction distance rules without importing the first program's Gram builder, and independently recomputes every pair label, centered rank and model eigenvalues. Both output the identical deterministic JSON results/certificate_d61.json with matching SHA256.

Four adversarial primary negative controls detect a corrupted new squared distance, duplicate final point, nonperpendicular tilted but norm-one added point, and histogram-preserving pair relabelling. Independent tests separately reject corrupted labels and histogram-preserving relabelled metrics.

The original D47 certificate carries an inaccurate textual D46 grandparent Git commit, disclosed since D48; historical source archives remain unmodified and the actual direct D60 scientific frozen tag is authenticated separately.

## 5. Reproducibility, DOI relationship and scientific boundaries

Python 3.12 and sympy==1.14.0 reproduce the exact calculations. Orthogonal norm-one vector extension and complete graph joins are standard mathematical constructions. This preprint proves properties of this constructed synthetic metric and the separately selected ideal graph, not a novel universal law, independently human-peer-reviewed experimental result, physical particle, measured hertz or extra physical spacetime dimension.

Zenodo metadata must contain nine current D61 keywords including sixty-one and fifty-fivefold, structured isDerivedFrom to immediate direct D60 DOI 10.5281/zenodo.24431598, and separate bibliographic references to D60 [1] and historical D7 [2]. All three public scientific tag ZIP, PDF and certificate JSON originals must match filenames, exact sizes and public MD5 against source SHA256.

## References

[1] St-Pierre, Gabriel (2026). Polybrutus 60D: Exact 65-Point Euclidean Metric and Fifty-Fourfold Ideal Graph Mode. Zenodo DOI 10.5281/zenodo.24431598. https://doi.org/10.5281/zenodo.24431598

[2] St-Pierre, Gabriel (2026). Polybrutus 7D: An Exact Twelve-Point Orthogonal Completion, the 12-35-37 Identity, and an Oscillator Model. Zenodo DOI 10.5281/zenodo.24407952. https://doi.org/10.5281/zenodo.24407952

[3] St-Pierre, Gabriel (2026). Full original Polybrutus D60 frozen scientific source Git tag v0.1.0, https://github.com/Topbrutus/polybrutus-d60/tree/v0.1.0, peeled commit 245cfbf39a9d79dea6bd701c151f89ba75920dbc, original source ZIP preserved unchanged.
