#! /usr/bin/env python3

import geopy, datetime, sys

def main():
	if len(sys.argv) >= 2:
		city = ", ".join(sys.argv[1:])
	else:
		if len(sys.argv) >= 1:
			progName = sys.argv[0]
		else:
			progName = "(program name)"
		sys.stderr.write("Usage: {0} (city name) [state/province name] (country name)\n".format(progName))
		return

	geolocator = geopy.geocoders.GoogleV3()

	try:
		place, (latitude, longitude) = geolocator.geocode(city)
	except TypeError as te:
		sys.stderr.write("ERROR: Couldn't find the current time for \"{0}\". Please ensure that \"{0}\" is the proper name of a city and then try again.\n".format(city))
		return
	except geopy.exc.GeocoderServiceError as gcse:
		sys.stderr.write("ERROR: Couldn't find the current time for \"{0}\". Please check your Internet connection and then try again.\n".format(city))
		return

	timeZone = geolocator.timezone((latitude, longitude))
	print(timeZone)
	sys.stdout.write("{0}\n".format(datetime.datetime.now(timeZone)))

if __name__ == "__main__":
	main()
