#Author: Grant Miller
#Class: SDEV140
#Last Updated: 12/15/2023
#Purpose: Multiple Conversion calculators all in one app for convenience.


import tkinter as tk
from tkinter import ttk
from datetime import datetime, timedelta

class MainApp:
    def __init__(self, root):
        #App Title
        self.root = root
        self.root.title("Converter App")

        # Main Window Size
        self.root.geometry("400x200")

        # Main Window
        self.main_frame = ttk.Frame(root)
        self.main_frame.pack(fill=tk.BOTH, expand=True)

        # Main Window Components
        main_label = ttk.Label(self.main_frame, text="Choose a conversion type:")
        main_label.pack(pady=20)

        #Variables for buttons in Main Window

        temperature_button = ttk.Button(self.main_frame, text="Temperature Conversion",
                                        command=self.open_temperature_window)
        temperature_button.pack()

        currency_button = ttk.Button(self.main_frame, text="Currency Conversion",
                                     command=self.open_currency_window)
        currency_button.pack()

        timezone_button = ttk.Button(self.main_frame, text="Time Zone Conversion",
                                     command=self.open_timezone_window)
        timezone_button.pack()
    #Opens Temperature Window upon request
    def open_temperature_window(self):
        TemperatureConversionWindow(self.root, self.main_frame)
    #Opens Currency Window upon request
    def open_currency_window(self):
        CurrencyConversionWindow(self.root, self.main_frame)
    #Opens Timezone Window upon request
    def open_timezone_window(self):
        TimeWindow(self.root, self.main_frame)

class TemperatureConversionWindow:
    def __init__(self, root, main_frame):
        self.root = root
        self.main_frame = main_frame

        # Temperature Window
        self.temperature_window = tk.Toplevel(self.root)
        self.temperature_window.title("Temperature Conversion")

        # Temperature Window Back to Main button
        back_button = ttk.Button(self.temperature_window, text="Back to Main",
                                 command=self.return_to_main)
        back_button.pack(pady=10)

        # Load information from the main program
        self.temp_direction_var = tk.StringVar()
        self.temp_direction_var.set("C to F")

        direction_label = tk.Label(self.temperature_window, text="Select Conversion Direction:")
        direction_label.pack()

        direction_dropdown = ttk.Combobox(self.temperature_window, textvariable=self.temp_direction_var)
        direction_dropdown['values'] = ('C to F', 'F to C')
        direction_dropdown.pack()

        temperature_label = tk.Label(self.temperature_window, text="Enter Temperature:")
        temperature_label.pack()

        self.temperature_entry = ttk.Entry(self.temperature_window)
        self.temperature_entry.pack()

        convert_button = ttk.Button(self.temperature_window, text="Convert", command=self.convert_temperature)
        convert_button.pack()

        self.result_label_temperature = tk.Label(self.temperature_window, text="")
        self.result_label_temperature.pack()

    #Converts Temperature upon pressing Convert button
    def convert_temperature(self):
        try:
            temp_direction = self.temp_direction_var.get()
            temperature = float(self.temperature_entry.get())

            if temp_direction == "C to F":
                converted_temp = (temperature * 9/5) + 32
                result_text = f"{temperature} Celsius is {converted_temp:.2f} Fahrenheit"
            elif temp_direction == "F to C":
                converted_temp = (temperature - 32) * 5/9
                result_text = f"{temperature} Fahrenheit is {converted_temp:.2f} Celsius"
            else:
                result_text = "Invalid conversion direction."

            self.result_label_temperature.config(text=result_text)

        except ValueError:
            self.result_label_temperature.config(text="Invalid input. Please enter a valid number.")
    #Returns to main
    def return_to_main(self):
        self.temperature_window.destroy()
        self.main_frame.deiconify()
class CurrencyConversionWindow:
    def __init__(self, root, main_frame):
        self.root = root
        self.main_frame = main_frame

        # Currency Window
        self.currency_window = tk.Toplevel(self.root)
        self.currency_window.title("Currency Conversion")

        # Currency Window Back to Main button
        back_button = ttk.Button(self.currency_window, text="Back to Main",
                                 command=self.return_to_main)
        back_button.pack(pady=10)

        # Load information from the main program
        self.from_currency_var = tk.StringVar()
        self.to_currency_var = tk.StringVar()

        from_currency_label = tk.Label(self.currency_window, text="From Currency:")
        from_currency_label.pack()

        from_currency_dropdown = ttk.Combobox(self.currency_window, textvariable=self.from_currency_var)
        from_currency_dropdown['values'] = ('USD', 'CAD', 'GBP', 'EUR')
        from_currency_dropdown.pack()

        to_currency_label = tk.Label(self.currency_window, text="To Currency:")
        to_currency_label.pack()

        to_currency_dropdown = ttk.Combobox(self.currency_window, textvariable=self.to_currency_var)
        to_currency_dropdown['values'] = ('USD', 'CAD', 'GBP', 'EUR')
        to_currency_dropdown.pack()

        amount_label = tk.Label(self.currency_window, text="Enter Amount:")
        amount_label.pack()

        self.amount_entry = ttk.Entry(self.currency_window)
        self.amount_entry.pack()

        convert_button = ttk.Button(self.currency_window, text="Convert", command=self.convert_currency)
        convert_button.pack()

        self.result_label_currency = tk.Label(self.currency_window, text="")
        self.result_label_currency.pack()

    #Converts currency upon request
    def convert_currency(self):
        try:
            amount = float(self.amount_entry.get())
            from_currency = self.from_currency_var.get()
            to_currency = self.to_currency_var.get()

            # Updated conversion rates
            conversion_rates = {
                ('USD', 'CAD'): 1.34,
                ('USD', 'GBP'): 0.72,
                ('USD', 'EUR'): 0.92,
                ('CAD', 'USD'): 0.75,
                ('CAD', 'GBP'): 0.54,
                ('CAD', 'EUR'): 0.68,
                ('GBP', 'USD'): 1.39,
                ('GBP', 'CAD'): 1.86,
                ('GBP', 'EUR'): 1.12,
                ('EUR', 'USD'): 1.09,
                ('EUR', 'CAD'): 1.47,
                ('EUR', 'GBP'): 0.89,
            }

            if (from_currency, to_currency) in conversion_rates:
                exchange_rate = conversion_rates[(from_currency, to_currency)]
                converted_amount = amount * exchange_rate
                self.result_label_currency.config(text=f"{amount} {from_currency} is {converted_amount:.2f} {to_currency}")
            else:
                self.result_label_currency.config(text="Invalid currency conversion.")
        except ValueError:
            self.result_label_currency.config(text="Invalid input. Please enter a valid number.")
    #Returns to main
    def return_to_main(self):
        self.currency_window.destroy()
        self.main_frame.deiconify()

class TimeWindow:
    def __init__(self, root, main_frame):
        self.root = root
        self.main_frame = main_frame

        # Time Window
        self.time_window = tk.Toplevel(self.root)
        self.time_window.title("Time Window Conversion")

        # Time Window Back to Main button
        back_button = ttk.Button(self.time_window, text="Back to Main",
                                 command=self.return_to_main)
        back_button.pack(pady=10)

        # Load information from the main program
        enter_time_label = tk.Label(self.time_window, text="Enter Time (24hr Time):")
        enter_time_label.pack()
        
        self.from_timezone_var = tk.StringVar()
        self.time_entry = ttk.Entry(self.time_window)
        self.time_entry.pack()

        from_timezone_label = tk.Label(self.time_window, text="From Timezone:")
        from_timezone_label.pack()

        from_timezone_dropdown = ttk.Combobox(self.time_window, textvariable=self.from_timezone_var)
        from_timezone_dropdown['values'] = ('EST', 'PST', 'CST', 'GMT', 'CET', 'AWST', 'AEST')
        from_timezone_dropdown.pack()

        convert_button = ttk.Button(self.time_window, text="Convert", command=self.convert_time)
        convert_button.pack()

        self.result_label_time = tk.Label(self.time_window, text="")
        self.result_label_time.pack()

    #Converts Time
    def convert_time(self):
        try:
            from_timezone = self.from_timezone_var.get()
            entered_time = self.time_entry.get()

            entered_time_obj = datetime.strptime(entered_time, "%H:%M")

            # Timezone Differences
            time_diff = {
                'EST': -5,
                'PST': -8,
                'CST': -6,
                'GMT': 0,
                'CET': 1,
                'AWST': 8,
                'AEST': 10,
            }

            # Convert entered time to GMT
            gmt_time = entered_time_obj - timedelta(hours=time_diff[from_timezone])

            # Calculate Converted Times
            converted_times = {}
            for tz in time_diff:
                converted_time = gmt_time + timedelta(hours=time_diff[tz])
                converted_times[tz] = converted_time.strftime("%H:%M")

            # Display result
            self.result_label_time.config(text=f"Entered Time in {from_timezone}: {entered_time}\n"
                                               f"Converted Times: {converted_times}")

        except ValueError:
            self.result_label_time.config(text="Invalid input. Please enter a valid time.")

    def return_to_main(self):
        self.time_window.destroy()
        self.main_frame.deiconify()



if __name__ == "__main__":
    root = tk.Tk()
    app = MainApp(root)
    root.mainloop()
