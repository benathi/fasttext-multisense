# Probabilistic FastText for Multi-Sense Word Embeddings
This repository contains the implementation of the models in *[Athiwaratkun et al.](https://arxiv.org/abs/1704.08424), Probabilistic FastText for Multi-Sense Word Embeddings, ACL 2018*.

Similar to our previous work in *[Athiwaratkun and Wilson](https://arxiv.org/abs/1704.08424), Multimodal Word Distributions, ACL 2017*, we represent each word in the dictionary as a Gaussian Mixture distribution that can extract multiple meanings. We use FastText as our subword representation to enhance semantic estimation of rare words or words outside the training vocabulary. 

The BibTeX entry for the paper is:

```bibtex
@InProceedings{athi_multift_2018,
    author = {Ben Athiwaratkun, Andrew Gordon Wilson, and Anima Anandkumar},
    title = {Probabilistic FastText for Multi-Sense Word Embeddings},
    booktitle = {Conference of the Association for Computational Linguistics (ACL)},
    year = {2018}
}
```

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
This command will generate *multift*, an executable of our model for training and loading existing models. 

2. Obtain text data. We included scripts to download **text8** and **text9** in **data/**.
```
bash data/get_text8.sh
bash data/get_text9.sh
```
In our paper, we use the concatenation of *ukWaC* and *WaCkypedia_EN* as our English text corpus. Both datasets can be requested [here](http://wacky.sslmit.unibo.it/doku.php?id=download).

The foreign language datasets *deWac* (German), *itWac* (Italian), and *frWac* (French) can be requested using the above link as well. 

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


## Evaluate  Models

1. The provided python module **multift.py** can be used to load the multisense FT object. 

```
ft = multift.MultiFastText(basename="", multi=True)
```

We can query for nearest neighbors give a word or evaluate the embeddings against word similarity datasets. ***See the code for the API. ---- Show sample code instead. ***

2. Sample scripts **eval/eval_text9_model_nn.py** and **eval/eval_text9_model_wordsim.py** show the nearest neighbors and the word similarity respectively. 

```
python eval/eval_text9_model_nn.py | tee log/eval_text9_model_nn.txt

python eval/eval_model_wordsim.py --modelname modelfiles/multi_text8_e10_d300_vs2e-4_lr1e-5_margin1 | tee log/eval_wordsim_text8.txt
python eval/eval_model_wordsim.py --modelname modelfiles/multi_text9_e10_d300_vs2e-4_lr1e-5_margin1 | tee log/eval_wordsim_text9.txt
```


## Download Pretrained Models

### English Model
