# Hello World Iron Python
import sys
sys.LoadAssemblyFromFile("HelloIron.dll")
import IronPyTest

f = IronPyTest.IronPythonTest()
f.greeting()
