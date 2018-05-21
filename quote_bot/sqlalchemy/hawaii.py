import datetime as dt
import numpy as np
import pandas as pd

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from sqlalchemy import and_, or_, not_

from flask import Flask, jsonify, request


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///hawaii.sqlite")
#engine = create_engine("sqlite:///C:\\sqlite\\hawaii.db")
    # reflect an existing database into a new model
Base = automap_base()
    # reflect the tables
Base.prepare(engine, reflect=True)

    # Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement

    # Create our session (link) from Python to the DB
session = Session(engine)

print("Initialized")



app = Flask(__name__)
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////mnt/c/sqlite/hawaii.db'
app.config['DEBUG'] = True
app.config['PROPAGATE_EXCEPTIONS'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""        
    return (
        f"/api/v1.0/precipitation</br>"
        f"/api/v1.0/stations</br>"
        f"/api/v1.0/tobs</br>"
        f"/api/v1.0/<start>"
    )


@app.route("/api/v1.0/precipitation/<pre_date>")
def precipitation(pre_date):
    """Return a list of all passenger names"""
    # Query for the dates and temperature observations from the last year.
    # Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.
    # Return the json representation of your dictionary.
    results = session.query(Measurement).filter(Measurement.date == pre_date)

    # Print all passengers of that gender
    all_tobs = [] 
    for measure in results:
        measure_dict = {}
        measure_dict["station"] = measure.station
        measure_dict["date"] = measure.date
        measure_dict["prcp"] = measure.prcp
        all_tobs.append(measure_dict)

    return jsonify(all_tobs)


    # print(results)
    # Convert list of tuples into normal list
    # all_names = list(np.ravel(results))
    # print(all_names)

    # print(all_names)
    return jsonify({'TempMin': tmp_min, 'TempMax': tmp_max, 'TempAvg': tmp_avg})


@app.route("/api/v1.0/stations")
def stations():
    results = session.query(Station).all()
    # Create a dictionary from the row data and append to a list of all_passengers
    all_stations = []
    for station in results:
        print(station.station)
        station_dict = {}
        station_dict["key"] = station.id
        station_dict["station"] = station.station
        station_dict["name"] = station.name
        station_dict["latitude"] = station.latitude
        station_dict["longitude"] = station.longitude
        station_dict["elevation"] = station.elevation 
        all_stations.append(station_dict)

    return jsonify(all_stations)


# New Routes (Gender)
@app.route("/api/v1.0/tobs/<pre_date>")
def tobs(pre_date):
    results = session.query(Measurement).filter(Measurement.date == pre_date)

    # Print all passengers of that gender
    all_tobs = [] 
    for measure in results:
        measure_dict = {}
        measure_dict["station"] = measure.station
        measure_dict["date"] = measure.date
        measure_dict["tobs"] = measure.tobs
        all_tobs.append(measure_dict)

    return jsonify(all_tobs)

@app.route("/api/v1.0/temperaturestats", methods=['GET'])
def temperaturestats():
    """Return a list of all passenger names"""
    # Query for the dates and temperature observations from the last year.
    # Convert the query results to a Dictionary using `date` as the key and `tobs` as the value.
    # Return the json representation of your dictionary.
    start_date = request.args.get('start', '2017-01-02') # use default value repalce 'None'
    fin_date = request.args.get('end', '2017-02-03')
    tmp_min = session.query(func.min(Measurement.tobs)).filter(and_(Measurement.date > start_date, Measurement.date < fin_date)).first()
    tmp_max = session.query(func.max(Measurement.tobs)).filter(and_(Measurement.date > start_date, Measurement.date < fin_date)).first()
    tmp_avg = session.query(func.avg(Measurement.tobs)).filter(and_(Measurement.date > start_date, Measurement.date < fin_date)).first()
 
    # print(results)
    # Sample Request  http://127.0.0.1:5000/api/v1.0/temperaturestats?start=2017-01-20&end=2017-02-03
    
    # print(all_names)
    return jsonify({'TempMin': tmp_min, 'TempMax': tmp_max, 'TempAvg': tmp_avg})
     
    #Sample output##
    #    
    #{
    #"TempAvg": [
    #    69.09210526315789
    #],
    #"TempMax": [
    #    76
    #],
    #"TempMin": [
    #    59
    #]
   #}
    
# New Routes (Survival)

if __name__ == '__main__':
    app.run(debug=True)
