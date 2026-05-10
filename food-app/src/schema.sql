CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    password TEXT,
    goal_calories INTEGER
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

CREATE TABLE today_meals (
    id INTEGER PRIMARY KEY,
    date TEXT,
    user_id INTEGER,
    meal_id INTEGER,
    FOREIGN KEY (user_id) REFERENCES users(id),
    FOREIGN KEY (meal_id) REFERENCES meals(id)
);
