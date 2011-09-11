# -*- coding: utf-8 -*-
from fake_webapp import EXAMPLE_APP

class MouseInteractionTest(object):

    def test_mouse_over(self):
        "Should be able to perform a mouse over on an element"
        self.browser.visit(EXAMPLE_APP)
        self.browser.find_by_css(".add-element-mouseover").first.mouseover()
        assert self.browser.is_element_present_by_id('what-is-your-name')

    def test_mouse_out(self):
        "Should be able to perform a mouse out on an element"
        self.browser.visit(EXAMPLE_APP)
        element = self.browser.find_by_css(".add-element-mouseover").first
        element.mouseover()
        element.mouseout()

    def test_double_click(self):
        "double click should shows a hidden element"
        button = self.browser.find_by_css(".db-button").first
        button.double_click()
        assert self.browser.find_by_css(".should-be-visible-after-double-click").visible
        assert self.browser.is_element_not_present_by_id('what-is-your-name')

    def test_right_click(self):
        "should be able to perform a right click on an element"
        element = self.browser.find_by_css(".right-clicable")
        element.right_click()
        assert self.browser.find_by_css('.right-clicable').text == 'right clicked' 

    def test_drag_and_drop(self):
        "should be able to perform a drag an element and drop in another element"
        droppable = self.browser.find_by_css('.droppable')
        draggable = self.browser.find_by_css('.draggable')
        draggable.drag_and_drop(droppable)
        assert self.browser.find_by_css('.dragged').text == 'yes'