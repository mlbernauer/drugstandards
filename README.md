# Drug Standards
This package provides tools for standardizing drug names into a single format.  For example; Benadryl and diphenhydramine refer to the same chemical entity. In certain tasks, such as mining the FDA Adverse Event Reporting System database, it is useful to standardize all drug names (i.e. convert all instances of Benadryl to diphenhydramine) in order to compute various statistics. This package uses a database of drug synonyms and brand names to return the generic name for a drug. To handle misspellings the standardize function will return the generic name for the most similar match based on Jaro-Winkler similarity. A threshold can be set in order to specify the minimal similarity required to be considered a match.

## Installation

```bash
# install Levenshtein package
sudo pip3 install Levenshtein==0.21.0

# download repo and enter the following
cd drugstandards
sudo python3 setup.py install
```

## Usage

```python
# import module
import drugstandards as ds

# create standardizer object
s = ds.DrugStandardizer()

# map a brand name to generic (case insensitive) 
s.standardize(["lopressor"])
s.standardize(["Benadryl"])

# handles misspellings and multiple mappings
s.standardize(["Benadril", "lopresor"])

# can a adjust match threshold, will return None if not match found
s.standardize(["Benadril"], thresh=0.9)

# add custom mappings, key is case insensitive but value letter case is preserved
s.add_drug_mapping({"MULTI-VITAMIN":"VITAMIN"})

# add multiple mappings simultaneously 
s.add_drug_mapping({"MULTI-VITAMIN":"VITAMIN", "TYLENOL EXTRA STRENGTH": "ACETAMINOPHEN"})
```
## Questions/issues/contact

mlbernauer@gmail.com

## Citing
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.571248.svg)](https://doi.org/10.5281/zenodo.571248)
