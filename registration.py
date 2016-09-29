import requests

def main():
	registration()

def registration():
	authentication = {
		'token': '055755d0bef8118fe9960bcf4f12b2be',
		'github': 'https://github.com/alejandrogarciasalas/code2040'
	}
	r = requests.post('http://challenge.code2040.org/api/register', json=authentication)

if __name__ == "__main__":
	main()