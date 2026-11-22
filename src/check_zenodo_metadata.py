#!/usr/bin/env python3
from pathlib import Path
import json
R=Path(__file__).resolve().parents[1]
c=json.loads((R/'results/certificate_d61.json').read_text('utf8'))
m=json.loads((R/'publication/zenodo_metadata_blueprint.json').read_text('utf8'))
assert c['status']=='PASS' and c['dimension']==m['scientific_dimension']==61
assert c['vertices']==m['norm_one_vertices']==66
assert c['pairs']==m['exact_labelled_squared_pairs']==2145
assert c['affine_rank']==c['centered_gram_rank']==61
assert c['eigenvalue_33_multiplicity']==m['model_eigenvalue_33_multiplicity']==55
assert c['eigenvalue_65_over_2_multiplicity']==m['model_eigenvalue_65_over_2_multiplicity']==4
assert c['parent_tag_commit']=='245cfbf39a9d79dea6bd701c151f89ba75920dbc'
assert c['parent_doi']==m['scientific_parent_doi']=='10.5281/zenodo.24431598'
assert m['related_identifiers']==[{'identifier':'10.5281/zenodo.24431598','relation':'isDerivedFrom','resource_type':'publication-preprint','scheme':'doi'}]
assert len(m['keywords'])==9
assert 'affine Euclidean dimension sixty-one' in m['keywords']
assert 'fifty-fivefold ideal eigenvalue' in m['keywords']
assert len(m['references'])==2
assert '10.5281/zenodo.24431598' in m['references'][0]
assert '10.5281/zenodo.24407952' in m['references'][1]
assert not set(m['keywords']).intersection({'affine Euclidean dimension sixty','fifty-fourfold ideal eigenvalue','affine Euclidean dimension sixty-two','fifty-sixfold ideal eigenvalue'})
note=(R/'publication/POLYBRUTUS_61D_NOTE.md').read_text('utf8')
assert all(x in note for x in ('## References','10.5281/zenodo.24431598','10.5281/zenodo.24407952'))
print('D61_CURRENT_9_KEYWORDS_STRUCTURED_DIRECT_D60_PARENT_AND_SEPARATE_D60_D7_REFERENCES_PASS')
