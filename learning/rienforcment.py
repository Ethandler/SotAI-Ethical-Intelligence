class ReinforcmentLearning:
    def __init__ (self): # type: ignore
        self.feedback = {} # Store feedback for responses

    def add_feedback(self, response, feedback_type):
        """
        Update feedback for a response
        feedback_type "like" or "dislike"
        """
        if response not in self.feedback:
            self.feedback[response] = {"like": 0, "dislike": 0}
        self.feedback[response][feedback_type] += 1

    def adjust_weights(self, response):
        """
        Adjust weights based on feedback
        """
        if response in self.feedback:
            likes = self.feedback[response]["like"]
            dislikes = self.feedback[response]["dislike"]
            return likes - dislikes  # Return net score as weight
        return 0       