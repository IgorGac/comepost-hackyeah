App is live and accesible here:
http://srv12.mikr.us:40118/


To run this app in your localhost:
1. Ensure you have python with pip installed
2. Install dependencies using pip and: pip install flask flask-sqlalchemy flask-login requests beautifulsoup4
3. Set up environment variable in comepost-hackyeah directory using: 
	- $env:FLASK_APP = "comepost" - in Windows
	= export FLASK_APP-"compost" - for Linux
4. Run server using "flask run", or "python -m flask run"