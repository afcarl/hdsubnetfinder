import unittest
import cStringIO
from hdsubnetfinder.kernel.kernel_generator import KernelGenerator

class KernelGeneratorTests(unittest.TestCase):


    def test_kernel_generator_network(self):
        print('\n---------- Kernel Generator tests start -----------\n')

        generator = KernelGenerator()

        small_network = 'https://s3-us-west-2.amazonaws.com/ci-service-data/small.sif'
        med_network = 'https://s3-us-west-2.amazonaws.com/ci-service-data/yeastHighQuality.sif'

        generator.compute_kernel(small_network)


        output = cStringIO.StringIO()
        kernel = generator.get_kernel(output)
        output.close()
        self.assertIsNotNone(kernel)

        print(len(kernel))

        import pandas as pd
        input_stream = cStringIO.StringIO(kernel)
        df = pd.read_csv(input_stream, sep='\t')
        input_stream.close()
        self.assertIsNotNone(df)

        print(df.head())

        print('\n---------- Generator tests finished! -----------\n')
