import random, datetime, time, csv

class Temperature_sensor:
    def __init__(self):
        self.__temperature = 0

    def get_temperature(self):
        self.__temperature = 20 + random.randint(0, 10)/10
        return self.__temperature
    
class Saver (Temperature_sensor):
    def __init__(self):
        super().__init__()
        self.data = []

    def save_now(self):
        T = super().get_temperature()
        t = datetime.datetime.now().strftime("%H:%M:%S")
        self.data.append({'Temperature': T, 'Time': t})

class Logger (Saver):
    def __init__(self, file_name):
        super().__init__()
        self.filename = file_name
        self.log_counter = 0
        with open(self.filename, 'w', newline='') as file:
            logfile = csv.writer(file)
            logfile.writerow(['Time', 'Temperature'])

    def log_temperature(self, log_times):
        with open(self.filename, 'a', newline='') as file:
            logfile = csv.DictWriter(file, fieldnames=['Time', 'Temperature'])
            for _ in range(log_times):
                super().save_now()
                logfile.writerow(self.data[-1])
                time.sleep(1)

log = Logger("tempLog.csv")
log.log_temperature(4)
