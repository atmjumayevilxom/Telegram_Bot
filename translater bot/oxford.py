
import requests
import json
app_id = "6202bfcc"
app_key = "7c13fd08467ec2ec64becc7aba61df33"
language = "en-gb"
 
def getDefinitions(word_id):
    url = "https://od-api.oxforddictionaries.com:443/api/v2/entries/" + language + "/" + word_id.lower()
    response = requests.get(url, headers={"app_id": app_id, "app_key": app_key})
    data=response.json()
    if 'error' in data.keys():
        return False
    output={}
    senses=data['results'][0]['lexicalEntries'][0]['entries'][0]['senses']
    definitions=[]
    for sense in senses:
        definitions.append(f"👉 {sense['definitions'][0]}")
    output['definitions']='\n'.join(definitions)
    if data['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0].get('audioFile'):
        output['audio']=data['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile']
    return output
if __name__=='__main__':
    from pprint import pprint as print
    print(getDefinitions("america"))
    print(getDefinitions("Great Britain "))
# print('Yakum translate',data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][0]['definitions'][0])
# print('Duyum translate',data['results'][0]['lexicalEntries'][0]['entries'][0]['senses'][1]['definitions'][0])
# print('audioFile',data['results'][0]['lexicalEntries'][0]['entries'][0]['pronunciations'][0]['audioFile'])