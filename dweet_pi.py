from datetime import datetime
import grovepi, time, math

# Returns the current time
def getCurrentTime():
	return datetime.utcnow()

# Returns formatted temperature sensor data
def getTemperatureSensorData():
	try:
		[temperature_raw, humidity_raw] = grovepi.dht(temperature_sensor_port,0)
		return math.floor(temperature_raw)
	except IOError:
		print "Error reading Temperature and Humidity sensor on port {}".format(temperature_sensor_port)

# Returns formatted range sensor data
def getUltrasonicRangerData():
	try:
		return grovepi.ultrasonicRead(ultrasonic_ranger_port)
	except IOError:
		print "Error reading Ultrasonic Ranger on port {}".format(ultrasonic_ranger_port)

# Returns if the button is pressed or not as a boolean
def getButtonData():
	try:
		return grovepi.digitalRead(button_port) == 1
	except IOError:
		print "Error reading Light sensor on port {}".format(light_sensor_port)

# Returns formatted RAM usage in MB
def getMemoryUsageData():
	return 1;

# Returns formatted data ready for upload as a dictionary
def getUploadData():
	time.sleep(0.1)
	dict = {}
	dict['temperature'] = getTemperatureSensorData()
	dict['distance'] = getUltrasonicRangerData()
	dict['button'] = getButtonData()
	dict['memory_usage'] = getMemoryUsageData()
	return dict



# ===================================
# 'Main' script execution begins here
# ===================================
temperature_sensor_port = 6
ultrasonic_ranger_port = 8
button_port = 3

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
		print 'Button Pressed:    {}'.format(upload_data['button'])
		print 'Memory Usage (MB): {}'.format(upload_data['memory_usage'])

		# TODO: Upload the data

		# TODO: Store it in a SQLite db
except KeyboardInterrupt:
	print 'Finished.'
	exit(0)
except:
	raise
	exit(1)
