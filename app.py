from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    return render_template_string("""
    <html>
        <head>
            <title>My Simple Website</title>
        </head>
        <body>
            <h1>Welcome to my simple website!</h1>
        </body>
    </html>
    """)

if __name__ == '__main__':
     app.run(host='0.0.0.0', debug=True)