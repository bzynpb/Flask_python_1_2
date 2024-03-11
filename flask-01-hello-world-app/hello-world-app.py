from flask import Flask 
app = Flask(__name__)

@app.route("/") 
def head():
    return "hello word clarusway-17"

@app.route("/second") # url sonuna /second yazarsa, belirtilen sayfaya gider
def head2():
    return "This is second page."

@app.route("/third") # url sonuna /third yazarsa, belirtilen sayfaya gider
def head2():
    return "This is third page."




if __name__ == '__main__':

    # app.run(debug=True, port=30000)
    app.run(host= '0.0.0.0', port=8081) # hostta calismasi icin yukaridaki kodu comment yaptik