from flask import Flask, redirect , render_template , request , session , flash

import pickle

app=Flask(__name__)

model = pickle.load(open("savemodel.sav",'rb'))


@app.route("/")
def home():
    return render_template("lap.html", **locals())


@app.route("/predict", methods=["GET","POST"])
def predict():
    processor_speed	= float(request.form["processor_speed"])
    ram_size = float(request.form["ram_size"])	
    storage_capacity = float(request.form["storage_capacity"])	
    screen_size	= float(request.form["screen_size"])
    weight		= float(request.form["weight"])
    brand_acer	= float(request.form["brand_acer"])
    brand_asus	= float(request.form["brand_asus"])
    brand_dell	= float(request.form["brand_dell"])
    brand_hp	= float(request.form["brand_hp"])
    brand_lenovo= float(request.form["brand_lenovo"])

    result= model.predict([[processor_speed, ram_size, storage_capacity, screen_size, weight, brand_acer, brand_asus, brand_dell,brand_hp,brand_lenovo]])[0]
    return render_template("lap.html", **locals())







if __name__ == '__main__':
    app.run(debug=True)