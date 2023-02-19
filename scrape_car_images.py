import os
import shutil
import requests
import pandas as pd
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


def parsing_img_and_info():
    """function to parse car details and images
    Details include vehicles' type, car model, year and place

    Returns
    -------
    list : Array
        return list of vehicle' type, model, year, place,
        image and plate number image
    """
    results = []
    urls = [
        'https://platesmania.com/uz/gallery.php?&ctype=1&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=20149&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=43788&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=85450&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=42093&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=55639&start={0}',
    ]
    for url in urls:
        # for each page
        for i in range(101):
            # set url
            full_url = url.format(i)
            print(full_url)

            # soap object
            content = read_html(full_url)

            # extract images section from html
            containers = content.find_all("div", class_="panel-body")

            for container in containers:
                # images
                image_tags = container.find_all('img')
                img_urls = [img['src'] for img in image_tags if 'src' in img.attrs]
                number_in_text = image_tags[1]['alt']

                # car types
                car_types = container.h4.text

                # car model
                car_models = container.find_all("p", class_="text-center")
                models = [model.text.replace('\n', ' ') for model in car_models if model.text is not None]

                results.append([img_urls, number_in_text, car_types, models])

    return results


def download_images():
    """function to download and save parsed images"""
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.108 Safari/537.36 '
    }
    currentDir = os.getcwd()
    cars_path = os.path.join(currentDir, 'cars')
    numbers_path = os.path.join(currentDir, 'numbers')
    cars_count = 0
    numbers_count = 0
    urls = [
        'https://platesmania.com/uz/gallery.php?&ctype=1&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=20149&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=43788&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=85450&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=42093&start={0}',
        'https://platesmania.com/uz/gallery.php?&ctype=1&usr=55639&start={0}',
    ]
    for url in urls:
        # for each page
        for i in range(101):
            # set url
            full_url = url.format(i)
            print(full_url)
            results = parsing_img(full_url)

            for result in results:

                # cars
                try:
                    filename = result[0].split('/')[-1]
                    if not os.path.exists(os.path.join(cars_path, filename)):
                        r = requests.get(result[0], headers=headers, stream=True, timeout=5)
                        if r.status_code == 200:
                            with open(os.path.join(cars_path, filename), 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                                cars_count += 1
                except Exception as e:
                    print(e)

                # plate numbers
                try:
                    filename = result[1].split('/')[-1]
                    if not os.path.exists(os.path.join(numbers_path, filename)):
                        r = requests.get(result[1], headers=headers, stream=True, timeout=5)
                        if r.status_code == 200:
                            with open(os.path.join(numbers_path, filename), 'wb') as f:
                                r.raw.decode_content = True
                                shutil.copyfileobj(r.raw, f)
                                numbers_count += 1
                except Exception as e:
                    print(e)

    print(f" {cars_count} car images have been downloaded!\n")
    print(f" {numbers_count} license plate images have been downloaded!\n")


if __name__ == '__main__':
    print("Process has started")
    # save images
    # download_images()  # activate when you want to download new imgs

    # parsing vehicles' images, models, types, plate in text
    pd.DataFrame(parsing_img_and_info()).to_csv('uz_license_plates.csv',
                                                index_label="Index",
                                                header=['car & license plates img',
                                                        'license plates in txt',
                                                        'vehicle type',
                                                        'vehicle model & other info'])
    print("Process has finished")
