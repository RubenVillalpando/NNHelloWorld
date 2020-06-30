import network
import mnist_loader as ml

if __name__ == '__main__':

    net = network.Network([2, 3])
    training_data, validation_data, test_data = ml.load_data_wrapper()