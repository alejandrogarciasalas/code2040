import requests
import datetime

def get_interval_datestamp(token):
	authentication = {
		'token': token
	}
	r = requests.post('http://challenge.code2040.org/api/dating', json=authentication)
	d = r.json()
	interval = d['interval']
	datestamp = d['datestamp']
	return interval, datestamp

def get_new_datestamp(interval, datestamp):
	date = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
	new_date = date + datetime.timedelta(seconds=interval)
	new_datestamp = new_date.strftime('%Y-%m-%dT%H:%M:%SZ')
	return new_datestamp

def validate(token, new_date):
	solution = {
		'token': token,
		'datestamp': new_date
	}
	r = requests.post('http://challenge.code2040.org/api/dating/validate', json=solution)
	return r.text

def main():
	token = '055755d0bef8118fe9960bcf4f12b2be'	
	interval, datestamp = get_interval_datestamp(token)
	ans = get_new_datestamp(interval, datestamp)
	validation = validate(token, ans)
	print(validation)


if __name__ == "__main__":
	main()