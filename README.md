# Movie Data Analysis Project

## Project Overview

This project focuses on analyzing movie data obtained from Rotten Tomatoes. The project involves three main stages:

1. **Web Scraping**: We scraped data for 300 movies from the Rotten Tomatoes website, capturing the movie name, audience score, and critic score.
2. **Exploratory Data Analysis (EDA) and Visualization**: We conducted an in-depth analysis of the dataset using visualizations to understand the distribution and relationships between the features.
3. **Clustering**: We performed clustering on the dataset based on the audience and critic scores to group similar movies together.

## 1. Web Scraping

We started by scraping movie data from the Rotten Tomatoes "Movies at Home" section. Using Python's `Selenium`, `requests` and `BeautifulSoup` libraries, we extracted the movie names, audience scores, and critic scores. The scraping process involved:

- Automating the "Load More" button on the Rotten Tomatoes page to fetch more movies.
- Extracting and storing the data into a CSV file.

The resulting dataset consists of 300 movies, with three columns: `Movie Name`, `Audience Score`, and `Critics Score`.

## 2. Exploratory Data Analysis (EDA) and Visualization

After obtaining the data, we performed EDA to uncover insights and patterns:

- **Histograms**: We plotted the distribution of both the critics' and audience scores to understand how these scores are spread across the dataset.
- **Scatter Plot**: We plotted a scatter plot to examine the relationship between audience and critic scores, with interactive features allowing users to hover over points to see the movie names and scores.

All visualizations were created using Plotly, which provides interactive and aesthetically pleasing plots.

## 3. Clustering

Finally, we applied clustering to the data:

- **K-Means Clustering**: We used the K-Means algorithm to cluster movies based on their audience and critic scores.
- **Silhouette Score**: We calculated the silhouette score to determine the optimal number of clusters.
- **Cluster Visualization**: The clusters were visualized with a scatter plot, where each cluster is color-coded to show distinct groupings of movies based on their scores.

## Conclusion

This project demonstrates how to collect, analyze, and extract insights from movie data. The final dataset and analysis can be used for various purposes, such as recommending movies or understanding trends in movie ratings.

## Files Included

- **`rottentomatoes_movies.csv`**: The scraped dataset containing 300 movies with their names, audience scores, and critic scores.
- **Python Scripts**: Scripts for scraping, EDA, and clustering.
- **Visualizations**: Plotly visualizations of the data analysis and clustering results.

## Requirements

To run this project, you need the following Python libraries:

- `requests`
- `BeautifulSoup`
- `pandas`
- `matplotlib`
- `numpy`
- `plotly`
- `scikit-learn`
- `selenium` (if web scraping is repeated)

This project provides a comprehensive look at the process of data collection, analysis, and machine learning application in the context of movie ratings.
