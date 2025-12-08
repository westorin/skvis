from main.wrappers.datawrapper import DataWrapper
from main.wrappers.logicwrapper import LogicWrapper

data = DataWrapper()
logic = LogicWrapper(data)

logic.tournament_manager.export_tournament_results("YOLO","/Users/krissi/Documents/GitHub/skvis/main/IO/csv")