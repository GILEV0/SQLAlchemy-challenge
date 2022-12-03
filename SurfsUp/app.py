# Import all dependencies: 
################################################# 

import numpy as np
import pandas as pd
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

session = Session(engine)

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

    return jsonify(multi_day_temp_results)

# Define main behaviour (runs the application on a local dev server)
if __name__ == '__main__':
    app.run(debug=True) 