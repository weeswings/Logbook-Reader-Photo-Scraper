from bs4 import BeautifulSoup
import urllib
import requests
from PIL import Image
from io import BytesIO
import pandas as pd

def define_URL(date,reg):
	#Create and return the URL with the Date and Registration inserted.
	return "https://www.airliners.net/search?datePhotographed={}&registrationActual={}&sortBy=dateAccepted&sortOrder=desc&perPage=36&display=detail""".format(date,reg)

def get_request(date,reg):
	try:
		url = define_URL(date,reg)
		headers = {}
		headers['User-Agent'] = "Mozilla/5.0 (X11; Linux i686) AppleWebKit/537.17 (KHTML, like Gecko) Chrome/24.0.1312.27 Safari/537.17"
		req = urllib.request.Request(url, headers = headers)
		resp = urllib.request.urlopen(req)
		respData = resp.read()
		return respData
	except Exception as e:
	    print(str(e))


def get_photo_info(date,reg):
	try:
		Data = get_request(date,reg)
		soup = BeautifulSoup(Data, 'html.parser')

		div=soup.find('div', class_="ps-v2-results-photo")
		print("--------\nwww.airliners.net{}".format(div.find('a').get('href')))
		photo = div.find('img')
		photo_src =photo.get('src')
		response = requests.get(photo_src)
		img = Image.open(BytesIO(response.content))
		img.show()
	except AttributeError:
		print("No photograph found for {} on date: {}".format(reg,date))

def main():
	#load data, set the date column to datetime
	data = pd.read_csv("Logbook.csv")
	data['Date'] = pd.to_datetime(data['Date'])

	#initalise variable to check for repetition
	reg_prev = None
	date_prev = None

	#loop through each row taking the date and reg to check airliners.net
	for iterator in range(0,len(data)):
		try:
			date = data.loc[iterator,'Date'].strftime('%Y-%m-%d')
			reg = data.loc[iterator, 'Registration']

			#if the request is the same as previous then skip
			if date != date_prev and reg != reg_prev:
				get_photo_info(date,reg)

			#set the previous variables
			date_prev = date
			reg_prev = reg
		except:
			pass


if __name__ == '__main__':
	main()
	