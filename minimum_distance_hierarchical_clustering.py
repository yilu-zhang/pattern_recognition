import math


def read_features_from_file(filename):
    print("The features is:")
    i = 1
    features = {}
    with open(filename) as f:
        for line in f.readlines():
            f_key = str(i)
            features[f_key] = [int(x) for x in line.split()]
            print('x' + f_key + ':')
            print(features[f_key])
            i = i + 1
    return features


def distance(x1, x2):
    i = 0
    square_sum = 0
    for x in x1:
        square_sum = square_sum + pow(x - x2[i], 2)
        i = i + 1
    return math.sqrt(square_sum)


def distance_map(features):
    i = 1
    dist_map = {}
    map_key = features.keys()
    for key1 in map_key:
        for key2 in map_key:
            if key1 < key2:
                dist_map[key1 + '|' + key2] = distance(features.get(key1), features.get(key2))
        i = i + 1
    return dist_map


def clustering(class_num):
    features = read_features_from_file("features.txt")
    f_num = len(features)

    if (class_num > f_num):
        print("Error:The number of input categories is too large. Please restart and enter a smaller value!")
        exit(-1)
    if (class_num < 1):
        print("Error:The number of input categories should be greater than 1. Please restart and enter a larger value!")
        exit(-1)

    result = []
    class_result = []
    result.append(features.keys())
    class_result.append(features.keys())
    dist_map = []
    dist_map.append(distance_map(features))

    iter_num = f_num - class_num
    iter_cn = 0
    # print(result[0])
    print(dist_map[0])
    while iter_cn < iter_num:
        min_key = '12'
        min_dist = float("inf")
        for key1 in dist_map[iter_cn].keys():
            if (dist_map[iter_cn].get(key1) < min_dist):
                min_key = key1
                min_dist = dist_map[iter_cn].get(key1)
        set1 = []
        set2 = []
        temp_map = {}
        min_key_list = min_key.split('|')
        min_key_str = min_key_list[0] + min_key_list[1]
        # print(min_key)
        delete_list = []
        delete_idx = 0
        for key in result[iter_cn]:
            if key not in min_key_list:
                set1.append(key)  # 1 2 3|5 4
            else:
                set2.append(key)  # 3|5|4
                delete_list.append(delete_idx)
            delete_idx = delete_idx + 1

        for key1 in set1:
            for key2 in set1:
                if key1 < key2:
                    temp_map[key1 + '|' + key2] = dist_map[iter_cn].get(key1 + '|' + key2)

        for key in set1:
            value = []
            for i in range(len(set2)):
                if set2[i] < key:
                    value.append(dist_map[iter_cn].get(set2[i] + '|' + key))
                else:
                    value.append(dist_map[iter_cn].get(key + '|' + set2[i]))

            if key < min_key_str:
                if value[0] < value[1]:
                    temp_map[key + '|' + min_key_str] = value[0]
                else:
                    temp_map[key + '|' + min_key_str] = value[1]
            else:
                if value[0] < value[1]:
                    temp_map[min_key_str + '|' + key] = value[0]
                else:
                    temp_map[min_key_str + '|' + key] = value[1]

        pre_class_result = list(class_result[iter_cn])
        pre_class_result.append((pre_class_result[delete_list[0]] + '|' + pre_class_result[delete_list[1]]))
        class_result.append(pre_class_result)
        set1.append(min_key_str)
        iter_cn = iter_cn + 1
        dist_map.append(temp_map)
        result.append(set1)
        class_result[iter_cn].pop(delete_list[0])
        class_result[iter_cn].pop(delete_list[1] - 1)
        # print(result[iter_cn])
        # print(class_result[iter_cn])
        print(dist_map[iter_cn])

    print("\nThe classification results are as follows:")
    i = 0
    for cla in class_result[iter_cn]:
        i = i + 1
        print("class " + str(i) + ':')
        cla_idx_list = [int(x) for x in cla.split('|')]
        cla_idx_list.sort()
        cla_display_list = ['x' + str(cla_idx) + ' ' for cla_idx in cla_idx_list]
        cla_diaplay_str = ""
        for fea in cla_display_list:
            cla_diaplay_str = cla_diaplay_str + fea
        print(cla_diaplay_str)
