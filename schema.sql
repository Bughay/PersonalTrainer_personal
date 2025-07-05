

CREATE TABLE food(
    food_name TEXT NOT NULL,
    serving_g REAL,
    calories REAL,
    protein REAL,
    carbs REAL,
    fats REAL,
    date_added TEXT DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE exercises(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    exercise_name TEXT NOT NULL,
    weight_total REAL,
    reps INTEGER,
    rpe INTEGER CHECK(rpe BETWEEN 1 AND 10),
    fatigue INTEGER CHECK(fatigue BETWEEN 1 AND 10),
    date_added TEXT DEFAULT CURRENT_TIMESTAMP
);


CREATE TABLE Cardio (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER NOT NULL,
    cardio_name TEXT NOT NULL,
    distance_m INTEGER,
    time_sec INTEGER,
    speed REAL GENERATED ALWAYS AS (
        CASE WHEN time_sec > 0 
             THEN distance_m / (time_sec / 3600.0)  
             ELSE NULL 
        END
    ) VIRTUAL,
    date_added TEXT DEFAULT CURRENT_TIMESTAMP
);

