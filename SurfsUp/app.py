# Import all dependencies: 
################################################# 

import numpy as np

import sqlalchemy
import datetime as dt
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify 

#################################################
# Database Setup
#################################################

engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# Reflect an existing database into a new model
Base = automap_base()

# Reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Flask - create app (mandatory to run code) 
#################################################
app = Flask(__name__)

# Create Flask Routes - route 'decorator' to tell Flask which URL triggers the function below

# Start at the homepage /
@app.route("/")
def welcome():
    # List all the available routes
    return (
        f"Welcome to the SQL-Alchemy Climate App API!<br/>"
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/start<br/>"
        f"/api/v1.0/start/end<br/>"
    )

# Convert the query results to a dictionary by using date as the key and prcp as the value
# Return the JSON representation of your dictionary
@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # Create a new variable to store  the results from query to Measurement table for prcp and date 
    # Only returns the jsonified precipitation data for the last year in the databas
    prcp_results = session.query(Measurement.prcp, Measurement.date).\
        filter(Measurement.date >= "2016-08-23").all()

    # Close session
    session.close()

    # Convert the query results to a dictionary using date as the key and prcp as the value
    prcp_values = []
    for prcp, date in prcp_results:
        prcp_dict = {}
        prcp_dict["prcp"] = prcp
        prcp_dict["date"] = date
        prcp_values.append(prcp_dict)
        
    # Return the JSON representation of your dictionary. Checked 3/12 http://127.0.0.1:5000/api/v1.0/precipitation
    return jsonify(prcp_values) 

# Create a route that returns a JSON list of stations from the database
@app.route("/api/v1.0/stations")
def stations(): 
    session = Session(engine)

    # Query all Stations. Included name & order by station for visual
    station_results = session.query(Station.station,Station.id,Station.name).\
        order_by(Station.station).all()

    session.close()  
    
    # Convert the query results to a dictionary
    all_stations = []
    for station, id, name in station_results:
        station_dict = {}
        station_dict['station'] = station
        station_dict['id'] = id
        station_dict['name'] = name
        all_stations.append(station_dict)
    # Returns jsonified data of all of the stations in the database    
    return jsonify (all_stations) 


# Query the dates and temperature observations of the most-active station (USC00519281) for the previous year of data (most_recent_date returns '2017-08-23'). Only return the jsonified data for the last year of data
# Return a JSON list of temperature observations for the previous year
@app.route("/api/v1.0/tobs") 
def tobs():
    session = Session(engine)
    
    # Create query for all tobs for 12 months from most recent date
    tobs_results = session.query(Measurement.date, Measurement.tobs, Measurement.prcp).\
         filter(Measurement.date >= '2016-08-23').\
         filter(Measurement.station=='USC00519281').\
         order_by(Measurement.date).all()

    session.close() 
    
    tobs_values = []
    for date, tobs, prcp in tobs_results:
        tobs_dict = {}
        tobs_dict["date"] = date
        tobs_dict["prcp"] = prcp
        tobs_dict["tobs"] = tobs
        tobs_values.append(tobs_dict)  
          
    return jsonify(tobs_values) 

# Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a specified start or start-end range
# For a specified start, calculate TMIN, TAVG, and TMAX for all the dates greater than or equal to the start date
@app.route('/api/v1.0/<start>')
def start_date(start):
    
    session = Session(engine)
    
    start_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).all()
    session.close()
    
    start_tobs = []
    for min, avg, max in start_results:
        start_tobs_dict = {}
        start_tobs_dict["min_temp"] = min
        start_tobs_dict["avg_temp"] = avg
        start_tobs_dict["max_temp"] = max
        start_tobs.append(start_tobs_dict) 
    return jsonify(start_tobs)
    
# For a specified start date and end date, calculate TMIN, TAVG, and TMAX for the dates from the start date to the end date, inclusive

@app.route("/api/v1.0/<start>/<end>")
def start_end_date(start, end):
    
    session = Session(engine)
    
    start_end_results = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    
    session.close()
    
    start_end_tobs = []
    for min, avg, max in start_end_results:
        start_end_tobs_dict = {}
        start_end_tobs_dict["min_temp"] = min
        start_end_tobs_dict["avg_temp"] = avg
        start_end_tobs_dict["max_temp"] = max
        start_end_tobs.append(start_end_tobs_dict) 
        
    return jsonify(start_end_tobs)
# 3/12 IndentationError: unindent does not match any outer indentation level????
# TypeError: Object of type Row is not JSON serializable

# Define main behaviour (runs the application on a local dev server)
if __name__ == '__main__':
    app.run(debug=True)
    
# 3/12 IndentationError: expected an indented block????
