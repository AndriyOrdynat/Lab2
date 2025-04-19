import random, datetime, time

class Temperature_sensor:
    def __init__(self):
        self.__temperature = 0

    def get_temperature(self):
        self.__temperature = 20 + random.randint(0, 10)/10
        return self.__temperature
    
class Saver:
    def __init__(self):
        self.__sensor = Temperature_sensor()
        self.data = []

    def save_now(self):
        T = self.__sensor.get_temperature()
        t = datetime.datetime.now().strftime("%H:%M:%S")
        self.data.append({'Temperature': T, 'Time': t})

    def get_data(self):
        return self.data

class Logger:
    def __init__(self, file_name):
        self.filename = file_name
        self.shared_data = Saver()
        self.log_counter = 0
        with open(self.filename, 'w') as file:
            file.write("Time                Temperature\n")

    def log_temperature(self, log_times):
        for _ in range(log_times):
            self.shared_data.save_now()
            latest_data = self.shared_data.get_data()[-1]
            with open(self.filename, 'a') as file:
                file.write(f"{latest_data['Time']}            {latest_data['Temperature']}\n")
            self.log_counter += 1
            time.sleep(1)

log = Logger("My_measurements.txt")
log.log_temperature(10)
