# Probabilistic FastText for Multi-Sense Embeddings

## Getting Started

1. Compile the C++ files.
```
make
```

2. Obtain text data. We included scripts to download text8 and text9. 
```
bash get_text9.sh
```

3. Run a sample script.
```
bash exps/train_text9_multi.sh
```
After the training is complete, the following model files will be saved:

model.words     List of words in the dictionary
model.bin       A binary file for the subword embedding model
model.in        The subword embeddings
model.in2       The subword embeddings for the second component.
model.subword   The final representation of words in the dictionary. Note that the representation for words outside the dictionary can be computed using the provided python module.

4. The provided python module **multift.py** can be used to load the multisense FT object. 

ft = multift.MultiFastText(basename="", multi=True)

We can query for nearest neighbors give a word or evaluate the embeddings against word similarity datasets. See the code for the API.

5. Sample scripts **eval/eval_text9_model_nn.py** and **eval/eval_text9_model_wordsim.py** show the nearest neighbors and the word similarity respectively. 

```
python eval/eval_text9_model_nn.py | tee log/eval_text9_model_nn.txt
python eval/eval_text9_model_wordsim.py | tee log/eval_text9_model_wordsim.txt
```

