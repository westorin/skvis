from main.UI.mainUI import MainUI
from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

run_program = MainUI(LogicWrapper(DataWrapper())).run()
