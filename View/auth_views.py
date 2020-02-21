from flask import render_template, redirect, request, flash
from application.View.listview import ListView
from application.View.methodview import MView

from application import app, db
from application.Model.db_model import Fridge, Users, InFridge, ItemsCategories, Items, OpenedItem
from application.Model.forms import LoginForm, RegistrationForm


class Register(MView):
    def __init__(self):
        super().__init__()
        self.template = 'register.html'
        self.objects = {'register-form': RegistrationForm()}

    def get(self):
        if self.objects['register-form'].validate_on_submit():
            self.post()
        return render_template(self.template, form=self.objects['register-form'])

    def post(self):

        data = self.objects['register-form'].data
        data.pop('csrf_token')
        user = Users(data['username'],data['email'],data['password'])
        db.session.add(user)
        db.session.commit()

        flash(f'succesfully registerd {data["username"]}')
        return redirect('/navigation')


class U(MView):
    def __init__(self):
        super().__init__()
        self.template = 'U.html'
        self.objects = {'users': db.session.query(Users).all()}
        print(self.objects)
    def get(self):
        return render_template(self.template, users=self.objects['users'])

app.add_url_rule('/register', methods=['GET', 'POST'], view_func=Register.as_view('register_view'))
app.add_url_rule('/U', methods=['GET', 'POST'], view_func=U.as_view('U_view'))