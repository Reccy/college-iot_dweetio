from datetime import datetime
import grovepi

# Returns the current time
def getCurrentTime():
	return datetime.utcnow()

# Returns formatted temperature sensor data
def getTemperatureSensorData():
	try:
		[temperature_raw, humidity_raw] = grovepi.dht(temperature_sensor_port,0)
		return temperature_raw
	except IOError:
		print "Error reading Temperature and Humidity sensor on port {}".format(temperature_sensor_port)

# Returns formatted range sensor data
def getUltrasonicRangerData():
	try:
		return grovepi.ultrasonicRead(ultrasonic_ranger_port)
	except IOError:
		print "Error reading Ultrasonic Ranger on port {}".format(ultrasonic_ranger_port)

# Returns formatted light sensor data
def getLightSensorData():
	return 1;

# Returns formatted RAM usage in MB
def getMemoryUsageData():
	return 1;

# Returns formatted data ready for upload as a dictionary
def getUploadData():
	dict = {}
	dict['temperature'] = getTemperatureSensorData()
	dict['distance'] = getUltrasonicRangerData()
	dict['light'] = getLightSensorData()
	dict['memory_usage'] = getMemoryUsageData()
	return dict



# ===================================
# 'Main' script execution begins here
# ===================================
temperature_sensor_port = 6
ultrasonic_ranger_port = 8

# Update loop
try:
	while True:
		# Get the upload data
		upload_data = getUploadData()

		# Print upload data
		print '========================================================='
		print 'Current Time:      {}'.format(getCurrentTime())
		print 'Temperature:       {}'.format(upload_data['temperature'])
		print 'Distance:          {}'.format(upload_data['distance'])
		print 'Light:             {}'.format(upload_data['light'])
		print 'Memory Usage (MB): {}'.format(upload_data['memory_usage'])

		# TODO: Upload the data

		# TODO: Store it in a SQLite db
except KeyboardInterrupt:
	print 'Finished.'
	exit(0)
except:
	raise
	exit(1)
