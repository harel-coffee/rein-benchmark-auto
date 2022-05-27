####################################################
# Benchmark: script for detecting errors in the datasets
# Authors: Mohamed Abdelaal
# Date: March 2022
# Software AG
# All Rights Reserved
####################################################

# Create a path to the Profiler directory
import argparse as argparse

from rein.auxiliaries.configurations import *
from rein.auxiliaries.datasets_dictionary import datasets_dictionary
from rein.benchmark import Benchmark

####################################################


if __name__ == '__main__':

    # Initialize an argument parser
    parser = argparse.ArgumentParser()
    # Add the parser's options
    parser.add_argument('--dataset_name', default=None, required=True)
    parser.add_argument('--n_iterations', type=int, default=10)
    parser.add_argument('--detect_method', type=DetectMethod, choices=list(DetectMethod), nargs='+', default=None)
    parser.add_argument('--no_ground_truth', action='store_true')
    args = parser.parse_args()

    # Retrieve the input arguments
    dataset_name = args.dataset_name
    iterations = args.n_iterations
    detectors_list = args.detect_method

    # Check if the dataset has a dictionary
    if dataset_name not in datasets_dictionary:
        raise ValueError(f"Dataset {dataset_name} is not known.")
    
    # Instantiate a benchmark object
    app = Benchmark(False, args.no_ground_truth)

    # ======================= Define Experimental settings ==============================

    # Define a list of datasets dataset to run experiments with
    datasets_list = [dataset_name]

    # All detectors are executed, iff empty list is passed to which_detectors
    app.run_detectors(exp_id=1, datasets_list=datasets_list, specified_detectors=detectors_list, iterations=iterations)
    # Obtain the IoU metric between the various detectors for each dataset
    for dataset in datasets_list:
        app.get_iou(dataset)
