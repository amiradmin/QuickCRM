from locust import HttpLocust, TaskSet, task
import json


class UserBehavior(TaskSet):
    def __init__(self, parent):
        super(UserBehavior, self).__init__(parent)
        self.token = ""
        self.headers = {}


def on_start(self):
    self.token = self.login()
    self.headers = {'Authorization': 'Token ' + self.token}


def login(self):
    response = self.client.post("/", data={'username': 'amiradmin', 'password': 'Eddy@747', 'Login': 'Login'})
    return json.loads(response._content)['key']


@task(2)
def index(self):
    self.client.get("/admin/", headers=self.headers)

#
# @task(1)
# def profile(self):
#     self.client.get("/profile/", headers=self.headers)
#

class WebsiteUser(HttpLocust):
    task_set = UserBehavior
    min_wait = 5000
    max_wait = 9000
