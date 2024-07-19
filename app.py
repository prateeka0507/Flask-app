from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process_button', methods=['POST'])
def process_button():
    button = request.form['button']
    if button == 'button1':
        message = "Button 1 was clicked!"
    elif button == 'button2':
        message = "Button 2 was clicked!"
    elif button == 'button3':
        message = "Button 3 was clicked!"
    else:
        message = "Unknown button clicked!"
    return render_template('output.html', message=message)

if __name__ == '__main__':
    app.run(debug=True)
