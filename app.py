from twitter import *
import datetime
import json
import os


#Tokens define
TOKEN = "880400083178487808-pmaZtHEKPdp0z6GeXSILlfwtfJVXSKv"
TOKEN_SECRET = "FEjMBnfy0lpPlKiLJn7OtoblZfquuMKuv0yg2H6TfPnq1"
CONSUMER = "A0Ukc5aY4WTv8dyqqhZAF3vGW"
CONSUMER_SECRET = "BI4Dclwrex0mkY33UH8up3jnN44gqxC3X9hAHzleGlxZlUF7xq"

#t = Twitter(auth=OAuth(TOKEN, TOKEN_SECRET, CONSUMER, CONSUMER_SECRET))

#t.statuses.update(status="Bot稼働開始")

TEMPLATE = """[ミールカード利用額Bot]
今日({0})の利用可能額は、
一人暮らし¥1150コース生: ¥{1}
自宅生¥550コース生: ¥{2}
"""
TEMPLATE_FALSE = """[ミールカード利用額Bot]
今日({0})はミールカード利用できません。
"""

today = datetime.datetime.today()

def check():
    prices = {
        "flag": True,
        "remoter":1150,
        "gmter":550
    }


    print(today.weekday())

    #fix
    fileName = os.path.dirname(os.path.abspath(__file__)) + "/fix.json"
    f = open(fileName, 'r')
    fixData = json.load(f)
    for fix in fixData:
        
        if fix["range"] == False:
            print("PinPoint:",fix)
            if today == datetime.datetime.strptime(fix["date"], '%Y/%m/%d'):
                prices["remoter"] = fix["price"]["remoter"]
                prices["gmter"] = fix["price"]["gmter"]

        else:
            print(fix)
            endDate = datetime.datetime.strptime(fix["end"], '%Y/%m/%d')
            startDate = datetime.datetime.strptime(fix["start"], '%Y/%m/%d')
            if startDate <= today <= endDate:
                prices["remoter"] = fix["price"]["remoter"]
                prices["gmter"] = fix["price"]["gmter"]
        
            

    #Sunday
    if today.weekday() == 6:
        prices["flag"] = False
    
    #Saturday
    if today.weekday() == 5:
        prices["remoter"] = 600
        prices["gmter"] = 600
        
    #return
    return prices

def update():
    _prices = check()
    print(_prices)
    #if _prices["flag"] == False:
    #    t.statuses.update(status= TEMPLATE_FALSE.format(today.today()))
    #else:
    #    t.statuses.update(status= TEMPLATE.format(today.today(), _prices["remoter"], _prices["gmter"]))


update()