import random, datetime, time, csv

class Temperature_sensor:
    def __init__(self, min_temp, max_temp):
        self._min_temp = min_temp
        self._max_temp = max_temp
        self.__temperature = 0

    def get_temperature(self):
        self.__temperature = round(random.uniform(self._min_temp, self._max_temp))
        return self.__temperature
    
class Saver(Temperature_sensor):
    def __init__(self, min_temp, max_temp):
        super().__init__(min_temp, max_temp)
        self.data = []

    def save_now(self):
        T = self.get_temperature()
        t = datetime.datetime.now().strftime("%H:%M:%S")
        self.data.append({'Temperature': T, 'Time': t})

class Logger (Saver):
    def __init__(self, file_name, min_temp, max_temp):
        super().__init__(min_temp, max_temp)
        self.filename = file_name
        self.log_counter = 0
        with open(self.filename, 'w', newline='') as file:
            logfile = csv.writer(file)
            logfile.writerow(['Time', 'Temperature'])

    def log_temperature(self, log_times):
        with open(self.filename, 'a', newline='') as file:
            logfile = csv.DictWriter(file, fieldnames=['Time', 'Temperature'])
            for _ in range(log_times):
                self.save_now()
                logfile.writerow(self.data[-1])
                time.sleep(1)

log = Logger("tempLog.csv", 10, 20)
log.log_temperature(4)
