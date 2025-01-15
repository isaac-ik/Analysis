Analysis Repository
===================

This repository contains two individual projects developed as part of my coursework, each focused on data analysis and visualization. The projects explore sales performance analytics and football team performance analytics, showcasing data processing, visualization, and insights generation using Python and Power BI.

Project 1: Football Teams Performance Analytics
-----------------------------------------------

**Author:** Isaac Ikhaiduwor

This project involves the development of a Football Performance Dashboard using Python and data visualization libraries. The goal is to assist teams, leagues, media organizations, and betting operators in making optimal decisions based on Premier League team performances.

### Key Features:

#### Team Performance Analysis:

-   Compared and visualized the number of wins, draws, and losses for each team.

#### Goal Analysis:

-   Analyzed the distribution of goals scored and conceded across different time intervals.

-   Compared the number of clean sheets for each team.

#### Streak Analysis:

-   Identified the longest winning, drawing, and losing streaks.

-   Compared the biggest wins and losses, both home and away.

#### Discipline Analysis:

-   Visualized yellow and red card distribution across different time intervals.

#### Team Comparison:

-   Used bar charts to compare goals scored, clean sheets, and cards received.

-   Built a Streamlit dashboard for side-by-side performance comparisons.

### Data Collection and Processing:

-   Automated data retrieval using API-football (freemium sports API).

-   Tools Used: Python libraries - `json`, `pandas`.

### Workflow:

1.  Converted JSON response data into a Python dictionary.

2.  Flattened nested dictionaries for easier data manipulation.

3.  Converted the data into a pandas DataFrame.

4.  Consolidated team data into a single CSV (`TeamsStat.csv`).

### Files Included:

-   `Sport Analytics.html`: Project report and description.

-   `TeamsStat.csv`: Cleaned dataset used for analysis.

-   `Visuals.py`: Python scripts for data visualization.

-   `requirements.txt`: List of required Python libraries.

-   `streamlit_app.py`: Streamlit application for interactive dashboards.
<img width="928" alt="club comparison visualization" src="https://github.com/user-attachments/assets/b1e22156-91eb-4087-891c-2fe0f8404f01" />

* * * * *

Project 2: Sales Performance Analytics
--------------------------------------

This project involves analyzing sales data and developing a **Power BI Dashboard** to assist Sales and Marketing teams in making data-driven decisions for improved customer targeting and increased sales.

### Key Insights and Business Questions Addressed:

#### Sales Performance:

-   What is the total sales amount and profit generated?

-   How many items were sold in total?

-   What is the average order amount and profit?

#### Category and Sub-Category Analysis:

-   Which categories and sub-categories are most popular in terms of sales and profit?

-   Are there any seasonal trends in category sales?

#### Payment Method Analysis:

-   What are the preferred payment methods?

-   Do certain payment modes correlate with higher order amounts or profits?

#### Customer Analysis:

-   How many unique customers made purchases?

-   What is the average number of orders per customer?

-   Are there repeat customers, and how frequently do they purchase?

#### Geographic Analysis:

-   Which states or cities generate the highest sales?

-   Are there regional trends in product preferences?

#### Time-Based Analysis:

-   How do sales vary across months and seasons?

-   Are there specific days of the week with peak sales?

#### Profitability Analysis:

-   Which products or categories have the highest profit margins?

-   Are there any unprofitable products that should be reconsidered?

### Tools Used:

-   **Power BI** for data visualization and dashboard creation.

-   **Python (pandas, json)** for data preprocessing and cleaning.

* * * * *

How to Use This Repository
--------------------------

1.  **Clone the Repository:**

    ```
    git clone https://github.com/isaac-ik/Analysis-Repo.git
    ```

2.  **Navigate to the Project Directory:**

    ```
    cd Analysis-Repo
    ```

3.  **For Football Analytics:**

    -   Open `streamlit_app.py` to launch the interactive dashboard.

    -   Run the notebook for data preprocessing and analysis.

4.  **For Sales Analytics:**

    -   Open the Power BI file to explore the dashboard.

* * * * *

Author
------

**Isaac Ikhaiduwor**
