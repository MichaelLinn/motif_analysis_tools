# -*- coding: utf-8 -*-
# @Time    : 7/5/18 10:06 AM
# @Author  : Jason Lin
# @File    : run_fimo.py
# @Software: PyCharm

import re
import os
import glob
import concurrent.futures


# fimo --oc . --verbosity 1 --bgfile db/ucsc_hg19.fna.bfile --thresh 1.0E-4 TEA_Homeo_TEAD4_HOXD4_nmax_product.txt db/ucsc_hg19.fna

def run_fimo(motif):
    motif_name = re.split("/|\.", motif)[-2]
    output_fold = "./fimo_output/" + motif_name
    database = ["./ucsc_hg19/ucsc_hg19.fna.bfile", "./ucsc_hg19/ucsc_hg19.fna"]
    command = "~/meme/bin/fimo --oc " + output_fold + " --verbosity 1 --bfile " + database[0] + " --thresh 1.0E-4 " + motif + " " + database[1]
    os.system(command)
    return "Finished!"


motifs = glob.glob("./input_file_for_meme/*.txt")

with concurrent.futures.ProcessPoolExecutor() as executor:
    for motif, result in zip(motifs, executor.map(run_fimo, motifs)):
        print(motif, result)


