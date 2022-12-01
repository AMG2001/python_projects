from flask import Flask , request # this line is to import flask package in your project

app = Flask(__name__) # here is the start point of flask application

# stores list
stores=[
    {
        "name":"amgad_store",
        "items":[
        {
        "name":"Chair",
            "price":15.99
        }
        ]
    },
    {
        "name": "ansary_store",
        "items": [
            {
                "name": "lefta",
                "price": 15.99
            }
        ]
    }
]

# initial endpoint in application
@app.route('/') # this is an endpoint .
def hello_world():  # put application's code here
    return 'Hello World!'


if __name__ == '__main__':
    app.run()

# this end point used to get all stores that stored in server .
@app.get("/stores") # here we create our end point , note that get is the type of request "Get , Post"
def getStores(): # this is the function that associated with endpoint
    return  {"stores":stores}


# this method is used to add new store to stores list
def addNewStore(storeName):
    newStore = {
        "name":storeName,
        "items":[
            {
                "name":"",
                "price":""
            }
        ]
    }
    stores.append(newStore)

# this end point is used to add new store to stores list
@app.post("/<string:storeName>")
def postStore(storeName):
    for store in stores:
        if(storeName == store['name']):
            print("Store is already exist")
            return  stores,201
    addNewStore(storeName)
    return  stores , 201 # here we returned stores list with status code 201

# this end point is used to add item in store if it exist .
@app.post("/<string:storeName>/editstore/additem/<string:itemName>")
def addItemInStore(storeName,itemName):
    for store in stores:
        if(storeName==store['name']):
            store['items'][0]['name']=itemName
            return stores
    print("Store is not found !!")
    return stores

@app.post("/<string:storeName>/getItems")
def getStoreItems(storeName):
    for store in stores:
        if(store['name']==storeName):
            return store['items']
    return "store not exist" , 404

