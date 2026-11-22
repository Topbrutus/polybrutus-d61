# Polybrutus D61 — exact 66-point labelled Euclidean squared-distance metric

**Exclusive direct parent scientific source:** Topbrutus/polybrutus-d60@v0.1.0, actual peeled scientific Git commit \`245cfbf39a9d79dea6bd701c151f89ba75920dbc\`, DOI 10.5281/zenodo.24431598, original full source ZIP SHA256 \`90f87e839256bd095eb599a70c2fbbf05cf3e53ce39b18bfe18fcf2aa83a0eda\`, original D60 certificate SHA256 \`9728ea783514a7be5132b6ee535402d06cddeb5455cbd25b0778dfaf59b1760c\`.

## Conservative perpendicular norm-one extension

Embed all 65 predecessor norm-one vectors p_i as q_i=(p_i,0). Append one perpendicular unit vector q_66. Every one of C(65,2)=2080 old labelled squared distances remains unchanged; all 65 new squared distances equal 2R². Total C(66,2)=2145 labelled unordered pairs.

Construct a rational Gram G as orthogonal sum of seven original canonical norm-one points (Gram rank 3), a separate centered five-point regular unit simplex (rank 4) with mutual inner products -1/4, and **54** independent mutually orthogonal norm-one axes (rank 54). Hence G=XXᵀ is PSD, unit diagonal, exact rank **3+4+54=61**. Set D_ii=0 and D_ij=2-2G_ij. With H=I-11ᵀ/66, B=-(HDH)/2=HGH is PSD of rank **61**. An inherited canonical antipodal point pair implies the origin lies in the affine hull. Minimum affine Euclidean dimension of this particular metric is therefore 61 (62 coordinate storage).

At R=1, \`k=4d²/R²\` exact histogram: 4:6, 7:2, 8:2114, 9:3, 10:10, 12:6, 13:2, 16:2; total 2145. Exact sum of squared pair distances R=1: **17207/4**.

## Independently stipulated ideal weighted graph

Freely choose scalar unit masses, weighted complete edges w_ij=1/d_ij². New point connects to all 65 old points with weight 1/2. The chosen ideal Laplacian is L61=[[L60+I65/2,-1_65/2],[-1_65ᵀ/2,65/2]]. Its characteristic recurrence is chi66(z)=z(z-33)chi65(z-1/2)/(z-1/2).
Using the inherited seven-point factor f6(z)=chiP7(z)/z:
chi66(z)=z(z-33)^55(z-65/2)^4*f6(z-59/2).
Exact rational nullities yield Laplacian eigenvalue **33 multiplicity 55**, and **65/2 multiplicity 4**. These values are dimensionless model eigenmodes, not physical frequencies.

**Bibliography:** immediate D60 DOI 10.5281/zenodo.24431598; historical D7 DOI 10.5281/zenodo.24407952.
