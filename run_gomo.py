# -*- coding: utf-8 -*-
# @Time    : 7/4/18 12:19 PM
# @Author  : Jason Lin
# @File    : run_gomo.py
# @Software: PyCharm

import os
import re
import glob
import concurrent.futures

def run_ama(motif_file):
    database_paths = []
    database_paths.append("/home/jieconlin3/meme/db/gomo_databases/mammal_homo_sapiens_1000_199.na " +
                         "/home/jieconlin3/meme/db/gomo_databases/mammal_homo_sapiens_1000_199.na.bfile")
    database_paths.append("/home/jieconlin3/meme/db/gomo_databases/mammal_mus_musculus_1000_199.na " +
                         "/home/jieconlin3/meme/db/gomo_databases/mammal_mus_musculus_1000_199.na.bfile")
    database_paths.append("/home/jieconlin3/meme/db/gomo_databases/mammal_canis_familiaris_1000_199.na " +
                         "/home/jieconlin3/meme/db/gomo_databases/mammal_canis_familiaris_1000_199.na.bfile")
    database_paths.append("/home/jieconlin3/meme/db/gomo_databases/mammal_canis_familiaris_1000_199.na " +
                         "/home/jieconlin3/meme/db/gomo_databases/mammal_canis_familiaris_1000_199.na.bfile")
    database_paths.append("/home/jieconlin3/meme/db/gomo_databases/mammal_equus_caballus_1000_199.na " +
                         "/home/jieconlin3/meme/db/gomo_databases/mammal_equus_caballus_1000_199.na.bfile")

    ama_output = "./gomo_output/ama_output/"
    ama_output += re.split("/|\.", motif_file)[-2]

    for database in database_paths:
        cisml_name = re.split("/|\.| ", database)[-3] + ".na.cisml"
        command = "~/meme/libexec/meme-5.0.1/ama --oc " + ama_output + " --pvalues --verbosity 1 " + motif_file + " " + database
        os.system(command)
        ama_file = glob.glob(ama_output + "/*.xml")
        new_name = ama_file[0].replace("ama.xml", cisml_name)
        os.rename(ama_file[0], new_name)
        ama_file = glob.glob(ama_output + "/*.txt")
        new_name = ama_file[0].replace("ama.txt", cisml_name.split(".cisml")[-2] + ".txt")
        os.rename(ama_file[0], new_name)

def run_gomo(motif_file):
    run_ama(motif_file)
    dag_path = "~/meme/db/gomo_databases/go.dag"
    ama_files = ""
    motif_name = re.split("/|\.", motif_file)[-2]
    pre_ama = "./gomo_output/ama_output/" + motif_name
    ama_files += pre_ama + "/mammal_homo_sapiens_1000_199.na.cisml "
    ama_files += pre_ama + "/mammal_mus_musculus_1000_199.na.cisml "
    ama_files += pre_ama + "/mammal_canis_familiaris_1000_199.na.cisml "
    ama_files += pre_ama + "/mammal_equus_caballus_1000_199.na.cisml"
    # print(ama_files)
    output_fold = "./gomo_output/" + motif_name
    # print(output_fold)
    csv_path = "~/meme/db/gomo_databases/mammal_homo_sapiens_1000_199.na.csv"
    command = "~/meme/bin/gomo --nostatus --verbosity 1 --oc " + output_fold +  " --t 0.05 --shuffle_scores 1000 --dag " + dag_path + " --motifs " \
              + motif_file + " " + csv_path +" " + ama_files
    print(motif_file)
    os.system(command)
    return "Finished!"

motifs = glob.glob("./input_file_for_meme/*.txt")

with concurrent.futures.ProcessPoolExecutor(max_workers=6) as executor:
    for m, result in zip(motifs, executor.map(run_gomo, motifs)):
        print(m, result)


# gomo --nostatus --verbosity 1 --oc . --t 0.05 --shuffle_scores 1000 --dag ~/meme/db/gomo_databases/go.dag --motifs
# ../../../input_file_for_meme/ETS_Homeo_ELK1_PITX1_nmax_product.txt ~/meme/db/gomo_databases/mammal_homo_sapiens_1000_199.na.csv *.cisml
"""
i = 0
for motif in motifs:
    print("----------", str(i), "-----------")
    print(motif)
    # run_ama(motif)
    run_gomo(motif)
    i += 1
"""
