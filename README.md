# UZLPR

## Vehicles' lcicense plates extraction project

# Website
https://platesmania.com/uz/typenomer1

# Links used in scrapting data
- https://platesmania.com/uz/gallery.php?&ctype=1&start=0
- https://platesmania.com/uz/gallery.php?&ctype=1&usr=20149&start=0
- https://platesmania.com/uz/gallery.php?&ctype=1&usr=43788&start=0
- https://platesmania.com/uz/gallery.php?&ctype=1&usr=85450&start=0
- https://platesmania.com/uz/gallery.php?&ctype=1&usr=42093&start=0
- https://platesmania.com/uz/gallery.php?&ctype=1&usr=55639&start=0

# Google Drive Link for all images
https://drive.google.com/drive/folders/1yVb1np_7Q_cUkO77ppGBDP2Ei47QyeQX?usp=sharing

# Statistics about the extracted data
| No. of vehicle images  | No. of license plates' images | No. of trucks, vans and buses| No. of other vehicle   |
| ---------------------- | ----------------------------- | ---------------------------- | ---------------------- |
| 5147                   | 5147                          |         1739                 |           3408         |

# Used characteristics for license plates
CHARS = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

# Some examples of vehicle images
![17543196](https://user-images.githubusercontent.com/15974766/218662443-164f1567-9219-4cff-b17f-1a371d43e2a5.jpg)  ![17458079](https://user-images.githubusercontent.com/15974766/218662487-8aca5355-f7bd-4ef5-9bab-084e94a29c6e.jpg)
![20884341](https://user-images.githubusercontent.com/15974766/218662534-a19217db-95d8-4b95-bfc9-1e2c87da3d0d.jpg)  ![20879256](https://user-images.githubusercontent.com/15974766/218662572-50496311-8a65-436f-b711-c172fdf401e8.jpg) 

# Some examples of vehicle plate number images
![10741232d441e7](https://user-images.githubusercontent.com/15974766/218662675-7380488c-fb6d-4dc2-ab4b-6ca51b048e9a.png)  ![17306802ee2b2b](https://user-images.githubusercontent.com/15974766/218662693-7a807cb6-0fbb-4e1f-9e54-84e5d0b7eb01.png) 
![17349581c5a631](https://user-images.githubusercontent.com/15974766/218662732-2cf9cf18-dd2b-4084-a66d-674b1311c7c2.png)  ![17807968fd6c94](https://user-images.githubusercontent.com/15974766/218662760-7136baa2-6431-4007-9beb-001051a86895.png) 
![17847943c20a70](https://user-images.githubusercontent.com/15974766/218662839-9d6cb04c-4f1c-477c-aa30-fa5a26a03ccb.png)  ![18240796b25f7f](https://user-images.githubusercontent.com/15974766/218662872-f5dafd38-4321-43eb-ae85-bc7c03f27b24.png) ![18240788e46873](https://user-images.githubusercontent.com/15974766/218663464-f6858700-731c-47ff-a70e-f1c9f51e3027.png)

# Extract a vehicle details
Extracted data is provided in csv file - **uz_license_plates.csv** in the directory folder
parsing_img_and_info method enables scripte vehicle details from the site according to each given item. For example, in the following picture can be seen which information is extracted.

![image](https://user-images.githubusercontent.com/15974766/219029647-32d0e22e-b2b3-485d-816a-4ac86a945e97.png)

The method returns the list of the extracted data according to a provided url. The result will be in the following order:
| Property                     | Value |
| ---------------------------- | ------------- |
| image of vehicle             | 'https://img03.platesmania.com/230214/m/20892803.jpg'  |
| image of license plates      | 'https://img03.platesmania.com/230214/inf/20892803eac4c7.png' |
| license plates in text       | '01 K 173 DB' |
| vehicle type                 | 'DAF XF' |
| vehicle model and other info |  '3rd gen (XF105), 2006–2013', 'Russia - Россия, п.Зайцево Новгородская область, 12/2022 ...прицеп: 8663AA|01...' |

# Vehicle registration plates of Uzbekistan
Types of license plates issued to vehicles
![image](https://user-images.githubusercontent.com/15974766/219033237-a71fcf0c-bb6a-477f-9a99-a80c18263ae7.png)

![image](https://user-images.githubusercontent.com/15974766/219032804-00e218ee-590c-4a96-990f-6bde374bf713.png)
![image](https://user-images.githubusercontent.com/15974766/219032900-dc290edc-f3fd-457b-87a3-d29c427304df.png)
![image](https://user-images.githubusercontent.com/15974766/219033005-2f6cc199-bb3d-4d15-8ed3-46689ceff968.png)
![image](https://user-images.githubusercontent.com/15974766/219033086-f0920174-7d13-49ca-b80d-2b237410e05e.png)

Full information can be checked here:
https://uz.wikipedia.org/wiki/O%CA%BBzbekiston_avtomobil_raqamlari_indeksi

# Used libraries
* BeautifulSoup - to parse html file
* requests_html - to read javascripe file
* requests
* shutil
* os


