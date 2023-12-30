import pymysql as p

def connect():
    return p.connect(host="localhost",user="root",password="",database="christmas")



def view():
    con=connect()
    cur=con.cursor()
    sql="select * from christmas_describe"
    cur.execute(sql)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def viewvenue(venue):
    con=connect()
    cur=con.cursor()
    sql="select * from christmas_describe where Venue = %s"
    cur.execute(sql,venue)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def checkemail(t):
    con=connect()
    cur=con.cursor()
    sql="select * from email where email = %s and venue=%s"
    cur.execute(sql,t)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def insertemail(t):
    con=connect()
    cr = con.cursor()
    sql = "insert into email(email,venue) values(%s,%s)"
    cr.execute(sql, t)
    con.commit()
    con.close()

def insertdiscount(t):
    con=connect()
    cr = con.cursor()
    sql = "update email set discount=%s,spin='yes' where email=%s and venue=%s"
    cr.execute(sql, t)
    con.commit()
    con.close()

def venue_details(venue):
    con=connect()
    cur=con.cursor()
    sql="select * from christmas_describe where Venue = %s"
    cur.execute(sql,venue)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data

def viewstate(state):
    con=connect()
    cur=con.cursor()
    sql="select * from christmas_describe where State = %s"
    cur.execute(sql,state)
    data=cur.fetchall()
    con.commit()
    con.close()
    return data[0]

def insertbookings(t):
    con=connect()
    cr = con.cursor()
    sql = "insert into booking_details(email,phone,quantity,card_number,cvv,name,venue,discount) values(%s,%s,%s,%s,%s,%s,%s,%s)"
    cr.execute(sql, t)
    con.commit()
    con.close()

def insertcontact(t):
    con=connect()
    cr = con.cursor()
    sql = "insert into contact(name,email,phone,message) values(%s,%s,%s,%s)"
    cr.execute(sql, t)
    con.commit()
    con.close()

