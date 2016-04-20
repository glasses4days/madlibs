from random import choice

from flask import Flask, render_template, request


# "__name__" is a special Python variable for the name of the current module
# Flask wants to know this to know what any imported things are relative to.
app = Flask(__name__)

AWESOMENESS = [
    'awesome', 'terrific', 'fantastic', 'neato', 'fantabulous', 'wowza', 'oh-so-not-meh',
    'brilliant', 'ducky', 'coolio', 'incredible', 'wonderful', 'smashing', 'lovely']

# global_person =""

@app.route('/')
def start_here():
    """Homepage."""

    return "Hi! This is the home page."


@app.route('/hello')
def say_hello():
    """Save hello to user."""

    return render_template("hello.html")


@app.route('/greet')
def greet_person():
    """Greet user."""

    person = request.args.get("person")
    # global_person = person

    compliment = choice(AWESOMENESS)

    return render_template("compliment.html",
                           person=person,
                           compliment=compliment)

@app.route('/game')
def show_game_form():
    """Allow user to play game"""

    answer = request.args.get("game-response")

    if answer == "yes":
        return render_template("game.html")

    else:
        return render_template("goodbye.html")

@app.route('/madlib')
def show_madlib():
    """Create madlib game"""

    person_name = request.args.get("person_name")
    color = request.args.get("color")
    noun = request.args.get("noun")
    adjective = request.args.get("adjective")
    # person = global_person


    return render_template("madlib.html",
                            # person=person, 
                            person_name=person_name, 
                            color=color, 
                            noun=noun, 
                            adjective=adjective)


if __name__ == '__main__':
    # debug=True gives us error messages in the browser and also "reloads" our web app
    # if we change the code.
    app.run(debug=True)
