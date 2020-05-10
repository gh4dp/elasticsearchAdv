import datetime
import random
import json
from faker import Faker
from dateutil.relativedelta import relativedelta

fkr = Faker()

fnames = [ fkr.first_name() for x in range(15) ]
lnames = [ fkr.last_name() for x in range(15) ]
occupations = [ fkr.job() for x in range(7) ]
mindate = datetime.date(1968,1,1)
dateToday = datetime.datetime.now()

dates15 = [ mindate+datetime.timedelta(days = random.randint(-1000,1000) ) for x in range(15) ]
users15 = [ fnames[x][0] + lnames[x] for x in range(15) ]
names15 = [ fnames[x] + ', ' + lnames[x] for x in range(15) ]
ages15 = [ relativedelta(dateToday, dates15[x]).years for x in range(15)  ]
aHeaderLine = "tweetid" + "\t" + "user" + "\t" + "post_date" + "\t" + "message" + "\t" + "name" + "\t"+ "age"


if __name__ == "__main__":
    indexLinePrefix='{"index":{"_id":"'
    indexLineSuffix='"}}'

    fw=open('tweets.json','w')
    fwt = open('tweets.txt', 'w')
    fwt.write(aHeaderLine)
    fwt.write("\n")


    for x in range(1000):    
        randompick = random.randint(0,14)
        postdate = dateToday + datetime.timedelta(days = random.randint(-100,0) )
        loremdata = fkr.paragraph()
        indexid = x+1000
        aLine = str(indexid) + "\t" + users15[randompick] + "\t" + postdate.strftime('%Y-%m-%d') + "\t" + loremdata + "\t" + names15[randompick] + "\t"+ str(ages15[randompick])

        fw.write(indexLinePrefix + str(indexid) + indexLineSuffix)
        fw.write("\n")
        fw.write(json.dumps( {
            "user" : users15[randompick],
            "post_date" : postdate.strftime('%Y-%m-%d'),
            "message": loremdata,
            "name" : names15[randompick],
            "age:" : str(ages15[randompick])
            }
        ))
        fw.write("\n")
        fwt.write(aLine)
        fwt.write("\n")
    fw.close()        
    fwt.close()





"""
aTweet = {
    "user": users15[randompick],
    
    ,
    "name" = names15[randompick],
    "age" = ages15[randompick]
}
"""

