import telebot

from .models import User


def bot_update(json_data):
    return telebot.types.Update.de_json(json_data)


def get_user(chat_id):
    """get user from db and return it"""
    obj, created = User.objects.get_or_create(chat_id=chat_id)
    return obj if obj else created
