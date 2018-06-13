from flask import Flask

app=Flask(__name__)

''' 1 '''
# simple route to hello world
@app.route('/')
def index():
	return 'This is the Homepage.'


if __name__=="__main__":
	app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)