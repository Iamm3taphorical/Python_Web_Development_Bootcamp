from flask import Flask, render_template_string, request

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>My Template Website</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: linear-gradient(to right, #4facfe, #00f2fe);
            text-align: center;
            padding-top: 80px;
            color: #333;
        }
        .container {
            background: white;
            padding: 30px;
            border-radius: 12px;
            width: 350px;
            margin: auto;
            box-shadow: 0 8px 20px rgba(0,0,0,0.2);
        }
        input {
            padding: 10px;
            width: 80%;
            margin-top: 10px;
            border-radius: 6px;
            border: 1px solid #ccc;
        }
        button {
            padding: 10px 15px;
            margin-top: 10px;
            border: none;
            border-radius: 6px;
            background-color: #4facfe;
            color: white;
            cursor: pointer;
        }
        button:hover {
            background-color: #00c6ff;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Welcome, {{ name }}</h1>
        <p>This is a dynamic Flask website using templates.</p>

        <form method="GET">
            <input type="text" name="name" placeholder="Enter your name">
            <br>
            <button type="submit">Update Name</button>
        </form>

        <p style="margin-top:20px;">Try changing your name above!</p>
    </div>
</body>
</html>
"""

@app.route('/')
def home():
    name = request.args.get("name", "Student")
    return render_template_string(HTML_TEMPLATE, name=name)

if __name__ == '__main__':
    app.run(debug=True)