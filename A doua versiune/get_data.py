import requests


class Data:

    def __init__(self, link):
        self.link = link

    def get_last_price(self):
        r = requests.get(self.link)
        return float(r.json()["last"])

