from base.base_object import BaseObject
from support.assertions import Assertions
from base.locators import ConstructorLocators as Cnstr


class Constructor(BaseObject, Assertions):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def click_on_bunks_tab(self):
        self.click(Cnstr.BUNKS_TAB)

    def click_on_sauce_tab(self):
        self.click(Cnstr.SAUCES_TAB)

    def click_on_stuffing_tab(self):
        self.click(Cnstr.STUFFING_TAB)

    def check_transition_to_bunks_tab(self):
        self.assert_equal(self.get_text(Cnstr.BUNKS_SECTION), self.get_text(Cnstr.BUNKS_TAB))

    def check_transition_to_sauce_tab(self):
        self.assert_equal(self.get_text(Cnstr.SAUCES_SECTION), self.get_text(Cnstr.SAUCES_TAB))

    def check_transition_to_stuffing_tab(self):
        self.assert_equal(self.get_text(Cnstr.STUFFING_SECTION), self.get_text(Cnstr.STUFFING_TAB))

