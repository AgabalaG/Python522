import React, { useState } from 'react';
import './App.css';

function App() {
  const [tasks, setTasks] = useState([
    { id: 1, text: 'Выучить JavaScript', completed: true },
    { id: 2, text: 'Познакомиться с React', completed: true },
    { id: 3, text: 'Устроиться на работу', completed: true },
    { id: 4, text: 'Выучить React', completed: true }
  ]);

  const [newTask, setNewTask] = useState('');

  const toggleTask = (id) => {
    setTasks(tasks.map(task => 
      task.id === id ? { ...task, completed: !task.completed } : task
    ));
  };

  const addTask = () => {
    if (newTask.trim() !== '') {
      const newTaskItem = {
        id: Date.now(),
        text: newTask,
        completed: false
      };
      setTasks([...tasks, newTaskItem]);
      setNewTask('');
    }
  };

  const deleteTask = (id) => {
    setTasks(tasks.filter(task => task.id !== id));
  };

  return (
    <div className="app">
      <div className="todo-container">
        <h1>Список задач</h1>
        
        <div className="add-task">
          <input
            type="text"
            value={newTask}
            onChange={(e) => setNewTask(e.target.value)}
            placeholder="Добавить новую задачу..."
            onKeyPress={(e) => e.key === 'Enter' && addTask()}
          />
          <button onClick={addTask}>Добавить</button>
        </div>

        <div className="tasks-list">
          {tasks.map(task => (
            <div key={task.id} className={task-item ${task.completed ? 'completed' : ''}}>
              <div className="task-content">
                <span 
                  className="checkbox"
                  onClick={() => toggleTask(task.id)}
                >
                  {task.completed && '✓'}
                </span>
                <span className="task-text">{task.text}</span>
              </div>
              <button 
                className="delete-btn"
                onClick={() => deleteTask(task.id)}
              >
                ×
              </button>
            </div>
          ))}
        </div>

        <div className="tasks-info">
          Выполнено: {tasks.filter(task => task.completed).length} из {tasks.length}
        </div>
      </div>
    </div>
  );
}

export default App;
