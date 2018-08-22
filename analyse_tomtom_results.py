# -*- coding: utf-8 -*-
# @Time    : 7/5/18 9:48 PM
# @Author  : Jason Lin
# @File    : analyse_tomtom_results.py
# @Software: PyCharm

import glob
import pandas as pd
import numpy as np
import re

tomtom_outputs = glob.glob("./tomtom_output/*_max_product")

tomtom_result_df = pd.DataFrame(columns=["motif_fullname", "name1", "name1_match", "name2", "name2_match", "number_of_tomtom_matches"])

def find_matched_name(full_name, n1, n2, tomtom_list):
    print(full_name)
    flag_n1 = 0
    flag_n2 = 0
    num_tomtom_matched = len(tomtom_list)
    for tomtom in tomtom_list:
        found_name = tomtom.split("_")[0]
        if not flag_n1 or not flag_n2:
           if n1 == found_name:
               flag_n1 = 1
           if n2 == found_name:
               flag_n2 = 1
    # result_str = ','.join([full_name, n1, str(flag_n1), n2, str(flag_n2), str(num_tomtom_matched)]) + "\n"
    tomtom_result_df.loc[tomtom_result_df["motif_fullname"].count() + 1] = {"motif_fullname":full_name, "name1":n1, "name1_match":flag_n1,
                                                              "name2":n2, "name2_match":flag_n2,
                                                              "number_of_tomtom_matches":num_tomtom_matched}

for tomtom_f in tomtom_outputs:
    tomtom_df = pd.read_csv(tomtom_f +"/tomtom.tsv", delimiter="\t")
    tomtom_df = tomtom_df.dropna(axis=0,how="any")
    tomtom_matched = tomtom_df["Target_ID"]
    f1, f2, n1, n2 = re.split("/|_", tomtom_f)[-6:-2]
    find_matched_name(tomtom_f.split("/")[-1], n1, n2, tomtom_matched)

tomtom_result_df.to_csv("./tomtom_max_product_result.csv", index=False)