from utils import Days

from flask import Flask, request,render_template

app = Flask(__name__)

@app.route("/")
def home_api():
    return render_template("index.html")

@app.route("/calday",methods = ["GET","POST"])
def get_days():

    if request.method == "GET":
        name = request.args.get("name")
        day = request.args.get("day")
        month = request.args.get("month")

        obj = Days(name,day,month)
        days = obj.calculation()

        wish = f"Hey {name} today is your birthday..!!!"
        other = f"Hey {name}, {days} days remains for your birthday"

        if days == 0:
            return render_template("index.html",msg = wish)
        else:
            return render_template("index.html",msg = other)
        
if __name__ == "__main__":
    app.run(port=8080)

