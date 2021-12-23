import os
import telebot
from loguru import logger

from django.conf import settings
from .bot_tools import bot_update, get_user
from .models import Question, Answer
from .variable_messages import text_start_message, text_no_question, text_start_question


class TelBot(object):
    """
    Class TeleBot
    """

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super().__new__(cls)
            cls.instance.bot = telebot.TeleBot(settings.BOT_TOKEN, parse_mode='HTML')
        return cls.instance

    def __init__(self):
        pass

    def start_message(self, message):
        """
        Start message
        """

        question = Question.objects
        user = get_user(message.from_user.id)
        user.set_user_state()

        if question.count():
            question = question.first()
            user.state = f"{question.id},"
            user.save()

            self.bot.send_message(message.chat.id, text_start_message.format(
                username=message.from_user.username,
                question=question.name))
        else:
            self.no_questions(message)

    def answer_user(self, message):
        """ Handler for Answer user and save"""
        user = get_user(message.from_user.id)
        question_ids = list(filter(None, user.state.split(',')))
        questions = Question.objects.all()

        text = text_start_question

        if not len(question_ids) > questions.count():
            # get next question
            question_next = questions[len(question_ids):][0] if questions[len(question_ids):] else None

            # get current question
            question = questions.first() if len(question_ids) < 2 else questions[len(question_ids) - 1:][0]

            if question_next:
                text = question_next.name
                user.state = f"{user.state} {question_next.id},"
                user.save()

            obj, created = Answer.objects.get_or_create(user=user, question=question)
            answer = obj if obj else created

            answer.name = message.text
            answer.save()

        self.bot.send_message(message.chat.id, text)

    def no_questions(self, message):
        """
        if no question in db
        """
        self.bot.send_message(message.chat.id, text_no_question)





