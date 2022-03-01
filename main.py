import pytz, json
from datetime import datetime as dt
from  flask import Flask, jsonify

timezones = pytz.all_timezones

from config import PORT
app = Flask(__name__)
app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home_page():
    time_list = []
    def time_calculator():
        for element in timezones:
            Name = element
            country_name = pytz.timezone(element)
            country_time = dt.now(country_name)
            Date = country_time.strftime("Date = %b-%d-%Y")
            Time = country_time.strftime("Time = %H:%M:%S") 
            Month = country_time.strftime("%B")
            Day = country_time.strftime("%D")
            Year = country_time.strftime("%Y")
            H = country_time.strftime("%H") 
            M = country_time.strftime("%M")
            S = country_time.strftime("%S")

            if H >= "13":
              Merdian = "PM"
            else:
              Merdian = "AM"

            time = {
                    'Country_Name': Name,
                    'Time' : Time,
                    'Date': Date,
                    'Month': Month,
                    'Day': Day,
                    'Year': Year,
                    'Hour': H,
                    'Minute': M,
                    'Second': S,
                    'Merdian' : Merdian
                   }

            time_list.append(time)
            New_List = json.dumps(time_list, indent =2)
            with open("time.json", "w", encoding="utf-8") as file:
                file.write(str(New_List))

    time_calculator()
    return jsonify(time_list)

if __name__ == '__main__':
    app.run(debug = True, host = '0.0.0.0', port= PORT)
    