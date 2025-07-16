from flask import Flask,render_template,request
app=Flask(__name__)
@app.route('/')
def hello():
    return render_template('form.html')
@app.route('/submit',methods=['POST'])
def submit():
    username= request.form['usname']
    return render_template('results.html',name=username)
if __name__=='__main__':
    app.run(debug=True)