from flask import Flask
from pygeocoder import Geocoder

app = Flask(__name__)

@app.route('/')
def geo():
	address = '706 NE 161st Court Vancouver, WA'
	geo_info = Geocoder.geocode(address)[0].coordinates
	return str(geo_info)

if __name__ == "__main__":
	app.run()
