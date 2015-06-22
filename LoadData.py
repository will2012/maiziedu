import json
def loadData(filepath):
    file_object = open(filepath)
    try:
        jsonstr = file_object.read()
        array = json.loads(jsonstr)
        for item in array:
            link = item['link'].encode('utf-8')
            print link
    finally:
        file_object.close()

if __name__ == "__main__":
     loadData('/Users/will/workspace/github/python/scrapy/maiziedu/Course.json');