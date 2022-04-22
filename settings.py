from os import environ

SESSION_CONFIGS = [
    dict(
        name='guess_two_thirds',
        display_name="Guess 2/3 of the Average",
        app_sequence=['guess_two_thirds', 'payment_info'],
        num_demo_participants=3,
    ),
    dict(
        name='survey', app_sequence=['survey', 'payment_info'], num_demo_participants=1
    ),
    dict(
        name='bargaining', app_sequence=['bargaining', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='bertrand', app_sequence=['bertrand', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='common_value_auction', app_sequence=['common_value_auction', 'payment_info'], num_demo_participants=0
    ),
    dict(
        name='cournot', app_sequence=['cournot', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='dictator', app_sequence=['dictator', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='matching_pennies', app_sequence=['matching_pennies', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='prisoner', app_sequence=['prisoner', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='public_goods_simple', app_sequence=['public_goods_simple', 'payment_info'], num_demo_participants=3
    ),
    dict(
        name='traveler_dilemma', app_sequence=['traveler_dilemma', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='trust', app_sequence=['trust', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='trust_simple', app_sequence=['trust_simple', 'payment_info'], num_demo_participants=2
    ),
    dict(
        name='volunteer_dilemma', app_sequence=['volunteer_dilemma', 'payment_info'], num_demo_participants=3
    ),
    dict(
        display_name="Trust Game",
        name='trust_game',
        app_sequence=['trust_game', 'payment_info'],
        num_demo_participants=2
    ),
]

# if you set a property in SESSION_CONFIG_DEFAULTS, it will be inherited by all configs
# in SESSION_CONFIGS, except those that explicitly override it.
# the session config can be accessed from methods in your apps as self.session.config,
# e.g. self.session.config['participation_fee']

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = []
SESSION_FIELDS = []

# ISO-639 code
# for example: de, fr, ja, ko, zh-hans
LANGUAGE_CODE = 'en'

# e.g. EUR, GBP, CNY, JPY
REAL_WORLD_CURRENCY_CODE = 'USD'
USE_POINTS = True

ROOMS = [
    dict(
        name='econ101',
        display_name='Econ 101 class',
        participant_label_file='_rooms/econ101.txt',
    ),
    dict(name='live_demo', display_name='Room for live demo (no participant labels)'),
]

ADMIN_USERNAME = 'admin'
# for security, best to set admin password in an environment variable
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')

DEMO_PAGE_INTRO_HTML = """
Here are some oTree games.
"""

SECRET_KEY = '{{ secret_key }}'

INSTALLED_APPS = ['otree']
