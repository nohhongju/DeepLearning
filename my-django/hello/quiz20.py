import random
import urllib.request
from urllib.request import urlopen
from bs4 import BeautifulSoup

class Quiz20:

    def quiz20list(self) -> str:
        list1 = [1, 2, 3, 4]
        print(list1, type(list1))
        print(list1[0], list1[-1], list1[-2], list1[1:3])

        list2 = ['math', 'english']
        print(list2[0])
        print(list2[0][1])

        list3 = [1, '2', [1, 2, 3]]
        print(list3)

        list4 = [1, 2, 3]
        list5 = [4, 5]
        print(list4 + list5)
        print(2 * list4)

        list4.append(list5)
        print(list4)

        list4[-2] = []
        print(list4)

        a = [1, 2]
        b = [0, 5]
        c = [a, b]
        print(c)

        print(c[0][1])

        c[0][1] = 10
        print(c)

        a = range(10)
        print(a)

        print(sum(a))

        b = [2, 10, 0, -2]
        print(sorted(b))

        b.index(0)
        len(b)
        print(b.index(0), len(b))
        return None

    def quiz21tuple(self) -> str:
        a = (1, 2)
        print(a, type(a))

        a[0] = 4

        a = (1, 2)
        b = (0, (1, 4))
        print(a + b)
        return None

    def quiz22dict(self) -> str:
        a = {"class": ['deep learning', 'machine learning'], "num_students": [40, 20]}

        print(type(a))

        print(a["class"])

        a['grade'] = ['A', 'B', 'C']
        print(a)

        print(a.keys())

        print(list(a.keys()))

        print(a.values())

        print(a.ltems)

        print(a.get('class'))

        print("class" in a)
        return None

    def quiz23listcom(self) -> str:
        print('---------legacy---------')
        a = []
        for i in range(5):
            a.append(i)
        print(a)
        print('------comprehension------')
        a2 = [i for i in range(5)]
        print(a2)
        return None

    def quiz24zip(self) -> str:
        url = 'https://music.bugs.co.kr/chart/track/realtime/total'
        html_doc = urlopen(url)
        soup = BeautifulSoup(html_doc, 'lxml') # html.parser VS lxml
        artists = soup.find_all('p', {'class': 'artist'})
        artists = [i.get_text() for i in artists]
        print(''.join(i for i in artists))
        # print(type(artists))
        # print(soup.prettify())
        return None

    def quiz25dictcom(self) -> str: return None

    def quiz26map(self) -> str: return None

    def quiz27melon(self) -> str:
        headers = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://www.melon.com/chart/index.htm?dayTime=2022030816'
        req = urllib.request.Request(url, headers=headers)
        soup = BeautifulSoup(urlopen(req).read(), 'lxml')
        music = soup.find_all('div', {'class': 'ellipsis rank01'})
        music = [i.get_text() for i in music]
        print(''.join(i for i in music))
        return None

    def quiz28(self) -> str: return None

    def quiz29(self) -> str: return None