# a python program that prints hello world 
# in main
import numpy as np
import matplotlib.pyplot as plt
# plt.style.use('./deeplearning.mplstyle')

def compute_model_output(x, w, b):
    """
    Computes the prediction of a linear model
    Args:
      x (ndarray (m,)): Data, m examples 
      w,b (scalar)    : model parameters  
    Returns
      f_wb (ndarray (m,)): model prediction
    """
    m = x.shape[0]
    f_wb = np.zeros(m)
    for i in range(m):
        f_wb[i] = w * x[i] + b
        
    return f_wb


x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(f"x_train = {x_train}")
print(f"y_train = {y_train}")
print(f"x_train.shape: {x_train.shape}")
# m = x_train.shape[0]
m = len(x_train)
print(f"Number of training examples is: {m}")

i = 0 # Change this to 1 to see (x^1, y^1)

x_i = x_train[i]
y_i = y_train[i]
print(f"(x^({i}), y^({i})) = ({x_i}, {y_i})")

TEST_SCATTER_PLOT = False
if TEST_SCATTER_PLOT:
  # Plot the data points
  plt.scatter(x_train, y_train, marker='x', c='r')
  # Set the title
  plt.title("Housing Prices")
  # Set the y-axis label
  plt.ylabel('Price (in 1000s of dollars)')
  # Set the x-axis label
  plt.xlabel('Size (1000 sqft)')
  plt.show()

TEST_COMPUTE_MODEL_OUTPUT = True
if TEST_COMPUTE_MODEL_OUTPUT:
  w = 150.0
  b = 170.0
  tmp_f_wb = compute_model_output(x_train, w, b,)
  # Plot our model prediction
  plt.plot(x_train, tmp_f_wb, c='b',label='Our Prediction')

  # Plot the data points
  plt.scatter(x_train, y_train, marker='x', c='r',label='Actual Values')

  # Set the title
  plt.title("Housing Prices")
  # Set the y-axis label
  plt.ylabel('Price (in 1000s of dollars)')
  # Set the x-axis label
  plt.xlabel('Size (1000 sqft)')
  plt.legend()
  plt.show()