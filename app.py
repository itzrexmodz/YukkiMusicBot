import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'

os.system("curl -sL https://deb.nodesource.com/setup_16.x -o /tmp/nodesource_setup.sh")
os.system("bash /tmp/nodesource_setup.sh")
os.system("pip3 install -U -r requirements.txt && nohup python3 -m YukkiMusic &")
