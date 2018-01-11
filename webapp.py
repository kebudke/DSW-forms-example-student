from flask import Flask, url_for, render_template, request

app = Flask(__name__) #__name__ = "__main__" if this is the file that was run.  Otherwise, it is the name of the file (ex. webapp)

@app.route('/', methods=['POST'])
def render_main():
    return render_template('home.html')

@app.route('/response', methods=['POST', 'GET'])
def render_response():
    color = request.form['color']
    if color == 'turquoise':
        reply = "That's my favorite color, too!"
    else:
        reply = "My favorite color is turquoise."
    return render_template('response.html', response = reply)   
    
if __name__=="__main__":
    app.run(debug=False, port=54321)
