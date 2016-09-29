import requests

def get_prefix_arr(token):
	authentication = {
		'token': token
	}
	r = requests.post('http://challenge.code2040.org/api/prefix', json=authentication)
	d = r.json()
	prefix = d['prefix']
	arr = d['array']
	return prefix, arr

def get_strings_starting_with_prefix(prefix, arr):
	return [str for str in arr if str[0:len(prefix)] != prefix]

def validate(token, arr):
	solution = {
		'token': token,
		'array': arr
	}
	print(arr)
	r = requests.post('http://challenge.code2040.org/api/prefix/validate', json=solution)
	return r.text

def main():
	token = '055755d0bef8118fe9960bcf4f12b2be'	
	prefix, arr = get_prefix_arr(token)
	ans = get_strings_starting_with_prefix(prefix, arr)
	validation = validate(token, ans)
	print(validation)


if __name__ == "__main__":
	main()