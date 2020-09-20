from flask import Flask
from flask import render_template
app = Flask(__name__)
import pandas as pd
import csv, json
import sqlite3
from flask import g	



#############   database   #####################################
def get_db():
    conn = None
    try:
        conn = sqlite3.connect("data/db.sqlite3")
    except Error as e:
        print(e)

    return conn


def create_dataset():
    conn=get_db()
    sql = ''' INSERT INTO microservices(ID,APIEndpoint,APIForumMessageBoards,APIPortalHomePage,APIProvider,ArchitecturalStyle,AuthenticationModel,DeviceSpecific,DocsHomePageUR,IsThisanUnofficialAPI,IstheAPIDesign,class_1,RestrictedAccess,SSLSupport,Scope,class_2,SupportEmailAddress,SupportedRequestFormats,SupportedResponseFormats,name,data,class_code)
              VALUES(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?) '''
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
def show_dataset():
    conn=get_db()
    acat=[]
    a=[]
    curcat = conn.cursor()
	#alter table microservices add column type varchar default 'standard'
    curcat.execute("SELECT distinct class_1 FROM microservices ")

    rows = curcat.fetchall()

    for row in rows:
        acat.append(row)
    
	
	
    cur = conn.cursor()
    cur.execute("SELECT distinct name,class_1,type FROM microservices ")

    rows = cur.fetchall()

    for row in rows:
        #print(row)
        print()
        a.append(tuple((row[0].replace("&","and").replace("'", "") ,row[1],row[2])))	
    return a,acat
@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()
################################################################
@app.route('/')
def hello_world(microservice=None):
    a,acat=show_dataset()
    #print(a)
    

	
    return render_template('index.html',data={'data':a,'data2':acat})