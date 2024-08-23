from flask import Flask,request,render_template,redirect,url_for
app=Flask(__name__)

@app.route("/",methods=['GET','POST'])
def home():
    if request.method == "POST" :
       e=request.form.get("email")
       return redirect(url_for("about",email=e))
    return render_template("index.html")

@app.route("/about")
def about():
    email=request.args.get("email")
 
    u=email[:email.index("@")]
    do=email[email.index("@")+1 :]
    return render_template("thankyo.html",email=email,username=u,domain=do)

if __name__=="__main__":
    app.run(debug=True)
