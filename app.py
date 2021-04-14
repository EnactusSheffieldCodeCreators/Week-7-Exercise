# Flask server setup
from flask import Flask
app = Flask(__name__, template_folder='views')

# Other useful flask functions
from flask import request, render_template, redirect

# Home Route
@app.route("/", methods=["GET"])
def render_blank_grid():
    board = generate_blank_board()
    session['board'] = board
    return render_template("board.html", board=board, current_piece="x")

# Helper Functions
def generate_blank_board():
    return [[None for y in range(3)] for x in range(3)]

# Run server when the python script is called.
if __name__ == "__main__":
    app.run(debug=True)