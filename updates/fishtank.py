# start_monitoring.py
import tkinter as tk
import tkinter.messagebox as mb
import os
import fishtank as tank

# Assuming fishtank.py contains a FishTank class and is working properly.

# import environmental factors to monitor
import alkalinity
import calcium
import magnesium
import ph
import phosphate
import salinity
import temperature


class FishTankMonitor(tk.Tk):

    # check fish tank environmental factors
    def monitor(self):
        msg = "ENVIRONMENTAL FACTORS:\n"
        msg += ph.monitor() + "\n"
        msg += alkalinity.monitor() + "\n"
        msg += salinity.monitor() + "\n"
        msg += temperature.monitor() + "\n"
        msg += "\nTRACE CHEMICALS:\n"
        msg += calcium.monitor() + "\n"
        msg += magnesium.monitor() + "\n"
        msg += phosphate.monitor()

        mb.showinfo("Status Check", msg)

    # The GUI for the monitoring software
    def __init__(self):
        tk.Tk.__init__(self)
        
        # reference a PNG to use as the background image
        dirname = os.path.dirname(__file__)
        tank_picture = os.path.join(dirname, 'tank.PNG')

        self.title("Fish Tank Monitor")
        self.geometry("750x500")  # size of tank image
        try:
            self.image_tank = tk.PhotoImage(file=tank_picture)
        except Exception as e:
            print(f"Error loading image: {e}")
            self.image_tank = None

        self.background = tk.Label(self, image=self.image_tank)
        self.background.image = self.image_tank  # keep a reference to the image
        self.background.pack(fill="both", expand=True)

        self.frame_info = tk.Frame(self.background, background="white")
        self.frame_info.pack(pady=75)

        font_setup = ("Arial", 20, "bold")
        self.lbl_title = tk.Label(self.frame_info, font=font_setup, background="white", text="Fish Tank Monitor")
        self.lbl_title.pack(pady=5)

        font_setup = ("Arial", 16, "normal")
        self.lbl_status = tk.Label(self.frame_info, background="white", text="Current Status:\n All factors OK")
        self.lbl_status.pack(pady=5)

        self.btn_check = tk.Button(self.frame_info, text="Perform Manual Check", command=self.monitor)
        self.btn_check.pack(pady=20, padx=20)

# Create and run the application
if __name__ == "__main__":
    my_tank = FishTankMonitor() 
    my_tank.mainloop()
