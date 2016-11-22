from flask import Flask, render_template
from flask_bootstrap import Bootstrap
app = Flask(__name__)

@app.route("/")
def onboarding():
	return render_template("onboardform.html", title = 'DC2.0/Polaris - OnBoarding')

if __name__ == "__main__":
    app.run()
