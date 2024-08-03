from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

# In-memory storage for user details
user_details = []

# HTML template with styling
form_template = '''
<!doctype html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>User Details Form</title>
    <style>
      body {
        font-family: Arial, sans-serif;
        background-color: #f4f4f9;
        color: #333;
        margin: 0;
        padding: 0;
        display: flex;
        flex-direction: column;
        align-items: center;
      }
      h1, h2 {
        color: #0056b3;
      }
      .container {
        width: 80%;
        max-width: 600px;
        margin: 20px auto;
        padding: 20px;
        background: #fff;
        box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        border-radius: 8px;
      }
      form {
        margin-bottom: 20px;
      }
      label {
        display: block;
        margin-bottom: 8px;
      }
      input[type="text"], input[type="email"] {
        width: calc(100% - 22px);
        padding: 10px;
        margin-bottom: 20px;
        border: 1px solid #ccc;
        border-radius: 4px;
      }
      input[type="submit"] {
        background-color: #0056b3;
        color: #fff;
        border: none;
        padding: 10px 20px;
        border-radius: 4px;
        cursor: pointer;
        font-size: 16px;
      }
      input[type="submit"]:hover {
        background-color: #004494;
      }
      ul {
        list-style-type: none;
        padding: 0;
      }
      li {
        background: #e9ecef;
        margin-bottom: 10px;
        padding: 10px;
        border-radius: 4px;
      }
    </style>
  </head>
  <body>
    <div class="container">
      <h1>Welcome to My DevOps World</h1>
      <form action="/submit" method="post">
        <label for="name">Name:</label>
        <input type="text" id="name" name="name" required>
        <label for="email">Email:</label>
        <input type="email" id="email" name="email" required>
        <input type="submit" value="Submit">
      </form>
      <h2>Stored User Details:</h2>
      <ul>
        {% for user in users %}
          <li>{{ user['name'] }} - {{ user['email'] }}</li>
        {% endfor %}
      </ul>
    </div>
  </body>
</html>
'''

@app.route('/')
def index():
    return render_template_string(form_template, users=user_details)

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form.get('name')
    email = request.form.get('email')
    if name and email:
        user_details.append({'name': name, 'email': email})
    return render_template_string(form_template, users=user_details)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
