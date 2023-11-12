from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

# Sample data to simulate a database
transactions = []

@app.route('/')
def index():
    return render_template('index.html', transactions=transactions)

@app.route('/add_transaction', methods=['POST'])
def add_transaction():
    description = request.form.get('description')
    amount = float(request.form.get('amount'))
    transaction_type = request.form.get('transaction_type')

    transactions.append({
        'description': description,
        'amount': amount if transaction_type == 'income' else -amount,
        'type': transaction_type
    })

    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
