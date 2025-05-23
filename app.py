import os
from flask import Flask
from config import Config
from Controller.user_controller import UseControler

app = Flask(__name__, template_folder= os.path.join('View'))
app.config.from_object(Config)

app.add_url_rule('/', 'index', UseControler.index)

if __name__ == '__main__':
    app.run(debug=True);
    
