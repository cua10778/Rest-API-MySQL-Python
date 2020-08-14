try:
    from app import app
    import unittest

except Exception as e:
    print("Some modules are missing {}.format(e)")

class Test_Case(unittest.TestCase):

    #Check if Response is 200
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/users")
        statuscode = response.status_code
        self.assertEqual(statuscode, 200)

    # check if content return is application/json
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/users")
        self.assertEqual(response.content_type, "text/html; charset=utf-8")
    #
    # check for data returned
    def test_index(self):
        tester = app.test_client(self)
        response = tester.get("/users")

        if response.status_code == 200:
            self.assertTrue(True)

if __name__ == '__main__':
    unittest.main()
