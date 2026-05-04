CREATE TABLE posts (
    post_id INT PRIMARY KEY,
    title VARCHAR(255),
    body TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);