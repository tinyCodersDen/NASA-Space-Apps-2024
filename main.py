# Importing Modules:
from flask import *

# Flask Setup:
app = Flask(__name__)

# Homepage:
@app.route('/',methods=['GET','POST'])
def home():
    return render_template('main.html')

# Info Page:
@app.route('/info',methods=['GET','POST'])
def info():
    return render_template('info.html')

# SDG Page:
@app.route('/sdg',methods=['GET','POST'])
def SDG():
    return render_template('sdg.html')

# Solution Page:
@app.route('/solution',methods=['GET','POST'])
def sdg():
    return render_template('solution.html')

# Ending the script
if __name__=='__main__':
    app.run(debug=True)