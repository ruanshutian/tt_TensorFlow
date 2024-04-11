import math
import numpy

def softmax(inMatrix):
    print("="*30)
    m,n = numpy.shape(inMatrix)
    outMaxtrix = numpy.mat(numpy.zeros((m,n)))
    soft_nunm =0
    for idx in range(0, n):
        outMaxtrix[0,idx] = math.exp(inMatrix[0,idx])
        soft_nunm += outMaxtrix[0,idx]
    for idx in range(0,n):
        outMaxtrix[0, idx] = outMaxtrix[0, idx] / soft_nunm
    return outMaxtrix

if __name__ == "__main__":
    print("numpy_and_softmax")
    a = numpy.array([[10,10,10,10,10]])
    res = softmax(a)
    print(res)
