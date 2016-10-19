#! /usr/bin/env python3

#Copyright 2016 Andrew Zuelsdorf. All rights reserved.

#This program takes, on the command line, a city,
#an optional state, and an optional country. Its output
#is the current time in that city or an error message
#if no such time can be found. The user is not guaranteed to get
#an error message if she enters an invalid city
#(such as Noplaceville, NY, USA). But if she enters a valid city,
#then she will get a valid time assuming no network
#issues and no issues with the remote web service.

import geopy, datetime, sys

def main():
	if len(sys.argv) >= 2:
		city = ", ".join(sys.argv[1:])
	else:
		if len(sys.argv) >= 1:
			progName = sys.argv[0]
		else:
			progName = "(program name)"
		sys.stderr.write("Usage: {0} (city name) [state/province name] [country name]\n".format(progName))
		sys.stderr.write("Example: {0} \"Albany\" \"New York\" \"USA\"\n".format(progName))
		sys.stderr.write("Example: {0} \"Nairobi\" \"Kenya\"\n".format(progName))
		sys.stderr.write("Example: {0} \"Tokyo\"\n".format(progName))
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
	except:
		sys.stderr.write("ERROR: Couldn't find the current time for \"{0}\". Please try again.\n".format(city))
		return

	timeZone = geolocator.timezone((latitude, longitude))
	sys.stdout.write("{0}\n".format(datetime.datetime.now(timeZone)))

if __name__ == "__main__":
	main()
