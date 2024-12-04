from flask import Flask, render_template, request, redirect, url_for
from database import Tasks

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        description = request.form['description']
        task_time = request.form['task_time']

        # Добавление новой задачи
        Tasks().addTask(description=description, task_time=task_time)

        return redirect(url_for('index'))
    
    # Получение всех задач
    tasks = Tasks().getTasks()

    return render_template('index.html', tasks=tasks)

@app.route('/complete/<int:task_id>', methods=['POST'])
def complete_task(task_id):
    # Получаем список всех задач
    tasks = Tasks().getTasks()
    
    # Находим задачу с данным task_id
    task = next((t for t in tasks if t['task_id'] == task_id), None)
    
    if task:
        # Меняем статус задачи на противоположный
        Tasks().updateTaskStatus(task_id, not task['completed'])
    
    # Перенаправляем обратно на главную страницу
    return redirect(url_for('index'))

@app.route('/delete/<int:task_id>', methods=['POST'])
def delete_task(task_id):
    # Удаляем задачу по ID
    Tasks().deleteTask(task_id)
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
