# Download the helper library from https://www.twilio.com/docs/python/install
import os
from flask import Flask, request, jsonify, render_template, redirect, url_for
from twilio.rest import Client


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('home.html')


# Define Verify_otp() function
@app.route('/login' , methods=['POST'])
def verify_otp():
    username = request.form['username']
    password = request.form['password']
    mobile_number = request.form['number']

    if username == 'verify' and password == '12345':   
        account_sid = 'AC9e5a2b71e58ac84b9470813b53003f0d'
        auth_token = '35c639064a29c815464d5202cefe8e68'
        client = Client(account_sid, auth_token)

        verification = client.verify \
            .services('ISa6b1a3a19808e13a93cb344e77363d18') \
            .verifications \
            .create(to=mobile_number, channel='sms')

        print(verification.status)
        return render_template('otp_verify.html')
    else:
        return render_template('user_error.html')



@app.route('/otp', methods=['POST'])
def get_otp():
    print('processing')

    received_otp = request.form['received_otp']
    mobile_number = request.form['number']

    account_sid = 'AC9e5a2b71e58ac84b9470813b53003f0d'
    auth_token = '35c639064a29c815464d5202cefe8e68'
    client = Client(account_sid, auth_token)
                                            
    verification_check = client.verify \
        .services('ISa6b1a3a19808e13a93cb344e77363d18') \
        .verification_checks \
        .create(to=mobile_number, code=received_otp)
    print(verification_check.status)

    if verification_check.status == "pending":
        return render_template('otp_error.html')    # Write code here
    else:
        return redirect("https://collab-document-thingy.onrender.com")


if __name__ == "__main__":
    app.run()

