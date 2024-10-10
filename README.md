# IMDA_data_processing_analysis_sentiment

This repository contains notebooks, data, and visualizations for Our Capstone Sentiment Analysis Project Phase 2 of utilizing the Singapore IMDA Nation Corpus Speech Dataset - PART 6 Call Center Design Part.  
The project aims to develop and fine-tune models for analyzing sentiments in call center audio recordings.

## Overview

This project builds upon the foundation established in Phase 1, focusing on custom self-built audio sentiment dataset, for sentiment analysis in the call center context. The datasets used are derived from the IMDA National Speech Corpus, specifically the call center part, which provides a diverse set of dialogues for training and evaluation.

### Contents

	•	notebooks/: Contains various Jupyter notebooks for data processing, labeling, model training, evaluation, and voting analysis.
	•	doc/: This folder includes key visualizations that illustrate different aspects of the methodology and results.
	•	data/: Placeholder for the data used in the project.
	•	utils_checkpoints.py / utils_v2.py: Utility scripts for supporting the notebooks.
	•	README.md: Project documentation.


## Methodology

#### Data Processing Flow

The above image illustrates the workflow for processing the IMDA dataset, including data augmentation, train-test splitting, feature engineering, and sentiment labeling.

![Data Processing Flow](doc/data_processing_flow.png)


#### LLM Prompting

This image describes how Large Language Models (LLMs) are leveraged for sentiment annotation. The process involves generating prompts and using LLMs such as GPT for labeling sentiments based on provided dialogues.

![LLM Prompt](doc/LLM_Prompt.png)

#### Ground truth labelling Annotation

The methodology includes multiple steps, from dataset consolidation, feature selection, and model fine-tuning to ensemble strategies. These steps are aimed at improving the accuracy and robustness of the sentiment classification.

![ground truth labelling](doc/methodology.png)


#### Discrepancy in Score Distribution

This figure highlights the differences in sentiment score distribution between different models or labeling strategies (e.g., Gemini vs. GPT-4). It provides insights into how models may vary in sentiment scoring due to different LLM models.

![Discrepancy](doc/score_disctirbution_discrepancy.png)

#### How to Use the Notebooks

	1.	Data Preparation: Use the data processing notebooks (01_v2_IMDA_processing_*.ipynb) to preprocess and prepare the datasets for training and evaluation.
	2.	Sentiment Labeling: The notebooks (02_v1_IMDA_labelling_Sentiment_base.ipynb, 03_v11_IMDA_labelling_sentiment_GPT4o.ipynb, etc.) are used for applying different LLMs and NLP tools to label sentiment scores.
	3.	Voting Analysis: The 05_v0_IMDA_labelling_exp_voting_analysis.ipynb and related notebooks are designed to analyze the consensus between different models/labelers and determine the final sentiment label.
	4.	Model Training and Evaluation: Use the 06_fine_tune_models_V3.ipynb and 06_model_evaluationV3.ipynb notebooks to fine-tune the models on the processed data and evaluate their performance.


## License & Contact

This project is sponsor by NCS, Singapore. This repo is for capstone project code submission only. 
**NOT for any commericial usage without grants**  
For any questions or issues, please contact Bianca at e0533381@u.nus.edu .