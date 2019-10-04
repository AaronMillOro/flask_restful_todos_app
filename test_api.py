import unittest
import models

from app import app


class TodoTests(unittest.TestCase):
    def setUp(self):
        models.initialize()
        self.app = app.test_client()

    def tearDown(self):
        models.DATABASE.drop_tables(models.Todo)
        models.DATABASE.close()

    def test_index_page(self):
        index = self.app.get('/')
        self.assertEqual(index.status_code, 200)
        self.assertTrue('My TODOs!' in index.get_data(as_text=True))

    def test_get(self):
        todo1 = self.app.post('/api/v1/todos', data={'name': 'TODO 1'})
        resp_get = self.app.get('/api/v1/todos')
        self.assertEqual(resp_get.status_code, 200)
        self.assertIn('TODO 1', str(resp_get.data))

    def test_post(self):
        resp_post = self.app.post('/api/v1/todos', data={'name': 'TODO 1'})
        self.assertEqual(resp_post.status_code, 201)
        self.assertIn('TODO 1', str(resp_post.data))

    def test_put(self):
        todo1 = self.app.post('/api/v1/todos', data={'name': 'TODO 1'})
        resp_put = self.app.put('/api/v1/todos/1', data={'name': 'TODO new'})
        self.assertEqual(resp_put.status_code, 200)
        self.assertIn('TODO new', str(resp_put.data))

    def test_delete(self):
        todo1 = self.app.post('/api/v1/todos', data={'name': 'TODO 1'})
        resp_delete = self.app.delete('/api/v1/todos/1')
        self.assertEqual(resp_delete.status_code, 204)
        self.assertNotIn('TODO 1', str(resp_delete.data))


if __name__ == '__main__':
    unittest.main()
