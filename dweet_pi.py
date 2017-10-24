from datetime import datetime
import grovepi, time, math, sys, random, dweepy, psutil

# Returns the current time
def getCurrentTime():
	return datetime.utcnow()

# Returns formatted light sensor data
def getLightSensorData():#
	try:
		light_raw = grovepi.analogRead(light_sensor_port)
		time.sleep(0.2)
		return light_raw
	except IOError:
		print "Error reading Light sensor on port {}".format(light_sensor_port)

# Returns formatted range sensor data
def getUltrasonicRangerData():
	try:
		ultrasonic_read_raw = grovepi.ultrasonicRead(ultrasonic_ranger_port)
		time.sleep(0.2)
		return ultrasonic_read_raw
	except IOError:
		print "Error reading Ultrasonic Ranger on port {}".format(ultrasonic_ranger_port)

# Returns if the button is pressed or not as a boolean
def getButtonData():
	try:
		button_data_raw = grovepi.digitalRead(button_port) == 1
		time.sleep(0.1)
		return button_data_raw
	except IOError:
		print "Error reading Light sensor on port {}".format(button_port)

# Returns formatted processor usage in MB
def getProcessorUsageData():
	return psutil.cpu_percent()

# Returns formatted data ready for upload as a dictionary
def getUploadData():
	dict = {}
	dict['light'] = getLightSensorData()
	dict['distance'] = getUltrasonicRangerData()
	dict['button'] = getButtonData()
	dict['cpu_usage'] = getProcessorUsageData()
	return dict

# Uploads a dictionary to the dweet.io service
def uploadToDweet(dict):
	try:
		print "   > dweet.io upload: {}".format(dweepy.dweet_for('aaron_meaney_test', dict))
	except dweepy.api.DweepyError as e:
		print "   > dweet.io upload exception: {}".format(e)




# ===================================
# 'Main' script execution begins here
# ===================================

# Set sensor port numbers
light_sensor_port = 0
ultrasonic_ranger_port = 8
button_port = 3

# Update loop
try:
	while True:
		# Get the upload data
		upload_data = getUploadData()

		# Print upload data
		print '========================================================='
		print 'Current Time:        {}'.format(getCurrentTime())
		print 'Light:               {}'.format(upload_data['light'])
		print 'Distance:            {}'.format(upload_data['distance'])
		print 'Button Pressed:      {}'.format(upload_data['button'])
		print 'CPU Usage %:         {}'.format(upload_data['cpu_usage'])

		# TODO: Upload the data
		uploadToDweet(upload_data)

		# TODO: Store it in a SQLite db
except KeyboardInterrupt:
	print 'Finished.'
	exit(0)
except:
	raise
	exit(1)
