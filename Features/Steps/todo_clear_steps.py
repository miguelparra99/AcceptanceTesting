from behave import given, when, then

from Features.Steps.main_steps import create_task, add_task, list_tasks, clear_todo_list, edit_task


@given('the user already adds a task before "{task}" with category "{category}" and priority "{priority}"')
def step_impl(context, task, category, priority):
    existing_task = create_task(task, category, priority)
    context.todo_list = add_task([], existing_task)

# When the user clears the to-do list
@when('the user clears the to-do list')
def step_impl(context):
    context.todo_list = clear_todo_list()

# Then the to-do list should be empty
@then('the to-do list should be empty')
def step_impl(context):
    assert len(context.todo_list) == 0, 'To-do list is not empty'