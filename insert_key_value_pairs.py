import hash_tables
import avl_tree
import gen_data
import random
import time
import matplotlib.pyplot as plt
import binary_tree
import sys
import os
import argparse
import matplotlib
matplotlib.use('Agg')
sys.path.insert(1, "hash-tables-tlfobe")  # noqa: E402

sys.setrecursionlimit(20000)


def get_key_value_pairs_from_file(file, n_values):
    if not os.path.isfile(file):
        raise FileNotFoundError(
            "get_key_value_pairs_from_file: File not found!")
    if os.path.isdir(file):
        raise IsADirectoryError(
            "get_key_value_pairs_from_file: Input not a file!")

    keys = []
    values = []
    count = 0
    with open(file, "r") as fh:
        for line in fh:
            if count < n_values:
                line_data = line.rstrip().split(' ')
                if len(line_data) != 2:
                    raise IOError(
                        "get_key_value_pairs_from_file: Incorrect file format")
                keys.append(line_data[0])
                values.append(line_data[1])
                count += 1
            else:
                break
    return keys, values


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--data_struct",
                        help="type of data structure to use for storing data",
                        choices=["hash", "AVL", "tree"],
                        required=True
                        )
    parser.add_argument("--data_file",
                        help="data file to pull keys/value pairs from",
                        required=True,
                        )
    parser.add_argument("--n_values",
                        help="number of hash values to pull" +
                        " from the data file",
                        default="10000",
                        )
    parser.add_argument("--sub_sample",
                        help="fraction of samples to test searching values",
                        default="0.2"
                        )
    parser.add_argument("--outfile",
                        help="name of file to write to",
                        default="out.png"
                        )

    args = parser.parse_args()

    str_to_data_strct_map = {"hash": hash_tables.ChainedHash,
                             "AVL": avl_tree.AVLTree,
                             "tree": binary_tree.BinaryTree}

    data_struct = str_to_data_strct_map[args.data_struct]
    # Load in Data

    keys, values = get_key_value_pairs_from_file(
        args.data_file, int(args.n_values))

    # Time it takes to insert

    data_struct_instance = data_struct()

    add_times = []
    for key, value in zip(keys, values):
        t0 = time.time()
        data_struct_instance.insert(key, value)
        t1 = time.time()
        add_times.append(t1 - t0)

    # Time it takes to search subset of data

    sample_keys = random.sample(keys, round(
        int(args.n_values)*float(args.sub_sample)))
    search_times = []
    for key in sample_keys:
        t0 = time.time()
        val = data_struct_instance.search(key)
        t1 = time.time()
        search_times.append(t1 - t0)

    # Time it takes to search for not in database
    not_in_db = []
    while len(not_in_db) < int(args.n_values)*float(args.sub_sample):
        word = gen_data.random_string()
        if word not in keys:
            not_in_db.append(word)
    not_in_db_times = []
    for key in not_in_db:
        t0 = time.time()
        val = data_struct_instance.search(key)
        t1 = time.time()
        not_in_db_times.append(t1 - t0)
        assert val == -1

    plt.subplots_adjust(wspace=5)
    fig, ax = plt.subplots(nrows=1, ncols=3, dpi=500, figsize=[15, 5])
    fig.tight_layout()
    # fig = plt.figure(figsize=(10,3), dpi=300)
    # ax = fig.add_subplot(1,1,1)
    # ax.boxplot([add_times, search_times, not_in_db_times])
    #
    # names = [args.data_struct +
    #          plot_type for plot_type in
    #          [" Add Time", " Search Time", " Full Search Time"]]
    # ax.xticks(names)

    ax[0].boxplot(add_times)
    ax[0].set_xlabel(args.data_struct + " Add Time")
    ax[0].set_ylabel("Time (seconds)")
    ax[0].tick_params(labelsize=6)
    ax[1].boxplot(search_times)
    ax[1].set_xlabel(args.data_struct + " Search Time")
    ax[1].tick_params(labelsize=6)
    ax[2].boxplot(not_in_db_times)
    ax[2].set_xlabel(args.data_struct + " Full Search Time")
    ax[2].tick_params(labelsize=6)

    if args.outfile.split(".")[-1] != "png":
        args.outfile += ".png"

    plt.savefig(args.outfile, bbox_inches="tight")


if __name__ == "__main__":
    main()
