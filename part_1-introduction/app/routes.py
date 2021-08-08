from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"


@app.route('/latihan-flask')
def latihan_flask():
    return "Aku sedang belajar Flask loh!"