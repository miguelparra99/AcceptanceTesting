from behave import given, when, then

from Features.Steps.main_steps import create_task, add_task, list_tasks, clear_todo_list, edit_task

@given('there is a task already created "{task}" with category "{category}" and priority "{priority}"')
def step_impl(context, task, category, priority):
    task = create_task(task, category, priority)
    context.todo_list = add_task([], task)  # Initialize the todo_list with the added task

# When the user edits task "Buy groceries" to "Buy clothes" with new category "Fashion" and new priority "Low"
@when('the user edits task "{old_task}" to "{new_task}" with new category "{new_category}" and new priority "{new_priority}"')
def step_impl(context, old_task, new_task, new_category, new_priority):
    for index, task_dict in enumerate(context.todo_list):
        if task_dict['Descripcion'] == old_task:
            context.todo_list = edit_task(context.todo_list, index, new_task, new_priority, new_category)
            break

# Then the to-do list should show edited task "Buy clothes" with new category "Fashion" and new priority "Low"
@then('the to-do list should show edited task "{edited_task}" with new category "{new_category}" and new priority "{new_priority}"')
def step_impl(context, edited_task, new_category, new_priority):
    found = False
    for task_dict in context.todo_list:
        if task_dict['Descripcion'] == edited_task:
            assert task_dict['Categoria'] == new_category, f'Category for task "{edited_task}" is not updated'
            assert task_dict['Prioridad'] == new_priority, f'Priority for task "{edited_task}" is not updated'
            found = True
            break
    assert found, f'Task "{edited_task}" not found in the todo_list'