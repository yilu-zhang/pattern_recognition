import numpy as np


def read_features_from_file(filename):
    print("The features is:")
    features = []
    with open(filename) as f:
        for line in f.readlines():
            line_feature = [int(x) for x in line.split()]
            if line_feature[0] == 0:
                line_feature.pop(0)
                line_feature.append(1)
            else:
                line_feature.pop(0)
                line_feature = [x * -1 for x in line_feature]
                line_feature.append(-1)
            print(line_feature)
            features.append(line_feature)
    return np.array(features)


def perceptron(rho):
    features = read_features_from_file("perceptron_features.txt")
    f_num = features.shape[0]
    dimen = features.shape[1]
    # weight = np.ones(dimen)
    weight = np.zeros(dimen)
    print("\nThe W(0) is:"+str(weight)+". The rho is:"+str(rho)+".\n")

    correct_cnt = 0
    iter_cnt = 0
    print("The iterative process is:")
    while correct_cnt < f_num:
        x_index = iter_cnt % f_num
        result = np.dot(weight, features[x_index])
        if result > 0:
            weight = weight
            correct_cnt = correct_cnt + 1
            print("k=" + str(iter_cnt) + ", " + "d(X" + str(x_index + 1) + ")=" + "W(" + str(
                iter_cnt) + ")*X" + str(x_index + 1) + "=" + str(result) + ", W(" + str(
                iter_cnt + 1) + ")= W(" + str(iter_cnt) + ")=" + str(weight))

        else:
            weight = weight + rho * features[x_index]
            correct_cnt = 0
            print("k=" + str(iter_cnt) + ", " + "d(X" + str(x_index + 1) + ")=" + "W(" + str(
                iter_cnt) + ")*X" + str(x_index + 1) + "=" + str(result) + ", W(" + str(
                iter_cnt + 1) + ")= W(" + str(iter_cnt) + ")+" + str(rho) + "*X" + str(x_index + 1) + "=" + str(weight))
        iter_cnt = iter_cnt + 1
    print("\nThe optimal W is:" + str(weight))
