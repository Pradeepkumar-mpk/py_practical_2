from flask import Flask,render_template,request
app = Flask("__name__")
 
@app.route("/home")
def home():
    return "<h1> hai, i am pradeep </h1>"

subscribersList=[]
post=[]
products=[]
@app.route("/form",methods=["POST","GET"])
def form():
   subscribersList.append(request.form.get("subscribersList"))
   post.append(request.form.get("post"))
   products.append(request.form.get("products"))
   print(subscribersList)
   print(post)
   print(products)
   return render_template("index.html",data1=subscribersList,data2=post,data3=products)


if __name__ == ("__main__"):
    app.run(debug=True)

       