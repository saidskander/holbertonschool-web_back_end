-- resets the attribute valid_email
DELIMITER $$
CREATE TRIGGER change_email
BEFORE UPDATE ON users
FOR EACH ROW
BEGIN
IF NEW.email <> OLD.email
THEN
    SET NEW.valid_email = 0;
END IF;
END
$$
DELIMITER;
