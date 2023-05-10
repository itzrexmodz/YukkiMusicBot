import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
   return 'Hello, World!'
os.system("curl -sL https://deb.nodesource.com/setup_18.x | -E bash -")
os.system("pip3 install -U -r requirements.txt && nohup python3 -m YukkiMusic &")
