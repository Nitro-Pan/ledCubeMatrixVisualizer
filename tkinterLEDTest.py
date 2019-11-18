from gpiozero import LED
import tkinter as tk

led = [None, None, LED(2), LED(3), LED(4), LED(5), LED(6), LED(7), LED(8), LED(9), LED(10), LED(11), LED(12), LED(13), LED(14), LED(15), LED(16), LED(17), LED(18), LED(19), LED(20), LED(21), LED(22), LED(23), LED(24), LED(25), LED(26)]
currLed = 21

def openWindow():
    root = tk.Tk()
    root.title("ElectroJesus: The Second Coming")
    frame = tk.Frame(root)
    frame.pack()
    btnOn = tk.Button(frame, text="on", bg="green", command=ledXOn)
    btnOn.grid(row=1, column=1)
    btnOff = tk.Button(frame, text="off", bg="red", command=ledXOff)
    btnOff.grid(row=1, column=2)
    entChangeLED = tk.Entry(frame)
    entChangeLED.grid(row=2, column=2)
    btnChange = tk.Button(frame, text="change", bg="yellow", command=lambda: changeLED(entChangeLED.get()))
    btnChange.grid(row=2, column=1)
    root.mainloop()

def changeLED(e):
    try:
        int(e)
    except:
        print("LED number is NaN")
        return
    print("Changed LED to " + e)
    global currLed
    currLed = int(e)

def ledXOn():
    try:
        led[currLed].on()
    except:
        print("LED " + str(currLed) + " doesn't exist. Not a real GPIO pin?")
        return
    print("LED" + str(currLed) + " is on.")

def ledXOff():
    try:
        led[currLed].off()
    except:
        print("LED " + str(currLed) + " doesn't exist. Not a real GPIO pin?")
        return
    print("LED" + str(currLed) + " is off.")

openWindow()
    
