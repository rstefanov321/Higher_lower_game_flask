from flask import Flask
import random

app = Flask(__name__)


@app.route("/")
def heading_page():
    return "<h1> Guess a number between 0 and 9</h1>" \
           "<p></p>" \
           "<img src='https://media4.giphy.com/media/LMn7PRCVDcnvO/giphy.webp?cid" \
           "=ecf05e47m65t6aatm14ifcpyk8hmz76i29xv7wg2l1za2vb8&rid=giphy.webp&ct=g'>"


random_number = random.randint(0, 9)
colors = ["red", "orange", "yellow", "green", "blue", "purple",
          "pink", "brown", "gray", "black", "white"]


@app.route(f'/<int:num>')
def check_num(num):
    if num == random_number:
        return f"<h1 style='color:{colors[num]}'> Bang on! </h1>" \
               f"<img src='https://media.giphy.com/media/4T7e4DmcrP9du/giphy.gif'>"
    elif num < random_number:
        return f"<h1 style='color:{colors[num]}'> Too low my friend, go up! </h1>" \
               f"<img src='https://media.giphy.com/media/jD4DwBtqPXRXa/giphy.gif'>"
    else:
        return f"<h1 style='color:{colors[num]}'> Too high man, go down! </h1>" \
               f"<img src='https://media.giphy.com/media/3o6ZtaO9BZHcOjmErm/giphy.gif'>"


if __name__ == "__main__":
    app.run(debug=True)
