import requests
from bs4 import BeautifulSoup
from scraper.utils import create_headers

def scrape_cars(params):
    base_url = "https://bama.ir/car"
    url = f"{base_url}/{params['model']}?price={params['price_min']},{params['price_max']}&color={params['color']}"

    # ارسال درخواست به سایت
    headers = create_headers()
    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        print(f"خطا در درخواست: {response.status_code}")
        return []

    # تحلیل محتوای HTML
    soup = BeautifulSoup(response.text, "html.parser")
    car_list = []

    # پیدا کردن خودروها
    cars = soup.find_all("div", class_="listdata")
    for car in cars:
        name = car.find("h2").text.strip()
        price = car.find("p", class_="cost").text.strip()
        link = car.find("a")["href"]
        car_list.append({"name": name, "price": price, "link": link})

    return car_list
