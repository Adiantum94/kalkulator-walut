import json

with open("C.json", "r") as file:
    data = json.load(file)

data = data[0]["rates"]

import csv

with open('plik.csv', 'w') as csvfile:

    fieldnames = ['currency', 'code', 'bid', 'ask']
    csvwriter = csv.DictWriter(csvfile, fieldnames=fieldnames)
    csvwriter.writeheader()
    for n in data:
        csvwriter.writerow(n)

codes=[]
with open('plik.csv', 'r', encoding='utf-8') as csvfile:
    csvreader = csv.DictReader(csvfile)
    for row in csvreader:
           codes.append(row['code'])

           

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
   if request.method == 'GET':
       print("We received GET")
       return render_template("form.html", codes=codes)

   elif request.method == 'POST':
        print("We received POST")
        value= request.form['amount']
        currency= request.form['currency']
        with open('plik.csv', 'r', encoding='utf-8') as csvfile:
            csvreader = csv.DictReader(csvfile)
            for row in csvreader:
                if row['code']== currency:
                    ask= row['ask']
        result= float(value)*float(ask)
        return render_template("form.html", codes=codes, result=result, value=value, currency=currency)

