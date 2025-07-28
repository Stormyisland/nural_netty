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
      for inputs, lsbel in zip(training_data, labels):
