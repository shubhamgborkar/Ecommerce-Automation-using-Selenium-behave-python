Feature: ecom
  Scenario: register
    Given Launch the browser
    When open the website
    Then then click register
    Then fill reg details
    Then click register
    And close browser

  Scenario: login
    Given Launch the browser
    When open the website
    Then then click login
    Then fill log details
    Then click login
    And close browser

  Scenario: making purchase
    Given Launch the browser
    When open the website
    Then then click login
    Then fill log details
    Then click login
    Then click product
    Then add product
    Then click shopping cart
    Then click agree
    Then click checkout
    Then fill details
    Then click continue
    And close browser

