from flask import Flask, render_template, request, jsonify
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/save-data', methods=['POST'])
def save_data():
    data = request.get_json()
    vards = data.get('vards')
    klikski = data.get('klikski')
    laiks = data.get('laiks')
    datums = data.get('datums')

    # Save the data to name.txt
    with open("name.txt", "a") as f:
        f.write(f"{vards},{klikski},{laiks},{datums}\n")

    # Append the data to result.json
    with open("result.json", "r+") as f:
        result_data = json.load(f)
        result_data.append({
            "vards": vards,
            "klikski": klikski,
            "laiks": laiks,
            "datums": datums
        })
        f.seek(0)
        json.dump(result_data, f, indent=4)

    return jsonify({"message": "Data saved successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
