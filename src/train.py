import argparse
import multiprocessing
import dlib

parser = argparse.ArgumentParser(description="Train a pupil shape predictor")
parser.add_argument('dataset', metavar='d', type=str)
parser.add_argument('output', metavar='o', type=str)

args = parser.parse_args()

print("[INFO] setting shape predictor options...")
options = dlib.shape_predictor_training_options()

# range [2.8]
options.tree_depth = 5

# range [0-1]
options.nu = 0.1

# rage [6,18]
options.cascade_depth = 15

# more pixels more accurate probably, but more slower
options.feature_pool_size = 400

# the more num_test_splits more accurate but more time do train
options.num_test_splits = 50

# range [0, 50]
options.oversampling_amount = 5

# range [0, 0.5]
options.oversampling_translation_jitter = 0.1

# print information while trainig
options.be_verbose = True

options.num_threads = multiprocessing.cpu_count()

print("[INFO] start trainig...")
dlib.train_shape_predictor(args.dataset, args.output, options)
