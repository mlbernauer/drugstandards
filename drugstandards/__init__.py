import Levenshtein
import operator
import csv
import os
import re

class DrugStandardizer():
    def create_drug_dictionary(self, filename, delimiter = "\t"):
        """ This function creates a drug dictionary of the form
            {"synonym1":"generic1", "synonym2":"generic1"} using
            drug names (brand, generic, synonyms) found in DrugBank.
        """ 
        self.drugdict= {}  
        with csv.reader(open(filename, 'r'), delimiter = delimter) as csvfile:
            for k, v in csvfile:
                self.drugdict[k.upper()] = v
      
    def find_closest_string(self, query, dictionary, thresh=0.90):
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
    
    def add_drug_mapping(self, mapdict):
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
        for k,v in mapdict.items():
            self.drugdict[k.upper()] = v
      
    def standardize(self, druglist, thresh=0.90):
        """ This function takes a list of drugs (brand name,
            misspelled drugs, generic names) and converts them
            to the generic names. 
        """
        splitter = re.compile("\\W+|\d+")
        standardized_druglist = []
        for drug in druglist:
            drug = drug.upper()
            drug = " ".join(splitter.split(drug)).strip()
            gen = self.drugdict.get(drug)
            if gen:
                standardized_druglist.append(gen)
                continue
            else:
                close_match = self.find_closest_string(str(drug), self.drugdict.keys(), thresh=thresh)
                close_match = self.drugdict.get(close_match)
                standardized_druglist.append(close_match)
        return standardized_druglist
