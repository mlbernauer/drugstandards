# Drug Standards
 This package provides tools for standardizing drug names into a single format.  For example; Benadryl and diphenhydramine refer to the same chemical entity. In certain tasks, such as mining the FDA Adverse Event Reporting System database, it is useful to standardize all drug names (i.e. convert all instances of Benadryl to diphenhydramine) in order to compute various statistics. This package uses a database of drug synonyms and brand names to return the generic name for a drug. To handle misspellings the standardize function will return the generic name for the most similar match based on Jario-Winkler similarity. A threshold can be set in order to specify the minimal similarity required to be considered a match.

## Installation

#### 1. Install drugstandards pacakge

`sudo pip install drugstandards`

## Usage
#### 1. Import the module

`import drugstandards as drugs`

#### 2. Standardize a single, correctly spelled drugname to generic.
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

#### 5. Return generic name for terms that have a Jario-Winkler similarity greater than 0.9
```
# Will return None if no match is found.
drugs.standardize(["Benadril"], thresh=0.9)
```

## Questions/issues/contact
mlbernauer@gmail.com
