from twilio.rest import Client


def send_otp(mobile_number, otp):
    # Your Account SID from twilio.com/console
    account_sid = "ACed5e022828cfdb481c7e108b9b5b25c3"
    # Your Auth Token from twilio.com/console
    auth_token = "138aedcf164aa9f8b6187a8fc30128e4"

    client = Client(account_sid, auth_token)
    print(client)
    to_number = "+91" + str(mobile_number)
    print(to_number)
    message = client.messages.create(
        to=to_number,
        from_="+19704364968",
        body="Mobile number otp verification is {otp}".format(otp=otp))

    print(message.sid)
    return None
