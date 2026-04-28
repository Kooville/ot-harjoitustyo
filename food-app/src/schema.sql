CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    goal_calories INTEGER,
    today_calories INTEGER
);

CREATE TABLE items (
    id INTEGER PRIMARY KEY,
    name TEXT,
    calories INTEGER,
    carbs INTEGER,
    protein INTEGER,
    fat INTEGER
    );

CREATE TABLE meals (
    id INTEGER PRIMARY KEY,
    name TEXT,
    calories INTEGER,
    carbs INTEGER,
    protein INTEGER,
    fat INTEGER
    );
