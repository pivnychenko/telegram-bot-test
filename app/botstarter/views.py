from loguru import logger

from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse
from django.core.exceptions import PermissionDenied
from django.conf import settings

from .models import Question, User, Answer
from .bot_tools import bot_update, get_user
from .tbot import TelBot

TBot = TelBot()


@csrf_exempt
def get_hook(request):
    """
    get hook for message handler
    """
    if request.META['CONTENT_TYPE'] == 'application/json':
        json_data = request.body.decode('utf-8')
        update = bot_update(json_data)
        logger.info('update:', update)
        TBot.bot.process_new_updates([update])
        return HttpResponse(status=200)
    else:
        raise PermissionDenied


def set_hook(request):
    """
    set hook for telebot
    """
    try:
        webhook_url = settings.SERVER_URL + '/get_hook/'
        TBot.bot.set_webhook(webhook_url)
        logger.info(settings.SERVER_URL)
        return JsonResponse(data={"message": "success"}, status=200)
    except:
        return HttpResponse(status=401)


@TBot.bot.message_handler(commands=['start'])
def start(message):
    """
    Start message handler and first Question for user
    """
    TBot.start_message(message)


@TBot.bot.message_handler(func=lambda message: True, content_types=["text"])
def client_request(message):
    """ message handler for Answer user and save"""
    TBot.answer_user(message)


@TBot.bot.message_handler(content_types=["document", "audio", "sticker", "pinned_message", "photo", "audio"])
def handle_text_doc(message):
    """ message handler for Other content types"""
    TBot.no_questions(message)