from flask import Flask, jsonify, render_template, request, session
from flask_sqlalchemy import SQLAlchemy
from select import select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import Integer, String, Boolean, func, column
from sqlalchemy.sql.functions import random
import random
import os
from dotenv import load_dotenv
load_dotenv()
api_key = os.environ.get("API_KEY")
app = Flask(__name__)

# CREATE DB
class Base(DeclarativeBase):
    pass
# Connect to Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cafes.db'
db = SQLAlchemy(model_class=Base)
db.init_app(app)


# Cafe TABLE Configuration
class Cafe(db.Model):
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String(250), unique=True, nullable=False)
    map_url: Mapped[str] = mapped_column(String(500), nullable=False)
    img_url: Mapped[str] = mapped_column(String(500), nullable=False)
    location: Mapped[str] = mapped_column(String(250), nullable=False)
    seats: Mapped[str] = mapped_column(String(250), nullable=False)
    has_toilet: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_wifi: Mapped[bool] = mapped_column(Boolean, nullable=False)
    has_sockets: Mapped[bool] = mapped_column(Boolean, nullable=False)
    can_take_calls: Mapped[bool] = mapped_column(Boolean, nullable=False)
    coffee_price: Mapped[str] = mapped_column(String(250), nullable=True)

    def to_dict(self):
        return {column.name: getattr(self,column.name) for column in self.__table__.columns }

with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/random",methods=['GET'])
def get_random_cafe():
    all_record= Cafe.query.all()
    random_cafe = random.choice(all_record)
    return  jsonify(cafe = {
        "id" : random_cafe.id,
        "name" : random_cafe.name,
        "map_url" : random_cafe.map_url,
        "img_url" : random_cafe.img_url,
        "location":random_cafe.location,
        "has_sockets": random_cafe.has_sockets,
        "has_toilet": random_cafe.has_toilet,
        "has_wifi": random_cafe.has_wifi,
        "can_take_calls": random_cafe.can_take_calls,
        "seats" : random_cafe.seats,
        "coffee_price" : random_cafe.coffee_price

    })
@app.route("/all")
def get_all_cafes():
    result =db.session.execute(db.select(Cafe).order_by(Cafe.name))
    all_cafe = result.scalars().all()
    return jsonify(cafes = [cafe.to_dict() for cafe in all_cafe])

@app.route("/search")
def get_cafe_at_location():
    query_location = request.args.get("loc")
    result = db.session.execute(db.select(Cafe).where(Cafe.location == query_location))
    all_cafe = result.scalars().all()
    if all_cafe:
        return jsonify(cafes=[cafe.to_dict() for cafe in all_cafe])
    else:
        return jsonify(error={"Not Found": "Sorry, we don't have a cafe at that location."}), 404

@app.route("/add", methods=["POST"])
def post_new_cafe():
    new_cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        has_sockets=bool(request.form.get("sockets")),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        can_take_calls=bool(request.form.get("calls")),
        seats=request.form.get("seats"),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(new_cafe)
    db.session.commit()
    return jsonify(response={"success": "Successfully added the new cafe."})
@app.route("/update_price/<int:cafe_id>",methods=['PATCH'])
def update_price(cafe_id):
    query_price = request.args.get("new_price")
    cafe = db.get_or_404(Cafe, cafe_id)
    # cafe = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
    if cafe:
        cafe.coffee_price = query_price
        db.session.commit()
        return jsonify(response={"success": "Successfully updated the price."})
    else:
        return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}),404
@app.route("/report_closed/<int:cafe_id>",methods = ['DELETE'])
def delete_cafe(cafe_id):
    Api_key = request.args.get("Api_key")
    if Api_key == api_key:
        cafe_delete = db.session.execute(db.select(Cafe).where(Cafe.id == cafe_id)).scalar()
        # cafe_delete = db.get_or_404(Cafe, cafe_id)
        if cafe_delete:
            db.session.delete(cafe_delete)
            db.session.commit()
            return jsonify(response={"success": "Successfully deleted the cafe."})
        else:
            return jsonify(error={"Not Found": "Sorry a cafe with that id was not found in the database."}), 404
    else:
        return jsonify(error={"Not Found": "Sorry that's not allowed. Make sure you have correct api key."}), 403


if __name__ == '__main__':
    app.run(debug=True)

      
