
/* broad script to view database. Edit variables for further tuning  

SELECT effort_name, athlete_username, start_date_time, moving_time, average_watts, average_heart_rate, wind_speed, wind_direction 
FROM efforts
WHERE average_watts >= 170 AND wind_speed BETWEEN 3 AND 10 AND start_date_time BETWEEN '01-JAN-2023'::DATE AND '05-MAY-2023'::DATE AND wind_direction BETWEEN 240 AND 300
ORDER BY moving_time, average_watts, average_heart_rate, wind_speed, wind_direction DESC;


/* order all by date to take inventory of previously imported data

SELECT effort_name, athlete_username, start_date_time, moving_time, average_watts, average_heart_rate, wind_speed, wind_direction
FROM efforts
ORDER BY start_date_time DESC
