Feature: To-Do List Program

  Scenario: Add a task to the to-do list
    Given the to-do list is empty
    When the user adds a task "Buy groceries" with category "Shopping" and priority "High"
    Then the to-do list should contain the task "Buy groceries" with category "Shopping" and priority "High"

  Scenario: List all tasks in the to-do list
    Given the user adds a task "Buy groceries" with category "Shopping" and priority "High"
    When the user lists all tasks
    Then the output should contain
      """
      Tasks:
      1. [ ] Buy groceries (Category: Shopping, Priority: High)
      """

  Scenario: Mark a task as completed
    Given the user already adds a task "Buy cars" with category "Sport" and priority "Low"
    When the user marks task "Buy cars" as completed
    Then the to-do list should show task "Buy cars" as completed

  Scenario: Clear the entire to-do list
    Given the user already adds a task before "Buy cars" with category "Sport" and priority "Low"
    When the user clears the to-do list
    Then the to-do list should be empty

  Scenario: Edit a task in the to-do list
    Given there is a task already created "Buy groceries" with category "Shopping" and priority "High"
    When the user edits task "Buy groceries" to "Buy clothes" with new category "Fashion" and new priority "Low"
    Then the to-do list should show edited task "Buy clothes" with new category "Fashion" and new priority "Low"