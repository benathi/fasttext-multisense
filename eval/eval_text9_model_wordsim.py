# A sample script for quantitative evaluation on word similarity datasets
import sys, os
sys.path.append("../")
sys.path.append(".")
import embeval
import numpy as np
import pickle
import argparse


basename='modelfiles/multi_text9_e10_d300_vs2e-4_lr1e-5_margin1'
print "Basename to evaluate =", basename
ft = embeval.get_fts([basename], multi=True)[0]
df = embeval.eval_multi(ft, lower=False)
print "df ="
print df