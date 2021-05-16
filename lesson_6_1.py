from time import sleep


class TrafficLight:
    __color = "red"

    def running(self):
        self.__color = "red"
        print(self.__color)
        sleep(7)
        self.__color = "yellow"
        print(self.__color)
        sleep(2)
        self.__color = "green"
        print(self.__color)
        sleep(7)
        print()


a = TrafficLight()
a.running()
a.running()
