from flask import Flask, render_template #importing flask class obj from flask library 

app = Flask(__name__) #instantiating the class/obj

@app.route('/') #these are the routes you are directing through the URL like rails routing 
def home():
    return render_template("home.html")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__": #python assign the name to main but if we import this script from another it wont be main
    app.run(debug=True)