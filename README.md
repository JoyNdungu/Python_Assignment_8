CORD-19 Data Analysis and Streamlit App
📌 Assignment Overview

This project explores the CORD-19 metadata dataset by performing data cleaning, analysis, and visualization.
It also includes a Streamlit web application that allows interactive exploration of the research papers.


📂 Project Structure
├── analysis.ipynb       # Jupyter Notebook with full analysis
├── streamlit_app.py     # Streamlit application
├── metadata.csv         # Dataset (ignored in .gitignore if large)
├── .gitignore           # Files to be ignored by Git
└── README.md            # Project documentation

🛠️ Tools & Libraries

Python 3.7+

pandas

matplotlib

seaborn

streamlit

wordcloud

📊 Key Analysis & Visualizations

Number of publications per year

Top journals publishing COVID-19 research

Word cloud of frequent words in paper titles

Distribution of paper counts by source

🚀 How to Run
1. Clone the repo
git clone https://github.com/JoyNdungu/Python_Assignment_8.git
cd Python_Assignment_8

2. Install dependencies
pip install -r requirements.txt


(You may create a requirements.txt later with pip freeze > requirements.txt)

3. Run the Streamlit app
streamlit run streamlit_app.py
