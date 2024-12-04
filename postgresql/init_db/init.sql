CREATE TABLE tasks (
    task_id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL,
    task_time TIMESTAMP,
    description TEXT NOT NULL,
    completed BOOLEAN DEFAULT FALSE
);
