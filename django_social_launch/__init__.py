VERSION = (0, 0, 1)

__version__ = "".join([".".join(map(str, VERSION[0:3])), "".join(VERSION[3:])])

user_successfully_created_msg = 'You successfully edited your profile.'

referrer_url_session_key = 'social_launch_referrer_url'
referring_user_id_session_key = 'social_launch_referring_user_id'
