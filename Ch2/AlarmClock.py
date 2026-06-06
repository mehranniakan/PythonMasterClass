import tkinter as tk
from datetime import datetime
from tkinter import messagebox
current_time = None
alarm_time = None

def main_clock():
    global current_time
    current_time = datetime.now().strftime("%H:%M:%S")
    main_clock_label.config(text=current_time)
    window.after(1000, main_clock)
    time_compare()


def alarm_setter():
    global alarm_time
    alarm_time = f'{alarm_set_entry_hour.get()}:{alarm_set_entry_minute.get()}'
    alarm_label.config(text=f"{alarm_set_entry_hour.get()}:{alarm_set_entry_minute.get()}")
    print(f'Alarm set for {alarm_set_entry_hour.get()}:{alarm_set_entry_minute.get()}:00')


def time_compare():
    global current_time
    global alarm_time

    if alarm_time is not None and alarm_time <= current_time:
        messagebox.showinfo('Alarm Clock', 'Alarm Clock is over!')
        alarm_time = None
        alarm_label.config(text='No Alarm has been set')




window = tk.Tk()
window.title("Alarm Clock")

width = window.winfo_screenwidth()
height = window.winfo_screenheight()
window.geometry(f"{width}x{height}")

# تنظیمات برای وسط‌چین شدن
for i in range(5):  # تعداد ستون‌هایی که استفاده می‌کنی
    window.columnconfigure(i, weight=1)

for j in range(6):  # تعداد سطرهایی که استفاده می‌کنی
    window.rowconfigure(j, weight=1)

main_clock_label = tk.Label(window, text="12:00:00", font=("Arial", 50))
main_clock_label.grid(column=2, row=1, sticky="nsew")

alarm_label = tk.Label(window, text="No Alarm has been set", font=("Arial", 20))
alarm_label.grid(column=2, row=2, sticky="nsew")

alarm_set_entry_hour = tk.Entry(window, font=("Arial", 32))
alarm_set_entry_hour.grid(row=3, column=1, padx=5, pady=5, sticky="nsew")

dot_alarm_label = tk.Label(window, text=":", font=("Arial", 32))
dot_alarm_label.grid(column=2, row=3, sticky="nsew")

alarm_set_entry_minute = tk.Entry(window, font=("Arial", 32))
alarm_set_entry_minute.grid(row=3, column=3, padx=5, pady=5, sticky="nsew")

alarm_set_button = tk.Button(window, text="SET", font=("Arial", 20), command=alarm_setter)
alarm_set_button.grid(row=4, column=2, padx=5, pady=5, sticky="nsew")

main_clock()
window.mainloop()
