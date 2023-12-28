from abc import ABC, abstractmethod


class SubjectInterface(ABC):
    @property
    @abstractmethod
    def observers_list(self):
        pass

    @abstractmethod
    def register_observer(self, observer):
        pass

    @abstractmethod
    def remove_observer(self, observer):
        pass

    @abstractmethod
    def notifyObservers():
        pass


class ObserverInterface(ABC):
    @abstractmethod
    def update(self):
        pass


class DisplayElement(ABC):
    @abstractmethod
    def display(self):
        pass


class CurrentConditionDisplay(ObserverInterface, DisplayElement):
    def __init__(self):
        self.temperature = None
        self.humidity = None

    def update(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.display()

    def display(self):
        print(f"The current temperature is {self.temperature}")
        print(f"The current humidity is {self.humidity}")


class WeatherData(SubjectInterface):
    def __init__(self):
        self._observers_list: list[ObserverInterface] = []
        self.temperature = None
        self.humidity = None
        self.pressure = None

    @property
    def observers_list(self):
        return self._observers_list

    @observers_list.setter
    def observers_list(self, value):
        self._observers_list = value

    def register_observer(self, observer: ObserverInterface):
        self._observers_list.append(observer)

    def remove_observer(self, observer: ObserverInterface):
        self._observers_list.remove(observer)

    def notifyObservers(self):
        for observer in self._observers_list:
            observer.update(self.temperature, self.humidity, self.pressure)

    def measurements_changed(self):
        self.notifyObservers()

    def set_measurements(self, temperature, humidity, pressure):
        self.temperature = temperature
        self.humidity = humidity
        self.pressure = pressure
        self.measurements_changed()


def weather_station_app():
    weather_data = WeatherData()
    current_condition_display = CurrentConditionDisplay()
    weather_data.register_observer(current_condition_display)
    weather_data.set_measurements(150, 200, 300)
    return


if __name__ == "__main__":
    weather_station_app()
