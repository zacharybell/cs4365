import numpy
from scipy import special as ss
from sklearn import preprocessing as pps

def main():
	
		# reads in all the resource files
    xtest = numpy.loadtxt(fname="../res/xtest.txt", delimiter=",") / 255
    ytest = numpy.loadtxt(fname="../res/ytest.txt", delimiter=",")

    W0 = numpy.loadtxt(fname="../res/W0.txt", delimiter=",")
    W1 = numpy.loadtxt(fname="../res/W1.txt", delimiter=",")
    W2 = numpy.loadtxt(fname="../res/W2.txt", delimiter=",")

    B0 = numpy.loadtxt(fname="../res/B0.txt", delimiter=",")
    B1 = numpy.loadtxt(fname="../res/B1.txt", delimiter=",")
    B2 = numpy.loadtxt(fname="../res/B2.txt", delimiter=",")

		# set up the encoder
    enc = pps.OneHotEncoder(n_values=[10])

		# layers
    H0 = numpy.clip(first_deg(xtest, W0, B0), 0, None)
    H1 = numpy.clip(first_deg(H0, W1, B1), 0, None)
    H2 = numpy.clip(first_deg(H1, W2, B2), 0, None)

		# sigmoid
    H2 = ss.expit(H2)

    # converts ytest from 1D to 2D (10000 X 1) then to a 1 hot enc array
    ytest = enc.fit_transform(numpy.reshape(ytest, (-1, 1))).toarray()

    H2 = enc.fit_transform(numpy.reshape(numpy.argmax(H2, axis=1), (-1, 1))).toarray()

    print(compare_one_hot(H2, ytest))

def first_deg(X, W, B):
    return [B + i for i in numpy.dot(X, W)]

def max_only(X):
    return

def compare_one_hot(A, B):
    l = len(A)
    if (l == 0):
        raise Exception("matrix cannot be of length 0")
    if (l != len(B)):
        raise Exception("matrix lengths don't match")
    counter = 0
    for a, b in zip(A, B):
        if (a == b).all():
            counter += 1
    return counter / l

if __name__ == "__main__":
    main()
