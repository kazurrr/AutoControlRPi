import obd

# connection = obd.OBD("/dev/ttyUSB0", baudrate=38400, fast=False)
connection = obd.OBD(protocol="3") # create connection with USB 0

print connection.port_name()
print connection.protocol_id()
print connection.protocol_name()


speed = connection.query(obd.commands.SPEED)
rpm = connection.query(obd.commands.RPM)
dtc = connection.query(obd.commands.GET_DTC)
temp = connection.query(obd.commands.COOLANT_TEMP)
temp2 = connection.query(obd.commands.INTAKE_TEMP)


print "RPM: " + str(rpm)
print "Speed: " + str(speed)
print "DTC: " + str(dtc)
print "COOLANT_TEMP: " + str(temp)
print "INTAKE_TEMP: " + str(temp2)

connection.close()