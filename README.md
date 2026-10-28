# English–French Translation with an LSTM Encoder–Decoder

A sequence-to-sequence learning notebook for English-to-French translation using TensorFlow/Keras.

## Why this project matters

Encoder–decoder models provide a concrete foundation for understanding sequence representation, teacher forcing, and autoregressive decoding.

## Technical focus

Python · TensorFlow/Keras · NumPy · text preprocessing · LSTM sequence models

## Explore the implementation

Open [the notebook](<machine-translation-using-encoder-and-decoder.ipynb>) to inspect preprocessing, implementation, and saved outputs.

## Run locally

```bash
git clone https://github.com/Arjun1443/Machine-Translation-Using-Encoder-Decoder-Model.git
cd Machine-Translation-Using-Encoder-Decoder-Model
python -m venv .venv
# Activate .venv before continuing.
python -m pip install tensorflow numpy jupyter
python -m jupyter notebook
```

Select `machine-translation-using-encoder-and-decoder.ipynb` in Jupyter and review its configuration before executing cells in order.

## Reproducibility notes

Review the notebook's English–French dataset path before execution; the dataset and an `Eng2french.h5` checkpoint are not present in the repository tree. Training requires time and may benefit from a GPU. Token-level validation accuracy is not equivalent to translation quality; inspect held-out translations and use an appropriate translation metric before reporting performance.

Saved notebook outputs describe a prior execution; they are not an independently reproduced benchmark. Dependency versions are not locked, so compatibility may require adjustment.


## Author

[Naga Anweesh Reddy](https://github.com/Arjun1443/Naga-Anweesh-Reddy) · AI development and technical training
