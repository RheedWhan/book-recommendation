# Book Recommendation System using Machine Learning

[![Project Image](https://user-images.githubusercontent.com/115232340/201062991-1256ac4b-e96f-4103-8b54-cedee9b85c6b.png)](https://github.com/YourGitHubUsername/YourRepoName)

## Overview

This project focuses on creating a Book Recommendation System using machine learning algorithm. The system suggests similar books to users based on their interests. Recommender systems have become integral in various online platforms, from e-commerce to streaming services.

## Dataset

The dataset includes information on users, books identified by ISBN, and book ratings. Users' demographic data (location, age) is provided when available. The book dataset contains content-based information such as title, author, publication year, and publisher. Ratings can be explicit (1-10) or implicit (0).

**Dataset Link:** [Book Recommendation Dataset](https://www.kaggle.com/datasets/arashnic/book-recommendation-dataset)

## Visuals

- **Bar Graph:** Ratings distribution on books.
- **Line Plot:** Relationship between the year of publication and book ratings.
- **Correlation Plot and Pair Plot:** Explore relationships in the dataset.

## Functionality

The project includes a function to recommend the top 10 books based on the implemented algorithm. A pickle file is utilized for web development.

## Deployment

The book recommendation system is deployed using [Streamlit](https://streamlit.io/). Screenshots of the Streamlit app deployment are provided in the repository.

## Instructions for Running the Code

1. Clone the repository:

    ```bash
    git clone https://github.com/RheedWhan/book-recommendation.git
    ```

2. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Run the Streamlit app:

    ```bash
    streamlit run app.py
    ```

4. Open your browser and go to [http://localhost:8501](http://localhost:8501) to access the Book Recommendation System.

## Conclusion

This project successfully builds a reliable book recommendation system using unsupervised learning techniques. Contributors are encouraged to explore the dataset further and share insights in the comments.

