import requests
import geocoder
import smtplib
import json
import datetime as dt
import time


def gmail(email, message):
    """Sends an email via gmail smtp"""
    with open("sender_credentials.json") as sender_credentials_file:
        sender = json.load(sender_credentials_file)
    host = "smtp.gmail.com"
    with smtplib.SMTP(host) as connection:
        connection.starttls()
        connection.login(sender['email'], sender['password'])
        connection.sendmail(sender['email'], email, message)


def close_to_me(lat, lng, margin_of_error):
    """Returns true if a given location is close to my current location"""
    g = geocoder.ip('me')
    my_lat = g.geojson['features'][0]['properties']['lat']
    my_lng = g.geojson['features'][0]['properties']['lng']
    return abs(lat - my_lat) < margin_of_error and abs(lng - my_lng) < margin_of_error


def is_night(lat, lng):
    """Returns true if it's night at given location"""
    # Get sunrise and sunset time at given latitude and longitude. (the hour in 24hrs clock)
    res = requests.get(url="https://api.sunrise-sunset.org/json", params={
        'lat': lat,
        'lng': lng,
        'formatted': 0
    })
    res.raise_for_status()
    sunrise_sunset_data = res.json()
    sunrise_hour = int(sunrise_sunset_data['results']['sunrise'].split('T')[1].split(':')[0])
    sunset_hour = int(sunrise_sunset_data['results']['sunset'].split('T')[1].split(':')[0])

    # Get the current time (the hour in 24hrs clock)
    # We need UTC time as sunrise and sunset time we got from API is in UTC.
    hour_now = dt.datetime.now(dt.timezone.utc).hour

    # Check if current time is at night.
    return sunset_hour <= hour_now <= sunrise_hour


# Get the current location of ISS.
response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()
latitude = float(data['iss_position']['latitude'])
longitude = float(data['iss_position']['longitude'])


# If ISS is close to my current position,
# and it is currently dark,
# then email me to tell me to look up.

print(f"ISS position: {(round(latitude, 2), round(longitude,2 ))}")
print(f"Is it close to me? {'Yes' if close_to_me(lat=latitude, lng=longitude, margin_of_error=5) else 'No'}")
print(f"Is it night there? {'Yes' if is_night(lat=latitude, lng=longitude) else 'No'}")

# Check every 60 seconds if the ISS can be located.
while True:
    time.sleep(60)
    if close_to_me(lat=latitude, lng=longitude, margin_of_error=5) and is_night(lat=latitude, lng=longitude):
        gmail(
            email="roni.abusayeed@gmail.com",
            message='Subject: Look Up!\n\nISS is above you in the sky.'
        )
