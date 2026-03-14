import numpy as np

# Neural network weights and biases (trained example)
w0 = np.array([[ 1.19627687e+01,  2.60163283e-01],
               [ 4.48832507e-01,  4.00666119e-01],
               [-2.75768443e-01,  3.43724167e-01],
               [ 2.29138536e+01,  3.91783025e-01],
               [-1.22397711e-02, -1.03029800e+00]])

w1 = np.array([[11.5631751 , 11.87043684],
               [-0.85735419,  0.27114237]])

w2 = np.array([[11.04122165],
               [10.44637262]])

b0 = np.array([-4.21310294, -0.52664488])
b1 = np.array([-4.84067881, -4.53335139])
b2 = np.array([-7.52942418])

# Activation functions
def relu(z):
    return np.maximum(0, z)

def linear(z):
    return z

# Function to predict price
def predict_price(features):
    # First hidden layer
    h1_in = np.dot(features, w0) + b0
    h1_out = relu(h1_in)

    # Second hidden layer
    h2_in = np.dot(h1_out, w1) + b1
    h2_out = relu(h2_in)

    # Output layer
    o_in = np.dot(h2_out, w2) + b2
    prediction = linear(o_in)

    return prediction[0]

if __name__ == "__main__":
    # Test cabin feature vector
    test_cabin = np.array([82, 2, 65, 3, 516])
    price = predict_price(test_cabin)
    print(f"Predicted cabin price: {price:.2f} €")
