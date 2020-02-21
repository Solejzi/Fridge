from flask import render_template, redirect, request, flash
from application.View.listview import ListView
from application.View.methodview import MView
from application import app, db
from application.Model.db_model import Fridge, Users, InFridge, ItemsCategories, Items, OpenedItem
from application.Model.forms import LoginForm, RegistrationForm


class Welcome(MView):

    def __init__(self):
        super().__init__()
        self.template = 'welcome.html'
        self.objects = {'login-form': LoginForm()}

    def get(self):
        return render_template(self.template, form=self.objects['login-form'])

    def post(self):
        pass


class ItemsView(MView):
    def __init__(self):
        super().__init__()
        self.template = 'Items.html'
        self.objects = {'items': db.session.query(Items).all()}

    def get(self):
        # show a list of all available items
        pass

    def post(self):
        # adds item to a list
        pass

    def update(self):
        # updates item
        pass

    def delete(self):
        # deletes item
        pass


class FridgeView(MView):

    def __init__(self):
        super().__init__()
        self.template = 'fridge.html'
        self.objects = {'items': db.session.query(InFridge).all()}

    def get(self):
        # shows items in fridge
        pass

    def post(self):
        # adds item to fridge
        pass

    def put(self):
        # opens item
        pass

    def delete(self):
        # deletes item
        pass


app.add_url_rule('/fridge', methods=['GET', 'POST'], view_func=FridgeView.as_view('fridge_view'))
app.add_url_rule('/navigation', view_func=Welcome.as_view('welcome_view'))
