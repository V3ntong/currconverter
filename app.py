import os
import requests
from flask import Flask, render_template, request
from dotenv import load_dotenv

# Load variables from .env
load_dotenv()
API_KEY = os.getenv('apikey')
print(f"DEBUG: My key is {API_KEY}")

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    result = None
    
    
    if request.method == 'POST':
        amount = request.form.get('amount')
        target = request.form.get('to_currency')
        
        # API URL for ExchangeRate-API (v6)
        url = f"https://v6.exchangerate-api.com/v6/{API_KEY}/pair/USD/{target}/{amount}"
        
        try:
            response = requests.get(url)
            data = response.json()
            
            if data.get('result') == 'success':
                converted = data['conversion_result']
                # Formatting the output nicely
                result = f"${float(amount):,.2f} = {converted:,.2f} {target}"
            else:
                result = "Error: Invalid API response."
        except Exception as e:
            result = "Error: Connection to API failed."

    return render_template('index.html', result=result)

if __name__ == '__main__':
    app.run(debug=True)