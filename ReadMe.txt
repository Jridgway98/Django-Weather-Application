To begin, first extract the files contained in the .zip file.
Next, be sure that you have the latest version of Python installed. Python is required to operate Django. It can be found here: https://www.python.org/downloads/
Once you have downloaded and installed the latest version of Python, we need to ensure that we have the latest version of pip, which will be used to install Django. Download it here: python get-pip.py
Finallly, we are ready to install Django. Use this command in the console to finish installing Django: python -m pip install Django
(Note: if the above command doesn't work properly, try using python3 instead,)
Once Django is installed, we need to run the web server to access the application.
Change directories within the console to .../myProject 
Now enter the following into the console: python(3) manage.py runserver
This should start Django's built-in web server, which should now allow us to access the web application in a web browser.
In your browser's search bar, enter: http://127.0.0.1:8000/

This should direct you to the homepage of the web application from where the rest of the application will be accessible.
In order to end the server running press ctr+c on the keyboard.

Enjoy!!