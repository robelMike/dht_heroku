from flask import Flask, request, render_template
import Adafruit_DHT
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://localhost/pre-registration'
db = SQLAlchemy(app)

class dht_data(db.Model):
	__tablename__ = 'dht'
	
	id = db.Column(db.Integer, primary_key = True)
	
	temperature = db.Column(db.String(80)) 
		
	def __init__(self, temperature):
		self.temperature = temperature 
        
	def get_data(self, temp):
		db.session.save(self)
		db.session.commit()
		
		
@app.route('/post', methods=['POST'])
def postTemp():
	if request.method =='POST':
		request.body
		return 'post'
	
@app.route('/get', methods=['GET'])
def getTemp():
		
	DHT_SENSOR = Adafruit_DHT.DHT11
	DHT_PIN = 17
	
	while True:
		humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
		temperature =  temperature 
		if humidity is not None and temperature is not None:
			print("Temp={0:0.1f}*C  Humidity={1:0.1f}%".format(temperature, humidity))
		else:
			print("Failed to retrieve data from humidity sensor")
		return {'temperature': temperature,'humidity': humidity}
		
		dht_data.get_data(temperature, humidity)
if __name__ == '__main__':
	from app import db
	db.create_all()
	app.run(port = 5000, debug = True)

		
