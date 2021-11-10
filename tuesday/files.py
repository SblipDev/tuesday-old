import requests
import json

from .utils import j,s
from .errors import MondayError

class File:

    def __init__(self, token, url='https://api.monday.com/v2'):
        self.token = token
        self.url = url
        self.headers = {'Authorization': 'Bearer ' + self.token}

    def make_request(self, query):
        data = {'query': query}
        r = requests.post(url=self.url, json=data,
                        headers=self.headers)
        return r.json()

    def get_assets_by_ids(self, ids):
        query = """
        query {
            assets (ids: %s) {
                id
                name
                url
                file_extension
                file_size
            }
        }
        """ % (self.ids)

        try:
            dictory = {
                'data': self.make_request(query)['data'],
                'message': 'All assets(from the id you have specified) have been requested.'
            }
            
            return dictory
        except KeyError:
            raise MondayError(self.make_request(query)['errors'][0]['message'])
    
    def add_file_to_column(self, item_id, column_id, file):
        query = """
        mutation {
            add_file_to_column (item_id: %s, column_id: '%s', $file: %s) {
                id
            }
        }
        """ % (item_id, column_id, file)

# The code of files.py ends here.
# Have a nice day.
