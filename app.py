from flask import Flask, request, jsonify

app = Flask(__name__)

users = [{
        "name": "Moses Tete",
        "username": "wango",
        "email": "galiwango@gmail.com",
        "password": "kabulasoke1",
        "confirmation": "kabulasoke1"

    },
    {
        "name": "Samuel Bagonza",
        "username": "samex",
        "email": "teziita@gmail.com",
        "password": "goodislove",
        "confirmation": "goodislove"

    },
    {
        "name": "Daniel Stevens",
        "username": "bravo",
        "email": "semusu@gmail.com",
        "password": "yesuamala",
        "confirmation": "yesuamala"

    },
    {
        "name": "Jamie Jones",
        "username": "sampthon",
        "email": "sampthon@gmail.com",
        "password": "kamukama2",
        "confirmation": "kamukama2"

    },
    {
        "name": "Talmon Sidie",
        "username": "telolan",
        "email": "jjaviira@gmail.com",
        "password": "trumpet3",
        "confirmation": "trumpet3"

    }]
sales = []

@app.route('/', methods=['GET'])
def index():
    return 'Welcome to the store of abundance.'

@app.route('/auth/signup', methods=['POST'])
def sign_up():
    user_data = request.get_json()
    # get data from user
    name = user_data.get('name')
    username = user_data.get('username')
    email = user_data.get('email')
    password = user_data.get('password')
    confirmation = user_data.get('confirmation')

    # validate user data
    if not user_data:
        return jsonify({'message': 'Please all fields should be filled'}), 400

    if not name:
        return jsonify({'message': 'Please name is required'}), 400

    if not username:
        return jsonify({'message': 'Please username is required'}), 400
  
    if not email:
        return jsonify({'message': 'Please email is required'}), 400
    
    if not password:
        return jsonify({'message': 'Please password is required'}), 400

    if not confirmation:
        return jsonify({'message': 'confirmation for password is required'}), 400
    
    # store your data to your database
    users.append(user_data)

    return jsonify({"message": f"user '{username}' has been successfully registered"}), 201

# @app.route('/auth/signin', methods=['POST'])
# def signin():
#     user_data = request.get_json()
#     # getting user signin data
#     username = user_data.get('username')
#     password = user_data.get('password')
    
#     # validate user signin data
#     if not user_data:
#         return jsonify({'message': 'Please fill all fields'}), 400

#     if not username:
#         return jsonify({'message': 'Username is required'}), 400
    
#     if not password:
#         return jsonify({'message': 'Password is required'}), 400
    
#     return jsonify({ 'message': f'Hi {username} you are successfully logged in'}), 201

@app.route('/api/v1/users/sales', methods=['POST'])
def make_a_sale():
    sale_data = request.get_json()
    # get sale data
    attendant_id = sale_data.get('attendant_id')
    attendantname = sale_data.get('attendantname')
    productname = sale_data.get('productname')
    productid = sale_data.get('productid')
    manufacturer = sale_data.get('manufacturer')
    price = sale_data.get('price')

    # validate sale data
    if not sale_data:
        return jsonify({'message': 'Please all fields should be filled'}), 400

    if not attendant_id:
        return jsonify({'message': 'Please attendant Id is required'}), 400

    if not attendantname:
        return jsonify({'message': 'Please name is required'}), 400

    if not productname:
        return jsonify({'message': 'Please fill in the product name'}), 400
  
    if not productid:
        return jsonify({'message': 'Product Id is required'}), 400
    
    if not manufacturer:
        return jsonify({'message': 'Please product manufacturer is required'}), 400

    if not price:
        return jsonify({'message': 'Please the price is required'}), 400
    
    # store your data to your database
    sales.append(sale_data)

    return jsonify({"message": f"attendant '{attendantname}' you have successfully made a sale!"}), 201

@app.route('/api/v1/users/sales', methods=['GET'])
def get_all_sales():
    if len(sales) >= 1:
       return jsonify({'sales': sales}), 200
    else:  
        return jsonify({
            "Status": "Failure",
            "Message": "Have no sales yet"}), 404

@app.route('/auth/sales/<int:attendant_id>', methods=['GET'])
def get_a_sale(attendant_id):
    for each_sale in sales:
        if each_sale.get('id') == attendant_id:
            return jsonify({'sale': each_sale})

    return jsonify({'error': 'Attendant Not Found'}), 404

@app.route('/auth/sales/<int:attendant_id>', methods=['PUT'])
def modify_a_sale(attendant_id):
    if len(sales) < 1:
        return jsonify({
            "status": "Failure",
            "Sorry": "You have no sales to modify"}), 404

    sale_data = request.get_json()

    attendant_id = sale_data.get('attendant_id')
    attendantname = sale_data.get('attendantname')
    productname = sale_data.get('productname')
    productid = sale_data.get('productid')
    manufacturer = sale_data.get('manufacturer')
    price = sale_data.get('price')

    for sale in sales:
        if sale.attendant_id == attendant_id:
           sale.attendantname = attendantname 
           sale.productname = productname
           sale.productid = productid
           sale. manufacturer =  manufacturer
           sale. price =  price
            
        return jsonify({
            "request": sale.__dict__,
            "status": "OK",
            "Congratulations": "You successfully modified a request"}), 200

@app.route('/auth/sales/attendantname', methods=['DELETE'])
def delete_a_sale(attendantname):
       global sales
       sales = [sale for sale in sales if sale["attendantname"] != attendantname]
       return "{} is deleted.".format(attendantname), 200
      
sales.append(sales)

# @app.route('/auth/login', methods=['POST'])
# def login(): 
#     user_data = request.get_json() 
#     username = user_data.get('username')
#     password = user_data.get('password')  
    
#     for user in users:
#         if user.username == username and user.password == password:
#             return  "You have successfully logged in"
#         else:
#             return  "Login with the right credentials"

@app.route('/auth/login', methods=['POST'])
def login_user():
    # getting user data
    user_data = request.get_json()
    username = user_data.get('username')
    password = user_data.get('password')

    for user in users:
        if user.username == username:
           user.password == password 

           return  "You have successfully logged in"
        else:
            return  "Login with the right credentials"
           
if __name__=="__main__":
    app.run(debug=True)