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

## 0. What's in this Library?

We provide 

(1) pre-trained models in **1.**.

(2) scripts to train the multi-sense FastText embeddings. We give instructions on how to train the model in **2**. 

(3) Python scripts to evaluate the trained models on word similarity or nearest neighbor search in **3**. 
   
(4) intructions on how to load a pre-trained FastText model (single sense) into Python **4**.

## 1. Pre-Trained Models

### 1.1 English

### 1.2 Italian

### 1.3 German

### 1.4 French

## 2. Train

1. Compile the C++ files. The step requires a compiler with C++11 support such as g++-4.7.2 or newer or clang-3.3 or newer. It also requires **make** which can be installed via ``sudo apt-get install build-essential`` on Ubuntu. 

Once you have **make** and a C++ compiler, you can compile our code by executing:
```
make
```
This command will generate *multift*, an executable of our model. 

2. Obtain text data for training. We included scripts to download **text8** and **text9** in **data/**.
```
bash data/get_text8.sh
bash data/get_text9.sh
```
In our paper, we use the concatenation of *ukWaC* and *WaCkypedia_EN* as our English text corpus. Both datasets can be requested [here](http://wacky.sslmit.unibo.it/doku.php?id=download).

The foreign language datasets *deWac* (German), *itWac* (Italian), and *frWac* (French) can be requested using the above link as well. 

3. Run sample training scripts for *text8* or *text9*.

```
bash exps/train_text8_multi.sh
```

After the training is complete, the following files will be saved:

```
modelname.words         List of words in the dictionary
modelname.bin           A binary file for the subword embedding model
modelname.in            The subword embeddings
modelname.in2           The embeddings for the second Gaussian component.
modelname.subword       The final representation of words in the dictionary. Note that the representation for words outside the dictionary can be computed using the provided python module based on the files *.in and *.in2.
```

## 3. Evaluate

1. The provided python module **multift.py** can be used to load the multisense FT object. 

```
ft = multift.MultiFastText(basename="modelfiles/modelname", multi=True)
```

We can query for nearest neighbors give a word or evaluate the embeddings against word similarity datasets. 

2. The script **eval/eval_model_wordsim.py** calculates the Spearman's correlation for multiple word similarity datasets given a model. We provide examples below.

```
python eval/eval_model_wordsim.py --modelname modelfiles/multi_text8_e10_d300_vs2e-4_lr1e-5_margin1 | tee log/eval_wordsim_text8.txt
python eval/eval_model_wordsim.py --modelname modelfiles/multi_text9_e10_d300_vs2e-4_lr1e-5_margin1 | tee log/eval_wordsim_text9.txt
```

Sample output of the text8. *sub* and *sub2* correspond to the Spearman's correlation of the first and second Gaussian components. We can see that having two components with potentially disentangled meanings improve the Spearman's correlation for word similarity. 
```
   Dataset        sub       sub2  sub-maxsim  
0       SL  26.746543  10.859781   27.699946  
1       WS  65.720245  34.064534   66.638705  
2     WS-S  70.978888  36.393886   70.474031  
3     WS-R  62.104036  34.294508   60.655725  
4      MEN  63.523683  34.983555   68.341550  
5       MC  57.521141  37.650201   66.266134  
6       RG  57.971173  50.623423   58.956847  
7       YP  33.104499  10.518915   38.473373  
8   MT-287  65.407845  45.664255   70.200717  
9   MT-771  52.972120  33.979479   56.735716  
10      RW  36.954597   3.707983   33.639994  
```

A sample script **eval/eval_text9_model_nn.py** show the nearest neighbors of words such as *rock*, *star*, and *cell* where we observe multiple meanings for each word.
```
python eval/eval_text9_model_nn.py | tee log/eval_text9_model_nn.txt
```
```
Nearest Neighbors for rock, cluster 0
Top highest similarity of rock cl 0
['rock,:0', ..., 'bedrock:0', 'rocky:0', 'rocks,:0', '[[rock:0', ...

Nearest Neighbors for rock, cluster 1
Top highest similarity of rock cl 1
['(band)]],:0', '(band)]]:0', 'songwriters:0', 'songwriter,:0', 'songwriter:0', ...
```

### Replicating Paper Results


```
python eval/eval_model_wordsim.py --modelname modelfiles/
```

```
TODO -- Add the results here
```

## 4. Analyze FastText Object in Python
We additionally provide a FastText python wrapper for the original FastText objects (for instance, models downloaded from ..) or our multisense-FastText objects. Our models are in the format that can be loaded by *multift.py* directly. One can also  convert FastText objects to our model format via:

```
./multift output-model modelfiles/downloaded_model.bin 
```

The models in our format will be saved in **modelfiles/downloaded_model.in**. This model can be loaded with our Python script using:
```
ft = multift.MultiFastText(basename=modelfiles/downloaded_model, multi=False)
```

The following script downloads the Wiki English embeddings from www.fasttext.cc, converts it to the python-readable format, and evaluate it on word similarity datasets.

```
https://s3-us-west-1.amazonaws.com/fasttext-vectors/wiki.en.zip -P modelfiles/
cd modelfiles
unzip wiki.en.zip
cd ..
./multift output-model modelfiles/wiki.en.bin
python eval/eval_model_wordsim.py --modelname modelfiles/wiki.en --multi 0
```
