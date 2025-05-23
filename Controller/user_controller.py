from flask import render_template

class UseControler:
    @staticmethod
    def index():
        return render_template('index.html')
    
