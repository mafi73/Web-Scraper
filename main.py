from scraper.bama_scraper import scrape_cars
from database.db_operations import save_to_db

def main():
    
    search_params = {
        "price_min": 0,
        "price_max": 1000000000,
        "color": "white",
        "model": "peugeot-207"
    }

    
    car_data = scrape_cars(search_params)

    
    if car_data:
        save_to_db(car_data)
        print(f"{len(car_data)} رکورد به دیتابیس اضافه شد.")
    else:
        print("هیچ داده‌ای یافت نشد.")

if __name__ == "__main__":
    main()
