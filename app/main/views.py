


@main.route('/')
def index():
    title = 'Home. welcome to the best website for pitching your Ideas'
    return render_template('index.html', title = title )