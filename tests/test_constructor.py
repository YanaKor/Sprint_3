from pages.constructor import Constructor


class TestConstructor:
    def test_transition_to_sauces_tab(self, driver):
        constructor = Constructor(driver)

        constructor.click_on_sauce_tab()
        constructor.check_transition_to_sauce_tab()

    def test_transition_to_bunks_tab(self, driver):
        constructor = Constructor(driver)

        constructor.click_on_sauce_tab()
        constructor.click_on_bunks_tab()
        constructor.check_transition_to_bunks_tab()

    def test_transition_to_stuffing_tab(self, driver):
        constructor = Constructor(driver)

        constructor.click_on_stuffing_tab()
        constructor.check_transition_to_stuffing_tab()
