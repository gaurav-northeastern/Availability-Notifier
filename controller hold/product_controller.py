from app import app

@app.route("/product")
def product():
    return {
        "Visa API" : "Currently unavaiable",
    "working on it" : "BE READY"
    }