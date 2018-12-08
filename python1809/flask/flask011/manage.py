
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_script import Manager

from App.views import blue
from App.views1 import blue as blue2



app = Flask(__name__)
app.config['SECRET_KEY']='fa123344445feafsfsgggafadfkufihykfujhsgsgr'
app.register_blueprint(blueprint=blue)
app.register_blueprint(blueprint=blue2)
Bootstrap(app=app
          )

manage=Manager(app=app)






if __name__ == '__main__':
    manage.run()
