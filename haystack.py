import requests

def get_needle_haystack(token, request_endpoint):
	authentication = {
		'token': token
	}
	r = requests.post(request_endpoint, json=authentication)
	d = r.json()
	needle = d['needle']
	haystack = d['haystack']
	return needle, haystack

def get_needle_index(needle, haystack):
	return haystack.index(needle)

def validate(token, needle_index, validation_endpoint):
	solution = {
		'token': token,
		'needle': needle_index
	}
	r = requests.post(validation_endpoint, json=solution)
	return r.text

def main():
	token = '055755d0bef8118fe9960bcf4f12b2be'	
	request_endpoint = 'http://challenge.code2040.org/api/haystack'
	validation_endpoint = 'http://challenge.code2040.org/api/haystack/validate'
	needle, haystack = get_needle_haystack(token, request_endpoint)
	needle_index = get_needle_index(needle, haystack)
	validation = validate(token, needle_index, validation_endpoint)
	print(validation)


if __name__ == "__main__":
	main()