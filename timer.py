import tkinter as tk
from tkinter.font import Font
import winsound
import time
'''

print("Local Time: " + time.ctime(time.time()))

print("----------------------------------------------------------------")
result = time.localtime(time.time())
print("result:", result)
print("\nyear:", result.tm_year)
print("\ntm_hour:", result.tm_hour)
print("\ntm_minute:", result.tm_min)

named_tuple = time.localtime()  # get struct_time
time.strftime("%m/%d/%Y, %H:%M:%S", named_tuple)
num = 0'''

def play_sound():
    duration = 1000  # milliseconds
    freq = 440  # Hz
    winsound.Beep(freq, duration)
def on_entry_click(event, entry_var):
    if entry_var.get() == '0':
        entry_var.set('')


def on_focusout(event, entry_var):
    if entry_var.get() == '':
        entry_var.set('0')


def clear_window():
    # Hide or destroy all widgets in the window
    for widget in window.winfo_children():
        widget.destroy()


def handle_start_timer():
    hours = int(hour_var.get())
    minutes = int(minute_var.get())
    seconds = int(second_var.get())
    try:
        if hours == None:
            hours = 0
        if minutes == None:
            minutes = 0
        if seconds == None:
            seconds = 0
        total_seconds = hours * 3600 + minutes * 60 + seconds
        print(f"Timer starting for: {hours} hours, {minutes} minutes, {seconds} seconds.")
        clear_window()
        timer(total_seconds)
    except ValueError:
        textlabel.config(text="Please enter valid numbers for hours, minutes, and seconds")


def display_timer(hours, minutes, seconds):
    global timer_display
    try:
        # Attempt to update the label if it already exists and hasn't been destroyed
        timer_display.config(text=f"{hours:02d}:{minutes:02d}:{seconds:02d}")
    except (NameError, tk.TclError):
        # If it doesn't exist or has been destroyed, recreate and pack it
        timer_display = tk.Label(window, text=f"{hours:02d}:{minutes:02d}:{seconds:02d}", font=Font(family="Helvetica", size=14))
        timer_display.pack(pady=(100, 100))


def timer(total_seconds):
    if total_seconds > -1:
        minutes, seconds = (total_seconds // 60, total_seconds % 60)
        hours = 0
        if minutes > 60:
            hours, minutes = (minutes // 60, minutes % 60)
        print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
        display_timer(hours, minutes, seconds)
        window.after(1000, lambda: timer( total_seconds - 1))
    else:
        Restart_button = tk.Button(
            window, text="New Timer", command=Start_Command).pack(pady=(20, 10))
        play_sound()
        display_timer(0, 0, 0)


def Start_Command():
    clear_window()  # This clears the current window contents
    # Global declarations are needed if these variables are modified inside this function and accessed elsewhere
    global hour_var, minute_var, second_var
    hour_var = tk.StringVar(value="0")
    minute_var = tk.StringVar(value="0")
    second_var = tk.StringVar(value="0")
    global textlabel
    textlabel = tk.Label(window, text="Enter timer duration", font=Font(
        family="Helvetica", size=14)).pack(pady=(20, 10))
    tk.Label(window, text="Hour", font=Font(
        family="Helvetica", size=14)).pack()
    hour_entry = tk.Entry(window, textvariable=hour_var,
                          font=Font(family="Helvetica", size=14))
    hour_entry.pack(pady=(0, 20))
    hour_entry.bind("<FocusIn>", lambda event: on_entry_click(event, hour_var))
    hour_entry.bind("<FocusOut>", lambda event: on_focusout(event, hour_var))

    tk.Label(window, text="Minute", font=Font(
        family="Helvetica", size=14)).pack()
    minute_entry = tk.Entry(window, textvariable=minute_var,
                            font=Font(family="Helvetica", size=14))
    minute_entry.pack(pady=(0, 20))
    minute_entry.bind(
        "<FocusIn>", lambda event: on_entry_click(event, minute_var))
    minute_entry.bind(
        "<FocusOut>", lambda event: on_focusout(event, minute_var))

    tk.Label(window, text="Seconds", font=Font(
        family="Helvetica", size=14)).pack()
    second_entry = tk.Entry(window, textvariable=second_var,
                            font=Font(family="Helvetica", size=14))
    second_entry.pack(pady=(0, 20))
    second_entry.bind(
        "<FocusIn>", lambda event: on_entry_click(event, second_var))
    second_entry.bind(
        "<FocusOut>", lambda event: on_focusout(event, second_var))

    
    tk.Button(window, text="Set Timer",command=handle_start_timer).pack(pady=(20, 10))


window = tk.Tk()

window.title("Timer App")
window.geometry("600x500")


def Title_Screen():
    time_label = tk.Label(window, text="Timer", font=Font(
        family="Helvetica", size=40, weight="bold"))
    time_label.pack(pady=(180, 0))

    Start_button = tk.Button(window, text="Start", font=Font(
        family="Helvetica", size=20, weight="bold"), command=Start_Command)

    Start_button.pack(pady=(20, 10))


Title_Screen()
window.mainloop()
