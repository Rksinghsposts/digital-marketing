# Digital Marketing AI Agent 🚀

An intelligent agent that researches trending digital marketing topics and generates SEO-optimized blog posts automatically.

## Features
- **Trend Research**: Finds the latest trends using DuckDuckGo Search.
- **Content Generation**: Writes professional blog posts using OpenAI.
- **User Interface**: Clean and easy-to-use Streamlit dashboard.

## Setup

1.  **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

2.  **Environment Setup**:
    - The app uses an `.env` file to store your OpenAI API Key.
    - Ensure your key is in `.env` or enter it in the app sidebar.

3.  **Run the App**:
    ```bash
    streamlit run app.py
    ```

## Functionality
1.  Enter a niche (e.g., "Social Media Marketing").
2.  Click **Search for Trends**.
3.  Select a trending topic from the results.
4.  Click **Generate Blog** to get a full article.
