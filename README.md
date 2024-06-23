# Embedding ML Models in GUIs

### Introduction

This project aims to provide a comprehensive application for predicting customer churn using machine learning models. The application integrates data exploration, prediction capabilities, and historical logging into a user-friendly graphical user interface (GUI).

### Project Structure

```
Embedding-ML-Models-in-GUIs
├── Data
│   ├── history.csv
│   ├── LP2_Telco-churn-second-data.csv
│   ├── Telco-churn-last-200.csv
│   └── train.csv
├── Models
│   ├── AdaBoost.joblib
│   ├── Decision_tree.joblib
│   ├── encoder.joblib
│   ├── knn.joblib
│   ├── Logistic_reg.joblib
│   ├── random_forest.joblib
│   └── XGBoost.joblib
├── Pages
│   ├── 01_Data.py
│   ├── 02_Dashboard.py
│   ├── 03_Predict.py
│   └── 04_History.py
├── venv
├── .gitignore
├── config.yaml
├── Home.py
├── LICENSE
└── README.md
```

### Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/heldana30/Embedding-ML-Models-in-GUIs.git
   ```
2. Navigate to the project directory:
   ```bash
   cd Embedding-ML-Models-in-GUIs
   ```
3. Create a virtual environment and activate it:
   ```bash
   python -m venv venv
   venv\Scripts\activate  # On MAC use `source venv/bin/activate `
   
   ```
4. Install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

### Usage

1. Start the Streamlit application:
   ```bash
   streamlit run Home.py
   ```
2. Navigate through the different pages:
   - **Home page**: Log in to access the rest of the pages and explore relevant content about the application.
   - **Data Page**: Explore and filter the dataset.
   - **Dashboard Page**: View interactive visualizations and KPIs.
   - **Predict Page**: Input customer data to predict churn or upload a file for batch predictions.
   - **History Page**: Review past predictions.

## Article

| Topic                    | Link                                      |
|--------------------------|-------------------------------------------|
| Detailed Project Article | [Read the full article here](https://medium.com/@nheldana8/) |


## 👥 Author <a name="authors"></a>

👩‍💻 **Heldana Natnael Ambaw**

- GitHub: [GitHub Profile](https://github.com/heldana30)

- LinkedIn: [LinkedIn Profile](https://www.linkedin.com/in/heldana-n/)

## 🙏 Acknowledgments <a name="acknowledgements"></a>

A big shoutout to my awesome team, Team Curium! ♥
Your support, guidance, and collaboration have been invaluable.


### References

- Streamlit Documentation: https://docs.streamlit.io/
- Seaborn Documentation: https://seaborn.pydata.org/
- Plotly Documentation: https://plotly.com/python/
