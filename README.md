# Logbook-Reader-Photo-Scraper
Reads in the details from a pilot's e-logbook and scrapes through airliners.net to see if there are any matching photos.

Spotters regularly put photographs up of big jets landing, taking off or taxiing. But it can be a nightmare to search through all your flights to see if there's any been taken of you. Especially if you have thousands of flights.

This simple script reads the date and aircraft registration section of your logbook and searches through airliners.net to see if there are any matching photographs. Then the individual can go and double check if that picture is actually a photo of themselves flying.

Logbook needs to be a csv file in the same folder called 'Logbook.csv' with a 'Date' column in d/m/y format and a 'Registration' column like 'G-EZAI' or 'N976CT'. Look on Airliners.net to see which registration format is closest for your chosen region.

The script relies on the tags and the search function of Airliners.net which can be patchy and inconsistent so bear that in mind when using it.

Future bugs to fix:
The script won't return photopgrahs if they go into the preceding day. e.g. If you took off in the afternoon on the 1/1/2020 and landed in the morning the next day 2/1/2020 then the script would not pick up the landing. It only goes off the 'date' in the logbook.
It also has no way of differentiating if the same aircraft was flown later that day. Say you fly Heathrow to Paris and back. Then the same aircraft is flown by a different crew Heathrow to Edinburgh and back. If any photos exist of the aircraft on that day they will be scraped and shown. So you will need to double check manually.


REQUIRED PACKAGES:
Beautiful Soup (bs4)
Urlib
requests
pandas
PIL
