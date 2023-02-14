import os
import shutil
import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup


def read_html(page_url):
    """function to read html file from website

    Parameters
    ----------
    page_url : str
        site url to read html file

    Returns
    -------
    html script
        return BeautifulSoup's html script.
    """
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36 '
    }

    session = HTMLSession()
    r = session.get(page_url, headers=headers, stream=True, timeout=5)
    r.html.render()
    soup = BeautifulSoup(r.html.raw_html, "html.parser")
    return soup


def parsing_img(page_url):
    """function to parse only images
    Images can be car and plate number

    Parameters
    ----------
    page_url : str
        site url to read html file

    Returns
    -------
    list : Array
        return list of images containing vehicle and plate number.
    """
    content = read_html(page_url)

    image_list = []
    # parse by div class
    containers = content.find_all("div", class_="panel-body")
    for container in containers:
        image_tags = container.find_all('img')
        img_urls = [img['src'] for img in image_tags if 'src' in img.attrs]

        image_list.append(img_urls)

    return image_list


def parsing_img_and_info(page_url):
    """function to parse car details and images
    Details include vehicles' type, car model, year and place

    Parameters
    ----------
    page_url : str
        site url to read html file

    Returns
    -------
    list : Array
        return list of vehicle' type, model, year, place,
        image and plate number image
    """
    content = read_html(page_url)

    results = []
    containers = content.find_all("div", class_="panel-body")
    for container in containers:
        # images
        image_tags = container.find_all('img')
        img_urls = [img['src'] for img in image_tags if 'src' in img.attrs]

        # car types
        car_types = container.find_all("h4", class_="text-center")
        types = [car_type.text for car_type in car_types if car_type.text is not None]

        # car model
        car_models = container.find_all("p", class_="text-center")
        models = [model.text.replace('\n', ' ') for model in car_models if model.text is not None]

        results.append([img_urls, types, models])

    return results


def download_images(page_url):
    """function to download and save parsed images

    Parameters
    ----------
    page_url : str
        site url to read html file

    """
    results = parsing_img(page_url)

    cars_list = []
    plates_list = []
    for result in results:
        cars_list.append(result[0])
        plates_list.append(result[1])

    print(f"Found {len(cars_list)} cars' images")
    print(f"Found {len(plates_list)} plates' images")

    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    currentDir = os.getcwd()

    # cars
    count = 0
    path = os.path.join(currentDir, 'cars')
    if len(cars_list) != 0:
        for image_link in enumerate(cars_list):
            try:
                filename = image_link[1].split('/')[-1]
                r = requests.get(image_link[1], headers=headers, stream=True, timeout=5)
                if r.status_code == 200:
                    with open(os.path.join(path, filename), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                    count += 1
            except Exception as e:
                print(e)

            count += 1
        print(f" {count} the car images have been downloaded!\n")

    # plate numbers
    path = os.path.join(currentDir, 'numbers')
    count = 0
    if len(plates_list) != 0:
        for image_link in enumerate(plates_list):
            try:
                filename = image_link[1].split('/')[-1]
                r = requests.get(image_link[1], headers=headers, stream=True, timeout=5)
                if r.status_code == 200:
                    with open(os.path.join(path, filename), 'wb') as f:
                        r.raw.decode_content = True
                        shutil.copyfileobj(r.raw, f)
                    count += 1
            except Exception as e:
                print(e)

        print(f" {count} the plate number images have been downloaded!\n")


if __name__ == '__main__':
    urls = [
        'https://platesmania.com/uz/gallery.php?&ctype=1&start=',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=20149&start=',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=43788&start=',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=85450&start=',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=42093&start=',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=55639&start=',
    ]
    for url in urls:
        for i in range(0, 100):
            url = f'{url}{i}'
            download_images(url)

    print("Finished")
