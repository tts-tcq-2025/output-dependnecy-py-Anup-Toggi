def sensorStub():
    # This stub does NOT expose the bug (precipitation is 70, wind > 50)
    return {
        'temperatureInC': 50,
        'precipitation': 70,
        'humidity': 26,
        'windSpeedKMPH': 52
    }
 
def highPrecipLowWindStub():
    # This stub triggers the missed case: high precipitation, low wind
    return {
        'temperatureInC': 50,
        'precipitation': 80,  # High
        'humidity': 80,
        'windSpeedKMPH': 10   # Low
    }
 
def report(sensorReader):
    readings = sensorReader()
    weather = "Sunny Day"
 
    if (readings['temperatureInC'] > 25):
        if readings['precipitation'] >= 20 and readings['precipitation'] < 60:
            weather = "Partly Cloudy"
        elif readings['windSpeedKMPH'] > 50:
            weather = "Alert, Stormy with heavy rain"
    return weather
 
def testRainy():
    weather = report(sensorStub)
    print(weather)
    assert("rain" in weather)

def testHighPrecipitation():
    weather = report(highPrecipLowWindStub)
    print("High Precip Test:", weather)

    assert("rain" in weather or "Cloudy" in weather), "Expected rain or cloud-related weather, got: " + weather

testRainy()
testHighPrecipitation()
