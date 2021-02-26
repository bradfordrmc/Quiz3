from gpiozero import LED, Button  #import libraires for LED and button functionality
from guizero import App, Text, PushButton, Drawing  #import libraires 
from threading import Thread
from time import sleep

walk = LED(3)      #setting up pins for button and LEDs
button = Button(4, pull_up=True)
green = LED(17)
red = LED(22)
yellow = LED(27)

def light_cycle():  #function containing all light logic
    while True:
        if button.is_pressed:
            green.off()
            d.clear()
            sleep(.2)
            
            yellow.on()
            d.oval(30, 30, 50, 50, color="yellow")
            sleep(3)
            yellow.off()
            d.clear()
            
            red.on()
            d.oval(30, 30, 50, 50, color="red")
            walk.on()
            wanted_text = Text(app, "WALK")
            sleep(5)
            red.off()
            d.clear()
            walk.off()
            wanted_text.clear()  

        else:
            green.on()
            d.oval(30, 30, 50, 50, color="green")
            sleep(1)

if __name__ == '__main__':    #here is the code needed for the app to display a window and also calls the other function with the thread so they can run rogether
    app = App("Traffic Light")
    d= Drawing(app)
    
    thread = Thread(target=light_cycle)  #this is super useful, Solves many of the python issues ive been having
    thread.start()
    
    app.display()






