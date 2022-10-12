--Create a database connection
-- Grant privileges to the database user
CREATE DATABASE IF NOT EXISTS `hbnb_dev_db`;
CREATE USER IF NOT EXISTS 'hbnb_dev';
GRANT ALL PRIVILEDGES ON hbnb_dev_db.* TO hbnb_dev;
GRANT SELECT ON performance_schema.* TO hbnb_dev