

## About:
This repository gives ready made template to deploy deep learning model using flask. 

## How to use it:
1. Clone this repository : <br>
   git clone https://github.com/goutham-nekkalapu/deploying_ML_models

2. Install the requirements : <br>
   pip install -r requirements.txt 
      
    If you want to have different versions of python and other deep learning libraries, you can use [Anaconda](https://anaconda.org/anaconda/python) to create environments.

3. Start the server:
python flask_server.py

4. To use the model deployed, run the client program : python flask_client.py

### Example :
For the image 


![image](http://farm3.static.flickr.com/2500/4038251210_1060c180b0.jpg)

The response from server, has the top-5 predictions, as below:

{
  "1": [
    "hotdog", 
    "0.491872"
  ], 
  "2": [
    "bagel", 
    "0.139255"
  ], 
  "3": [
    "french loaf", 
    "0.107473"
  ], 
  "4": [
    "pretzel", 
    "0.0680968"
  ], 
  "5": [
    "plate", 
    "0.0374931"
  ]
}



## Model used:
The deep learning model deployed here is ResNet-50 and keras library V2.0 is used, this can be modified accordingly to your needs.
