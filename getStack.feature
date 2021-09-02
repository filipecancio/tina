Feature: Get a stack of students

    Scenario: We have a stack of students waiting to eat
    Given It have some students waiting
    Then It get all photographies from the camera
    Then It get the spected a not null stack
    Then It get the spected more then 2 students on the stack
    Then It get the spected less then 7 students on the stack
    Then It returns a stack of students photos