from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <html>
        <head>
            <title>My Flask Website</title>
        </head>
        <body style="font-family: Arial; text-align: center; margin-top: 50px;">
            <h1>Welcome to my Flask Website </h1>
            <p>This is my first web application built using Flask.</p>
            
            <p> My name is Mahir Dyan and I am currently exploring this new framework</p>
            <h3>What you can do here:</h3>
            <ul style="list-style-type: none;">
                <li> Explore different pages</li>
                <li> Learn about Flask basics</li>
                <li> Build your own projects</li>
            </ul>

            <p>Click below to learn more:</p>
            <a href="/about">Go to About Page</a>

            <footer style="margin-top: 40px;">
                <p>© 2026 My Flask wbesite by Mahir Dyan</p>
            </footer>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)