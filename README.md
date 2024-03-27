# Intrusion Detection System using Machine Learning

This repository contains code for a simple Intrusion Detection System (IDS) using machine learning techniques. The system aims to classify network connections as either "normal" or "anomaly" based on various parameters extracted from network traffic.

## Dataset
The system uses a dataset containing network traffic information with the following features:

- `src_bytes`: Number of data bytes from source to destination
- `dst_bytes`: Number of data bytes from destination to source
- `same_srv_rate`: Percentage of connections to the same service
- `flag`: Connection status (e.g., SYN, ACK)
- `diff_srv_rate`: Percentage of connections to different services
- `dst_host_srv_count`: Number of connections to the same host
- `dst_host_same_srv_rate`: Percentage of connections to the same service from the same host
- `count`: Number of connections to the same host as the current connection
- `protocol_type`: Protocol type (e.g., TCP, UDP)
- `serror_rate`: Percentage of connections that have "SYN" errors

## Models Used
The system employs the following machine learning models for classification:

1. Logistic Regression
2. Gradient Boosting Trees (using XGBoost)
3. Decision Trees
4. Gaussian Naive Bayes

## Usage
1. Clone the repository:

```bash
git clone https://github.com/yourusername/intrusion-detection-system.git
```

2. Install the required dependencies:

```bash
pip install -r requirements.txt
```

3. Run the `detection.ipynb` notebook to train and evaluate the models:

```bash
python detection.ipynb
```

## Results
After running the `detection.ipynb` notebook, you will see the evaluation results of each model on the dataset. The evaluation metrics may include accuracy, precision, recall, confusion matrix, and F1-score.