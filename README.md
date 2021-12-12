# WHATSAPP_BOT
A Whatsapp bot built with Python Flask + Twilio API 
If user gives any text , or songs or video then it searches in youtube using API and returns the first link to the user in whatsapp

1.	Python environment  
2.	Download all necessary package – flask , requests , twilio   #pip install flask requests Twilio
3.	Ngrok – download it ( used for converting the flask to a url which communicates with twillio )

CREATE AN ACCOUNT ON TWILLIO

installation of ngrok to convert the flask app to a url which connects to twillio
download ngrok and unzip and run..
signup in ngrok website where u download to get authorized token in ngrok..


In command prompt (open that ngrok.exe file) type ngrok authtoken [your token]

Now run the python flask code .....
Open new command prompt run ngrok http 5000 to allocate a temporary public domain that redirects HTTP requests to our local port 5000.
  
Note the lines beginning with “Forwarding”. These show the public URL that ngrok uses to redirect requests into our service. What we need to do now is tell Twilio to use this URL to send incoming message notifications.

Go back to the Twilio Console, click on Programmable Messaging, then on Settings, and finally on WhatsApp Sandbox Settings. Copy the https:// URL from the ngrok output and then paste it on the “When a message comes in” field. Since our chatbot is exposed under the /bot URL, append that at the end of the root ngrok URL. Make sure the request method is set to HTTP Post. Don’t forget to click the red Save button at the bottom of the page

(before setup the sandbox in twilio – connects your number to twilio)


Keep in mind that when using ngrok for free there are some limitations. In particular, you cannot hold on to an ngrok URL for more than 8 hours, and the domain name that is assigned to you will be different every time you start the ngrok command. You will need to update the URL in the Twilio Console every time you restart ngrok.
