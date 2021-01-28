import numpy as np
import matplotlib.pyplot as plt


class LinearRegression:
	

	def estimate_coef(self, x, y):
		# number of observations/points
		n = np.size(x)

		# mean of x and y vector
		m_x = np.mean(x)
		m_y = np.mean(y)
		
		# calculating cross-deviation and deviation about x
		SS_xy = np.sum((x - m_x) * (y - m_y))
		SS_xx = np.sum((x - m_x) * (x - m_x))
		
		# calculating regression coefficients
		b_1 = SS_xy / SS_xx
		b_0 = m_y - b_1*m_x
	 
		return(b_0, b_1)
	 
	

	def lr(self, l1, l2):

		# observations
		# x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
		# y = np.array([1, 3, 2, 5, 7, 8, 8, 9, 10, 12])
		
		x = np.array(l1)
		y = np.array(l2)

		# estimating coefficients
		b = self.estimate_coef(x, y)

		print("Estimated coefficients:\nb_0 = {}  \
		  \nb_1 = {}".format(b[0], b[1]))
		
		# plotting regression line
		# self.plot_regression_line(x, y, b)

	

	def plot_regression_line(self, x, y, b):
		# plotting the actual points as scatter plot
		plt.scatter(x, y, color = "b", marker = "o", s = 10)
	 
		# predicted response vector
		y_pred = b[0] + b[1]*x
	 
		# plotting the regression line
		plt.plot(x, y_pred, color = "r")
	 
		# putting labels
		plt.xlabel('x')
		plt.ylabel('y')

		# function to show plot
		plt.show()
		