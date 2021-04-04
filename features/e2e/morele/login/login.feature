@morele
Feature: Login to morele.net page

  @correct_login @successful
  Scenario: Correct login
    Given I am on morele.net login page
     When I enter login and password
     Then I can see login confirmation element on the page present

  @incorrect_login @successful
  Scenario: Incorrect login
    Given I am on morele.net login page
     When I enter wrong credentials
     Then I am not logged in