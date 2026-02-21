from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        # Here you can process form data
        return render_template('success.html')
    else:
        return render_template('register.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
