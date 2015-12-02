import Levenshtein
import operator
import csv
import pickle
import os

def create_drug_dicitonary(filename):
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
  
def standardize(druglist, drugdict=False, thresh=0.90):
    """ This function takes a list of drugs (brand name,
        misspelled drugs, generic names) and converts them
        to the generic names. It is used to provide naming
        consistency to the FAERS reports.
    """
    if not drugdict:
        this_dir, this_filename = os.path.split(__file__)
        DATA_PATH = os.path.join(this_dir, "data", "synonyms.pkl")
        drugdict = pickle.load(open(DATA_PATH, "rb")) 
    standardized_druglist = []
    for drug in druglist:
        drug = drug.upper()
        gen = drugdict.get(drug)
        if gen:
            standardized_druglist.append(gen)
            continue
        else:
            close_match = find_closest_string(str(drug), drugdict.keys(), thresh=thresh)
            close_match = drugdict.get(close_match)
            standardized_druglist.append(close_match)
    return standardized_druglist
