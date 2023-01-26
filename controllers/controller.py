from flask import render_template, request # ADDED
from app import app
from events.event import Event


@app.route('/tasks')
def index():
    return render_template('index.html', title='EventZ', event=Event)


     # task_name =  request.form['title']
    # task_date = request.form['datetime_local']
    # task_guests = request.form['details']
    # task_location = request.form['details']
    # task_description =request.form ['description']
    # new_task = Task(task_title, task_desc, True)