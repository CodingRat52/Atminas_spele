from flask import Flask, render_template, request, jsonify
import json
from datubaze import get_top_results, pievienot
app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/game')
def game():
    return render_template("game.html")

@app.route('/save-data', methods=['POST'])
def about():
    return render_template ("about.html")
@app.route('/topData', methods={'GET'})
def topdata():
    try:
        top_rezultati = get_top_results()
        top_5 =  sorted (top_rezultati, key=lambda x : (x['klikski'], x['laiks']))[:5]
        return jsonify(top_5), 200
    except Exception:
        return jsonify({'status': 'error'}), 500
@app.route('/pievienot-rezultatu', methods=['POST'])
def pievienot_rezultatu():
    dati = request.json
    try:
        pievienot(dati)
        top_5 = sorted(get_top_results(), key=lambda x : (x['klikski'], x['laiks']))[:5]
        with open('result.json', 'w', encoding='utf-8') as fail:
            json.dump(top_5, fail, ensure_ascii=False, indent=4)
        return jsonify ({'status': 'success'}), 200
    except Exception:
        return jsonify ({'status': 'error'}), 500

    
if __name__ == '__main__':
    app.run(debug=True)
