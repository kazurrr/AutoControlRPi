import obd


class CarData:
    def __init__(self):
        self.odb_connection = obd.OBD()

    def close(self):
        self.odb_connection.close()

    def get_speed(self):
        return str(self.odb_connection.query(obd.commands.SPEED))

    def get_rpm(self):
        return str(self.odb_connection.query(obd.commands.RPM))

    def get_engine_load(self):
        return str(self.odb_connection.query(obd.commands.ENGINE_LOAD))

    def get_voltage(self):
        return str(self.odb_connection.query(obd.commands.ELM_VOLTAGE))
