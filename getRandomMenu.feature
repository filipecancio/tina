Feature: Get a new menu for today

    Scenario: It's lunch time and we gotta a new menu
    Given It gotta some food options
    Then It choose a food option
    Then It get a quantity of food unit
    Then It get a limit of repetitions for student
    Then It returns a menu object with all of this things