# Customer Insights Analysis using Watson AI

This project provides a comprehensive analysis of customer data using IBM Watson's Natural Language Understanding service and machine learning techniques. The analysis includes sentiment analysis, customer segmentation, and predictive modeling.

## Features

- **Data Preprocessing**: Load and clean customer data, handle missing values
- **Sentiment Analysis**: Analyze customer reviews using IBM Watson NLU
- **Customer Segmentation**: Perform K-Means clustering based on income and spending patterns
- **Predictive Modeling**: Train a Random Forest model to predict spending scores
- **Visualization**: Generate insightful visualizations of the data and analysis results
- **Recommendations**: Provide actionable insights based on the analysis

## Requirements

- Python 3.8+
- Required Python packages:
  - pandas
  - numpy
  - matplotlib
  - seaborn
  - scikit-learn
  - ibm-watson
  - tqdm

## Setup

1. Clone this repository:
   ```bash
   git clone https://github.com/deappy/customer-insights-watson.git
   ```

2. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up IBM Watson credentials:
   - Create a `.env` file in the project root with your API credentials:
     ```
     WATSON_API_KEY=your_api_key
     WATSON_URL=your_service_url
     ```

## Usage

1. Place your customer data in a CSV file named `CSVFILE.csv` in the project root
2. Run the Jupyter notebook:
   ```bash
   jupyter notebook notebook.ipynb
   ```
3. Execute the cells in the notebook to perform the analysis

## File Structure

- `notebook.ipynb`: Main analysis notebook
- `README.md`: This documentation file
- `app.py`: (Optional) Streamlit application for serving results
- `.gitattributes`: Git configuration file

## Analysis Workflow

1. Data Loading and Preprocessing
2. Sentiment Analysis using IBM Watson NLU
3. Data Exploration and Visualization
4. Customer Segmentation using K-Means Clustering
5. Predictive Modeling with Random Forest
6. Insights Generation and Recommendations

## Results

The analysis generates several output files:
- `preprocessed_data.csv`: Cleaned and preprocessed data
- `partial_results.csv`: Data with sentiment analysis results
- `clustered_data.csv`: Data with customer segmentation results
- `spending_score_predictor.pkl`: Trained Random Forest model

## Contributing

Contributions are welcome! Please follow these steps:
1. Fork the repository
2. Create a new branch for your feature
3. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- IBM Watson Natural Language Understanding service
- Scikit-learn machine learning library
- Pandas and NumPy for data manipulation
