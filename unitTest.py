import io
import sys
import unittest.mock

from src.managers.assetAllocator import AssetAllocator
from src.util import constants

EXPECTED_OUTPUT_1 = "10593 7897 2272\n23619 11809 3936\n"
EXPECTED_OUTPUT_2 = "15937 14552 6187\n23292 16055 7690\nCANNOT_REBALANCE\n"


class TestValidAssetAllocation1(unittest.TestCase):
    def setUp(self):
        self.testfile = "inputs/input1.txt"
        with open(self.testfile, 'r') as file:
            self.input_lines = [line.strip() for line in file]

        self.asset_all = AssetAllocator(None, self.input_lines)

    def runTest(self):
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput
        self.asset_all.startSelfAllocation()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), EXPECTED_OUTPUT_1)


class TestValidAssetAllocation2(unittest.TestCase):
    def setUp(self):
        self.testfile = "inputs/input2.txt"
        with open(self.testfile, 'r') as file:
            self.input_lines = [line.strip() for line in file]

        self.asset_all = AssetAllocator(None, self.input_lines)

    def runTest(self):
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput
        self.asset_all.startSelfAllocation()
        sys.stdout = sys.__stdout__
        self.assertEqual(capturedOutput.getvalue(), EXPECTED_OUTPUT_2)


class TestInValidAssetAllocation1(unittest.TestCase):
    def setUp(self):
        self.testfile = "inputs/invalidInput1.txt"
        with open(self.testfile, 'r') as file:
            self.input_lines = [line.strip() for line in file]

        self.asset_all = AssetAllocator(None, self.input_lines)

    def runTest(self):
        capturedOutput = io.StringIO()  # Create StringIO object
        sys.stdout = capturedOutput
        self.asset_all.startSelfAllocation()
        sys.stdout = sys.__stdout__
        self.assertIn(capturedOutput.getvalue(), constants.NO_SIP_AMOUNT)


unittest.TextTestRunner().run(TestValidAssetAllocation1())
unittest.TextTestRunner().run(TestValidAssetAllocation2())
unittest.TextTestRunner().run(TestInValidAssetAllocation1())
