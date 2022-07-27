from flask import Flask, redirect, request, render_template, url_for


app = Flask( __name__, template_folder='templates', templates="home.html", static_folder='static'
)

@app.route('product.html')
def product.html ():
	return render_template("product.html")

if __name__ == "__main__":
    app.run(debug=True)


@app.route('cart.html')
def cart.html ():
	return render_template("cart.html")

if __name__ == "__main__"
	app.run(debug=true)
	