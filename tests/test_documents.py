from unittest import TestCase

from tigrisdb.client import TigrisClient
from tigrisdb.config import TigrisClientConfig
from tigrisdb.errors import TigrisException


class DbTestCase(TestCase):
    __client: TigrisClient
    coll_name: str = 'users'

    def setUp(self) -> None:
        self.__client = TigrisClient(TigrisClientConfig(project_name='db1'))

    def test_execute(self):
        db = self.__client.get_db()
        # drop a collection if exists
        try:
            db.drop_collection(self.coll_name)
        except:
            print('no collection found, skipping....')

        schema = {
            'title': 'users',
            'additionalProperties': False,
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'string'
                },
                'name': {
                    'type': 'string'
                },
                'scores': {
                    'type': 'array',
                    'items': {
                        'type': 'number'
                    }
                }
            },
            'primary_key': ['id']
        }
        coll = db.create_or_update_collection('users', schema)
        self.assertIsNotNone(coll)

        # negative test on drop collection
        with self.assertRaises(TigrisException):
            db.drop_collection('invalid_collection')

        docs = [
            {'id': '1', 'name': 'Tom', 'scores': [2.4, 3.1]},
            {'id': '2', 'name': 'List', 'scores': [2, 1.49]},
            {'id': '3', 'name': 'Jack', 'scores': [89.1, 3]},
            {'id': '4', 'name': 'Jenny', 'scores': [41.5, 3.15]},
        ]
        # insert documents should succeed
        self.assertTrue(coll.insert_many(docs))

        found = coll.find_many()
        self.assertCountEqual(found, docs)

        # finally
        self.assertTrue(db.drop_collection(self.coll_name))
