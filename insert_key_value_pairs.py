import binary_tree
import sys
import os
import argparse
import time
import random
import gen_data
sys.path.insert(1, "hash-tables-tlfobe")  # noqa: E402
sys.path.insert(1, "avl_tree")  # noqa: E402
import hash_tables
import avl


def get_key_value_pairs_from_file(file):
    if not os.path.isfile(file):
        raise FileNotFoundError(
            "get_key_value_pairs_from_file: File not found!")
    if os.path.isdir(file):
        raise IsADirectoryError(
            "get_key_value_pairs_from_file: Input not a file!")

    keys = []
    values = []
    with open(file, "r") as fh:
        for line in fh:
            line_data = line.rstrip().split(' ')
            if len(line_data) != 2:
                raise IOError(
                    "get_key_value_pairs_from_file: Incorrect file format")
            keys.append(line_data[0])
            values.append(line_data[1])
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
                        help = "number of samples to test searching",
                        default="0.2"
    )

    args = parser.parse_args()

    str_to_data_strct_map = {"hash": hash_tables.ChainedHash,
                             "AVL": avl.AVL, "tree": binary_tree.BinaryTree}

    data_struct = str_to_data_strct_map[args.data_struct]
    print(data_struct)
    # Load in Data

    keys, values = get_key_value_pairs_from_file(args.data_file)

    # Time it takes to insert

    data_struct_instance = data_struct()

    add_times = []
    for key, value in zip(keys, values):
        t0 = time.time()
        data_struct_instance.insert(key, value)
        t1 = time.time()
        add_times.append(t1 - t0)

    # Time it takes to search subset of data

    sample_keys = random.sample(keys, round(int(args.n_values)*float(args.sub_sample)))
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
    
    print(add_times)
    print(search_times)
    print(not_in_db_times)
        

if __name__ == "__main__":
    main()
