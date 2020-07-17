import tkinter as tk
from tkinter import *

window = tk.Tk()
window.minsize(500, 800)

frame_title = tk.Frame(width="500", height="50")
frame_tab = tk.Frame(width="500", height="30")
frame_sequence = tk.Frame(width="500", height="50")
frame_light = tk.Frame(width="500", height="50")
frame_lock = tk.Frame(width="500", height="50")
frame_thermostat = tk.Frame(width="500", height="50")
frame_speaker = tk.Frame(width="500", height="50")
frame_status = tk.Frame(width="500", height="50")

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

photo = PhotoImage(file="icon.gif")
label_title = Label(frame_title, image=photo)
label_title.photo = photo
label_title.pack()

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

label_sequence = Label(frame_sequence, text="Sequences", width=12)
label_sequence.pack(side="left")

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

window.mainloop()
