from flask import Flask,render_template

app = Flask(__name__)

# localhost:5000
# landing page/route of the website
@app.route('/')
def index():
    name = "John Graham"#string
    title = "Jumia"#string
    fruits = ['Avacado','Apple','Mango','Guava']#list
    # fruits = []#list
    details = {
        "name":"John Graham",
        "country":"Kenya",
        "age":23,
        "career":"Python developer"
    }
    return render_template('index.html',jina=name,kichwa=title,fruits=fruits,details=details)

# localhost:5000/about
@app.route('/about')
def about():
    # always add title page when rendeing a template
    title= "About page"
    return render_template('about.html', title=title)


if __name__ == '__main__':
    app.run(debug=True, port=3000)
