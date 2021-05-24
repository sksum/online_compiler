from flask import Flask,request
import compiler_service
app = Flask(__name__)

@app.route("/")
def hello_world():
    return """
<center>
<h1>You shouldn't be here ... </h1> 
<div class="tenor-gif-embed" data-postid="19877831" data-share-method="host" data-width="20%" data-aspect-ratio="1.0"></div>
<img id = "shushImage" src="https://thumbs.gfycat.com/SomberVacantLadybug-max-1mb.gif" height = "40%" style="display:none;"  />
<button id="butt" onClick=' 
let x  = () => {
    alert("Piss OFF !!");
    document.getElementById("shushImage").style.display = "block";
    return false;
}
x();
return false;
'
> SHUSH !</button>
</center>
    """

@app.route('/submit', methods=['POST'])
def submit_for_compilation():
    if request.method == 'POST':
        lang = request.form['lang']
        code = request.form['code']
        _input = request.form['input']
        a = (compiler_service.compile(lang, code, _input))
        return a

@app.route('/check/<sid>', methods=['GET'])
def check_result(sid):
    if request.method == 'GET':
        return compiler_service.get_output(sid)
