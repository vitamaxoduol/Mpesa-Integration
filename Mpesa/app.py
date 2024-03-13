from flask import Flask, jsonify
from flask_mpesa import MpesaAPI
from apis.auth import MpesaBase
# import os




app = Flask(__name__)


mpesa_api =MpesaAPI(app, name='mpesa_api_blueprint')
# mpesa_api.init_app(app)

# Instantiate MpesaBase with my CONSUMER_KEY and CONSUMER_SECRET
mpesa = MpesaBase()





@app.route('/auth/get-access-token')
def get_access_token():
    # Calling the get_access_token to fetch the access token
    access_token = mpesa.get_access_token()
    if access_token:
        return jsonify({"access_token": access_token}), 200
    else:
        return jsonify({"error": "Failed to fetch access token"}), 500






if  __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0",)

