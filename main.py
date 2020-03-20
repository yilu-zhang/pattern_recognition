import minimum_distance_hierarchical_clustering as mdhc

if __name__ == '__main__':
    print("Please enter the number of categories:")
    cat_num = input()
    cat_num = int(cat_num)
    print("The number of categories is:" + str(cat_num))
    mdhc.clustering(cat_num)

    # 0 1 3 1 3 4
    # 3 3 3 1 2 1
    # 1 0 0 0 1 1
    # 2 1 0 2 2 1
    # 0 0 1 0 1 0

