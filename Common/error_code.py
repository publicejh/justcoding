

# # status code 작성하기 위해 코드별 상태 매칭
# A = {
#     0: 'Failure',
#     1: 'Informational',
#     2: 'Success',
#     3: 'Redirection',
#     4: 'ClientError',
#     5: 'ServerError',
#     6: 'DBError',
#     7: 'NeedModification'
#
# }
#
# B = {
#     0: 'Backend',
#     1: 'Frontend',
# }
#
# C_0 = {
#     1: {
#         'app': 'AuthServer',
#         0: '/',
#         1: 'auth_',
#         2: 'auth_server',
#         3: 'chat',
#         4: 'sig',
#
#     },
#
#     2: {
#         'app': 'ChatServer',
#         0: '/',
#         1: 'chat',
#         2: 'justcoding_chat',
#         3: 'sig',
#     },
#
#     3: {
#         'app': 'PlatformServer',
#         0: '/',
#         1: 'band',
#         2: 'post',
#         3: 'sig',
#     },
#
# }
#
# C_1 = {
#
#     0: {
#         0: 'App',
#         1: 'main',
#         2: 'settings',
#         3: 'websocket',
#
#     },
#
#     1: {
#
#         1: 'BandInvitationHome',
#
#     },
#
#     2: {
#
#
#         1: 'Chat',
#         2: 'Chats',
#         3: 'Emoji',
#         4: 'EmojiPicker',
#         5: 'Message',
#
#     },
#
#     3: {
#
#         1: 'Signin',
#
#     },
#
# }


# const value들 넣기. 아래는 원더우먼 팀 예시
const_value = {
    # 'TTL': 300,
    # 'HEADER_DOES_NOT_EXIST': 'NO_token_in_header',
    # 'SESSION_EXIST': 'Session_exist',
    # 'SESSION_CREATED': 'Session_created',
    # 'SESSION_DOES_NOT_EXIST': 'Session does not exist',
    # 'TOKEN_DOES_NOT_EXIST': 'Token does not exist',
    # 'INVITATION_LINK' : 'http://192.168.0.24:9000/api/group/invitation/',
    # 'PARTICIPATION_LINK': 'http://192.168.0.24:9000/api/group/join/',
    # 'CONFIRMATION_LINK' : 'http://192.168.0.24:8000/api/accounts/signup/',

}


status_code = {
    'SUCCESS': {
            "code": 1,
            "msg": "Request Sucess",
            # # "path": ""
    },

    'FAILURE': {
        "code": 0,
        "msg": "Request Failure",
        # # "path": "Frontend\components\Signup.vue"
    },

    'SIGNUP_SUCCESS' : {
        # "code": 1200,
        'code': 1200,
        "msg": "SignUp Success",
        # # "path": "Frontend\components\Signup.vue"
    },

    'SIGNUP_WRONG_PARAMETER': {
        "code": 1401,
        # "code" : 4110,
        "msg": "SignUp Wrong Parameter",
        # # "path": "Frontend\components\Signup.vue"
    },

    'SIGNUP_INVALID_EMAIL' : {
        "code": 1402,
        "msg": "SignUp Invalid Email",
        # # "path": "Frontend\components\Signup.vue"
    },

    'USER_SIGNOUT_SUCCESS': {
        "code": 1203,
        "msg": "User signout success",
        # # "path": "Frontend\components\Signup.vue"
    },
    'USER_SIGNOUT_FAILURE': {
        "code": 1403,
        "msg": "User signout failure",
        # # "path": "Frontend\components\Signup.vue"
    },


    'LOGIN_SUCCESS' : {
        "code" : 2200,
        "msg" : "Login success",
        # # "path" : "Frontend\components\Signin.vue"
    },
    'LOGIN_WRONG_PARAMETER' : {
        "code" : 2401,
        "msg" : "Login Wrong Parameter",
        # # "path" : "Frontend\components\Signin.vue"
    },
    'LOGIN_INVALID_EMAIL' : {
        "code" : 2402,
        "msg" : "Login Invalid Email",
        # # "path" : "Frontend\components\Signin.vue"
    },
    'LOGIN_INVALID_PASSWORD': {
        "code": 2403,
        "msg": "Login Invalid Password",
        # # "path": "Frontend\components\Signin.vue"
    },
    'LOGIN_SESSION_EXISTS' : {
        "code" : 2304,
        "msg" : "Session Exists",
        # # "path" : "Frontend\components\Signin.vue"
    },

    'LOGOUT_SUCCESS' : {
        "code" : 3200,
        "msg" : "Logout Success",
        # # "path" : "Frontend\components\Signin.vue"
    },
    'LOGOUT_FAILURE' : {
        "code" : 3401,
        "msg" : "Logout Failure",
        # # "path" : ""
    },

    # 'USER_INFO_GET_SUCCESS' : {
    #     "code" : 4200,
    #     "msg" : "User information Retrieve",
    #     # "path" : ""
    # },
    # 'USER_INFO_GET_FAILURE' : {
    #     "code" : 4401,
    #     "msg" : "User information retrieve fail",
    #     # "path" : ""
    # },
    # 'USER_INFO_MODIFY_SUCCESS' : {
    #     "code" : 4202,
    #     "msg" : "User information modified success",
    #     # "path" : ""
    # },
    # 'USER_INFO_MODIFY_FAILURE' : {
    #     "code" : 4403,
    #     "msg" : "User information modification failure",
    #     # "path" : ""
    # },
'BAND_MADE_SUCCESS' : {
        "code" : 5200,
        "msg" : "New Band is made",
        # # "path" : ""
    },
    'BAND_LIST_SUCCESS' : {
        "code" : 5201,
        "msg" : "Band list is retreived",
        # # "path" : ""
    },
    'BAND_MEMBER_GET_SUCCESS': {
        "code": 5202,
        "msg": "Band memeberlist get success",
        # # "path": ""
    },
    'BAND_INVITATION_SUCCESS': {
        "code": 5203,
        "msg": "Band invite Success",
        # # "path": ""
    },
    'BAND_INVITATION_ACTIVATE_SUCCESS': {
        "code": 5204,
        "msg": "Activation Success",
        # # "path": ""
    },
    'BAND_DELETE_SUCCESS': {
        "code": 5205,
        "msg": "Band Delete Success",
        # # "path": ""
    },
    'BAND_EXIT_SUCCESS': {
        "code": 5206,
        "msg": "Band Exit Success",
        # # "path": ""
    },
    'BAND_GET_DETAIL_SUCCESS': {
        "code": 5207,
        "msg": "Get Band detail Success",
        # # "path": ""
    },
    'BAND_MADE_FAILURE': {
        "code": 5400,
        "msg": "Band creation fail",
        # # "path": ""
    },
    'BAND_LIST_FAILURE': {
        "code": 5401,
        "msg": "Cannot retrieve list of Band",
        # # "path": ""
    },
    'BAND_MEMBER_GET_FAILURE': {
        "code": 5402,
        "msg": "Band memeberlist get fail",
        # # "path": ""
    },
    'BAND_INVITATION_FAILURE': {
        "code": 5403,
        "msg": "Band invite Fail",
        # # "path": ""
    },
    'BAND_INVITATION_ACTIVATE_FAILURE': {
        "code": 5404,
        "msg": "Activation Fail",
        # # "path": ""
    },
    'BAND_DELETE_FAIL': {
        "code": 5405,
        "msg": "Band Delete Fail",
        # # "path": ""
    },
    'BAND_EXIT_FAIL': {
        "code": 5406,
        "msg": "Band Exit Fail",
        # # "path": ""
    },
    'BAND_GET_DETAIL_FAILURE': {
        "code": 5407,
        "msg": "Get Band detail Fail",
        # # "path": ""
    },


    'POST_MADE_SUCCESS': {
        "code": 6200,
        "msg": "New POST is made",
        # # "path": ""
    },
    'POST_LIST_SUCCESS': {
        "code": 6201,
        "msg": "POST list is retreived",
        # # "path": ""
    },
    'POST_MEMBER_GET_SUCCESS': {
        "code": 6202,
        "msg": "POST memeberlist get success",
        # # "path": ""
    },
    'POST_INVITATION_SUCCESS': {
        "code": 6203,
        "msg": "POST invite Success",
        # # "path": ""
    },
    'POST_INVITATION_ACTIVATE_SUCCESS': {
        "code": 6204,
        "msg": "Activation Success",
        # # "path": ""
    },
    'POST_DELETE_SUCCESS': {
        "code": 6205,
        "msg": "POST Delete Success",
        # # "path": ""
    },
    'POST_EXIT_SUCCESS': {
        "code": 6206,
        "msg": "Post Exit Success",
        # # "path": ""
    },
    'POST_GET_DETAIL_SUCCESS': {
        "code": 6207,
        "msg": "Get Post detail Success",
        # # "path": ""
    },
    'POST_MODIFY_SUCCESS': {
        "code": 6208,
        "msg": "Get Post modify Success",
        # # "path": ""
    },
    'POST_MADE_FAILURE': {
        "code": 6400,
        "msg": "Post creation fail",
        # # "path": ""
    },
    'POST_LIST_FAILURE': {
        "code": 6401,
        "msg": "Cannot retrieve list of Post",
        # # "path": ""
    },
    'POST_MEMBER_GET_FAILURE': {
        "code": 6402,
        "msg": "Post memeberlist get fail",
        # # "path": ""
    },
    'POST_INVITATION_FAILURE': {
        "code": 6403,
        "msg": "Post invite Fail",
        # # "path": ""
    },
    'POST_INVITATION_ACTIVATE_FAILURE': {
        "code": 6404,
        "msg": "Activation Fail",
        # # "path": ""
    },
    'POST_DELETE_FAIL': {
        "code": 6405,
        "msg": "POST Delete Fail",
        # # "path": ""
    },
    'POST_EXIT_FAIL': {
        "code": 6406,
        "msg": "Post Exit Fail",
        # "path": ""
    },
    'POST_GET_DETAIL_FAILURE': {
        "code": 6407,
        "msg": "Get Post detail Fail",
        # "path": ""
    },
    'POST_MODIFY_FAILURE': {
        "code": 6408,
        "msg": "Get Post modify Fail",
        # "path": ""
    },

    'CHAT_MADE_SUCCESS': {
        "code": 7200,
        "msg": "New Chat is made",
        # "path": ""
    },
    'CHAT_LIST_SUCCESS': {
        "code": 7201,
        "msg": "Chat list is retreived",
        # "path": ""
    },
    'CHAT_MEMBER_GET_SUCCESS': {
        "code": 7202,
        "msg": "Chat memeberlist get success",
        # "path": ""
    },
    'CHAT_INVITATION_SUCCESS': {
        "code": 7203,
        "msg": "Chat invite Success",
        # "path": ""
    },
    'CHAT_INVITATION_ACTIVATE_SUCCESS': {
        "code": 7204,
        "msg": "Activation Success",
        # "path": ""
    },
    'CHAT_DELETE_SUCCESS': {
        "code": 7205,
        "msg": "Chat Delete Success",
        # "path": ""
    },
    'CHAT_EXIT_SUCCESS': {
        "code": 7206,
        "msg": "Chat Exit Success",
        # "path": ""
    },
    'CHAT_GET_DETAIL_SUCCESS': {
        "code": 7207,
        "msg": "Get Chat detail Success",
        # "path": ""
    },
    'CHAT_MADE_FAILURE': {
        "code": 7400,
        "msg": "Chat creation fail",
        # "path": ""
    },
    'CHAT_LIST_FAILURE': {
        "code": 7401,
        "msg": "Cannot retrieve list of Chat",
        # "path": ""
    },
    'CHAT_MEMBER_GET_FAILURE': {
        "code": 7402,
        "msg": "Chat memeberlist get fail",
        # "path": ""
    },
    'CHAT_INVITATION_FAILURE': {
        "code": 7403,
        "msg": "Chat invite Fail",
        # "path": ""
    },
    'CHAT_INVITATION_ACTIVATE_FAILURE': {
        "code": 7404,
        "msg": "Activation Fail",
        # "path": ""
    },
    'CHAT_DELETE_FAIL': {
        "code": 7405,
        "msg": "Chat Delete Fail",
        # "path": ""
    },
    'CHAT_EXIT_FAIL': {
        "code": 7406,
        "msg": "Chat Exit Fail",
        # "path": ""
    },
    'CHAT_GET_DETAIL_FAILURE': {
        "code": 7407,
        "msg": "Get Chat detail Fail",
        # "path": ""
    },
}


