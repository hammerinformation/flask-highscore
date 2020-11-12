from flask import Flask, request, render_template
import os
app = Flask(__name__)

# @hammerinformation

highScore = 0

def newText(fileName,value):
    f=open(fileName,"w");
    f.write(str(value))


def readText(fileName):
    if os.path.isfile(fileName):
        f = open(fileName, "r+")
        highScore=f.read()
        return highScore
       

@app.route('/')
def index():
    return 'Hello'



@app.route('/score', methods=["GET", "POST"])
def high_score():
    if request.method == "POST":
        score = request.form.get("score")
        _s = score
        global highScore
        highScore=readText("highscore.txt")

        if(int(score) > int(highScore)):
            highScore = int(score)
            newText("highscore.txt",highScore)
            highScore=readText("highscore.txt")
            return 'high score :' + str(highScore)

        else:
            return 'high score :' + str(highScore)
    else:
        return 'high score :' + str(highScore)


if __name__ == "__main__":
    app.run()
