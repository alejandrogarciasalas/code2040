import requests

def get_needle_haystack(token):
	authentication = {
		'token': token
	}
	r = requests.post('http://challenge.code2040.org/api/haystack', json=authentication)
	d = r.json()
	needle = d['needle']
	haystack = d['haystack']
	return needle, haystack

def get_needle_index(needle, haystack):
	return haystack.index(needle)

def validate(token, needle_index):
	solution = {
		'token': token,
		'needle': needle_index
	}
	r = requests.post('http://challenge.code2040.org/api/haystack/validate', json=solution)
	return r.text

def main():
	token = '055755d0bef8118fe9960bcf4f12b2be'	
	needle, haystack = get_needle_haystack(token)
	needle_index = get_needle_index(needle, haystack)
	validation = validate(token, needle_index)
	print(validation)


if __name__ == "__main__":
	main()