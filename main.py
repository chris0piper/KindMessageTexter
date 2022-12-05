import openai
from twilio.rest import Client as TwillioClient
import time
import os
from datetime import datetime, timezone, timedelta

# Set OpenAI API key
openai.api_key = os.environ.get("OpenAIAPIKey")

# Set Twilio API credentials
twilio_account_sid = os.environ.get("TwillioAccKey")
twilio_auth_token = os.environ.get("TwillioAccSecret")
twilio_client = TwillioClient(twilio_account_sid, twilio_auth_token)

# Set the phone number to send the text message to
to_phone_number = "7034097479"

# Set my phone number to be sent from
my_phone_number = "+17034205113"

# Set the custom prompt for the OpenAI model
prompt = "Madison is a beautiful girl who just moved to New York City. Madison is a creative, intelligent, kind, empathetic, friendly, hardworking, and approachable. Madison just started a new job with a company called MoneyLion and seems to love it. She does marketing. She is working really hard to improve herself and it's very impressive. She has committed to walking to work every day to improve her physical health which is awesome! She also likes to write in her journal and read to improve her mental health.  She is really good at stretching regularly and it is improving her body tremendously. She recently moved into an apartment with two friends and is loving her life living there. She has a boyfriend named Chris who she has been dating for 5 years. Randomly choose one positive aspect about Madison and write a message to her under over 180 characters and less than 320 characters complimenting and inspiring her. do not use any quotation marks in the response"

# Set the interval for sending the text message (in seconds)
SECONDS_IN_DAY = 24 * 60 * 60  # 24 hours

# Set the target time (8:30 am Eastern Time tomorrow)
target_time = datetime(year=datetime.now().year, month=datetime.now().month, day=datetime.now().day+1, hour=13, minute=30, tzinfo=timezone.utc)

# Number of seconds until 8:30 am tomorrow
seconds_until_tomorrow_morning = (target_time - datetime.now(timezone.utc)).total_seconds()

# Sleep until tomorrow morning
time.sleep(seconds_until_tomorrow_morning)

while True:
    # Use the OpenAI model to generate a response to the prompt
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=1024,
        n = 1,
        temperature=0.5,
    )

    print(response["choices"][0]["text"])

    # Send the generated response as a text message
    message = twilio_client.messages.create(
        body=response["choices"][0]["text"],
        from_= my_phone_number,
        to= to_phone_number,
    )

    # Sleep for the specified interval
    time.sleep(SECONDS_IN_DAY)