import random, datetime, time

class Temperature_sensor:
    def __init__(self):
        self.__temperature =  random.randint(10, 30)

    def get_temperature(self):
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
        self.sheare_data = Saver()
        self.log_counter = 0
        with open(self.filename, 'w') as file:
            file.write("Time                Temperature\n")

    def log_temperature(self, log_time):
        for i in range(log_time):
            self.sheare_data.save_now()
            last_data = self.shared_data.get_data()[-1]
            with open(self.filename, 'a') as file:
                file.write(f"{last_data['Time']}                     {last_data[i-1]['Temperature']}\n")
            time.sleep(1)

log = Logger("My measurements")
log.log_temperature(5)
