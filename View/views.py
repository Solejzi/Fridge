from flask import render_template, redirect
from flask import render_template, redirect, request
from application.View.listview import ListView
from application import app, db
from application.Model.db_model import Fridge, Cooler, ItemsCategories, Items

class Home(ListView):
    def get_template_name(self):
        return 'home.html'

    def get_objects(self):
        return Items.query.all()

    
class ItemsView(ListView):
    def get_template_name(self):
        return 'Items.html'

    def get_objects(self):
        return Items.query.all()


class AddItems(ListView):
    def get_template_name(self):
        return 'AddItems.html'

    def get_objects(self):
        return Items.query.all()


class FridgeView(ListView):
    def get_template_name(self):
        return 'Items.html'

    def get_objects(self):
        return Items.query.all()

