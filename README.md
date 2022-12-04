# SQLAlchemy-challenge
Module 10 Challenge: Advanced Data Storage &amp; Retrieval

![surfs-up](https://user-images.githubusercontent.com/112173540/205469927-1efe6554-3e67-48f6-94bd-cee8e6510ea9.png)


# Instructions

- Summary:  Congratulations! You've decided to treat yourself to a long holiday vacation in Honolulu, Hawaii. To help with your trip planning, you decide to do a climate analysis about the area. The following sections outline the steps that you need to take to accomplish this task.

# Part 1: Analyse and Explore the Climate Data
In this section, you’ll use Python and SQLAlchemy to do a basic climate analysis and data exploration of your climate database. Specifically, you’ll use SQLAlchemy ORM queries, Pandas, and Matplotlib. To do so, complete the following steps:

- Precipitation Analysis
  - Find the most recent date in the dataset
  - Using that date, get the previous 12 months of precipitation data by querying the previous 12 months of date
  - Select only the "date" and "prcp" values
  - Load the query results into a Pandas DataFrame, and set the index to the "date" column
  - Sort the DataFrame values by "date"
  - Plot the results by using the DataFrame plot method
  - Output:
 
![Precipitation_Analysis](https://user-images.githubusercontent.com/112173540/205470063-1bce7e1c-bbe7-4bbc-9b49-b9b28a9594ab.png)

- Station Analysis
  - Design a query to calculate the total number of stations in the dataset
  - Design a query to find the most-active stations (that is, the stations that have the most rows). To do so, complete the following steps:
  - List the stations and observation counts in descending order
  - Answer the following question: which station id has the greatest number of observations?
  - Using the most-active station id, calculate the lowest, highest, and average temperatures
  - Design a query to get the previous 12 months of temperature observation (TOBS) data. To do so, complete the following steps:
  - Filter by the station that has the greatest number of observations
  - Query the previous 12 months of TOBS data for that station
  - Plot the results as a histogram with bins=12
  - Output:

![USC00519281_temps](https://user-images.githubusercontent.com/112173540/205470137-573676a4-729d-4f5b-8fd8-5abb11dc426d.png)

# Part 2: Design Your Climate App
Now that you’ve completed your initial analysis, you’ll design a Flask API based on the queries that you just developed. Use the Flask jsonify function to convert your API data to a valid JSON response object. 
To do so, use Flask to create your routes as follows:

- /
  - Start at the homepage
  - List all the available routes

- /api/v1.0/precipitation
  - Convert the query results to a dictionary by using date as the key and prcp as the value
  - Return the JSON representation of your dictionary

- /api/v1.0/stations
  - Return a JSON list of stations from the dataset

- /api/v1.0/tobs
  - Query the dates and temperature observations of the most-active station for the previous year of data
  - Return a JSON list of temperature observations for the previous year

- /api/v1.0/<start> and /api/v1.0/<start>/<end>
  - Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range
  - For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date
  - For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive
  
