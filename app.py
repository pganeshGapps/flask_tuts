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

''' 3 '''
# HTTP methods : default is GET
from flask import request
@app.route('/bacon', methods=['GET','POST'])
def bacon():
	if request.method == 'POST':
		return 'You are using POST method.'
	else:
		return 'Most probably you are using GET! '

''' 4 '''
# render html file/ template
# that html file should be in templates folder
from flask import render_template
@app.route('/profile/<name>')
def profile(name):
	return render_template("profile.html", name=name)

''' 5 '''
# linking css file to html style.css/ filename.css

''' 6 '''
# Mapping multiple URLs
@app.route('/')
@app.route('/<user>')
def throw_msg(user=None):
	return render_template("user.html", user= user)

if __name__=="__main__":
	app.run(debug=True)

# if __name__ == '__main__':
#     app.run(host='0.0.0.0', port=5000)