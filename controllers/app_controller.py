from PyQt6.QtWidgets import QApplication
import sys

# Import all UI controllers
from controllers.main_ui_controller import MainUiController
from controllers.fin_obj_ui_controller import FinancialObjectiveController
from controllers.risk_ui_controller import RiskProfilingController
from controllers.know_exp_ui_controller import KnowledgeExperienceController
from controllers.invest_pref_ui_controller import InvestmentPreferencesController

class AppController:
    def __init__(self):
        self.app = QApplication(sys.argv)
        self.main_controller = MainUiController(self)
        self.fin_obj_controller = FinancialObjectiveController(self)
        self.risk_controller = RiskProfilingController(self)
        self.know_exp_controller = KnowledgeExperienceController(self)
        self.invest_pref_controller = InvestmentPreferencesController(self)

    def show_main(self):
        self.main_controller.show()

    def show_fin_obj(self):
        self.fin_obj_controller.show()

    def show_risk(self):
        self.risk_controller.show()

    def show_know_exp(self):
        self.know_exp_controller.show()

    def show_invest_pref(self):
        self.invest_pref_controller.show()

    def run(self):
        self.show_main()
        return self.app.exec()

if __name__ == "__main__":
    controller = AppController()
    sys.exit(controller.run())