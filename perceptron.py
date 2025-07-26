import as np

class Perceptron:
  def __init(self, input_size, learning_rate=0.10:
    self.weights = np.random.rand(input_size + 1 ) # +1 for bias
    self.learning_rate = learning_rate
    self error_history = []

  def predict(self, inputs):
    inputs = np.append(inputs, 1)
    summation = np.dot(inputs, self.weights)
