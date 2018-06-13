from flask import Flask

app=Flask(__name__)

''' 1 '''
# simple route to hello world
# @app.route('/')
# def index():
# 	return 'This is the Homepage.'

''' 2 '''
# returning HTML elements
@app.route('/raje')
def gp():
	return "<h1>Chhtrapati</h1><br/><p>Shivaji Maharaj<br/>King of Maratha Empire</p>"


# Passing variable as argument
@app.route('/profile/<username>')
def profile(username):
	return '<h1> Hi %s</h1>'%username

# Passing string as an argument doesn't require to specify data type but others do require(int,float).
@app.route('/post/<int:post_id>')
def show_post_id(post_id):
	return '<h1>Post ID is : %d</h1>' % int(post_id)
	


if __name__=="__main__":
	app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)