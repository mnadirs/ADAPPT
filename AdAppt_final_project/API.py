from flask import Flask, request, jsonify, render_template
import find_channels
import BERT_implemenntation
import compare

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict', methods=['POST'])
def predict():
    word = request.form["Keyword"]
    print(word)
    BERT_implemenntation.bert(str(word))
    category = compare.category_name()
    channels = find_channels.find_title("Sports")


    return render_template('home.html', prediction_text='Recommended channel is {}'.format(word))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='3030', debug=True)

