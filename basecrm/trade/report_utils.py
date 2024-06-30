from datetime import timedelta, date, datetime
import datetime
import requests
import json

from trade.models import ExchangeRates, Currencies


def get_colors(count):
    colors = [
        '#FF0000',
        '#800000',
        '#FFFF00',
        '#808000',
        '#00FF00',
        '#008000',
        '#00FFFF',
        '#008080',
        '#0000FF',
        '#000080',
        '#FF00FF'
    ]
    return colors[:count]


def date_range(start_date, end_date):
    for n in range(int((end_date - start_date).days) + 1):
        yield start_date + timedelta(n)


def get_array_date_between(start_date, end_date):
    result = []
    for dt in date_range(start_date, end_date):
        result.append(dt)
    return result

def check_load_exchange_rates_currencie():
    load_exchange_rates_currencie('840')
    load_exchange_rates_currencie('978')
    load_exchange_rates_currencie('643')
    load_exchange_rates_currencie('949')

def load_exchange_rates_currencie(code_currencie):
    currencie_res = Currencies.objects.filter(code=code_currencie)
    if currencie_res.count() > 0:
        currencie = currencie_res[0].name
    else:
        return

    date_start = datetime.date(2023, 1, 1)
    last_ten = ExchangeRates.objects.filter(currencie_id=code_currencie).order_by('-id')[:1]
    if last_ten.count() > 0:
        date_start = last_ten[0].date + timedelta(days=1)

    headers = {'Accept': 'application/json', 'Content-type': 'text/plain; charset=utf-8'}

    for x in get_array_date_between(date_start, date.today()):
        url = 'https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=' + currencie + '&date=' + x.strftime("%Y%m%d") + '&json'
        response = requests.get(url, headers=headers)
        response.encoding = 'utf-8-sig'
        data = json.loads(response.text)
        cur = ExchangeRates(currencie=currencie_res[0], date=x.strftime("%Y-%m-%d"), value=data[0].get('rate'), multiplicity=1)
        cur.save()
