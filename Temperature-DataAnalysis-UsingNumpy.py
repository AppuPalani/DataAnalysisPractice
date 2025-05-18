import numpy as np

temperature_data = np.array([
    [25, 26, 30, 33, 36], # Chennai
    [18, 20, 21, 19, 18], # Bangalore
    [32, 41, 36, 38, 39], # Hyderabad
    [21, 24, 26, 22, 24], # Tiruvandrum
    [28, 30, 32, 34, 36], # PortBlair
])

Cities = ["Chennai", "Bangalore", "Hyderabas", "Trivandrum", "PortBlair"]

daily_avg_temp = np.mean(temperature_data, axis=1)

print ("Daily avg temperature for each city: ", daily_avg_temp)

city_with_highest_max_temp = np.argmax(daily_avg_temp)

print("City with maximum high temperature is ",Cities[city_with_highest_max_temp])

temp_anomalies = temperature_data - daily_avg_temp[:,np.newaxis]

print("Temperature Anomalies for each city: ",temp_anomalies)