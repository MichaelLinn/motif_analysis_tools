# -*- coding: utf-8 -*-
# @Time    : 7/3/18 9:47 PM
# @Author  : Jason Lin
# @File    : run_tomtom.py
# @Software: PyCharm

# command of Tomtom
# tomtom -no-ssc -oc . -verbosity 1 -min-overlap 5 -mi 1 -dist pearson -evalue -thresh 10.0 TEA_Homeo_TEAD4_HOXD4_nmax_product.txt
# db/HUMAN/HOCOMOCOv11_full_HUMAN_mono_meme_format.meme

import os
import glob
import re

def run_tomtom(motif_file, output_dir):
    # output_dir = "tmp "
    dataset_path = " /home/jieconlin3/meme/db/motif_databases/HUMAN/HOCOMOCOv11_full_HUMAN_mono_meme_format.meme"
    # motif_file = "input_file_for_meme/TEA_Homeo_TEAD4_HOXD4_nmax_product.txt "
    command = "tomtom -no-ssc -oc " + output_dir + " -verbosity 1 -min-overlap 5 -mi 1 -dist pearson -evalue -thresh 10.0 "
    command += motif_file + dataset_path
    os.system(command)


motifs = glob.glob("./input_file_for_meme/*.txt")

for motif in motifs:
    output_dir = "./tomtom_output/"
    output_dir += re.split("/|\.", motif)[-2]
    # print(output_dir)
    print(motif)
    run_tomtom(motif, output_dir)


