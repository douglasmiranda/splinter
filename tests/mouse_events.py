from nose.tools import assert_true

class MouseEventsTests(object):

    def test_should_be_able_to_hover_over_an_element(self):
        element = self.browser.find_by_css('a.add-element-mouseover').first
        element.hover()
        assert_true(self.browser.is_element_present_by_xpath('//label[@class="over-label"]'))
