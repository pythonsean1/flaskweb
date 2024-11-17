from flask import Flask, render_template, request, url_for

app = Flask(__name__)           # initialise the Flask application

@app.route('/', methods=['GET'])                 # define a route for the root URL
def index():
    if request.method == 'GET':
        title = 'First page'
        name = 'Sean'
        message = 'Welcome to my website'
        
        return render_template("index.html",tab_bar_title=title , name=name, message=message)    # response sent when the route is accessed
        
@app.route('/about',methods={'POST'})
def about():
    if request.method == 'POST':
        username= request.form.get('username')
        age = request.form.get('age')
        title = "About Me"
        name = username
        message = 'Welcome to the Hello World Page'
        return render_template('about.html', username=username , age=age, name=name, title=title, message=message)
    
@app.route('/hello')
def hello():
    title = 'Hello'
    name = 'Yaw'
    message = ' Welcome to the hello world page!'
    return render_template('hello.html', name=name, message=message, title=title)


# running the application
if __name__ == '__main__':
    app.run(debug=True)

