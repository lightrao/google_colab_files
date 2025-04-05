# Codelab 1: Spam Comment Detection Model Training

This codelab demonstrates how to train a text classification model to detect spam comments using TensorFlow Lite Model Maker. The trained model is then exported in a format suitable for deployment with TensorFlow Serving.

## Workflow

The `SpamCommentsModelMaker.ipynb` Jupyter Notebook performs the following steps:

1.  **Setup:** Installs the `tflite-model-maker` library and imports necessary TensorFlow and Model Maker components.
2.  **Data Acquisition:** Downloads the `comment-spam.csv` dataset containing text comments labeled as spam or not spam.
3.  **Model Specification:** Defines an `average_word_vec` model specification. This approach uses pre-trained word embeddings and is generally faster to train than BERT-based models, though potentially less accurate. Key parameters like vocabulary size (`num_words`), sequence length (`seq_len`), and embedding dimension (`wordvec_dim`) are set.
4.  **Data Loading:** Loads the CSV data using `DataLoader.from_csv`, specifying the text and label columns, and splits it into 90% training and 10% testing data.
5.  **Model Training:** Creates and trains the text classification model using `text_classifier.create` for 50 epochs, using the training data and validating with the test data.
6.  **Evaluation:** Evaluates the trained model's loss and accuracy on the training data.
7.  **Export:** Exports the trained model, vocabulary, and labels to the `/mm_spam_savedmodel/` directory in the `SavedModel` format.
8.  **Versioning:** Renames the `saved_model` subfolder to `123` (a common practice for TensorFlow Serving versioning).
9.  **Packaging:** Zips the entire `/mm_spam_savedmodel/` directory into `mm_spam_savedmodel.zip` for easier download or transfer.
10. **(Optional) Embedding Export:** Includes code to export word embeddings and metadata (`vecs.tsv`, `meta.tsv`) for visualization using the TensorFlow Projector.

## How to Run

1.  **Environment:** This notebook is designed to run in a Google Colab environment or a similar setup with TensorFlow 2.x installed.
2.  **Install Dependencies:** Run the first cell to install `tflite-model-maker`.
    ```python
    %pip install -q tflite-model-maker
    ```
3.  **Execute Notebook:** Run the subsequent cells in `SpamCommentsModelMaker.ipynb` sequentially. The notebook will download data, train the model, and export the results.
4.  **Output:** The primary output is the `mm_spam_savedmodel.zip` file containing the trained model ready for TensorFlow Serving. You can find and download this file from the Colab file browser.

This codelab provides a practical example of using Model Maker for a common text classification task and preparing the model for serving.
