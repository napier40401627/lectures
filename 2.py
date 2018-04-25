from flask import Flask, render_template
app = Flask(__name__)
@app.route('/inherits/')
def inherits():
    return render_template('base.html')

@app.route('/inherits/one/')
def inherits_one():
    return render_template('in1.html')

@app.route('/inherits/two')
def inherits_two():
    return render_template('in2.html')
if __name__ == "__main__":
    app.run(host ='0.0.0.0', port=1234, debug = True )
