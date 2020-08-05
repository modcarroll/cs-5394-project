import tkinter as tk
from tkinter import *
from tkinter import ttk
import requests
import json
from datetime import datetime

url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
# url = "http://localhost:3000"
allUsers = ['LOGIN']
currentUser = ""
allLogs = []
allButtons = []

# example of how to do a post request
# response = requests.post(url + "/setvolume", json={"volume": 6})
# print(response.content)

# example of how to do a get request
# response = requests.get(url + "/devicestatus/speaker")
# speakerResult = json.loads(response.content)
# print(speakerResult['volume'])

# Get the current user based on who is selected in the dropdown
def _getUser(cur):
    global currentUser
    currentUser = cur
    print(currentUser + " has logged in.")

    # Disable buttons if no user is selected
    if currentUser == 'LOGIN':
        for btn in allButtons:
            btn.configure(state = 'disabled')
    else:
        for btn in allButtons:
            btn.configure(state = 'normal')

def _populateUsers():
    userResponse = requests.get(url + "/allusers")
    users = json.loads(userResponse.content)
    for user in users:
        allUsers.append(user['userId'])

def _pupolateLogsTab():
    log = requests.get(url + "/alllogs")
    logs = json.loads(log.content)
    for l in logs:
        print(l)
        logConstruct = {"user": l['user'] if l['user'] else "", "device": l['device'] if l['device'] else "", "action": l['action'] if l['action'] else "", "timestamp": l['timestamp'] if l['timestamp'] else ""}
        allLogs.append(logConstruct)

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master

        v = StringVar() # doorlock
        w = StringVar() # thermostat
        x = StringVar() # speaker
        y = StringVar() # lightbulb

        def _homeSequence():
            print("Home sweet home")
            # Set the temperature to 72
            # Turn lights on
            # Unlock the doors
            # Turn the speakers on
            speaker(10)
            lightBulb("on")
            doorlock("deviceoff")
            thermostat(72)

        def _awaySequence():
            print("Bye Felicia")
            # Set the temperature to 78
            # Turn the lights off
            # Lock the doors
            # Turn the speakers off
            thermostat(78)
            speaker(0)
            lightBulb("off")
            doorlock("deviceon")

        def _sleepSequence():
            print("Snoozle time zzzzzzz")
            # Set the temperature to 68
            # Turn the lights off
            # Lock the doors
            # Turn the speakers off
            lightBulb("off")
            doorlock("deviceon")
            speaker(0)
            thermostat(68)

        def _burglarSequence():
            print("Intruder alert!")
            # Set the temperature to 99
            # Turn the lights on
            # Lock the doors
            # Set the speaker volume to 100
            lightBulb("on")
            doorlock("deviceon")
            speaker(100)
            thermostat(99)

        #make a notebook
        notebook = ttk.Notebook()

        control_frame = Frame(notebook, width = 550, height = 600)
        log_frame = Frame(notebook,width = 550, height = 800)

        # Setup frames
        frame_login = tk.Frame(width="550", height="50")
        frame_title = tk.Frame(width="550", height="50")
        frame_tab = tk.Frame(control_frame,width="550", height="30")
        frame_sequence = tk.Frame(control_frame,width="550", height="50")
        frame_light = tk.Frame(control_frame,width="550", height="50")
        frame_lock = tk.Frame(control_frame,width="550", height="50")
        frame_thermostat = tk.Frame(control_frame,width="550", height="50")
        frame_speaker = tk.Frame(control_frame,width="550", height="50")
        frame_status = tk.Frame(control_frame,width="550", height="50")

        frame_login.pack(side="top", fill="x")

        # Add separators to frames
        frame_title.pack()
        separator = Frame(height=2, bd=1, relief=SUNKEN)
        separator.pack(fill=X, padx=5, pady=5)

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

        label_warning = Label(frame_login, text="You must login using the dropdown before issuing commands -->", width=70)
        label_warning.config(font=("Courier", 14), fg="red")
        label_warning.pack(side="left")

        photo = PhotoImage(file="icon.gif")
        label_title = Label(frame_title, image=photo)
        label_title.photo = photo
        label_title.pack()

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
        sequence_1.configure(state = 'disabled')
        sequence_2.pack(side="left")
        sequence_2.configure(state = 'disabled')
        sequence_3.pack(side="left")
        sequence_3.configure(state = 'disabled')
        sequence_4.pack(side="left")
        sequence_4.configure(state = 'disabled')
        allButtons.append(sequence_1)
        allButtons.append(sequence_2)
        allButtons.append(sequence_3)
        allButtons.append(sequence_4)

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
        light_on.configure(state = 'disabled')
        light_off.pack(side="left")
        light_off.configure(state = 'disabled')
        allButtons.append(light_on)
        allButtons.append(light_off)

        status_light = Label(frame_light, textvariable=v, width=12)
        response = requests.get(url + "/devicestatus/lightbulb")
        lightResult = json.loads(response.content)
        v.set(lightResult['status'])
        status_light.pack(side="left")

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
        lock.configure(state = 'disabled')
        unlock.pack(side="left")
        unlock.configure(state = 'disabled')
        allButtons.append(lock)
        allButtons.append(unlock)

        status_doorLock = Label(frame_lock, textvariable=w, width=12)
        response = requests.get(url + "/devicestatus/doorlock")
        lockResult = json.loads(response.content)
        if(lockResult == "on"):
            w.set("locked")
        else:
            w.set("unlocked")
        status_doorLock.pack(side="left")

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
        therm_up.configure(state = 'disabled')
        therm_down.pack(side="left")
        therm_down.configure(state = 'disabled')
        allButtons.append(therm_up)
        allButtons.append(therm_down)

        status_thermostat = Label(frame_thermostat, textvariable=x, width=12)
        response = requests.get(url + "/devicestatus/thermostat")
        tempResult = json.loads(response.content)
        x.set(tempResult['temperature'])
        status_thermostat.pack(side="left")

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
        speaker_up.configure(state = 'disabled')
        speaker_down.pack(side="left")
        speaker_down.configure(state = 'disabled')
        allButtons.append(speaker_up)
        allButtons.append(speaker_down)

        status_speaker = Label(frame_speaker, textvariable=y, width=12)
        response = requests.get(url + "/devicestatus/speaker")
        speakResult = json.loads(response.content)
        y.set(speakResult['volume'])
        status_speaker.pack(side="left")

        output = tk.Text(frame_status)
        output.pack()
        # output.insert(tk.END, "This will be some output text\nLine two\n")

        _pupolateLogsTab()
        log_Txt = tk.Text(log_frame, height = 500, state= NORMAL)
        log_Txt.pack()

        for log in allLogs:
            logString = log['timestamp'] + ", user: " + log['user'] + " " + log['device'] + " " + log['action'] + "\n"
            log_Txt.insert(tk.END, logString)

        def postToLog(device, act):
            response = requests.post(url + "/logs", json={"user": currentUser,
            "device":device,
            "action":act
            })

        def lightBulb(option):
            if option == "on":
                act = "/deviceon"
            else:
                act = "/deviceoff"
            # pass in one or off action as well as user
            # do the action
            url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
            action = requests.post(url + act + "/lightbulb")
            actResult = json.loads(action.content)
            print(actResult['message'])

            # post to log
            postToLog("lightbulb", option)

            output.insert(tk.END, datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " " + actResult['message'] + "\n")

            response = requests.get(url + "/devicestatus/lightbulb")
            bulbResult = json.loads(response.content)
            v.set(bulbResult['status'])

        def speaker(option):
            if option == 'up':
                act = "up"
            elif option == 'down':
                act = "down"
            else:
                act = "adjust"
            # pass in up or down action as well as user
            # do the action
            if(act == "adjust"):
                url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
                action = requests.post(url + "/setvolume/", json={"volume": option})
                actResult = json.loads(action.content)
                print(actResult['message'])
            else:
                url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
                action = requests.post(url + "/" + act + "/speaker")
                actResult = json.loads(action.content)
                print(actResult['message'])

            # post to log
            postToLog("speaker", act)

            output.insert('1.0', datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " " + actResult['message'] + "\n")

            response = requests.get(url + "/devicestatus/speaker")
            sResult = json.loads(response.content)
            y.set(sResult['volume'])

        def doorlock(option):
            if option == "deviceoff":
                act = "off"
            else:
                act = "on"
            # pass in unlock or lock action as well as user
            # do the action
            url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
            action = requests.post(url + "/" + option + "/doorlock")
            actResult = json.loads(action.content)
            print(actResult['message'])

            # post to log
            postToLog("doorlock", option)

            output.insert('1.0', datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " " + actResult['message'] + "\n")

            response = requests.get(url + "/devicestatus/doorlock")
            doorResult = json.loads(response.content)
            if(doorResult['status'] == "off"):
                w.set("unlocked")
            else:
                w.set("locked")

        def thermostat(option):
            if option == 'up':
                act = "up"
            elif option == 'down':
                act = "down"
            else:
                act = "adjust"
            # pass in up or down action as well as user
            # do the action
            if(act == "adjust"):
                url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
                action = requests.post(url + "/settemp/", json={"temperature": option})
                actResult = json.loads(action.content)
                print(actResult['message'])
            else:
                url = "https://pycontrolapi.us-south.cf.appdomain.cloud"
                action = requests.post(url + "/" + act + "/thermostat")
                actResult = json.loads(action.content)
                print(actResult['message'])

            # post to log
            postToLog("thermostat", act)

            output.insert('1.0', datetime.today().strftime('%Y-%m-%d-%H:%M:%S') + " " + actResult['message'] + "\n")

            response = requests.get(url + "/devicestatus/thermostat")
            tempResult = json.loads(response.content)
            x.set(tempResult['temperature'])

# Create the window
window = tk.Tk()
window.title("Smart PyControl")
app = Window(window)
window.minsize(550, 800)
window.mainloop()
