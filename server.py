# -*- coding: utf-8 -*-

#C:\Users\mag.jozsef\AppData\Local\Programs\Spyder\Python --spyder interpretter mappa ide kell a PIP-eket másolni

# web server activálásnál instalálni kell a Flask pip-et, ezértn em elég ha a spyder interpreterbe telepítjük azt fel

#web_server\Scripts\activate

#FONTOS - set FLASK_APP=server.py vagy set FLASK_ENV=development - ezután python -m flask run

# a parancssorban kiprintelt url-t kell a böngészőbe illeszteni

# git clone + a repositories link



from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)

@app.route('/')
def my_home():
    return render_template ("index.html")# a render_tepalte, mindig keresni fogja a server mappában a template mappát, amiben a html tempaltnek kell lennie

@app.route('/<string:page_name>')
def html_page(page_name):
    return render_template (page_name)

def write_to_txt(data):
    with open ("C:/python_kodok/udemy_oktatas/19_web_development/web_server/database.txt", mode="a") as database:
        email = data["email"]
        subject = data ["subject"]
        message = data ["message"]
        file = database.write(f"\n{email},{subject},{message}")

def write_to_csv(data):
    with open ("C:/python_kodok/udemy_oktatas/19_web_development/web_server/database.csv", mode="a") as database2:
        email = data["email"]
        subject = data ["subject"]
        message = data ["message"]
        csv_writer = csv.writer(database2, delimiter=",",quotechar='"', quoting = csv.QUOTE_MINIMAL)
        csv_writer.writerow([email, subject, message])
        

@app.route('/submit_form', methods=['POST', 'GET'])#contact html 62.sor
def submit_form():
    try:
        if request.method == 'POST':
            data = request.form.to_dict()
            write_to_csv(data)
            return redirect("/thankyou.html")
        else:
            return "The data did not got saved to the database"
    except:
        return "Something went wrong. Try Again!"



@app.route('/blog')
def blog():
    return 'These are my thoughts on blogs'

@app.route('/blog/2020/dogs')
def blog2():
    return 'This is my doggo'

