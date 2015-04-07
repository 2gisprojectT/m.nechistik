__author__ = 'mikhailnecistik'

# coding: utf-8
from selenium import webdriver
from unittest import TestCase
import unittest

class Test_Ya(TestCase):

    # driver = webdriver.Remote(
    #    command_executor='http://localhost:3333',
    #    desired_capabilities={
    #        "browserName" : 'Firefox'
    #    }
    # )

    def setUp(self):
        self.driver = webdriver.Firefox()
        self.driver.get("http://yandex.ru")

    def test_weather(self):
        inputElement = self.driver.find_element_by_xpath(".//*[text()='ещё']/..")
        inputElement.click()

        inputElement = self.driver.find_element_by_id("tab-pogoda")
        inputElement.click()

        inputElement = self.driver.find_element_by_id("header2input")
        inputElement.send_keys("f,e-lf,b")

        self.driver.implicitly_wait(20)

        inputElement.submit()

        try:
            self.assertEqual("Прогноз погоды в Абу-Даби на 10 дней — Яндекс.Погода", self.driver.title, "Wrong title")
        finally:
            self.driver.close()

    def test_dic(self):
        inputElement = self.driver.find_element_by_xpath("/html/body/div[2]/div[2]/div[2]/div[1]/div[5]/a")
        inputElement.click()

        inputElement = self.driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div/form/table/tbody/tr/td/span/span/input")
        inputElement.send_keys("Привет")

        inputElement_id = inputElement.get_attribute('id')
        inputElement_value = inputElement.get_attribute('value')

        Element = self.driver.find_element_by_xpath("/html/body/div[1]/table/tbody/tr[2]/td/table/tbody/tr/td[3]/div/div/form/table/tbody/tr/td[3]/span/input")
        Element.click()

        try:
            self.assertEqual("«Привет» в переводных словарях — Яндекс.Словари", self.driver.title, "Wrong title")
            self.assertEqual("search-input", inputElement_id, "Wrong id")
            self.assertEqual("Привет", inputElement_value, "Wrong value")
        finally:
            self.driver.implicitly_wait(20)
            self.driver.close()

    def test_avia(self):
        inputElement = self.driver.find_element_by_xpath(".//*[text()='ещё']/..")
        inputElement.click()

        inputElement = self.driver.find_element_by_id("tab-avia")
        inputElement.click()

        inputElement = self.driver.find_element_by_id("to")
        inputElement.send_keys("Москва, Россия")

        inputElement.submit()

        try:
            self.assertEqual("Некорректные параметры поиска", self.driver.title, "Wrong title")
        finally:
            self.driver.implicitly_wait(20)
            self.driver.close()

if __name__ == '__main__':
    unittest.main()
