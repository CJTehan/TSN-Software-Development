# Using Tensorflow
import tensorflow as tf

# Create two constants
a = tf.constant(5)
b = tf.constant(3)

# Perform some basic operations
total = tf.add(a, b)
product = tf.multiply(a, b)
difference = tf.subtract(a, b)
quotient = tf.divide(a, b)

# Print the results
print("Sum: ", total.numpy())
print("Product :", product.numpy())
print("Difference: ", difference.numpy())
print("Quotient: ", quotient.numpy())
