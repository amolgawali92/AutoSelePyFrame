Feature: Agent Logo

 Scenario: launch presence on Agent home Page
    Given launch chrome browser
    When open Agent portal homepage
    Then verify that the logo present on page
    And close browser