# -*- coding: utf-8 -*-
# @Time    : 7/8/18 2:54 PM
# @Author  : Jason Lin
# @File    : analyse_gomo_results.py
# @Software: PyCharm

import pandas as pd
import glob
import re

gomo_outputs = glob.glob("./gomo_output/*_max_product")
gomo_result_df = pd.DataFrame(columns=["motif_name", "num_GO_terms", "GO_terms_with_pvalue"])

def extract_info(gomo_df):

    motif_name = gomo_df.iloc[0,0]
    # print(motif_name)
    num_go_items = len(gomo_df)
    go_dict = {}
    for idx, row in gomo_df.iterrows():
        go_dict[row['GO_Term_Identifier']] = row['p-value']
    gomo_items_str = str(go_dict).replace(",", ";")
    gomo_result_df.loc[gomo_result_df["motif_name"].count() + 1] = {"motif_name": motif_name, "num_GO_terms": num_go_items,
                                                                            "GO_terms_with_pvalue": gomo_items_str}
for gomo_fold in gomo_outputs:
    gomo_df = pd.read_csv(gomo_fold + "/gomo.tsv", delimiter="\t")
    gomo_df = gomo_df.dropna(axis=0, how="any")
    # print(gomo_df)

    if gomo_df.empty:
        print(gomo_fold.split("/")[-1])
        gomo_result_df.loc[gomo_result_df["motif_name"].count() + 1] = {"motif_name": gomo_fold.split("/")[-1],
                                                                        "num_GO_terms": 0, "GO_terms_with_pvalue": ""}
        continue
    extract_info(gomo_df)

gomo_result_df.to_csv("./gomo_max_product_result.csv", index=False)