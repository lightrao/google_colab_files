# Google Colab Files

This repository contains Jupyter Notebooks and Python scripts designed for use within the Google Colab environment.

## Google Colab Usage

Follow these general steps to run the notebooks in Google Colab:

1.  **Open Google Colab:** Navigate to [https://colab.research.google.com/](https://colab.research.google.com/).
2.  **Upload Files:** You can either:
    *   Upload individual `.ipynb` files directly using `File -> Upload notebook...`.
    *   Clone the entire repository into your Colab environment using:
        ```bash
        !git clone <repository_url>
        ```
        (Replace `<repository_url>` with the actual URL of this repository). Then navigate to the notebook file within the Colab file browser.
    *   Mount your Google Drive (`from google.colab import drive; drive.mount('/content/drive')`) if you have cloned or uploaded the repository there, and navigate to the files.
3.  **Install Dependencies:** Before running the code in a notebook, install its specific dependencies using `!pip install ...` in a code cell (see specific instructions below).
4.  **API Keys (if required):** Some notebooks require API keys (e.g., OpenAI). You can set these using Colab's "Secrets" feature (recommended) or by setting environment variables within the notebook (e.g., `import os; os.environ['OPENAI_API_KEY'] = 'YOUR_API_KEY'`).
5.  **Run Notebook Cells:** Execute the cells in the notebook sequentially.

---

### Project: AI Agent - Customer Support (`ai-agent-crewai/agent_cutomer_support/`)

*   **File:** `L3_customer_support.ipynb`
*   **Description:** Demonstrates a multi-agent system for customer support using `crewai`.
*   **Dependencies:**
    ```bash
    !pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29
    ```
*   **API Key:** Requires an OpenAI API key. Set it using Colab Secrets or environment variables.

---

### Project: AI Agent - Research & Write Article (`ai-agent-crewai/agent_write_article/`)

*   **File:** `L2_research_write_article.ipynb`
*   **Description:** Uses a `crewai` team to research a topic, write an article, and edit it.
*   **Dependencies:**
    ```bash
    !pip install crewai==0.28.8 crewai_tools==0.1.6 langchain_community==0.0.29 numpy==1.25.2
    ```
*   **API Key:** Requires an OpenAI API key. The notebook attempts to use `userdata.get('OPENAI_API_KEY')` (Colab Secrets) or the `OPENAI_API_KEY` environment variable.

---

### Project: TensorFlow Serving - Spam Comment Model (`tfserving-flutter/codelab1/`)

*   **File:** `SpamCommentsModelMaker.ipynb`
*   **Description:** Trains a spam comment detection model using TensorFlow Lite Model Maker and exports it in `SavedModel` format for TensorFlow Serving.
*   **Dependencies:** The notebook installs `tflite-model-maker` directly using `%pip install -q tflite-model-maker`.
*   **Notes:** This notebook downloads its own data and outputs a `mm_spam_savedmodel.zip` file containing the trained model.

*   **File:** `SpamCommentsModelMaker.py`
*   **Description:** A Python script version for training the spam comment model.
*   **Usage in Colab:**
    1.  Ensure dependencies are installed (likely `tensorflow` and `tflite-model-maker`). You might need to adapt the installation from the notebook:
        ```bash
        !pip install tensorflow tflite-model-maker
        ```
    2.  Run the script using:
        ```bash
        !python tfserving-flutter/codelab1/SpamCommentsModelMaker.py
        ```

---
