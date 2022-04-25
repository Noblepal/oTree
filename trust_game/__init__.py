from otree.api import *

doc = """Trust game is a 2-player game where both players are given an amount of money. 
Player 1 is asked to give any amount to Player 2. That amount if first tripled before Player 2 receives it.
Player 2 is then asked to send back some amount to Player 1. This amount is given as is. Read more here 
<a href="https://en.wikibooks.org/wiki/Bestiary_of_Behavioral_Economics/Trust_Game#:~:text=The%20Trust%20Game%2C%20designed%20by,economic%20transactions%20as%20self%2Dinterest">
Bestiary of Behavioral Economics/Trust Game
</a>."""


class C(BaseConstants):
    NAME_IN_URL = 'trust_game'
    PLAYERS_PER_GROUP = 2
    NUM_ROUNDS = 1
    INSTRUCTIONS_TEMPLATE = 'trust_game/instructions.html'
    AMOUNT_GIVEN = 1000
    MULTIPLIER = 3


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    sent_amount = models.FloatField(
        min=0,
        max=C.AMOUNT_GIVEN,
        doc="""Amount sent by Player 1""",
        label='How much will you send to Player 2?'
    )
    sent_back_amount = models.FloatField(
        doc="""Amount sent back by Player 2""",
        min=0
    )


class Player(BasePlayer):
    pass


def sent_back_amount(group: Group):
    return group.sent_amount * C.MULTIPLIER


def set_payoffs(group: Group):
    p1 = group.get_player_by_id(1)
    p2 = group.get_player_by_id(2)
    p1.payoff = C.AMOUNT_GIVEN - group.sent_amount + group.sent_back_amount
    p2.payoff = group.sent_amount * C.MULTIPLIER - group.sent_back_amount


# PAGES
class Introduction(Page):
    pass


class Send(Page):
    form_model = 'group'
    form_fields = ['sent_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 1


class SendBackWaitPage(WaitPage):
    pass


class SendBack(Page):
    form_model = 'group'
    form_fields = ['sent_back_amount']

    @staticmethod
    def is_displayed(player: Player):
        return player.id_in_group == 2

    @staticmethod
    def vars_for_template(player: Player):
        group = player.group
        tripled_amount = group.sent_amount * C.MULTIPLIER
        return dict(tripled_amount=tripled_amount)


class ResultWaitPage(WaitPage):
    after_all_players_arrive = set_payoffs


class Results(Page):
    @staticmethod
    def vars_for_template(player: Player):
        group = player.group

        return dict(tripled_amount=group.sent_amount * C.MULTIPLIER)


page_sequence = [
    Introduction,
    Send,
    SendBackWaitPage,
    SendBack,
    ResultWaitPage,
    Results,
]
