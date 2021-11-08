import requests
import json

from .utils import j, s
from .errors import MondayError

class Column:
    
    PEOPLE = 'people'
    PHONE = 'phone'
    PROGRESS = 'progress'
    DEPENDENCY = 'dependency'
    COLOR_PICKER = 'color_picker'
    LAST_UPDATED = 'last_updated'
    AUTO_NUMBER = 'auto_number'
    DATE = 'date'
    TEAM = 'team'
    TAGS = 'tags'
    EMAIL = 'email'
    RATING = 'rating'
    STATUS = 'status'
    LOCATION = 'location'
    INTEGRATION = 'integration'
    CREATION_LOG = 'creation_log'
    NUMBERS = 'numbers'
    CHECKBOX = 'checkbox'
    COUNTRY = 'country'
    WORLD_CLOCK = 'world_clock'
    TIME_TRACKING = 'time_tracking'
    DROPDOWN = 'dropdown'
    ITEM_ID = 'item_id'
    FILE = 'file'
    WEEK = 'week'
    TEXT = 'text'
    VOTE = 'vote'
    LONG_TEXT = 'long_text'
    PROGRESS = 'progress'
    HOUR = 'hour'
    LINK = 'link'
    TIMELINE = 'timeline'
    NAME = 'name'
    
    def __init__(self, token, board_id, url='https://api.monday.com/v2'):
        self.token = token
        self.url = url
        self.headers = {'Authorization': 'Bearer ' + self.token}
        self.id = board_id
        
    def make_request(self, query):
        data = {'query': query}
        r = requests.post(url=self.url, json=data,
                        headers=self.headers)
        return r.json()
    
    def get_columns(self):
        query = """
        query {
            boards (ids: %s) {
                owner {
                    id
                }
                columns {
                    id
                    title
                    type
                    archived
                    width
                }     
            }
        }
        """ % (self.id)

        try:
            dictory = {
                'data': self.make_request(query),
                'message': 'All board values have been put into the data key.'
            }
            
            try:
                test = dictory['data']['data']
            except KeyError:
                raise MondayError(dictory['data']['errors'][0]['message'])
            
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def get_columns_settings(self):
        query = """
        query {
            boards (ids: %s) {
                owner {
                    id
                }
                columns {
                    id
                    title
                    settings_str
                }     
            }
        }
        """ % (self.id)

        try:
            dictory = {
                'data': self.make_request(query)['data']['boards'],
                'message': 'All Column"s settings_str have been put into the data key.'
            }
            
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def create_column(self, title, type_):
        query = """
        mutation {
            create_column (board_id: %s, title: %s, column_type: %s) {
                id
            }
        }
        """ % (self.id, j(title), type_)

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Column %s has been created' % title
            }
            
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def change_column_value(self, item_id, column_id, value):
        query = """
        mutation {
            change_simple_column_value (board_id: %s, item_id: %s, column_id: %s, value: %s) {
                id
            }
        }
        """ % (self.id, item_id, j(column_id), j(value))

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Done.'
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def change_multiple_column_values(self, item_id, column_id, column_values):
        query = """
        mutation {
            change_multiple_column_values (board_id: %s, item_id: %s, column_id: %s, value: %s) {
                id
            }
        }
        """ % (self.id, item_id, j(column_id), s(column_values))

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Done.'
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])

    def change_column_title(self, column_id, title):
        query = """
        mutation {
            change_column_title (board_id: %s, column_id: %s, title: %s) {
                id
            }
        }
        """ % (self.id, j(column_id), j(title))

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'Column title "%s" has been changed to "%s"' % (column_id, title)
            }

            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
# THE CoDe ENDS HERE
# Have A Nice Day.
# And come again!

# (bonus if you get the reference.)
