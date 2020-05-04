import Levenshtein
import operator
import csv
import pickle
import os
import re
from pkg_resources import Requirement, resource_filename

dictionary_file = resource_filename(Requirement.parse("drugstandards"), "drugstandards/data/synonyms.dat")
drugdict = pickle.load(open(dictionary_file, "rb")) 

def create_drug_dictionary(filename):
    """ This function creates a drug dictionary of the form
        {"synonym1":"generic1", "synonym2":"generic1"} using
        drug names (brand, generic, synonyms) found in DrugBank.
    """ 
    f = csv.reader(open(filename, 'rb'), delimiter="\t")
    drug_dictionary = {}  
    for i in f:
        if i[0] == "WID": continue
        drug_dictionary[i[2].upper()] = i[2].upper()
        if i[3] != "NULL": drug_dictionary[i[3].upper()] = i[2].upper()
        if i[4] != "NULL": drug_dictionary[i[4].upper()] = i[2].upper() 
    return drug_dictionary
  
def find_closest_string(query, dictionary, thresh=0.90):
    """ This function returns the closest match for 
         a query string against a dictionary of terms
        using levenstein distance
    """
    dist = {i:Levenshtein.jaro_winkler(query, i) for i in dictionary}
    dist = sorted(dist.items(), key=operator.itemgetter(1), reverse=True)
    if dist[0][1] >= thresh:
        return dist[0][0]
    else:
        return None

def add_drug_mapping(mapdict):
    """ This function is used to add drug mappings to 
        the drug dictionary.  For example, if the term
        "benadry" is not found in the dictionary, you can
        add the custom mapping by using the following:

        drugs.add_drug_mapping({"benadryl":"diphenhydramine"})

        Additionally, one might want to map all instances of
        "multi-vitamin" to "vitamin" in which case you would
        use:

        drugs.add_drug_mapping({"multi-vitamin":"vitamin"})
    """
    filename = resource_filename(Requirement.parse("drugstandards"), "drugstandards/data/synonyms.dat")
    drugdict = pickle.load(open(filename, "rb"))
    for k,v in mapdict.items():
        drugdict[k] = v
    pickle.dump(drugdict, open(filename, "wb"))
    print("Drug dictionary successfully updated...")
  
def standardize(druglist, thresh=0.90):
    """ This function takes a list of drugs (brand name,
        misspelled drugs, generic names) and converts them
        to the generic names. It is used to provide naming
        consistency to the FAERS reports.
    """
    splitter = re.compile("\\W+|\d+")
    standardized_druglist = []
    for drug in druglist:
        drug = drug.upper()
        drug = " ".join(splitter.split(drug)).strip()
        gen = drugdict.get(drug)
        if gen:
            standardized_druglist.append(gen)
            continue
        else:
            close_match = find_closest_string(str(drug), drugdict.keys(), thresh=thresh)
            close_match = drugdict.get(close_match)
            standardized_druglist.append(close_match)
    return standardized_druglist
