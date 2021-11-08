import requests
import json
from .utils import j,s
from .errors import MondayError 

# Made by SblipDev. (shaurya-blip)
# https://github.com/shaurya-blip/moonday
class Board:
    
    PUBLIC = "public"
    SHARE = "share"
    PRIVATE = "private"
    TRUE = "true"
    FALSE = "false"
    WITH_STRUCTURE = "duplicate_board_with_structure"
    WITH_PULSES = "duplicate_board_with_pulses"
    WITH_PULSES_AND_UPDATES = "duplicate_board_with_pulses_and_updates"
    
    def __init__(self, token, url='https://api.monday.com/v2'):
        self.token = token
        self.url = url
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def make_request(self, query):
        data = {'query': query}
        r = requests.post(url=self.url, json=data,
                        headers=self.headers)
        return r.json()

    def get_boards(self, limit=1000):
        query = """
        { boards (limit:%s) { name id } }
        """ % (limit)
        try:
            return self.make_request(query)['data']['boards']
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def get_board_id(self, board_name):
        boards = self.get_boards()
        for board in boards:
            if board['name'] == board_name:
                return board['id']
        return None

    def get_board_data(self, board_id):
        query = """
        query {
            boards (ids: %s) {
                name
                state
                board_folder_id
                owner {
                    id
                }
                board_kind
            }
        }
        """ % (board_id)
        try:
            return self.make_request(query)['data']
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def get_board_permissions(self, board_id):
        query = """
        query {
            boards (ids: %s) {
                name
                id
                permissions
            }
        }
        """ % (board_id)
        
        try:
            return self.make_request(query)['data']['boards'][0]
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def get_board_updates(self, board_id):
        query = """
        query {
            boards (ids: %s) {
                name
                id
                updates {
                    id
                }
            }
        }
        """ % (board_id)

        dictory = {
            'data': self.make_request(query)['data']['boards'][0],
            'message': 'Only shares update id.'
        }
        
        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def get_board_subscribers(self, board_id):
        query = """
        query {
            boards (ids: %s) {
                name
                id
                subscribers {
                    name
                    id
                }
            }
        }
        """ % (board_id)

        dictory = {
            'data': self.make_request(query)['data']['boards'][0],
            'message': 'Only shares subscriber id.'
        }
        
        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def get_board_workspace(self, board_id):
        query = """
        query {
            boards (ids: %s) {
                name
                id
                workspace {
                    id
                    name
                }
            }
        }
        """ % (board_id)

        dictory = {
            'data': self.make_request(query)['data']['boards'][0],
            'message': 'It shares the workspace name and id. IT IS NULL IF it is the main workspace.'
        }

        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def create_board(self, board_name, board_kind):
        query = """
        mutation {
            create_board (board_name: %s, board_kind: %s) {
                id
                name
            }
        }
        """ % (j(board_name), board_kind)

        dictory = {
            'data': self.make_request(query)['data'],
            'message': '%s has been created.' % (board_name)
        }

        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def archive_board(self, board_id):
        query = """
        mutation {
            archive_board (board_id: %s) {
                id
            }
        }
        """ % (board_id)

        dictory = {
            'data': self.make_request(query)['data'],
            'message': 'Board %s has been archived.' % (board_id)
        }

        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def duplicate_board(self, board_id, duplicate_type, new_board_data):
        query = """
        mutation {
            duplicate_board(board_id:%s, duplicate_type: %s, board_name:%s, keep_subscribers:%s) {
                board {
                    id
                }
            }
        }
        """ % (board_id, duplicate_type, j(new_board_data[0]), new_board_data[1])



        dictory = {
            'data': self.make_request(query),
            'message': 'Board %s has been duplicated to %s' % (board_id, new_board_data[0])
        }

        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def get_board_views(self, board_id):
        query = """
        query {
            boards (ids: %s) {
                views {
                    id
                    name
                    type
                }
            }
        }
        """ % (board_id)

        dictory = {
            'data': self.make_request(query)['data']['boards'][0],
            'message': 'All the board views have been returned.'
        }
        
        try:
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def delete_board(self, board_id):
        raise MondayError(
            "Currently the Monday V2 API does not support deleting a board. Sorry. Go to the link if you wanna know more -> https://community.monday.com/t/how-to-delete-a-board/7490")
    

# THE CoDe ENDS HERE
# Have A Nice Day.
# And come again!

# (bonus if you get the reference.)