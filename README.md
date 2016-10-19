ABOUT:

This is a python script that retrieves the current time in a given city.
It uses pytz and geopy to do this. Because some classes in geopy
require Internet access, this program requires Internet access.

INSTALLATION:

To install, verify that you have Internet access. Then, run these
commands in this directory:

chmod u+x ./install.sh
./install.sh

NOTE: These commands assume that you are using
a Linux machine that has apt-get, bash, and sudo installed.

RUNNING:

To find the time in a city, follow the usage statement below. Several examples
are provided.

python3 getCurrentTime.py (city name) [state/province name] [country name]

Example: python3 getCurrentTime.py "Albany" "New York" "USA"
Example: python3 getCurrentTime.py "Nairobi" "Kenya"
Example: python3 getCurrentTime.py "Tokyo"
