import serial, os, signals, sys
from sklearn.externals import joblib

'''
Author: Federico Terzi
This is a work in progress, don't judge please :)
'''

TRY_TO_PREDICT = False
SAVE_NEW_SAMPLES = False
FULL_CYCLE = False
ENABLE_WRITE = False

SERIAL_PORT = "COM6"
BAUD_RATE = 38400
TIMEOUT = 100

target_sign = "e"
current_batch = 0

if len(sys.argv)>1:
	#Target example: python register_signals.py target=a:1
	if 'target' in sys.argv[1]:
		target_sign = sys.argv[1].split("=")[1].split(":")[0]
		current_batch = sys.argv[1].split("=")[1].split(":")[1]
		print "TARGET SIGN: '{sign}' USING BATCH: {batch}".format(sign=target_sign, batch = current_batch)
		SAVE_NEW_SAMPLES = True
	if 'predict' in sys.argv[1]:
		TRY_TO_PREDICT = True
	if 'write' in sys.argv[1]:
		TRY_TO_PREDICT = True
		ENABLE_WRITE = True

target_directory = "data"

clf = None
sentence = ""

if TRY_TO_PREDICT:
	print "Loading model..."
	clf = joblib.load('model.pkl')

print "OPENING SERIAL_PORT '{port}' WITH BAUDRATE {baud}...".format(port = SERIAL_PORT, baud = BAUD_RATE)

print "IMPORTANT!"
print "To end the program hold Ctrl+C and send some data over serial"

ser = serial.Serial(SERIAL_PORT, BAUD_RATE, timeout = TIMEOUT)

output = []

in_loop = True
is_recording = False

current_sample = 0

try:
    while in_loop:
	line = ser.readline().replace("\r\n","")
	if line=="STARTING BATCH":
		is_recording = True
		output = []
		print "RECORDING...",
	elif line=="CLOSING BATCH":
		is_recording = False
		if len(output)>1:
			#in_loop = False
			print "DONE, SAVING...",
			filename = "{sign}_sample_{batch}_{number}.txt".format(sign = target_sign, batch = current_batch, number = current_sample)
			path = target_directory + os.sep + filename
			if SAVE_NEW_SAMPLES == False:
				path = "tmp.txt"
				filename = "tmp.txt"
			f = open(path, "w")
			f.write('\n'.join(output))
			f.close()
			current_sample += 1
			print "SAVED IN {filename}".format(filename = filename)
			if TRY_TO_PREDICT:
				print "PREDICTING...",
				sample_test = signals.Sample.load_from_file(path)
				number = clf.predict(sample_test.get_linearized(reshape=True))
				char = chr(ord('a')+number[0])
				if ENABLE_WRITE:
					sentence += char
					print "[{char}] -> {sentence}".format(char = char, sentence = sentence)
				else:
					print char
		else:
			print "ERROR..."
	else:
		output.append(line)
except KeyboardInterrupt:
    print 'CLOSED LOOP!'

ser.close()