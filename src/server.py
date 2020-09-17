from flask import Flask, render_template, url_for, redirect, request
from random import randint
from Sequencinator import *

app = Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')


@app.route('/sequence')
def sequence():
    return render_template('sequence.html')

@app.route('/generate/', methods=['POST'])
def generateSequence():
    dna = Sequencinator('Server Generated Object')
    if request.form['number'].isdigit() == True:
        number = int(request.form['number'])
        gen = dna.generate_sequence(number)
    else:
        gen = dna.generate_sequence()
    return render_template('sequence.html', strand=gen)

@app.route('/protein/', methods=['POST'])
def sequenceProtein():
    protein = Sequencinator('Custom Object')
    strand = request.form['dna']
    final = protein.translate_protein(strand)
    return render_template('sequence.html', protein=final)

if __name__ == '__main__':
    app.run(debug=True)
