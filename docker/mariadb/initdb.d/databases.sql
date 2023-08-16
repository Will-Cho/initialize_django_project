# create databases
CREATE DATABASE IF NOT EXISTS `test_service_db`;

# create service user and grant rights
GRANT ALL PRIVILEGES ON `test_service_db`.* TO 'db_user'@'%';