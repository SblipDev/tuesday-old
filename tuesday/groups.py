import requests
import json

from sqlalchemy import column

from .utils import j, s
from .errors import MondayError


class Group:

    TRUE = "true"
    FALSE = "false"
    
    def __init__(self, token, id,url='https://api.monday.com/v2'):
        self.token = token
        self.url = url
        self.id = id
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def make_request(self, query):
        data = {'query': query}
        r = requests.post(url=self.url, json=data,
                        headers=self.headers)
        return r.json()

    def get_groups(self, limit=50):
        query = """
        query {
            boards (ids: %s) {
                groups(limit:%s) {
                    id
                    title
                    color
                    position
                    archived
                    deleted
                    position
                }
            }
        }
        """ % (self.id, limit)

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Alll the groups in the board have been put in the data key.'
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def duplicate_group(self, group_id, add_to_top="true"):
        query = """
        mutation {
            duplicate_group (board_id: %s, group_id: %s, add_to_top: %s) {
                id
            }
        }
        """ % (self.id, group_id, add_to_top)

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'All assets(from the id you have specified) have been requested.'
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def duplicate_group(self, group_id, add_to_top="true"):
        query = """
        mutation {
            duplicate_group (board_id: %s, group_id: %s, add_to_top: %s) {
                id
            }
        }
        """ % (self.id, j(group_id), add_to_top)

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Group %s has been duplicated.' % (group_id)
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def create_group(self, group_name):
        query = """
        mutation {
            create_group (board_id: %s, group_name: %s) {
                id
            }
        }
        """ % (self.id, j(group_name))

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Group %s has been created.' % (group_name)
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def archive_group(self, group_id):
        query = """
        mutation {
            archive_group (board_id: %s, group_id: %s) {
                id
                archived
            }
        }
        """ % (self.id, j(group_id))

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Group %s has been archived.' % (group_id)
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def archive_group(self, group_id):
        query = """
        mutation {
            delete_group (board_id: %s, group_id: %s) {
                id
                deleted
            }
        }
        """ % (self.id, j(group_id))

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Group %s has been deleted..' % (group_id)
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
        
# The code of groups.py ends here.
# Have a nice day.
