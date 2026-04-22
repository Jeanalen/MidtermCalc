from flask import Flask, render_template_string, request

app = Flask(__name__)

# The HTML page that will show in the browser
HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Integrity Check Program</title>
    <style>
        body { font-family: sans-serif; text-align: center; margin-top: 50px; background: #f4f4f4; }
        .container { background: white; padding: 20px; display: inline-block; border-radius: 10px; shadow: 0 4px 6px rgba(0,0,0,0.1); }
        input { padding: 10px; font-size: 16px; border: 1px solid #ccc; border-radius: 5px; }
        button { padding: 10px 20px; font-size: 16px; background: #0070f3; color: white; border: none; border-radius: 5px; cursor: pointer; }
        .success { color: green; font-weight: bold; }
        .error { color: red; font-weight: bold; }
    </style>
</head>
<body>
    <div class="container">
        <h1>System Fundamentals</h1>
        <p>Enter a number to verify its integrity:</p>
        
        <form method="POST">
            <input type="text" name="val" placeholder="Enter something..." autofocus>
            <button type="submit">Check</button>
        </form>

        {% if result %}
            <hr>
            <div class="{{ 'success' if status == 'SUCCESS' else 'error' }}">
                <h3>[RESULT]: {{ status }}</h3>
                <p>{{ message }}</p>
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route('/', methods=['GET', 'POST'])
def integrity_check():
    result = False
    status = ""
    message = ""
    
    if request.method == 'POST':
        result = True
        val = request.form.get('val', '').strip()

        # 1. Empty Input Check
        if val == "":
            status = "INVALID"
            message = "Error: Empty inputs are NOT PERMITTED."
        
        # 2. Integrity Check (Special Characters, Letters, and Decimals)
        elif not val.lstrip('-').isdigit():
            status = "INVALID"
            message = "Error: Special characters, letters, or spaces detected."
        
        # 3. Valid Input Confirmation
        else:
            status = "SUCCESS"
            message = f"Input '{val}' is a valid integer."

    return render_template_string(HTML_TEMPLATE, result=result, status=status, message=message)
