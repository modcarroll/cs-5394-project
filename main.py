import tkinter as tk
from tkinter import *
import requests
import json

# example of how to do a post request
url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
# url = "http://localhost:3000"
allUsers = ['LOGIN']
currentUser = ""

response = requests.post(url + "/setvolume", json={"volume": 6})
print(response.content)

def speaker():
    #pass in up or down action as well as user
    #do the action
    url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url+"/speaker")
    print(action.content)
    #post to log
    action= requests.post(url + "/logs", json={"user":"philip",
    "device":"speaker",
    "action":"down"
    })
    print(action.content)
def lightBulb():
    #pass in one or off action as well as user
    #do the action
    url =  "https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url+"/deviceoff/lightbulb")
    print(action.content)
    #post to log
    action=requests.post(url + "/logs", json={"user":"philip",
    "device":"lightbulb",
    "action":"turn-off"
    })
    print(action.content)
def doorlock():
    #pass in unlock or lock action as well as user
    #do the action
    url ="https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url+"/deviceon/doorlock")
    print(action.content)
    #post to log
    action=requests.post(url+"/logs",json={"user":"philip",
    "device":"doorlock",
    "action":"lock"
    })
    print(action.content)
def thermostat():
    #pass in up or down action as wel as user
    #action
    url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url + "/up")
    print(action.content)
    #print to log
    action = requests.post(url+"/logs", json = {"user":"Philip",
    "device":"thermostat",
    "action":"up"
    })
    print(action.content)

# Get the current user based on who is selected in the dropdown
def _getUser(cur):
    currentUser = cur
    print(currentUser)

def _homeSequence():
    print("Home sweet home")
    # Set the temperature to 72
    # Turn lights on
    # Unlock the doors
    # Turn the speakers on

def _awaySequence():
    print("Bye Felicia")
    # Set the temperature to 78
    # Turn the lights off
    # Lock the doors
    # Turn the speakers off

def _sleepSequence():
    print("Snoozle time zzzzzzz")
    # Set the temperature to 68
    # Turn the lights off
    # Lock the doors
    # Turn the speakers off

def _burglarSequence():
    print("Intruder alert!")
    # Set the temperature to 99
    # Turn the lights on
    # Lock the doors
    # Turn the speakers on
    # Set the speaker volume to 100

def _populateUsers():
    userResponse = requests.get(url + "/allusers")
    users = json.loads(userResponse.content)
    for user in users:
        allUsers.append(user['userId'])

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        speaker()
        lightBulb()
        doorlock()
        thermostat()

        # Setup frames
        frame_login = tk.Frame(width="500", height="50")
        frame_title = tk.Frame(width="500", height="50")
        frame_tab = tk.Frame(width="500", height="30")
        frame_sequence = tk.Frame(width="500", height="50")
        frame_light = tk.Frame(width="500", height="50")
        frame_lock = tk.Frame(width="500", height="50")
        frame_thermostat = tk.Frame(width="500", height="50")
        frame_speaker = tk.Frame(width="500", height="50")
        frame_status = tk.Frame(width="500", height="50")
        frame_login.pack(side="top", fill="x")

        # Add separators to frames
        frame_title.pack()
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_tab.pack(side="top", fill="x")
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_sequence.pack(side="top", fill="x")
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_light.pack(side="top", fill="x")
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_lock.pack(side="top", fill="x")
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_thermostat.pack(side="top", fill="x")
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_speaker.pack(side="top", fill="x")
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_status.pack(side="top")

        _populateUsers()
        # Create and populate login dropdown
        variable = StringVar(master)
        variable.set(allUsers[0]) # set the default value
        user_dropdown = tk.OptionMenu(frame_login, variable, command = _getUser, *allUsers)
        user_dropdown.pack(side="right")

        # Add logo to the top of the page
        photo = PhotoImage(file="icon.gif")
        label_title = Label(frame_title, image=photo)
        label_title.photo = photo
        label_title.pack()

        # Setup the navigation section
        label_tab = Label(frame_tab, text="Navigation", width=12)
        tab_control = tk.Button(
            text="Control",
            width=6,
            height=2,
            bg="white",
            fg="black",
            master=frame_tab
        )
        tab_logs = tk.Button(
            text="Logs",
            width=6,
            height=2,
            bg="white",
            fg="black",
            master=frame_tab
        )
        label_tab.pack(side="left")
        tab_control.pack(side="left")
        tab_logs.pack(side="left")

        # Sequence section
        label_sequence = Label(frame_sequence, text="Sequences", width=12)
        label_sequence.pack(side="left")
        sequence_1 = tk.Button(
            text="Home",
            width=5,
            height=2,
            bg="white",
            fg="black",
            command=_homeSequence,
            master=frame_sequence
        )
        sequence_2 = tk.Button(
            text="Away",
            width=5,
            height=2,
            bg="white",
            fg="black",
            master=frame_sequence
        )
        sequence_3 = tk.Button(
            text="Sleep",
            width=5,
            height=2,
            bg="white",
            fg="black",
            master=frame_sequence
        )
        sequence_4 = tk.Button(
            text="Burglar",
            width=5,
            height=2,
            bg="white",
            fg="black",
            master=frame_sequence
        )
        sequence_1.pack(side="left")
        sequence_2.pack(side="left")
        sequence_3.pack(side="left")
        sequence_4.pack(side="left")

        # Light section
        label_light = Label(frame_light, text="Lights", width=12)
        light_on = tk.Button(
            text="ON",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_light
        )
        light_off = tk.Button(
            text="OFF",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_light
        )
        label_light.pack(side="left")
        light_on.pack(side="left")
        light_off.pack(side="left")

        # Lock section
        label_lock = Label(frame_lock, text="Locks", width=12)
        lock = tk.Button(
            text="LOCK",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_lock
        )
        unlock = tk.Button(
            text="UNLOCK",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_lock
        )
        label_lock.pack(side="left")
        lock.pack(side="left")
        unlock.pack(side="left")

        # Thermostat section
        label_thermostat = Label(frame_thermostat, text="Thermostat", width=12)
        therm_up = tk.Button(
            text="+",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_thermostat
        )
        therm_down = tk.Button(
            text="-",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_thermostat
        )
        label_thermostat.pack(side="left")
        therm_up.pack(side="left")
        therm_down.pack(side="left")

        label_speaker = Label(frame_speaker, text="Speakers", width=12)
        speaker_up = tk.Button(
            text="+",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_speaker
        )

        speaker_down = tk.Button(
            text="-",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_speaker
        )
        label_speaker.pack(side="left")
        speaker_up.pack(side="left")
        speaker_down.pack(side="left")

        output = tk.Text(frame_status)
        output.pack()
        output.insert(tk.END, "This will be some output text\nLine two\n")

# Create the window
window = tk.Tk()
window.title("Smart PyControl")
app = Window(window)
window.minsize(500, 800)
window.mainloop()
