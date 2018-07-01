from flask import Blueprint

from app.libs.redprint import Redprint


api = Redprint("user")


@api.route('/get')
def get_user():
    return 'i am hah'


@api.route('/create')
def create_user():
    #name,pwd
    return 'i am hah'