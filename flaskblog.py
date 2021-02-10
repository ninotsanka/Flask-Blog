from flask import Flask, render_template, url_for
app = Flask(__name__)

posts = [
    {
        'author': 'Nino',
        'title': 'Blog post 1',
        'content': 'first post content here',
        'date': '2,9,2021'
    },
    {
        'author': 'Nino',
        'title': 'Blog post 2',
        'content': 'second post content here',
        'date': '2,9,2021'
    }
]

@app.route('/')
@app.route('/home')
def home_page():
    return render_template('home.html', posts=posts)
    

@app.route('/about')
def about_page():
    return render_template('about.html', title='About')


if __name__ == '__main__':
    app.run(debug=True)