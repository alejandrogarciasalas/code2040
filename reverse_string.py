import requests

def get_string(token):
	authentication = {
		'token': token
	}
	r = requests.post('http://challenge.code2040.org/api/reverse', json=authentication)
	return r.text

def reverse_string(str):
	return str[::-1]

def validate(token, str):
	str = reverse_string(str)
	solution = {
		'token': token,
		'string': str
	}
	r = requests.post('http://challenge.code2040.org/api/reverse/validate', json=solution)
	return r.text

def main():
	token = '055755d0bef8118fe9960bcf4f12b2be'	
	s = get_string(token)
	validation = validate(token, s)
	print(validation)


if __name__ == "__main__":
	main()