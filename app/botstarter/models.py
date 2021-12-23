from django.db import models
from .manager import UserManager


class User(models.Model):
    """
    User registration from UserManager
    """
    USER_STATES = [
	    ('start', 'start'),
    ]

    chat_id = models.CharField(
        verbose_name="User Chat_id",
        max_length=100,
        primary_key=True)

    state = models.CharField(
        verbose_name="User state",
        default='start',
        max_length=200,
        choices=USER_STATES)

    # Settings
    objects = UserManager()


    def set_user_state(self, commit: bool = True):
        """
        method for updating self.state
        Args:
            commit: save instance after update

        Returns:
            Nothing.
        """
        self.state = "start"

        if commit:
            self.save()

    def __str__(self):
        return f'User - {self.chat_id}'

    class Meta:
        verbose_name = "Bot Starter - User"
        verbose_name_plural = "Bot Starter - User"


class Question(models.Model):
    name = models.CharField(
        verbose_name="Question name",
        max_length=300)

    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bot Starter - Question"
        verbose_name_plural = "Bot Starter - Question"


class Answer(models.Model):
    question = models.ForeignKey(
        Question,
        verbose_name="Question",
        on_delete=models.CASCADE,
        blank=False,
        null=True)

    name = models.TextField(
        verbose_name="Answer name",
        max_length=1000)

    created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        User,
        verbose_name="User",
        on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Bot Starter - Answer"
        verbose_name_plural = "Bot Starter - Answer"