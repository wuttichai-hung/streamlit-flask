from flask import Flask, request, jsonify
from werkzeug.utils import secure_filename
app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return jsonify(resutl=0, msg="Not found image", status="fail")
        f = request.files['file']
        file_path = secure_filename(f.filename)
        f.save(file_path)

        # process data
        result = 1
        return jsonify(resutl=result, msg="", status="success")

    if request.method == 'GET':
        return "Hello World"


if __name__ == '__main__':
    app.run(debug=True)
