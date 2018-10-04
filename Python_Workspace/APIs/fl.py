from flask import Flask,jsonify,request
app= Flask(__name__)

@app.route("/test_api",methods=["GET"])#to reach the particular func of the domain
def test_func():
	a=int(request.args.get("num1"))
	b=int(request.args.get("num2"))
	
	return jsonify({"sum":a+b})

if __name__=="__main__":
	app.run(port=1234)
