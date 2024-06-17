import urllib.request
import urllib.parse

URL='https://www.algebra.hr'
URL2='https://index.hr'
URL3='https://24sata.hr'
URL4='https://phet-dev.colorado.edu/html/build-an-atom/0.0.0-3/simple-text-only-test-page.html'

konekcija=urllib.request.Request(URL4,headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW 64; rv:12.0) Gecko/20100101 Firefox/12.0'})

with urllib.request.urlopen(konekcija) as response:
    stranica=response.read().decode()

print(stranica)

print('*'*50)

upit='kako zaobici ssl'
encodirani_upit=urllib.parse.quote(upit)
eu_utf8=encodirani_upit.encode("utf-8")
UPIT=f'https://duckduckgo.com/?q={eu_utf8}'
request=urllib.request.Request(UPIT)
response=urllib.request.urlopen(request)
data=response.read().decode()
print(data)