import csv
import urllib2

import numpy as np
from scipy.sparse import csc_matrix
from kernel import Kernel


class KernelFromFile(Kernel):

    def __init__(self, pre_computed_kernel_url):
        """
        Input:
            pre_computed_kernel_file - filename of tab delemited kernel file,
                                        as made by KernelGenerator
        """
        self.__read_kernel_file(pre_computed_kernel_url)

    def __read_kernel_file(self, pre_computed_kernel_url):
        ker = []
        start = True
        for line in csv.reader(urllib2.urlopen(pre_computed_kernel_url), delimiter='\t'):
            if start:
                self.labels = line[1:]
                start = False
            else:
                ker.append([float(x) for x in line[1:]])

        self.kernel = csc_matrix(np.asarray(ker))
