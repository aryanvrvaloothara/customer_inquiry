from twilio.rest import Client


def send_otp(mobile_number, otp):
    # Your Account SID from twilio.com/console
    account_sid = "ACed5e022828cfdb481c7e108b9b5b25c3"
    # Your Auth Token from twilio.com/console
    auth_token = "cc088fc69d9ceb281b2900f6c5df6956"

    client = Client(account_sid, auth_token)
    print(client)

    message = client.messages.create(
        to="+91" + str(mobile_number),
        from_="+19704364968",
        body="Mobile number otp verification is {otp}".format(otp=otp))

    print(message.sid)
    return None
