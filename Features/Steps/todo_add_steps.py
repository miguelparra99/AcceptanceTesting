from behave import given, when, then

from Features.Steps.main_steps import create_task, add_task, list_tasks, clear_todo_list, edit_task

# Given the to-do list is empty
@given('the to-do list is empty')
def step_impl(context):
    context.todo_list = []

# When the user adds a task "{task}" with category "{category}" and priority "{priority}"
@when('the user adds a task "{task}" with category "{category}" and priority "{priority}"')
def step_impl(context, task, category, priority):
    new_task = create_task(task, category, priority)
    context.todo_list = add_task(context.todo_list, new_task)

# Then the to-do list should contain the task "{task}" with category "{category}" and priority "{priority}"
@then('the to-do list should contain the task "{task}" with category "{category}" and priority "{priority}"')
def step_impl(context, task, category, priority):
    task_found = False
    for task_dict in context.todo_list:
        if (task_dict['Descripcion'] == task and
            task_dict['Categoria'] == category and
            task_dict['Prioridad'] == priority):
            task_found = True
            break
    assert task_found
