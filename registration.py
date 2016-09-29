import requests

def main():
	registration()

def registration():
	data = {
		'token': '055755d0bef8118fe9960bcf4f12b2be',
		'github': 'https://github.com/alejandrogarciasalas/code2040'
	}
	r = requests.post('http://challenge.code2040.org/api/register', json=data)

if __name__ == "__main__":
	main()