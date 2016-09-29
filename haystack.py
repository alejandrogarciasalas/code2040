import requests

token = '055755d0bef8118fe9960bcf4f12b2be'	

def get_dict():
	authentication = {
		'token': token
	}
	r = requests.post('http://challenge.code2040.org/api/haystack', json=authentication)
	return r.json()

def get_needle_index(d):
	needle = d['needle']
	haystack = d['haystack']
	return haystack.index(needle)

def validate(needle_index):
	solution = {
		'token': token,
		'needle': needle_index
	}
	r = requests.post('http://challenge.code2040.org/api/haystack/validate', json=solution)

def main():
	d = get_dict()
	needle_index = get_needle_index(d)
	validate(needle_index)


if __name__ == "__main__":
	main()