


from flask import Flask, request, render_template
import paymentwall
app = Flask(__name__)
# Initialize Paymentwall API keys



paymentwall.Paymentwall.configure(
    paymentwall.PublicKey('YOUR_PUBLIC_KEY'),
    paymentwall.PrivateKey('YOUR_PRIVATE_KEY')
)



@app.route('/checkout', methods=['POST', 'GET'])
def checkout():
    if request.method == 'POST':
        product_id = 'your_product_id'  #actual product ID
        amount = 50.0  #$
        #paymentwall widget
        widget = paymentwall.Widget(
            product_id,
            'user_email@example.com',  #user's email
            {
                'amount': amount,
                'currency_code': 'USD',
                'description': 'Product Description',
                'custom': 'Custom Parameter'  # Optional custom parameter
            }
        )
        return render_template('checkout.html', widget=widget.get_html_code())
    return 'Invalid request'

@app.route('/payment_success', methods=['POST'])
def payment_success():
    widget = paymentwall.Widget(request.form['widget'])
    if widget.verify_signature(request.form):
        transaction_id = request.form['id']
        return 'Payment Success! Transaction ID: {}'.format(transaction_id)
    else:
        return 'Payment Verification Failed'

if __name__ == '__main__':
    app.run()


