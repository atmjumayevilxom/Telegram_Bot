import json

import requests

def instagramDowlonder(link):
    url = "https://instagram-downloader-download-instagram-videos-stories.p.rapidapi.com/index"

    querystring = {"url":link}

    headers = {
        "X-RapidAPI-Key": "c99c41a314msh9abd175cd091a11p10432bjsn46cdb5d56eb3",
        "X-RapidAPI-Host": "instagram-downloader-download-instagram-videos-stories.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    # print(response.text)
    test=response.text
    data=json.loads(test)
    print(data)
    if 'error' in data:
        return "Bad"
    else:
        dict={}
        if data['Type']=='Post-Video':
            dict['Type']='video'
            dict['media']=data['media']
            return dict
        elif data['Type']=='Post-Image':
            dict['Type'] = 'image'
            dict['media'] = data['media']
            return dict
        elif data['Type']=='Carousel':
            dict['Type']='carousel'
            dict['media'] = data['media']
            return dict
        else:
            return 'Bad'
# instagramDowlonder('https://www.instagram.com/p/CkQLvJfpmH4/?utm_source=ig_web_copy_link')