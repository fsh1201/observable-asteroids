import requests
from bs4 import BeautifulSoup
payload = {'pc': '1.1.3.1',
           'n': '16',
           'oc': 'D39',
           'y0': '2020',
           'm0': '8',
           'd0': '15',
           'h0': '13',
           'mi0': '00',
           'y1': '2020',
           'm1': '8',
           'd1': '15',
           'h1': '21',
           'mi1': '00',
           'ti': '1.0',
           'tiu': 'hours'}
an=[1,4,21,243,253,433,951,2867,4179,5535,9969,25143,
    101955,134340,162173,486958,16,617,3200,3548,11351,
    15094,21900,52246,65803,153591,1991,140,145,2019,2101,
    2530,2703,3352,3840,4015,4660,4979,5604,10302,99942,
    64070,175706,172034,138971,15091,65803]
for n in an:
    payload['n'] = str(n)
    strhtml = requests.get('https://newton.spacedys.com/astdys/index.php', params = payload)
    soup = BeautifulSoup(strhtml.text,'lxml')
    data = soup.select('#mainContent2 > pre')
    for item in data:
        result = {
            'title':item.get_text()
        }
    # print(data)
    # print(type(data))
    mstring = result['title']
    mag = []
    alt = []

    for i in range(5,13):
        # print(mstring.splitlines()[i].split())
        if mstring.splitlines()[i].split()[7] == '+' or mstring.splitlines()[i].split()[7] == '-':
            mag.append(mstring.splitlines()[i].split()[11])
            alt.append(mstring.splitlines()[i].split()[12])
        else:
            mag.append(mstring.splitlines()[i].split()[10])
            alt.append(mstring.splitlines()[i].split()[11])
    flag = 0
    for m in range(len(mag)):
        if float(mag[m]) < 17.2 and float(alt[m]) > 30:
            flag = 1

    if flag == 1:
        print(n)
        print(mag)
        print(alt)
