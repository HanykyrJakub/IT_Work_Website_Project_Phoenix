from flask import Flask, request, jsonify
from recomnendations import get_recommendations

app = Flask(__name__)

# Testovací endpoint
@app.route('/')
def home():
    return "Vítejte na backendu eshopového chatbota!"

# API endpoint pro doporučení
@app.route('/recommend', methods=['POST'])
def recommend():
    data = request.json
    user_id = data.get('user_id')

    recommend_products = get_recommendations(user_id)

    return jsonify({
        'user_id': user_id,
        'recommendations': recommend_products
    })

if __name__ == '__main__':
    app.run(debug=True)
