# Google-Play-store-Data-Analysis
This project provides an in-depth analysis of Google Play Store apps and user reviews, focusing on understanding app performance, user sentiment, and key trends in app categories. Using Python, I performed data cleaning, feature engineering, and exploratory data analysis (EDA) on app data and reviews
Google-Play-store-Data-Analysis
# Overview
This project aims to visualize various aspects of app data using different types of charts and graphs. The visualizations include scatter plots, choropleth maps, grouped bar charts, dual-axis charts, bubble charts, heatmaps, and violin plots. Each visualization is designed to provide insights into app performance, user engagement, and other key metrics.

# Visualizations
# Scatter Plot

Description: Visualizes the relationship between revenue and the number of installs for paid apps only.

Details: Includes a trendline to show the correlation and color-codes the points based on app categories.

# output visualization 

![Scatter plot](https://github.com/user-attachments/assets/cb46546e-f972-4a05-9ac9-4ff0f36261a1)



# Interactive Choropleth Map

Description: Uses Plotly to visualize global installs by category.

Details: Applies filters to show data for only the top 5 app categories and highlights categories where the number of installs exceeds 1 million. Excludes app categories starting with "A," "C," "G," or "S." This graph is displayed only between 6 PM IST and 8 PM IST.

# output visualization 

![Choropleth Map](https://github.com/user-attachments/assets/f0cb1b9d-6c7c-4b2c-8f5d-a81e9e1c778e)


# Grouped Bar Chart

Description: Compares the average rating and total review count for the top 10 app categories by number of installs.

Details: Filters out categories with an average rating below 4.0, size below 10 MB, and last update not in January. This graph is displayed only between 3 PM IST and 5 PM IST.

# output visualization

![Grouped BarChart](https://github.com/user-attachments/assets/07cd1507-c416-4649-8922-d0f5db5d00c2)




# Dual-Axis Chart

Description: Compares the average installs and revenue for free vs. paid apps within the top 3 app categories.

Details: Excludes apps with fewer than 10,000 installs, revenue below $10,000, Android version below 4.0, size below 15 MB, content rating not "Everyone," and app names longer than 30 characters. This graph is displayed only between 1 PM IST and 2 PM IST.

# output visualization

![Dual AxisChart](https://github.com/user-attachments/assets/6ee401f7-4738-41fc-b741-e3375d165f41)


# Bubble Chart

Description: Analyzes the relationship between app size (in MB) and average rating, with bubble size representing the number of installs.

Details: Includes only apps with a rating higher than 3.5 in the "Games" category and installs more than 50k. This graph is displayed only between 5 PM IST and 7 PM IST.

# output visualization

![Bubble chart](https://github.com/user-attachments/assets/28d63a8d-f7ed-44c5-8dbd-f04389cda8d6)


# Heatmap

Description: Shows the correlation matrix between installs, ratings, and review counts.

Details: Includes only apps updated within the last year, with at least 100,000 installs, review count more than 1k, and genres not starting with "A," "F," "E," "G," "I," or "K." This graph is displayed only between 2 PM IST and 4 PM IST.

# output visualization  


![Task 6](https://github.com/user-attachments/assets/9ce298a9-b1e1-4e7b-8570-ce43d6f73d09)


# Violin Plot

Description: Visualizes the distribution of ratings for each app category.

Details: Includes only categories with more than 50 apps, app names containing the letter "C," and excludes apps with fewer than 10 reviews and ratings below 4.0. This graph is displayed only between 4 PM IST and 6 PM IST.

# output visualization

![Task_7_Violin Plot](https://github.com/user-attachments/assets/5e94f298-e38a-461e-a612-7ba21bafa34f)


# Installation
Clone the repository:

git clone https://github.com/KesavprasathM/Google-Play-store-Data-Analysis.git
Install the required dependencies:

 pip install pandas numpy matplotlib seaborn plotly

Run the main script to generate the visualizations:

python main.py
The visualizations will be saved in the output directory.

# Contributing

Contributions are welcome! Please fork the repository and submit a pull request with your changes.

# License

This project is licensed under the MIT License. See the LICENSE file for more details.
