# Machine-Translation-Using-Encoder-Decoder-Model
This repository contains a Jupyter Notebook implementing a machine translation model using an encoder-decoder architecture with LSTM for translating English sentences to French. The model is trained on a dataset of English-French sentence pairs and uses TensorFlow/Keras for building and training the neural network.
# Project Overview
The project demonstrates a sequence-to-sequence (seq2seq) model for machine translation. It includes data preprocessing, model training, and decoding functions to translate English sentences into French. The model leverages an encoder-decoder framework with LSTM layers to capture the context of input sentences and generate accurate translations.
## Key Features
* Dataset: English-French sentence pairs from a Kaggle dataset.
* Model Architecture: Encoder-Decoder with LSTM layers.
* Training: 100 epochs with a validation split, achieving ~87% validation accuracy.
* Inference: Sampling-based decoding to generate translations for input sentences.
* Output: Sample translations for 100 input sentences, e.g., "Go." → "Va !", "Run!" → "Fuyez !".
# Repository Contents
* Machine-translation-using-encoder-and-decoder.ipynb: The main Jupyter Notebook containing the implementation
* Eng2french.h5: Trained model weights.
# Getting Started
## Prerequisites
* Python 3.7+
* TensorFlow/Keras
* NumPy
* Jupyter Notebook
* Optional: GPU support for faster training
## Installation
* pip install tensorflow numpy jupyter
## Usage
1) Run the notebook cells sequentially to preprocess the data, train the model, and test translations.
2) The notebook includes a decoding function to translate new English sentences.
3) Example translations are printed for the first 100 sentences in the dataset.
# The model uses an encoder-decoder architecture:
* Encoder: Takes English sentences, processes them through an LSTM layer, and outputs state vectors.
* Decoder: Uses the encoder's state vectors and generates French translations via another LSTM layer.
* Training: The model is trained with categorical cross-entropy loss and RMSp
* Inference: A sampling loop generates translations character by character.
# Results
The model achieves a validation accuracy of approximately 87% after 100 epochs. Sample translations include:
* "Go." → "Va !"
* "Run!" → "Fuyez !"
* "Hello!" → "Salut !"
* "I won." → "J'ai gagné."
# Contributing
Contributions are welcome! Please open an issue or submit a pull request for improvements or bug fixes.
# Acknowledgments
* Dataset: Kaggle English-French Dataset
* Inspired by TensorFlow/Keras seq2seq tutorials.
