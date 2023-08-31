from behave import given, when, then

from Features.Steps.main_steps import create_task, add_task, list_tasks, clear_todo_list, edit_task


@given('the user already adds a task "{task}" with category "{category}" and priority "{priority}"')
def step_impl(context, task, category, priority):
    task = create_task(task, category, priority)
    context.todo_list = add_task([], task)  # Initialize the todo_list with the added task

# When the user marks task "Pay bills" as completed
@when('the user marks task "{task}" as completed')
def step_impl(context, task):
    for task_dict in context.todo_list:
        if task_dict['Descripcion'] == task:
            task_dict['Completado'] = True
            break

# Then the to-do list should show task "Pay bills" as completed
@then('the to-do list should show task "{task}" as completed')
def step_impl(context, task):
    for task_dict in context.todo_list:
        if task_dict['Descripcion'] == task:
            assert task_dict['Completado'] == True, f'Task "{task}" is not marked as completed'
            break