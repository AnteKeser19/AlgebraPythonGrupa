import requests

URL='https://www.algebra.hr'
URL2='https://index.hr'
URL3='https://24sata.hr'
URL4='https://phet-dev.colorado.edu/html/build-an-atom/0.0.0-3/simple-text-only-test-page.html'

response=requests.get(URL3)
print(response.status_code)
print()
print(response.content)
print()
print(response.headers)
print()
print(response.text)