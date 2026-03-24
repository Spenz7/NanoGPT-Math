# Please download the pretrained NanoGPT model on QA data from the [link](https://drive.google.com/file/d/1gIZw-HAB-tHtEYCmNugwlIV7R3WsgjjZ/view?usp=sharing), and place it into the folder `./sft`!

# If you have any questions, please feel free to open an issue on GitHub, and I will respond.

Teaching NanoGPT to Solve Math (DPO Fine-Tuning)
================================================

Overview
--------

This project fine-tunes a pretrained NanoGPT model (originally trained on QA data) to solve simple algebra and arithmetic problems using **Direct Preference Optimization (DPO)**.

The base model can answer basic QA (e.g., "What's your name?") but fails on math problems. This project improves its performance by training it on **positive-negative response pairs**.

* * * * *

Repository Structure
--------------------
```
├── dpo/\
│   ├── dpo.pt                  # Fine-tuned model (output)\
│   ├── dpoFinal.ipynb          # Main notebook (RUN THIS)\
│   └── pos_neg_pairs.json      # Training dataset (positive-negative pairs)\
├── sft/\
│   └── meta.pkl                # Tokenizer / codebook\
├── configurator.py             # NanoGPT config (unchanged)\
├── model.py                    # NanoGPT model (unchanged)\
├── positivenegativedatapairs.py # Script to generate dataset\
├── dpoTest(forColab).ipynb     # Optional: Colab version\
├── README.md
```

* * * * *

Setup Instructions
------------------

### 1\. Download Pretrained Model

Download the pretrained NanoGPT model (`gpt.pt`) from the original source and place it in:

./sft/gpt.pt

Notes:

-   This file is excluded via `.gitignore` (to stay under GitHub size limits)
-   Each team member must download it separately

* * * * *

### 2\. Install Requirements

Use Python with Jupyter Notebook. Recommended:

-   Python 3.8+
-   PyTorch

* * * * *

### 3\. Running the Project

The **main file to run is:**

dpo/dpoFinal.ipynb

Run all cells from top to bottom.

This notebook includes:

-   Data loading
-   DPO training
-   Model evaluation

* * * * *

Training Notes
--------------

-   GPU is strongly recommended:
    -   GPU: ~40 minutes (10 epochs)
    -   CPU: ~3 hours

### If you don't have a GPU

Use Google Colab.

* * * * *

Running on Google Colab (Optional)
----------------------------------

Use:

dpoTest(forColab).ipynb

This version:

-   Clones the GitHub repository within Colab
-   Adjusts file paths for the Colab environment
-   Includes additional setup cells for remote execution

### Important Notes

-   This notebook is adapted from `dpo.ipynb`. The only differences are:
    -   Additional initial cells to clone the repository (required for accessing project files in Colab)
    -   Adjustments to file paths to ensure compatibility with the Colab environment
-   This approach was used because Colab's built-in GitHub import allowed loading the repository, but did not properly support editing/running the original notebook in code format.
-   When running the notebook:
    -   Some output errors may appear initially; these are usually resolved by re-running the cells
    -   If the Step 7 output is incorrect, it is likely due to inconsistencies with the corresponding code in `dpo.ipynb`
-   The `dpo.ipynb` file in the `dpo/` folder should be treated as the reference implementation.
    -   The Colab notebook should match it exactly in logic
    -   The only differences should be the initial setup cells and file path adjustments
-   If both notebooks are consistent, the outputs should match accordingly.

* * * * *

Dataset (Task 1)
----------------

Training data consists of **positive-negative pairs**:

Example:

-   Negative: `"x*8=48, x=? Sorry, I don't know!"`
-   Positive: `"x*8=48, x=? The answer is 6 because 48/8 equals 6."`

Stored in:

dpo/pos_neg_pairs.json

Dataset size:

-   Recommended: ~100k samples
-   Minimum: 10k samples

* * * * *

Output
------

After training:

-   Fine-tuned model saved as:

    dpo/dpo.pt

-   Notebook prints evaluation results directly

Make sure outputs are visible in the notebook before submission.

* * * * *

Key Notes
---------

-   Do **not** modify:
    -   `model.py`
    -   `configurator.py`
-   Ensure:
    -   Notebook runs top-to-bottom without errors
    -   Outputs are saved in the notebook
    -   All required files are included in submission

* * * * *

Submission Files
----------------

Zip the following:

-   `dpo/dpo.pt`
-   `dpo/dpoFinal.ipynb`
-   `dpo/pos_neg_pairs.json`

* * * * *

Additional Notes
----------------

-   A newer VS Code Colab extension exists, which may simplify running notebooks compared to the previous Colab workflow.
-   More info: https://marketplace.visualstudio.com/items?itemName=Google.colab
-   If using it, you may not need the separate Colab notebook.





