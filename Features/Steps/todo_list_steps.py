from behave import given, when, then

from Features.Steps.main_steps import create_task, add_task, list_tasks, clear_todo_list, edit_task

def list_tasks_output(todo_list):
    task_output = "Tasks:"
    for index, task in enumerate(todo_list, start=1):
        status = "✓" if task["Completado"] else " "
        task_output += f"\n{index}. [{status}] {task['Descripcion']} (Category: {task['Categoria']}, Priority: {task['Prioridad']})"
    return task_output

@given('the user adds a task "{task}" with category "{category}" and priority "{priority}"')
def step_impl(context, task, category, priority):
    task = create_task(task, category, priority)
    context.todo_list = add_task([], task)  # Initialize the todo_list with the added task

# When the user lists all tasks
@when('the user lists all tasks')
def step_impl(context):
    context.list_output = list_tasks_output(context.todo_list)

# Then the output should contain
@then('the output should contain')
def step_impl(context):
    expected_output = context.text.strip()
    assert expected_output == context.list_output.strip()
