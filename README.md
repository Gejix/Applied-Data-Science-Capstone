# Applied Data Science Capstone: Winning the Space Race with Data Science

Welcome to the repository for my Applied Data Science Capstone project, part of the Coursera/IBM Data Science Professional Certificate. This project explores the competitive dynamics in the space industry, particularly focusing on the potential of an emerging company, Space Y, to rival SpaceX. The project includes various methodologies, exploratory data analysis, and predictive modeling.

## Repository Overview

This repository contains all the code and documentation related to my capstone project. Below is a summary of the project's structure and key findings.

### Table of Contents

1. [Executive Summary](#executive-summary)
2. [Introduction](#introduction)
3. [Methodology](#methodology)
4. [Results](#results)
5. [Conclusion](#conclusion)
6. [Appendix](#appendix)
7. [Links](#links)

## Executive Summary

In this study, various methodologies were employed for data analysis:

- **Data Collection:** Utilized web scraping and the SpaceX API.
- **Exploratory Data Analysis (EDA):** Conducted data wrangling, visualization, and interactive visual analytics.
- **Machine Learning Prediction:** Applied multiple models to predict key characteristics influencing launch success.

### Key Findings

- Successfully gathered valuable data from public sources.
- Identified pivotal features influencing launch success through EDA.
- Determined the optimal model for predicting successful launches.

## Introduction

The primary aim of this project is to assess the feasibility of Space Y establishing a competitive stance against SpaceX. The analysis addresses critical inquiries to inform strategic decisions for Space Y.

### Objectives

1. **Cost Estimation:** Determine the most effective method for estimating total launch costs using predictive models.
2. **Optimal Launch Locations:** Identify geographic sites offering favorable conditions for successful and cost-effective launches.

## Methodology

### Data Collection

- **SpaceX API:** [API Documentation](https://api.spacexdata.com/v4/rockets/)
- **Web Scraping:** Data from the [Falcon 9 Launches Wikipedia Page](https://en.wikipedia.org/wiki/List_of_Falcon_9_and_Falcon_Heavy_launches)

### Data Processing

- Ensured data cleanliness and coherence.
- Created landing outcome labels from summarized data.

### Exploratory Data Analysis (EDA)

- Visualization techniques and SQL for data exploration.
- Interactive visual analytics using Folium and Plotly Dash.

### Predictive Analysis

- Employed classification models: logistic regression, support vector machines, decision trees, and k-nearest neighbors.
- Evaluated model performance to identify the most effective predictive approach.

## Results

### Exploratory Data Analysis

- SpaceX operates 4 distinct launch sites.
- The average payload of the F9 v1.1 booster is 2,928 kg.
- The first successful landing occurred in 2015.
- Several Falcon 9 boosters successfully landed on drone ships.
- Nearly 100% of mission outcomes were successful.

### Predictive Analysis

- **Decision Tree Classifier** emerged as the most effective model, with an accuracy exceeding 87%.

### Key Insights

- CCAFS SLC 40 is the top-performing launch site.
- Success rates for launches improved over time.
- Payloads exceeding 9,000 kg exhibit a high success rate.

## Conclusion

- KSC LC-39A is identified as the optimal launch site.
- Payloads exceeding 7,000 kg pose a lower risk.
- The Decision Tree Classifier effectively predicts successful landings, enhancing profitability.

## Appendix

- Detailed SQL queries and visualizations used in the EDA.
- Data wrangling steps and Jupyter notebooks for reproducibility.

## Links

- [GitHub Repository](https://github.com/Gejix/Applied-Data-Science-Capstone)
- [Data Collection (API)](https://github.com/Gejix/Capstone/blob/main/jupyter-labs-spacex-data-collection-api.ipynb)
- [Data Collection (Scraping)](https://github.com/Gejix/Capstone/blob/main/jupyter-labs-webscraping.ipynb)
- [Data Wrangling](https://github.com/Gejix/Capstone/blob/main/labs-jupyter-spacex-Data%20wrangling.ipynb)
- [Exploratory Data Analysis](https://github.com/Gejix/Capstone/blob/main/jupyter-labs-eda-dataviz.ipynb)
- [EDA with SQL](https://github.com/Gejix/Capstone/blob/main/jupyter-labs-eda-sql-coursera_sqllite.ipynb)
- [Launch Site Visualization](https://github.com/Gejix/Capstone/blob/main/lab_jupyter_launch_site_location.ipynb)
- [Dash App](https://github.com/Gejix/Capstone/blob/main/Dash_SpaceX_App.py)
- [Predictive Analysis](https://github.com/Gejix/Capstone/blob/main/lab_jupyter_launch_site_location.ipynb)

Feel free to explore the repository and reach out if you have any questions or feedback!

