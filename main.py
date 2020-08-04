import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import json

url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
# url = "http://localhost:3000"
allUsers = ['LOGIN']
currentUser = ""
allLogs = []

# example of how to do a post request
# response = requests.post(url + "/setvolume", json={"volume": 6})
# print(response.content)

# example of how to do a get request
# response = requests.get(url + "/devicestatus/speaker")
# speakerResult = json.loads(response.content)
# print(speakerResult['volume'])

def speaker(option):
    if option == "up":
        act = "up"
    else:
        act = "down"
    #pass in up or down action as well as user
    #do the action
    url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url + "/" + act + "/speaker")
    print(action.content)
    #post to log
    action= requests.post(url + "/logs", json={"user": currentUser,
    "device":"speaker",
    "action":act
    })
    print(action.content)

def lightBulb(option):
    if option == "on":
        act = "/deviceon"
    else:
        act = "/deviceoff"
    #pass in one or off action as well as user
    #do the action
    url =  "https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url + act + "/lightbulb" )
    print(action.content)
    #post to log
    action=requests.post(url + "/logs", json={"user": currentUser,
    "device":"lightbulb",
    "action":option
    })
    print(action.content)

def doorlock(option):
    if option == "deviceoff":
        act = "off"
    else:
        act = "on"
    #pass in unlock or lock action as well as user
    #do the action
    url ="https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url + "/" + option + "/doorlock")
    print(action.content)
    #post to log
    action=requests.post(url+"/logs",json={"user": currentUser,
    "device":"doorlock",
    "action":act
    })
    print(action.content)

def thermostat(option):

    #pass in up or down action as wel as user
    #action
    url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
    action = requests.post(url + "/" + option + "/thermostat")
    print(action.content)
    #print to log
    action = requests.post(url+"/logs", json = {"user": currentUser,
    "device":"thermostat",
    "action":option
    })
    print(action.content)

# Get the current user based on who is selected in the dropdown
def _getUser(cur):
    global currentUser
    currentUser = cur
    print(currentUser)
def postToLog(option, optionTwo = ""):
    if option == "Thermostat":
        act = "Adjust"
    else:
        act = optionTwo
    requests.post(url + "/logs", json={"user": currentUser,
    "device":option,
    "action":act
    })

def _homeSequence():
    print("Home sweet home")
    # Set the temperature to 72
    # Turn lights on
    # Unlock the doors
    # Turn the speakers on
    requests.post(url + "/settemp", json={"temperature": 72})
    postToLog("Thermostat") # just posts to log
    requests.post(url + "/deviceon/speaker")
    postToLog("Speaker", "On")# just posts to log
    lightBulb("on")
    doorlock("deviceoff")


def _awaySequence():
    print("Bye Felicia")
    # Set the temperature to 78
    # Turn the lights off
    # Lock the doors
    # Turn the speakers off
    requests.post(url + "/settemp", json={"temperature": 78})
    postToLog("Thermostat") # just posts to log

    requests.post(url + "/deviceoff/speaker")
    postToLog("Speaker", "Off")# just posts to log

    lightBulb("off")
    doorlock("deviceon")

def _sleepSequence():
    print("Snoozle time zzzzzzz")
    # Set the temperature to 68
    # Turn the lights off
    # Lock the doors
    # Turn the speakers off
    requests.post(url + "/settemp", json={"temperature": 68})
    postToLog("Thermostat") # just posts to log

    requests.post(url + "/deviceoff/speaker")
    postToLog("Speaker", "Off")# just posts to log

    lightBulb("off")
    doorlock("deviceon")

def _burglarSequence():
    print("Intruder alert!")
    # Set the temperature to 99
    # Turn the lights on
    # Lock the doors
    # Turn the speakers on
    # Set the speaker volume to 100
    requests.post(url + "/settemp", json={"temperature": 99})
    postToLog("Thermostat") # just posts to log

    requests.post(url + "/deviceon/speaker")
    postToLog("Speaker", "On")# just posts to log

    lightBulb("on")
    doorlock("deviceon")

def _populateUsers():
    userResponse = requests.get(url + "/allusers")
    users = json.loads(userResponse.content)
    for user in users:
        allUsers.append(user['userId'])

def _pupolateLogsTab():
    log = requests.get(url + "/alllogs")
    logs = json.loads(log.content)
    for l in logs:
        allLogs.append(l)


class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        #make a notebook
        notebook = ttk.Notebook()

        control_frame = Frame(notebook, width = 500, height = 600)
        log_frame = Frame(notebook,width = 500, height = 800)

        # Setup frames
        frame_login = tk.Frame(width="500", height="50")
        frame_title = tk.Frame(width="500", height="50")
        frame_tab = tk.Frame(control_frame,width="500", height="30")
        frame_sequence = tk.Frame(control_frame,width="500", height="50")
        frame_light = tk.Frame(control_frame,width="500", height="50")
        frame_lock = tk.Frame(control_frame,width="500", height="50")
        frame_thermostat = tk.Frame(control_frame,width="500", height="50")
        frame_speaker = tk.Frame(control_frame,width="500", height="50")
        frame_status = tk.Frame(control_frame,width="500", height="50")
        
        frame_login.pack(side="top", fill="x")
 

        
        # Add separators to frames
        frame_title.pack()
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        '''frame_tab.pack(side="top", fill="x")
        separator = Frame(control_frame,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)'''

        frame_sequence.pack(side="top", fill="x")
        separator = Frame(control_frame,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_light.pack(side="top", fill="x")
        separator = Frame(control_frame,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_lock.pack(side="top", fill="x")
        separator = Frame(control_frame,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_thermostat.pack(side="top", fill="x")
        separator = Frame(control_frame,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_speaker.pack(side="top", fill="x")
        separator = Frame(control_frame,height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

        frame_status.pack(side="top")

        
        notebook.pack(pady = 10)
        notebook.add(control_frame, text = "Control")
        notebook.add(log_frame, text = "Logs")

        _populateUsers()
        # Create and populate login dropdown
        variable = StringVar(master)
        variable.set(allUsers[0]) # set the default value
        user_dropdown = tk.OptionMenu(frame_login, variable, command = _getUser, *allUsers)
        user_dropdown.pack(side="right")

        photo = PhotoImage(file="icon.gif")
        label_title = Label(frame_title, image=photo)
        label_title.photo = photo
        label_title.pack()

        # Setup the navigation section
        '''label_tab = Label(frame_tab, text="Navigation", width=12)

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
        tab_logs.pack(side="left")'''

        # Sequence section
        label_sequence = Label(frame_sequence, text="Sequence", width=12)
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
            command = _awaySequence,
            master=frame_sequence
        )
        sequence_3 = tk.Button(
            text="Sleep",
            width=5,
            height=2,
            bg="white",
            fg="black",
            command = _sleepSequence,
            master=frame_sequence
        )
        sequence_4 = tk.Button(
            text="Burglar",
            width=5,
            height=2,
            bg="white",
            fg="black",
            command = _burglarSequence,
            master=frame_sequence
        )
        sequence_1.pack(side="left")
        sequence_2.pack(side="left")
        sequence_3.pack(side="left")
        sequence_4.pack(side="left")

        label_light = Label(frame_light, text="Lights", width=12)
        light_on = tk.Button(
            text="ON",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_light,
            command = lambda:lightBulb("on")
        )

        light_off = tk.Button(
            text="OFF",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_light,
            command = lambda:lightBulb("off")
        )
        label_light.pack(side="left")
        light_on.pack(side="left")
        light_off.pack(side="left")

        label_lock = Label(frame_lock, text="Locks", width=12)
        lock = tk.Button(
            text="LOCK",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_lock,
            command = lambda:doorlock("deviceon")
        )

        unlock = tk.Button(
            text="UNLOCK",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_lock,
            command = lambda:doorlock("deviceoff")

        )
        label_lock.pack(side="left")
        lock.pack(side="left")
        unlock.pack(side="left")

        label_thermostat = Label(frame_thermostat, text="Thermostat", width=12)

        therm_up = tk.Button(
            text="+",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_thermostat,
            command = lambda:thermostat("up")

        )

        therm_down = tk.Button(
            text="-",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_thermostat,
            command = lambda:thermostat("down")

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
            master=frame_speaker,
            command = lambda:speaker("up")
        )

        speaker_down = tk.Button(
            text="-",
            width=8,
            height=3,
            bg="white",
            fg="black",
            master=frame_speaker,
            command = lambda:speaker("down")

        )
        label_speaker.pack(side="left")
        speaker_up.pack(side="left")
        speaker_down.pack(side="left")

        output = tk.Text(frame_status)
        output.pack()
        output.insert(tk.END, "This will be some output text\nLine two\n")

        _pupolateLogsTab()
        log_Txt = tk.Text(log_frame, height = 500, state= NORMAL)
        log_Txt.pack()

        for log in allLogs:
            log_Txt.insert(tk.END, log)

# Create the window
window = tk.Tk()
window.title("Smart PyControl")
app = Window(window)
window.minsize(500, 800)
window.mainloop()
