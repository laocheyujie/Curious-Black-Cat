import os
import datetime
import json
import random
import requests
from dotenv import load_dotenv

# 加载环境变量
load_dotenv()

# 获取 API 密钥
NINJAS_API_KEY = os.getenv("NINJAS_API_KEY")

random.seed(2023)

def get_city_list():
    """
    Retrieves a list of city names from a JSON file and returns the shuffled list.

    Returns:
        list: A list of city names.
    """
    city_list = []
    with open('../data/city.json', 'r') as f:
        data = json.load(f)
        for province in data['provinces']:
            for city in province['citys']:
                city_list.append(city['cityName'])
    random.shuffle(city_list)
    return city_list

def generate_city_mapping(year):
    """
    Generates a mapping of dates to cities based on the given year.

    Parameters:
        year (int): The year for which the mapping needs to be generated.

    Returns:
        dict: A dictionary containing the mapping of dates to cities.
    """
    city_mapping = {}
    start_date = datetime.date(year, 1, 1)
    end_date = datetime.date(year, 12, 31)
    delta = datetime.timedelta(days=1)
    current_date = start_date
    while current_date <= end_date:
        city_mapping[current_date] = city_list[current_date.timetuple().tm_yday % len(city_list) - 1]
        current_date += delta
    return city_mapping

def get_city_for_date(date_str):
    """
    Given a date string, this function returns the corresponding city for that date.

    Args:
        date_str (str): A string representing a date in the format "YYYY-MM-DD".

    Returns:
        str: The city corresponding to the given date.

    Raises:
        ValueError: If the date string is not in the correct format.

    Examples:
        >>> get_city_for_date("2022-01-01")
        '烟台市'
        >>> get_city_for_date("2022-12-25")
        '北京市'
    """
    date_format = "%Y-%m-%d"
    try:
        input_date = datetime.datetime.strptime(date_str, date_format).date()
    except ValueError:
        return "无效日期格式。请使用YYYY-MM-DD格式。"
    year_mapping = generate_city_mapping(input_date.year)
    return year_mapping.get(input_date, "日期不在当前年份内")

city_list = get_city_list()


def get_qa(category=''):
    """
        Fetches a trivia question and answer from the API.

        Args:
            category (str): The category of the trivia question. Defaults to an empty string.

        Returns:
            dict: A dictionary containing the question and answer of the trivia.
    """
    api_url = 'https://api.api-ninjas.com/v1/trivia?category={}'.format(category)
    response = requests.get(api_url, headers={'X-Api-Key': NINJAS_API_KEY})
    if response.status_code == requests.codes.ok:
        content = response.json()[0]
        del content['category']
        return content
    else:
        print("Error:", response.status_code, response.json())
        return {}

        
if __name__ == "__main__":
    city_on_date = get_city_for_date("2023-11-25")
    print(city_on_date)
    qa = get_qa()
    print(qa)
