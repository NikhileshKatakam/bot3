from chatbot12 import find
from flask import Flask, render_template, request
import chatbot12
import re
import csv
app = Flask(__name__)
event=3422
order = 9983
stock=[875]
app.static_folder = 'static'
@app.route("/")
def home():
    return render_template("index.html")
li = ["i would like to order something","i want to place an order"," i want to order","show me menu card","order","menu card","place an order"]
@app.route("/get")
def get_bot_response():
    global stock
    global event
    global order
    inut = request.args.get('msg')
    if event == 1 or event ==2:
        event =0
        order=order+1
        stock.append(int(order))
        rowlist=[inut,str(order)]
        fields = ['order', 'orderno'] 
        with open('sales.csv', 'a') as data:
            writer = csv.writer(data)
            writer.writerow(fields)
            writer.writerow(rowlist)
        return("thank u for ur ordder😋😋 your order number  {} ".format(order))
    
    inut=inut.lower()
    x1=re.search(".*order.*",inut)
    x2 = re.search(".*menu.*",inut)
    x3 = re.search(".*cancel.*",inut)
    if x1:
        event=1 
        return("please write your order names with quantities and hotel name u want it from" )
    elif x2:
        event=2
        return("please write your order names with quantities and hotel name u want it from")
    elif x3:
        x = re.findall('[0-9]+',inut)
        print(x[0],stock)
        if x[0] in stock:
            return("got it")
        else:
            return("sorry no such order")
    else:
        event =7575
        return(str(chatbot12.find(inut))) 

if __name__ == "__main__":
    app.run() 