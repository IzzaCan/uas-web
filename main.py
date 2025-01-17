from flask import Flask, render_template, request, redirect, url_for, flash
from DB_Operations import connect, insert_kuliner, fetch_all_kuliners, update_kuliner, delete_kuliner, fetch_kuliner_by_id



app = Flask(__name__)
app.secret_key = "your_secret_key"

# Route untuk halaman utama (index.html)
@app.route('/')
def index():
    kuliner_list = fetch_all_kuliners()
    return render_template('index.html', kuliner_list=kuliner_list)

# Route untuk menambah kuliner (tambah_kuliner.html)
@app.route('/add_kuliner', methods=["POST", "GET"])
def add_kuliner():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        # Insert kuliner ke database
        insert_kuliner(name, description, price)
        flash('Kuliner Added Successfully!')
        return redirect("/#kuliner")
    return render_template('add_kuliner.html')

# Route untuk halaman edit kuliner (edit_kuliner.html)
@app.route('/edit_kuliner/<id>', methods=["GET", "POST"])
def edit_kuliner(id):
    kuliner = fetch_kuliner_by_id(id)
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        # Update kuliner
        update_kuliner(id, name, description, price)
        flash('Kuliner Updated Successfully!')
        return redirect("/#kuliner")
    return render_template('edit_kuliner.html', kuliner=kuliner)

# Route untuk menghapus kuliner
@app.route('/delete_kuliner/<id>', methods=["GET", "POST"])
def delete_kuliner_route(id):
    delete_kuliner(id)
    flash('Kuliner Deleted Successfully!')
    return redirect("/#kuliner")

if __name__ == '__main__':
    app.run(debug=True)
