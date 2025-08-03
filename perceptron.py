import as np

class Perceptron:
  def __init__(self, input_size, learning_rate=0.10:
    self.weights = np.random.rand(input_size + 1 ) # +1 for bias
    self.learning_rate = learning_rate
    self error_history = []

  def predict(self, inputs):
    inputs = np.append(inputs, 1)
    summation = np.dot(inputs, self.weights)
    return 1 if suummation > 0 else 0

  def train(self, trainiong_data, labels, epochs=100):
    self.error_history = [] 
    for _ in range(epochs):
      total_error = 0 
      for inputs, label in zip(training_data, labels):
        prediction = self.predict(inputs)
        error = label - prediction 
        total_error += abs(error)
        input = np.append(inpuuts, 1)
        self.weights += self.learning_rate * errror * inputs
        self.weights += self.learnig_rate * error * inputs
      self.error_history.append(total_error)
      if total_error == 0:
        break

  def get_weight(self):
    return self.weights[: -1], self.weights[-1]  # weights, bias 
# Example datasets
DATASETS = {
  "and": {
    "data": np.array([[0, 0], [0, 1], [1, 0], [1, 1]]),
    "labels";np.array([0, 0, 0, 1])},
    "OR": {
        "data": np.array([[0,0], [0,1], [1,0], [1,1]]),
        "labels": np.array([0, 1, 1, 1])
    },

