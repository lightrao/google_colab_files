# %% [markdown]
# <a href="https://colab.research.google.com/github/lightrao/google_colab_files/blob/master/tfserving-flutter/codelab1/SpamCommentsModelMaker.ipynb" target="_parent"><img src="https://colab.research.google.com/assets/colab-badge.svg" alt="Open In Colab"/></a>

# %%
# Install Model maker
# %pip install -q tflite-model-maker &> /dev/null

# %%
# Imports and check that we are using TF2.x
import numpy as np
import os

from tflite_model_maker import configs
from tflite_model_maker import ExportFormat
from tflite_model_maker import model_spec
from tflite_model_maker import text_classifier
from tflite_model_maker.text_classifier import DataLoader

import tensorflow as tf

assert tf.__version__.startswith("2")
tf.get_logger().setLevel("ERROR")

# %%
# Download the dataset as a CSV and store as data_file
data_file = tf.keras.utils.get_file(
    fname="comment-spam.csv",
    origin="https://storage.googleapis.com/laurencemoroney-blog.appspot.com/lmblog_comments.csv",
    extract=False,
)

# %%
# Use a model spec from model maker. Options are 'mobilebert_classifier', 'bert_classifier' and 'average_word_vec'
# The first 2 use the BERT model, which is accurate, but larger and slower to train
# Average Word Vec is kinda like transfer learning where there are pre-trained word weights
# and dictionaries
spec = model_spec.get("average_word_vec")
spec.num_words = 2000 # The number of words to use in the vocabulary
spec.seq_len = 20 # The length of the input sequences
spec.wordvec_dim = 7 # The number of dimensions for the word vectors

# %%
# Load the CSV using DataLoader.from_csv to make the training_data
data = DataLoader.from_csv(
    filename=data_file,
    text_column="commenttext",
    label_column="spam",
    model_spec=spec,
    delimiter=",",
    shuffle=True,
    is_training=True, # Set to False if you want to use the data for validation or testing
)

train_data, test_data = data.split(0.9)

# %%
# Build the model
# The model is built using the model_spec and the training data
model = text_classifier.create(
    train_data, model_spec=spec, epochs=50, validation_data=test_data
)

# %%
loss, accuracy = model.evaluate(train_data)

# %%
# This will export to SavedModel format with the model, vocabulary and labels.
model.export(
    export_dir="/mm_spam_savedmodel/",
    export_format=[ExportFormat.LABEL, ExportFormat.VOCAB, ExportFormat.SAVED_MODEL],
)

# You can find your files in colab by clicking the 'folder' tab to the left of
# this code window, and then navigating 'up' a directory to find the root
# directory listing -- and from there you should see /mm_spam_savedmodel/

# %%
# Rename the SavedModel subfolder to a version number
# !mv /mm_spam_savedmodel/saved_model /mm_spam_savedmodel/123
# !zip -r mm_spam_savedmodel.zip /mm_spam_savedmodel/

# %%
# Optional extra
# You can use this cell to export details for projector.tensorflow.org
# Where you can explore the embeddings that were learned for this dataset
embeddings = model.model.layers[0]
weights = embeddings.get_weights()[0]
tokenizer = model.model_spec.vocab

import io

out_v = io.open("vecs.tsv", "w", encoding="utf-8")
out_m = io.open("meta.tsv", "w", encoding="utf-8")
for word in tokenizer:
    # word = tokenizer.decode([word_num])
    value = tokenizer[word]
    embeddings = weights[value]
    out_m.write(word + "\n")
    out_v.write("\t".join([str(x) for x in embeddings]) + "\n")
out_v.close()
out_m.close()


try:
    from google.colab import files
except ImportError:
    pass
else:
    files.download("vecs.tsv")
    files.download("meta.tsv")
