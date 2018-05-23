# Probabilistic FastText for Multi-Sense Embeddings

## What's in this Library?

We provide 

(1) scripts to train the multi-sense FastText embedding in *src*. We provide instructions on how to train the model below. 

(2) scripts to load the pre-trained models and evaluate.

(3) We provide scripts to convert pre-trained FastText model (single sense) into Python as well. 
--- Ben: provide usage ---


## Training

1. Compile the C++ files.
```
make
```

2. Obtain text data. We included scripts to download **text8** and **text9**. 
```
bash get_text8.sh
bash get_text9.sh
```
In our paper, we use the concatenation of *ukWaC* and *WaCkypedia_EN* as our English text corpus. Both datasets can be requested [here](http://wacky.sslmit.unibo.it/doku.php?id=download).

The foreign language datasets *deWac* (German), *itWac* (Italian), and *frWac* (French) can be requested using the above link as well. 

**Note: add script to prepare ukWac + Wackypedia?**

3. Run a sample script for *text8* or *text9*.
```
bash exps/train_text8_multi.sh
bash exps/train_text9_multi.sh
```
After the training is complete, the following files will be saved:

```
modelname.words     List of words in the dictionary
modelname.bin       A binary file for the subword embedding model
modelname.in        The subword embeddings
modelname.in2       The embeddings for the second Gaussian component.
modelname.subword   The final representation of words in the dictionary. Note that the representation for words outside the dictionary can be computed using the provided python module.
```

## Evaluate Pretrained Models

1. The provided python module **multift.py** can be used to load the multisense FT object. 

```
ft = multift.MultiFastText(basename="", multi=True)
```

We can query for nearest neighbors give a word or evaluate the embeddings against word similarity datasets. ***See the code for the API. ---- Show sample code instead. ***

2. Sample scripts **eval/eval_text9_model_nn.py** and **eval/eval_text9_model_wordsim.py** show the nearest neighbors and the word similarity respectively. 

```
python eval/eval_text9_model_nn.py | tee log/eval_text9_model_nn.txt
python eval/eval_text9_model_wordsim.py | tee log/eval_text9_model_wordsim.txt
```
