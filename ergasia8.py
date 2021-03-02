import requests
import responses

c=' '
st=' '
while c!='DONE':
    c = input (' Give cryprocoin: ')
    a = input (' Give amount: ')
    
    if c == 'BTC':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC&tsyms=EUR")
        st=cr.json()
    elif c == 'LTC':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=LTC&tsyms=EUR")
        st=cr.json()
    elif c == 'ETH':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=ETH&tsyms=EUR")
        st=cr.json()
    elif c == 'ADA':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=ADA&tsyms=EUR")
        st=cr.json()
    elif c == 'BNB':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BNB&tsyms=EUR")
        st=cr.json()
    elif c == 'DOT':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=DOT&tsyms=EUR")
        st=cr.json()
    elif c == 'LINK':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=LINK&tsyms=EUR")
        st=cr.json()
    elif c == 'XRP':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=XRP&tsyms=EUR")
        st=cr.json()
    elif c == 'BCH':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=BCH&tsyms=EUR")
        st=cr.json()
    elif c == 'UNI':
        cr = requests.get("https://min-api.cryptocompare.com/data/pricemulti?fsyms=UNI&tsyms=EUR")
        st=cr.json()
    
    st2='"' + str(st) + '"'
    newstr = ''.join((ch if ch in '0123456789.-e' else ' ') for ch in st2)
    listOfNumbers = [float(i) for i in newstr.split()]
    print(float(listOfNumbers[0]) * float(a))
