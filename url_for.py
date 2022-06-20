from flask import Flask, url_for

app=Flask(__name__)
@app.route('/post/<int:post_id>')
def show_post(post_id):
    return 'POST_ID %d' % post_id

@app.route('/url/show_post')
def get_post_url():
    return url_for('show_post',post_id=2)

@app.route('/url/<username>')
def show_user_profile(username):
    return 'User: %s' % username

@app.route('/url/<username>')
def show_user_profile(username):
    return 'User: %s' % username

@app.route('/url/')
def get_url():
    return url_for('show_post',post_id=2)
if __name__=='__main__':
    app.run(debug=True) #本地服务器上运行APP
