#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from flask import Flask,render_template,request
from flask_mysqldb import MySQL

app=Flask(__name__)

app.config['MYSQL_HOST']='database-1.c53glwj3kh9m.ap-south-1.rds.amazonaws.com'
app.config['MYSQL_USER']='admin'
app.config['MYSQL_PASSWORD']='admin1234'
app.config['MYSQL_DB']='house'

mysql=MySQL(app)

@app.route("/")
def xyz():
    return render_template('google.html')
@app.route("/userinput",methods=['GET','POST'])
def nitin():
    if(request.method=='POST'):
        name=request.form['n1']
        email=request.form['e1']
        phone=request.form['p1']
        course=request.form['c1']
        env=mysql.connection.cursor()
        env.execute("INSERT INTO data(name,email,phone,course) VALUES(%s,%s,%s,%s)",(name,email,phone,course))
        mysql.connection.commit()
        env.close()
        return 'Successfully submitted'
    return render_template("google.html")
if __name__=='__main__':
    app.run()

