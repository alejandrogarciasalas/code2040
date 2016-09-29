import requests

token = '055755d0bef8118fe9960bcf4f12b2be'	

def get_string():
	authentication = {
		'token': token
	}
	r = requests.post('http://challenge.code2040.org/api/reverse', json=authentication)
	return r.text

def reverse_string(str):
	return str[::-1]

def validate(str):
	str = reverse_string(str)
	data = {
		'token': token,
		'string': str
	}
	r = requests.post('http://challenge.code2040.org/api/reverse/validate', json=data)
	return r.text

def main():
	s = get_string()
	validation = validate(s)
	print(validation)


if __name__ == "__main__":
	main()