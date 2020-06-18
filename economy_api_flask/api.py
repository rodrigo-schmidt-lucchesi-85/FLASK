from datetime import datetime
from sqlalchemy.sql import func
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from marshmallow_sqlalchemy import SQLAlchemySchema, auto_field
import os

app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))
# Database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    cpf = db.Column(db.Integer, unique=True, nullable=False)
    birthday_year = db.Column(db.Integer)

    def __init__(self, username, cpf, birthday_year):
        self.username = username
        self.cpf = cpf
        self.birthday_year = birthday_year


class UserSchema(SQLAlchemySchema):
    class Meta:
        model = User
        load_instance = True
    
    username = auto_field()
    cpf= auto_field()
    birthday_year= auto_field()

user_schema = UserSchema()
users_schema = UserSchema(many=True)



class Salary(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    date = db.Column(db.DateTime, nullable=False)
    cpf = db.Column(db.Integer, nullable=False) # Nao pode ser unico
    salary = db.Column(db.Float)
    discount = db.Column(db.Float)

    def __init__(self, date, cpf, salary, discount):
        self.date = date
        self.cpf = cpf
        self.salary = salary
        self.discount = discount


class SalarySchema(SQLAlchemySchema):
    class Meta:
        model = Salary
        load_instance = True
    
    date = auto_field()
    cpf= auto_field()
    salary= auto_field()
    discount= auto_field()

salaries_schema = SalarySchema(many=True)
salary_schema = SalarySchema()




@app.route('/users',methods=['GET'])
def get_all_users():
    try:
        data = User.query.all()
        dump_data = users_schema.dump(data)
        
        return jsonify({"msg":dump_data,
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})

@app.route('/users/<int:cpf>',methods=['GET'])
def get_user_by_cpf(cpf):
    try:
        
        user = User.query.filter_by(cpf=cpf).first()
        dump_data = user_schema.dump(user)
        
        return jsonify({"msg":dump_data,
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})



@app.route("/users/create", methods=["GET","POST"])
def create_new_user():
    try:
        data = request.get_json()
        username=data["username"]
        cpf=data["cpf"]
        birthday_year=data["birthday_year"]
        user = User(username,cpf,birthday_year)
        db.session.add(user)
        db.session.commit()
        dump_data = user_schema.dump(user)
        return jsonify({"msg":dump_data,
                        "status":200}) 
        
    except:
        return jsonify({"msg": "CPF existente",
                        "status":400})




@app.route('/users/delete/<int:cpf>',methods=["DELETE"])
def delete_user_by_cpf(cpf):
    try:
        print(cpf)
        user = User.query.filter_by(cpf=cpf).first()
        db.session.delete(user)
        db.session.commit()
        dump_data = user_schema.dump(user)
        
        return jsonify({"msg":f"Deleted cpf {cpf}",
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})

  
@app.route('/users/update/<int:cpf>', methods=['PUT'])
def update_user_by_cpf(cpf):
    try:
        user = User.query.filter_by(cpf=cpf).first()

        data = request.get_json()
        username=data["username"]
        cpf=data["cpf"]
        birthday_year=data["birthday_year"]

        user.username = username
        user.cpf = cpf
        user.birthday_year = birthday_year

        db.session.commit()
        dump_data = user_schema.dump(user)
        
        return jsonify({"msg":dump_data,
                            "status":200})

    except:

        return jsonify({"msg": "Bad request",
                        "status":400})


# ----------------------------------------------------------------
# Salaries Route



@app.route('/salaries',methods=['GET'])
def get_all_user__salaries():
    try:
        data = Salary.query.all()
        dump_data = salaries_schema.dump(data)
        
        return jsonify({"msg":dump_data,
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})



@app.route('/salaries/<cpf>',methods=['GET'])
def get_user_salary_by_cpf(cpf):
    try:
        user = User.query.filter_by(cpf=cpf).first()
        salaries = Salary.query.filter_by(cpf=user.cpf)
        dump_data = salaries_schema.dump(salaries)
        
        return jsonify({"msg":dump_data,
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})


@app.route("/salaries/create", methods=["GET","POST"])
def create_new_user_salary():
    try:
        data = request.get_json()
        date=datetime.now()
        cpf = data['cpf']
        salary = data['salary']
        discount = data['discount']
        registration = Salary(date,cpf,salary,discount)
        db.session.add(registration)
        db.session.commit()
        dump_data = salary_schema.dump(registration)
        print(dump_data)
        return jsonify({"msg":dump_data,
                        "status":200}) 
        
    except:
        return jsonify({"msg": "Bad Request",
                        "status":400})



@app.route('/salaries/mean_value',methods=['GET'])
def calculate_mean_values_from_all_users():
    try:
        user_salary = Salary.query.all()
        dump_data = salaries_schema.dump(user_salary)
        mean_salary = 0
        mean_discount = 0
        for item in range(len(dump_data)):
            mean_salary = mean_salary + dump_data[item]['salary']
            mean_discount = mean_discount + dump_data[item]['discount']

        mean_salary = mean_salary/len(dump_data)
        mean_discount = mean_discount/len(dump_data)
        # voltar valores
        return jsonify({"msg":{"mean_salary":mean_salary,"mean_discount":mean_discount},
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})




@app.route('/salaries/max_value',methods=['GET'])
def get_all_users_max_values():
    try:
        user_salary = Salary.query.all()
        dump_data = salaries_schema.dump(user_salary)
        max_salary = []
        max_discount = []
        for item in range(len(dump_data)):
            max_salary.append(dump_data[item]['salary'])
            max_discount.append(dump_data[item]['discount'])
        
        return jsonify({"msg":{"max_salary":max(max_salary),"max_discount":max(max_discount)},
                        "status":200})
        
    except:

        return jsonify({"msg": "Bad request",
                        "status":400})



        
if __name__ == "__main__":
    app.run(debug=True)