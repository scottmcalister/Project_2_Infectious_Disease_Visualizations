import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from aqlalchemy import create_engine, func, desc
from flask import Flask, jsonify


engine = create_engine("sqlite://data.sqlite")

Base = automap_base()
Base.prepare(engine, reflect=True)

<<<<<<< HEAD
# SET UP VARIABLES IF NEEDED
=======
Disease_Data = Base.classes.disease_data
>>>>>>> caf8f1df69ce0479c21f31eb53715da84a521c6f

session = Session (engine)

app = Flask(__name__)

@app.route("/")
def home():
	return(
<<<<<<< HEAD
		f"Welcome to the Dengue Case Report API" <br>
		f"Available routes: "<br>
		f"/api/v1.0/case totals" <br>


# This app will have to have a function that iterates through each year of the sample data, figures out whether the case report was cumulative or not, if cumulative, move onto the next record with the same start date until it reaches the end of the records with that start date, and adds the value count to an empty container. if the record is not cumulative, it adds the value count to the container and moves onto the next row. go from years 2007-2017 we should return the total number of cases in each state per year, and then total for each state, and total cases in the US over the last ten years.
=======
		f"Welcome to the West Nile Virus Case Report API <br>"
		f"Availbe routes: <br>"
		f"Cases_per_year <br>"
		f"/api/v1.0/case_totals <br>")


@app.route("/api.v1.0/Cases_per_year")
def cases():
	results=[]
	for row in data:
		if Disease_Data.State[i] != Disease_Data.State[i+1]:
			results.append({Disease_Data.State[i]: CountValue[i],EndDate[i]})
		else:
			next row
		return jsonify(results)




>>>>>>> caf8f1df69ce0479c21f31eb53715da84a521c6f