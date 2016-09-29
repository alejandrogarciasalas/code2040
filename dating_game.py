import requests
import datetime


def get_interval_datestamp(token, request_endpoint):
    authentication = {
        'token': token
    }
    r = requests.post(request_endpoint, json=authentication)
    d = r.json()
    interval = d['interval']
    datestamp = d['datestamp']
    return interval, datestamp


def get_new_datestamp(interval, datestamp):
    date = datetime.datetime.strptime(datestamp, '%Y-%m-%dT%H:%M:%SZ')
    new_date = date + datetime.timedelta(seconds=interval)
    new_datestamp = new_date.strftime('%Y-%m-%dT%H:%M:%SZ')
    return new_datestamp


def validate(token, new_date, validation_endpoint):
    solution = {
        'token': token,
        'datestamp': new_date
    }
    r = requests.post(validation_endpoint, json=solution)
    return r.text


def main():
    token = '055755d0bef8118fe9960bcf4f12b2be'
    request_endpoint = 'http://challenge.code2040.org/api/dating'
    validation_endpoint = 'http://challenge.code2040.org/api/dating/validate'
    interval, datestamp = get_interval_datestamp(token, request_endpoint)
    ans = get_new_datestamp(interval, datestamp)
    validation = validate(token, ans, validation_endpoint)
    print(validation)


if __name__ == "__main__":
    main()
