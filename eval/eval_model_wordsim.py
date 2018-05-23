# A sample script for quantitative evaluation on word similarity datasets
import sys, os
sys.path.append("../")
sys.path.append(".")
import embeval
import numpy as np
import pickle
import argparse

def calculate_wordsim(modelname, multi=1, verbose=True):
  if verbose: print "Basename to evaluate =", modelname
  multift = embeval.get_fts([modelname], multi=multi)[0]
  df = embeval.eval_multi(multift, lower=False)
  if verbose:
    print "df ="
    print df
  return df

if __name__ == "__main__":
  parser = argparse.ArgumentParser(description='')
  parser.add_argument('--modelname', default='', type=str, help="The model to be evaluated. For instance, the files 'modelname.in', 'modelname.bin', etc should exist.")
  parser.add_argument('--multi', default=1, type=int, help="Whether this is a multisense model")
  args = parser.parse_args()
  result = calculate_wordsim(modelname=args.modelname,
    multi=args.multi)