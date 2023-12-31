from unittest import TestCase

from app import app, games

# Make Flask errors be real errors, not HTML pages with error info
app.config['TESTING'] = True

# This is a bit of hack, but don't use Flask DebugToolbar
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']


class BoggleAppTestCase(TestCase):
    """Test flask app of Boggle."""

    def setUp(self):
        """Stuff to do before every test."""

        self.client = app.test_client()
        app.config['TESTING'] = True

    def test_homepage(self):
        """Make sure information is in the session and HTML is displayed"""

        with self.client as client:
            response = client.get('/')
            ...
            # test that you're getting a template
            html = response.get_data(as_text=True)

            self.assertIn('<table class="board', html)


    def test_api_new_game(self):
        """Test starting a new game."""

        with self.client as client:

            resp = client.post("/api/new-game")
            json_resp = resp.get_json()

            # breakpoint()
            self.assertIsInstance(json_resp['game_id'], str)
            self.assertIsInstance(json_resp['board'], list)
            self.assertIn(json_resp['game_id'], games)
            #TODO: DO we need to turn the jsonified list into a list?
            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # test that the game_id is a string
            # test that the board is a list
            # test that the game_id is in the dictionary of games (imported from app.py above)

    def test_score_word(self):
        """Test if word is valid"""

        with self.client as client:
            resp = client.post("/api/new-game")
            json_resp = resp.get_json()

            game_id = json_resp['game_id']
            test_word = 'SLJDKFLS'
            games[game_id].board = [["C","A","T"], ["O", "X", "X"], ["X", "G", "X"]]
            score_resp = client.post("/api/score-word", json={'game_id': game_id, 'word': test_word})
            score_json = score_resp.get_json()
            # breakpoint()
            self.assertEqual({'result': 'ok'}, score_json)

            # make a post request to /api/new-game
            # get the response body as json using .get_json()
            # find that game in the dictionary of games (imported from app.py above)

            # manually change the game board's rows so they are not random

            # test to see that a valid word on the altered board returns {'result': 'ok'}
            # test to see that a valid word not on the altered board returns {'result': 'not-on-board'}
            # test to see that an invalid word returns {'result': 'not-word'}




























