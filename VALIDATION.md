# Polybrutus D61 — proof-first validation and controlled publication

1. Direct scientific parent D60 frozen v0.1.0 peeled Git commit 245cfbf39a9d79dea6bd701c151f89ba75920dbc, DOI 10.5281/zenodo.24431598, entire original source ZIP SHA256 90f87e839256bd095eb599a70c2fbbf05cf3e53ce39b18bfe18fcf2aa83a0eda, certificate SHA256 9728ea783514a7be5132b6ee535402d06cddeb5455cbd25b0778dfaf59b1760c. Both exact programs validate original ZIP SHA/CRC, original certificate bytes and inherited labels.
2. Exhaust all 66 norm-one points and 2145 labelled exact squared distances; 2080 unchanged old D60 pairs and 65 new squared distances 2R²; Euclidean Gram and centered Gram PSD rank 61.
3. Two independent implementations (SymPy exact Gram vs fractions.Fraction separate pair rules), four adversarial negative controls, exact deterministic certificate. Chosen dimensionless ideal graph eigenvalue 33 mult 55 and 65/2 mult 4.
4. Scientific GitHub initial main CI must pass, then freeze source tag v0.1.0 and require tag CI green; after public Zenodo DOI document on main and require third green CI.
5. Public Zenodo originals: full frozen Git scientific source ZIP, two-page mathematical PDF and exact deterministic certificate JSON; all 3 filenames, sizes and MD5 from public API match SHA256-verified originals. Nine current D61 sixty-one/fifty-fivefold keywords, structured isDerivedFrom direct D60 DOI, separate D60/D7 textual bibliography.
6. Preserve entire historic original source ZIP nesting unchanged, disclose D47/D46 historical parent text SHA mistake, never claim physical spacetime, measured hertz or new universal theorem.

    python -m pip install sympy==1.14.0
    python src/verify_d61.py
    python tests/independent_d61.py
    python src/check_zenodo_metadata.py
