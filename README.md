# Spotify and YouTube Music Analysis Dashboard

## Project Overview

This project provides a comprehensive analysis of the "Spotify and YouTube" dataset, which contains a wealth of information about popular songs and their performance on two of the world's largest music streaming platforms. The primary objective of this project is to explore the dataset to uncover interesting trends and insights into what makes a song popular.

The project includes a detailed data analysis performed in a Jupyter Notebook and an interactive web-based dashboard built with Streamlit. The dashboard allows users to dynamically filter the data and visualize the analysis, making it easy to explore the relationships between different audio features and popularity metrics.

## Features

*   **In-depth Data Analysis:** A Jupyter Notebook (`analysis.ipynb`) provides a step-by-step analysis of the dataset, including data cleaning, exploratory data analysis, and visualization.
*   **Interactive Dashboard:** A user-friendly dashboard (`dashboard.py`) built with Streamlit allows for interactive exploration of the data.
*   **Data Filtering:** Users can filter the dataset by various audio features such as Danceability, Energy, and Loudness to narrow down the analysis.
*   **Data Visualization:** The dashboard includes a variety of visualizations, such as:
    *   Histograms to show the distribution of audio features.
    *   A correlation heatmap to visualize the relationships between variables.
    *   A scatter plot to compare Spotify streams and YouTube views.
*   **Compressed Dataset:** The dataset is compressed using gzip to reduce its size, making it easier to store and share.

## Dataset

The dataset used in this project is `Spotify Youtube Dataset.csv.gz`. It is a compressed CSV file containing data about thousands of songs. The dataset includes the following key features:

*   **Artist:** The name of the artist.
*   **Track:** The name of the song.
*   **Album:** The name of the album the song belongs to.
*   **Danceability:** A measure of how suitable a track is for dancing.
*   **Energy:** A measure of intensity and activity.
*   **Loudness:** The overall loudness of a track in decibels (dB).
*   **Speechiness:** The presence of spoken words in a track.
*   **Acousticness:** A measure of whether the track is acoustic.
*   **Instrumentalness:** Predicts whether a track contains no vocals.
*   **Liveness:** Detects the presence of an audience in the recording.
*   **Valence:** A measure of the musical positiveness conveyed by a track.
*   **Tempo:** The overall estimated tempo of a track in beats per minute (BPM).
*   **Stream:** The number of times the song has been streamed on Spotify.
*   **Views:** The number of times the video has been viewed on YouTube.
*   **Likes:** The number of likes the video has received on YouTube.
*   **Comments:** The number of comments the video has received on YouTube.

## Installation and Setup

To run this project, you need to have Python and pip installed on your system.

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/your-username/your-repository-name.git
    cd your-repository-name
    ```

2.  **Create and activate a virtual environment (optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required dependencies:**
    ```bash
    pip install streamlit pandas matplotlib seaborn
    ```

## Usage

### Running the Analysis Notebook

To view the detailed data analysis, you can run the Jupyter Notebook:

```bash
jupyter notebook analysis.ipynb
```

### Launching the Streamlit Dashboard

To launch the interactive dashboard, run the following command in your terminal:

```bash
streamlit run dashboard.py
```

This will open a new tab in your web browser with the dashboard.

## Technology Stack

*   **Python:** The core programming language used for the project.
*   **Pandas:** For data manipulation and analysis.
*   **Matplotlib & Seaborn:** For creating static and interactive visualizations.
*   **Streamlit:** For building the interactive web dashboard.
*   **Jupyter Notebook:** For the exploratory data analysis.

## Project Structure

```
.
├── analysis.ipynb
├── dashboard.py
├── Spotify Youtube Dataset.csv.gz
└── README.md
```

*   `analysis.ipynb`: Jupyter Notebook containing the detailed data analysis.
*   `dashboard.py`: Python script for the Streamlit dashboard.
*   `Spotify Youtube Dataset.csv.gz`: The compressed dataset.
*   `README.md`: This file.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
