
import requests,json

headers = {'Content-type':'application/json'}

#imageurl = 'https://www.organicfacts.net/wp-content/uploads/2013/05/Apple4-700x525.jpg'
#imageurl = 'http://pngimg.com/uploads/orange/orange_PNG780.png'
#imageurl = 'http://farm1.static.flickr.com/170/391919618_3f36cd757e.jpg' 
imageurl = 'http://farm3.static.flickr.com/2500/4038251210_1060c180b0.jpg'

data = {'url':imageurl}

res = requests.post('http://localhost:5001/api/v1/classify_image_top_5', data=json.dumps(data), headers=headers)

#printing response rx 
print(res.text)
