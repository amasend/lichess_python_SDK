LICHESS_URL = 'https://lichess.org/'

###########
# ACCOUNT #
###########
ACCOUNT_URL = 'api/account'
ACCOUNT_EMAIL_URL = 'api/account/email'
ACCOUNT_PREFERENCES_URL = 'api/account/preferences'
ACCOUNT_KID_URL = 'api/account/kid'

#########
# USERS #
#########
USERS_STATUS_URL = 'api/users/status'
USERS_PLAYER_URL = 'player'
USERS_PLAYER_TOP_URL = 'player/top/{nb}/{perfType}'
USERS_USER_PUBLIC_DATA_URL = 'api/user/{username}'
USERS_RATING_HISTORY_URL = 'api/user/{username}/rating-history'
USERS_ACTIVITY_URL = 'api/user/{username}/activity'
USERS_MY_PUZZLE_ACTIVITY_URL = 'api/user/puzzle-activity'
USERS_GET_BY_IDS_URL = 'api/users'
USERS_TEAM_MEMBERS_URL = 'team/{teamId}/users'
USERS_LIVE_STREAMERS_URL = 'streamer/live'

#############
# RELATIONS #
#############
RELATIONS_FOLLOWING_URL = 'api/users/{username}/following'
RELATIONS_FOLLOWERS_URL = 'api/users/{username}/followers'

#########
# GAMES #
#########
GAMES_EXPORT_ONE_URL = 'game/export/{gameId}'
GAMES_EXPORT_USER_URL = 'api/games/user/{username}'
GAMES_EXPORT_IDS_URL = 'games/export/_ids'
GAMES_STREAM_CURRENT_URL = 'api/stream/games-by-users'
GAMES_ONGOING_URL = 'api/account/playing'
GAMES_CURRENT_TV_URL = 'tv/channels'

#########
# TEAMS #
#########
TEAMS_JOIN_URL = 'team/{teamId}/join'
TEAMS_LEAVE_URL = 'team/{teamId}/quit'
TEAMS_KICK_USER_URL = '/team/{teamId}/kick/{userId}'
