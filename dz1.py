import time


class TrafficLight:
    __color = ['красный', 'желтый', 'зеленый']

    def running(self, red_timer, yellow_timer, green_timer):
        for i in TrafficLight.__color:
            if i == 'красный':
                print(i)
                time.sleep(red_timer)
            elif i == 'желтый':
                print(i)
                time.sleep(yellow_timer)
            else:
                print(i)
                time.sleep(green_timer)


light = TrafficLight()
print(light.running(7, 2, 3))
