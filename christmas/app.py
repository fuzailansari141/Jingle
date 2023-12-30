from flask import *
from dbm import *

from dbm import view

from dbm import viewvenue

from dbm import checkemail, insertbookings, insertdiscount, insertemail, venue_details

from dbm import viewstate

from dbm import insertcontact
app=Flask(__name__)

@app.route("/")
def home():
    data=view()
    data=data[0:4]
    return render_template("index.html",data=data)

@app.route("/chat")
def chat():
    return render_template("chat.html")

@app.route("/spin", methods=['GET', 'POST'])
def spin():
    email=request.form['email']
    venue=request.form['venue']
    t=(email,venue)
    data=checkemail(t)
    if not data:
        insertemail(t)
        data=checkemail(t)
        return render_template("spinmain.html",mail=data,insert="not")
    else:
        insertemail(t)
        return render_template("spinmain.html",mail=data,Venue=venue,other="yes")

@app.route("/card")
def card():
    data=view()
    return render_template("maincard.html",i=data)

@app.route("/card",methods=["get","post"])
def card1():
    state=request.form['state']
    if state=='All':
        data=view()
        return render_template("maincard.html",i=data)
    elif state!="All":
        data=viewstate(state)
        return render_template("maincard.html",i=data)


@app.route("/viewvenue")
def info1():
    venue=request.args.get("Venue")
    data=viewvenue(venue)
    return render_template("mainpage.html",i=data)

@app.route("/checkoutform")
def form():
    email=request.args.get("email")
    discount=request.args.get("discount")
    venue=request.args.get("venue")
    disc=discount.replace("%","")
    t=(discount,email,venue)
    insertdiscount(t)
    venue_details1=venue_details(venue)
    discount_value=(int(venue_details1[0][5]) * int(disc))/100
    total=int(venue_details1[0][5]) - discount_value
    return render_template("checkout.html",data=t,venue_details=venue_details1,discount=disc,discount_value=discount_value,total=total)



@app.route("/submitform", methods=['post'])
def submit():
    email=request.form['email']
    phone=request.form['phone']
    quantity=request.form['quantity']
    card1=request.form['card1']
    card2=request.form['card2']
    card3=request.form['card3']
    card4=request.form['card4']
    cvv=request.form['cvv']
    name=request.form['name']
    venue=request.form['venue']
    discount=request.form['discount_value']

    
    t=(email,phone,quantity,card1+card2+card3+card4,cvv,name,venue,discount)
    insertbookings(t)
    venue_details1=venue_details(venue)
    price=venue_details1[0][5] 
    disc=discount.replace("%","")
    total=((int(price)*int(quantity))*int(disc))/100
    total=(int(price)*int(quantity))-int(total)
    return render_template("invoice.html",data=t,venue_details=venue_details1,total=total)


@app.route("/contact", methods=['GET', 'POST'])
def contact():
    name=request.form['name']
    email=request.form['email']
    phone=request.form['phone']
    message=request.form['message']
    t=(name,email,phone,message)
    insertcontact(t)
    return render_template("index.html",contact="submitted")



if __name__=="__main__":
    app.run(debug=True)