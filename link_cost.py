# ------------------- Switch List -------------------------
# s1,s2,s3,s4,s5
# link -> cost
# s1 - s2 = 1
# s1 - s3 = 2
# s2 - s4 = 3
# s3 - s5 = 4
# s4 - s5 = 5

global link_array[][]


def data_link_cost(src, dst):

    # link_array = {([src],[dst]) = [cost]), .. }
    link_dict = {
        (1, 2): 1,
        (1, 3): 1,
        (2, 4): 1,
        (3, 4): 1,
        (4, 5): 1,
        # reverse
        (1, 2): 1,
        (1, 3): 1,
        (2, 4): 1,
        (3, 4): 1,
        (4, 5): 1,
    }

    return link_dict[src, dst]
