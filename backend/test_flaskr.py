import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        self.database_path = 'postgresql://{}:{}@{}/{}'.format('postgres', 'pizza10', 'localhost:5432', self.database_name)
        setup_db(self.app, self.database_path)

        self.new_question = {"question": "What  is the most populated country", "answer": "China", "category": 5, "difficulty": "5"}
         # mock request data
        self.request_data = {
            'previous_questions': [2, 7],
            'quiz_category': {
                'type': 'History',
                'id': 3
            }
        }
        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()
    
    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
    # Test question and categories
    # def test_get_paginated_questions(self):
    #     res = self.client().get('/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(len(data["questions"]))
    #     self.assertTrue(data["total_questions"])
    #     self.assertEqual(data["current_category"], None)
    #     self.assertTrue(data["categories"])

    # def test_get_categories(self):
    #     res = self.client().get('/categories')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["categories"]) 

    # # Test Delete

    # def test_delete_question(self):
    #     res = self.client().delete("/questions/2")
    #     data = json.loads(res.data)

    #     question = Question.query.filter(Question.id == 2).one_or_none()

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["total_questions"])
    #     self.assertTrue(len(data["questions"]))
    #     self.assertEqual(question, None)

    # def test_422_if_question_does_not_exist(self):
    #     res = self.client().delete("/questions/1200")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "unprocessable")

    # Test post
    # def test_create_new_question(self):
    #     res = self.client().post("/questions", json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["created"])
    #     self.assertTrue(len(data["questions"]))

    # def test_405_if_question_creation_not_allowed(self):
    #     res = self.client().post("/books/45", json=self.new_question)
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 405)
    #     self.assertEqual(data["success"], False)
    #     self.assertEqual(data["message"], "method not allowed")

    # Test search
    def test_get_question_search_with_results(self):
        res = self.client().post("/questions/search", json={"search": "country"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertTrue(data["total_questions"])
        self.assertEqual(len(data["questions"]), 7)

    def test_get_question_search_without_results(self):
        res = self.client().post("/questions/search", json={"search": "laughter"})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data["success"], True)
        self.assertEqual(data["total_questions"], 0)
        self.assertEqual(len(data["questions"]), 0)


    # def test_get_question_by_category(self):
    #     res = self.client().get("/questions/6/questions")
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 200)
    #     self.assertEqual(data["success"], True)
    #     self.assertTrue(data["total_questions"])
    #     self.assertEqual(len(data["questions"]), 0) 

    # def test_422_error_category_id(self):
    #     res = self.client().get('/categories/1776/questions')
    #     data = json.loads(res.data)

    #     self.assertEqual(res.status_code, 422)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Unprocessable entity')

    # def test_play_quiz_questions(self):

       

    #     # make request and process response
    #     response = self.client().post('/quizzes', json=self.request_data)
    #     data = json.loads(response.data)

    #     # Assertions
    #     self.assertEqual(response.status_code, 200)
    #     self.assertEqual(data['success'], True)
    #     self.assertTrue(data['question'])

    #     # Ensures previous questions are not returned
    #     self.assertNotEqual(data['question']['id'], 2)
    #     self.assertNotEqual(data['question']['id'], 7)

    #     # Ensures returned question is in the correct category
    #     self.assertEqual(data['question']['category'], 3)

    # def test_error_400_data_to_play_quiz(self):

    #     # process response from request without sending data
    #     response = self.client().post('/quizzes', json={})
    #     data = json.loads(response.data)

    #     # Assertions
    #     self.assertEqual(response.status_code, 400)
    #     self.assertEqual(data['success'], False)
    #     self.assertEqual(data['message'], 'Bad request')



    

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()