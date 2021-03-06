create table log(
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
   user_id INT UNSIGNED NOT NULL,
   clock_in TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( id )
);

create table card(
   id INT UNSIGNED NOT NULL AUTO_INCREMENT UNIQUE,
   rfid_uid VARCHAR(255) NOT NULL,
   name VARCHAR(255) NOT NULL,
   password VARCHAR(255) NOT NULL,
   created TIMESTAMP NOT NULL DEFAULT CURRENT_TIMESTAMP,
   PRIMARY KEY ( id )
);
