# webhook-cb-page
Create a webhook callback site to catch the webhook payloads

# Set up Environment
```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

# Run App
```
python app.py
```
App will listen on localhost:5000

# Make the App public
You will need to download/register ngrok, find download link here https://ngrok.com/

Follow the instruction once you log in, once your ngrok is ready, run:
```
./ngrok http 5000
```
Copy the ngrok HTTPS URL to your Dashboard/Webhooks as the Callback URL, you will now receive webhook payloads!
