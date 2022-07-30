from locust import HttpUser, TaskSet, task, between

class UserBehavior(TaskSet):
    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        self.login()

    def on_stop(self):
        """ on_stop is called when the TaskSet is stopping """
        self.logout()

    def login(self):
        self.client.post("", {"username":"amiradmin", "password":"Eddy@747"})

    def logout(self):
        self.client.post("/logout", {"username":"amiradmin", "password":"Eddy@747"})

    @task(2)
    def index(self):
        self.client.get("")
    #
    # @task(1)
    # def profile(self):
    #     self.client.get("/profile")

class ListProduct(HttpUser):
    @task(1)
    def product_list(self):
        self.client.get("/api/getproductlist/")


class WebsiteUser(HttpUser):
    tasks = [ListProduct]
    # wait_time = between(5, 9)


