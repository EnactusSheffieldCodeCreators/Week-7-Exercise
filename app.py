#AST to help with strings.
import ast

# Flask server setup
from flask import Flask
app = Flask(__name__, template_folder='views')

# Other useful flask functions
from flask import request, render_template, redirect, session

# Home Route
@app.route("/", methods=["GET"])
def render_blank_grid():
    board = generate_blank_board()
    return render_template("board.html", board=board, current_piece="x")

@app.route("/", methods=["POST"])
def play_move():
    location = list(request.form.get("place-selection"))
    coords = [int(location[0]), int(location[1])]
    app.logger.debug(request.form.get("place-selection"))
    board = ast.literal_eval(request.form.get("board"))
    piece = request.form.get("current-piece")

    # Place piece
    board[coords[0]][coords[1]] = piece

    # Flip piece
    if piece == "x":
        piece = "o"
    else:
        piece = "x"
    
    # Re render the page
    return render_template("board.html", board=board, current_piece=piece)

# Helper Functions
def generate_blank_board():
    return [[None for y in range(3)] for x in range(3)]

# Run server when the python script is called.
if __name__ == "__main__":
    app.run(debug=True)