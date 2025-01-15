class SupervisedLearning:
    def __init__(self):
        self.response = {}

    def teach_response(self, trigger, response):
        self.responses[trigger] + response
    def get_responses(self, trigger):
        return self.responses.get(trigger, "I don't know how to respond to that quite yet my man.")        