import datetime
import random
import json

lstProducts=['banana','Oranges','Kiwi','lattuce','Cucumber',
'asparagus','black beans','black-eyed peas','kidney beans','lentils'
'Ratlami Sev','Maggie','cabbage','cauliflower','celery','endive','okra','Poblano Pepper','Bell Pepper','Serrano Pepper','Piri Piri Pepper','Jalapeño Pepper','Scotch Bonnet Pepper'
'Ginger','Apples','Mint','Sprays','cream','Green Pepper','Wheet Flour','Laddies Finger','Cantaloupe','Haldi','Red Pepper','Coconuts'
'Cherries','Fig','Grapes','Honeydew','Mammee Apple','Lychee','Strawberry',
'Tomatillo']

lenlstProducts = len(lstProducts)
lstWeight=[100,500,1000,2000,5000]
lenlstWeight = len(lstWeight)
customerId=[x for x in range(1000,2000,2)]
timedelta1=datetime.timedelta(weeks = 22, days = 5)
minOrderdt=datetime.datetime.now().date()-timedelta1
maxOrderdt=datetime.datetime.now().date()
orderDtRange=(maxOrderdt-minOrderdt).days

def getOrder():
    global lstProducts
    global lenlstProducts
    global lstWeight
    global lenlstWeight
    global customerId
    global minOrderdt
    global maxOrderdt

    lstProds={}
    sampleProducts = random.randint(1,lenlstProducts-1)
    for x in random.sample(lstProducts, sampleProducts):
        y = lstWeight[random.randint(0,lenlstWeight-1)]
        lstProds[x] =  str(y) 

    return {
        "customerid": str(customerId[random.randint(0,len(customerId)-1)]),
        "orderdt": (minOrderdt + datetime.timedelta(days=random.randint(0,orderDtRange))).strftime("%m/%d/%Y"),
        "orderamt": str(round(random.uniform(11.02,9023.99),2)) ,
        "products": lstProds
    }


if __name__ == "__main__":
    print (minOrderdt, maxOrderdt, orderDtRange)
    indexLinePrefix='{"index":{"_id":"'
    indexLineSuffix='"}}'
    
    fw=open('orders.json','w')
    for x in range(1000,11000):
        newOrder = getOrder()
        fw.write(indexLinePrefix + str(x) + indexLineSuffix)
        fw.write("\n")
        fw.write(json.dumps(newOrder))
        fw.write("\n")
    fw.close()        
