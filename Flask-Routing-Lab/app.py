from flask import Flask, redirect, request, render_template, url_for


app = Flask( __name__, template_folder='templates', templates="home.html", static_folder='static'
)

@app.route('product.html')
def product.html ():
	return render_template("product.html")

<div>
	<a href=“{{ url_for(‘product.html’) }}”>product</a>
</div> 



<div>
	<a href=“{{ url_for(‘home.html’) }}”> home page</a>
</div> 




if __name__ == "__main__":  # Makes sure this is the main process
    app.run(debug=True)
