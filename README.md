# Drug Standards
 This package provides tools for standardizing drug names into a single format.  For example; Benadryl and diphenhydramine refer to the same chemical entity. In certain tasks, such as mining the FDA Adverse Event Reporting System database, it is useful to standardize all drug names (i.e. convert all instances of Benadryl to diphenhydramine) in order to compute various statistics. This package uses a database of drug synonyms and brand names to return the generic name for a drug. To handle misspellings the standardize function will return the generic name for the most similar match based on Jaro-Winkler similarity. A threshold can be set in order to specify the minimal similarity required to be considered a match.

## Installation

#### 1. Install drugstandards package using PIP

`sudo pip install drugstandards`

#### 2. Installing drugstandards from source
```
# Download this github repository and enter the following
cd drugstandards
sudo python setup.py install
```

## Usage
#### 1. Import the module

`import drugstandards as drugs`

#### 2. Standardize a single, correctly spelled drug name to generic.
```
# Note that this function is NOT case-sensitive.
drugs.standardize(["lopressor"])
```
#### 3. Standardize a single brand name to generic.
```
drugs.standardize(["Benadryl"])
```

#### 4. Standardize misspelled names to generic.

`drugs.standardize(["Benadril", "lopresor"])`

#### 5. Return generic name for terms that have a Jaro-Winkler similarity greater than 0.9
```
# Will return None if no match is found.

drugs.standardize(["Benadril"], thresh=0.9)
```

#### 6. Add drug mapping to drug dictionary
```
# If a mapping does not exist you may create your own by updating the drug-dictionary.
# For example, we may be interested in mapping the term "MULTI-VITAMIN" to "VITAMIN"
drugs.add_drug_mapping({"MULTI-VITAMIN":"VITAMIN"})

# We can also create many updates simultaneously
drugs.add_drug_mapping({"MULTI-VITAMIN":"VITAMIN", "TYLENOL EXTRA STRENGTH": "ACETAMINOPHEN"})
```
## Questions/issues/contact
mlbernauer@gmail.com
