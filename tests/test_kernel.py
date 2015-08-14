# -*- coding: utf-8 -*-
import unittest
import os

KERNEL_LOCATION = 'resource/kernel.txt'
k_file = os.path.abspath(os.path.dirname(__file__)) + '/' + KERNEL_LOCATION
SAMPLE_KERNEL_URL = 'file://' + k_file
print(SAMPLE_KERNEL_URL)


class KernelTests(unittest.TestCase):

    def test_pre_computed_kernel(self):

        from hdsubnetfinder.kernel.kernel_from_file import KernelFromFile
        small_kernel = KernelFromFile(pre_computed_kernel_url=SAMPLE_KERNEL_URL)

        self.assertIsNotNone(small_kernel)
        self.assertIsNotNone(small_kernel.kernel)
        self.assertIsNotNone(small_kernel.labels)

        self.assertTrue(list, type(small_kernel.labels))
        self.assertTrue(list, type(small_kernel.kernel))


        print(small_kernel.labels)
