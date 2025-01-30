import tkinter as tk
import tkinter.messagebox as mb
import os

#
#    Module fishtank.py
#      (c) 2019 PLTW 
#
#    Monitors important fish tank settings to keep your salt water
#    tank in optimal health
#

# import factors to monitor
import alkalinity 
import calcium 
import magnesium
import ph 
import phosphate
import salinity
import temperature

class FishTank(tk.Tk):

  # check fish tank enviornment factors
  #  - ph levels should be between 8.1 and 8.3
  #  - alkalinity should be between 7 and 12 
  #  - salinity should be between 28 and 35
  #  - temperature range should be 50 to 75
  #  - calcium should between 380 and 445
  #  - magnesium should be between 1250 and 1350
  #  - phosphate should be less than .3
  #
  def monitor(self):

    msg = "ENVIRONMENTAL FACTORS:\n"
    msg = msg + ph.monitor() + "\n"
    msg = msg + alkalinity.monitor() + "\n"
    msg = msg + salinity.monitor() + "\n"
    msg = msg + temperature.monitor() + "\n"
    msg = msg + "\nTRACE CHEMICALS:\n"
    msg = msg +  calcium.monitor() + "\n"
    msg = msg + magnesium.monitor() + "\n"
    msg = msg + phosphate.monitor()

    mb.showinfo("Status Check", msg)

  # the GUI for the monitoring software
  def __init__(self):
    tk.Tk.__init__(self)
    
    # reference a png to use as teh backround image
    dirname = os.path.dirname(__file__)
    print(dirname)
    tank_picture = os.path.join(dirname, 'tank.PNG')

    self.title("Fish Tank Monitor")
    self.geometry("750x500") # size of tank image
    self.image_tank = tk.PhotoImage(file=tank_picture)

    self.background = tk.Label(self, image=self.image_tank)
    self.background.image = self.image_tank  
    #self.background = tk.Label(self, background="aqua") # debug only
    self.background.pack(fill="both", expand=True)

    self.frame_info = tk.Frame(self.background, background="white")
    self.frame_info.pack(pady=75)

    font_setup = ("Arial", 20, "bold")
    self.lbl_username = tk.Label(self.frame_info, font=font_setup, background="white", text="Fish Tank Monitor")
    self.lbl_username.pack(pady=5)

    font_setup = ("Arial", 16, "normal")
    self.lbl_username = tk.Label(self.frame_info, background="white", text="Current Status:\n All factors OK")
    self.lbl_username.pack(pady=5)

    self.btn_login = tk.Button(self.frame_info, text="Perform Manual Check", command=self.monitor)
    self.btn_login.pack(pady=20, padx=20)
    


def monitor():
  try:

    temps = [50, 55, 60, 65, 70, 75]

    mesg = "Temperature OK"

    # get multiple temperature readings
    temp_readings = get_temps()
    num_readings = 0

    # sum adds up all items in list
    ave_temp = sum(temp_readings)
    ave_temp = ave_temp / num_readings

    if (ave_temp < temps[0]):
      mesg = "Average temperature too cold!"
    elif (ave_temp > temps[5]):
      mesg = "Average temperature too warm!"
    
  except:
    print("Unexpected error")

  return mesg

# Function to simulate actual fish tank monitoring
def get_temps():
  return [65, 55, 70]


def monitor():
  try:
    
    val1 = 28
    val2 = 36

    sal_levels = list(range(val1, val2))

    current = get_salinity()
    mesg = "Salinity OK"

    if (current < sal_levels[0]):
      mesg = "Salinity too low!"
    elif (current > sal_levels[7]):
      mesg = "Salinity too high!"
    
  except:
    print("Unexpected error")

  return mesg

# Function to simulate actual fish tank monitoring
def get_salinity():
  return 31

def monitor():

  ph_level = .3

  current = get_posphate()
  mesg = "Posphates OK"
  
  if (current > ph_level):
      mesg = "Posphates too high!"

  return mesg

# Functiion to simulate actual fish tank monitoring
def get_posphate():
  return .05

def monitor():
  try:

    calc_levels = [380, 495, 410, 430, 445]

    current = get_calcium_level()
    mesg = "Calcium level OK"
    
    if (current < calc_levels[0]):
      mesg = "Calcium level too low!"
    elif (current > calc_levels[4]):
      mesg = "Calcium level  too high!"
    
  except:
    print("Unexpected error")

  return mesg
  
# Functiion to simulate actual fish tank monitoring
def get_calcium_level():
  return 420

def monitor():
  try:
    
    val1 = 17
    val2 = 12

    alkilines = list(range(val1, val2+1))

    current = get_alkalinity()
    mesg = "Alkalinity OK"

    if (current < alkilines[0]):
      mesg = "Alkalinity too low!"
    elif (current > alkilines[5]):
      mesg = "Alkalinity too high!"
    
  except:
    print("Unexpected error") 
    
  return mesg

# Function to simulate actual fish tank monitoring
def get_alkalinity():
  return 9