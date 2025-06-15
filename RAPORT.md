## Training and Test Results

In this project, no explicit metrics were used during training. The main focus was on verifying whether the model is capable of generating **valid sequences** rather than achieving optimal performance.
Since this is an NLP task, qualitative inspection of the generated sequences was used to assess model behavior—e.g., coherence, grammatical correctness, and logical structure.
No BLEU, ROUGE, or accuracy scores were calculated in this version, as the primary goal was to understand the sequence generation process rather than benchmark performance.


## Model Choice Justification

The model was selected with the assistance of an LLM, and the decision was made to use an LSTM-based encoder-decoder architecture primarily due to its **faster training** time and **lower complexity** compared to transformers.

Although transformers currently dominate state-of-the-art benchmarks, they require significant engineering effort and resources. In contrast, LSTM models:
-	**Train faster** on small and medium datasets.
-	Are **easier to debug and analyze**, especially for educational purposes.
-	Can **achieve competitive** results on many real-world NLP tasks, particularly when the dataset is well-prepared and the task does not demand large-scale language modeling.

Therefore, for well-defined and concrete tasks (e.g., sequence tagging, text classification, or short-form generation), LSTM-based models can perform just as well as transformer-based ones—while being simpler and more efficient to train.


## Data Splitting Strategy

The dataset was created by concatenating three different CSV files containing question–answer pairs related to COVID-19. After data cleaning and renaming columns for consistency, 900 duplicate or irrelevant rows were removed.

The final dataset was randomly split into:
-	Training set: **80**%
-	Test set: **20**%

The splitting was done using train_test_split from scikit-learn, ensuring that both sets include diverse examples. No separate validation set was created—evaluation during training was performed directly on the test set to monitor overfitting.


## Input Data Description

The dataset consists of textual question–answer pairs about COVID-19. All entries were tokenized using nltk.word_tokenize, lowercased, and stripped of punctuation. A vocabulary was built based on all answers in the dataset, with rare words (frequency ≤10) excluded.

Special tokens were used:
-	**\<bos\>** (beginning of sequence)
-	**\<eos\>** (end of sequence)
-	**\<pad\>** (for padding)
-	**\<unk\>** (unknown words)

Each question and answer was converted into sequences of token IDs based on word2ind. Padding was applied dynamically in the collate_fn_with_padding function for batching. Maximum lengths were capped at:
-	Question: **256** tokens
-	Answer: **128** tokens

The FAQ_Dataset class was implemented using PyTorch’s Dataset, enabling flexible handling of train and inference modes.

## Results Analysis and Next Steps

The trained model is capable of generating answers to simple COVID-related questions. While its responses are not always precise or fluent, there are cases where the generated answers are surprisingly relevant and coherent, demonstrating that the model has captured some meaningful patterns in the data.

The current model uses a set of hyperparameters (e.g., embedding size, hidden dimension, dropout) that were selected via a basic greedy search during early experiments. However, further improvement is possible by:

-	Trying different hyperparameter configurations (e.g., more hidden layers, different dropout values, or increased vocabulary threshold).
-	Incorporating more high-quality training data to help the model generalize better.
-	Introducing evaluation metrics such as BLEU or ROUGE to track improvements quantitatively.

Additionally, adding a basic attention mechanism could help improve focus on relevant input tokens, and cleaning the dataset from noise or overly long sequences may also enhance performance.

The project shows promise as a baseline and provides a strong foundation for further development.
