import unittest
from buildSolution import BuildSolution
import filecmp

class Testing(unittest.TestCase):

    def parseTestcases(self):
        for i in range(1,4):
            BuildSolution().mainFunc("Testcases/input/testcase"+str(i)+".txt", "Testcases/output/testcase"+str(i)+".txt")
            self.test_check("Testcases/output/testcase"+str(i)+".txt", "Testcases/ref_output/testcase"+str(i)+".txt")

    def test_check(self,outputfile,reffile):
        try:
            self.assertTrue(filecmp.cmp(outputfile, reffile, shallow=False))
            print("Testcase passed for", outputfile)
        except:
            print("Testcase failed for", reffile)

Testing().parseTestcases()