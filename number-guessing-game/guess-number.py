from flask import Flask, render_template, request
import random

app = Flask(__name__,
            template_folder="templates",
            static_folder="static")

random_number = random.randint(1, 101)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/guess-number', methods=['POST', 'GET'])
def guess_number():
    if request.method == 'POST':
        number = int(request.form.get('guess-input'))
        if number > random_number:
            message = 'Too high, guess again loser!'
        elif number < random_number:
            message = 'Too low, guess again fool!'
        else:
            message = 'You guessed right!!!'

        return render_template('index.html', message=message)


if __name__ == '__main__':
    app.run(debug=True)