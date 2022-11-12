from flask import Flask
from flask import render_template
from PIL import Image
from flask import request
import ocr_task

app = Flask(__name__)


@app.route("/")
def index_show():
    return render_template("index.html")


@app.route("/upload", methods=["POST"])
def upload_show():
    image = request.files["out_file"]
    if image == "":
        txt = "読み取りエラー"
    txt = ocr_task.make(image)

    return render_template("index.html", txt=txt)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001, debug=True)
