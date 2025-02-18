from flask import Flask, render_template, request

app = Flask(__name__)

email_content = ""

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/page1")
def page1():
    return render_template("page1.html")

@app.route("/page2", methods=["GET", "POST"])
def page2():
    global email_content
    if request.method == "POST":
        email_content = request.form["email_content"]
        return render_template("page3.html")
    return render_template("page2.html")

@app.route("/page3")
def page3():
    return render_template("page3.html")

@app.route("/page4")
def page4():
    return render_template("page4.html")

@app.route("/page5")
def page5():
    return render_template("page5.html")

@app.route("/page6",methods=["GET"])
def page6():
    return render_template("page6.html",email_content=email_content)

@app.route("/page7")
def page7():
    return render_template("page7.html")

@app.route("/page8")
def page8():
    return render_template("page8.html")

@app.route("/page9")
def page9():
    return render_template("page9.html")

@app.route("/page10")
def page10():
    return render_template("page10.html")

@app.route("/page11")
def page11():
    return render_template("page11.html")

@app.route("/myaccount")
def myaccount():
    return render_template("myaccount.html")
#Dummy inbox and message data
inbox = [
    {"id": 1, "sender": "alice@example.com", "subject": "Meeting Update", "preview": "The meeting is rescheduled to..."},
    {"id": 2, "sender": "bob@example.com", "subject": "Project Deadline", "preview": "Don't forget the deadline is..."},
]

messages = {
    1: {"sender": "alice@example.com", "subject": "Meeting Update", "body": "The meeting is rescheduled to tomorrow at 3 PM."},
    2: {"sender": "bob@example.com", "subject": "Project Deadline", "body": "Don't forget the deadline is next Friday at 5 PM."},
}

@app.route("/inbox")
def inbox_page():
    return render_template("inbox.html", inbox=inbox)

@app.route("/email/<int:email_id>")
def email_page(email_id):
    message = messages.get(email_id)
    if message:
        return render_template("email.html", message=message)
    return "Email not found", 404


if __name__ == "__main__":
    app.run(debug=True)
