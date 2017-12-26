CREATE DATABASE IF NOT EXISTS heroku_5dbfec48ecba66c DEFAULT CHARACTER SET utf8;

USE heroku_5dbfec48ecba66c;

DROP TABLE IF EXISTS `bikes`;

CREATE TABLE `bikes` (
  `SKU` varchar(11) NOT NULL,
  `name` varchar(50) NOT NULL,
  `description` varchar(180) default NULL,
  `rating` smallint(1) default 1,
  `price` int(7) default 0,
  `quantity` smallint(5) default 0,
  `type` ENUM('Road Bike','Mountain Bike','Hybrid Bike','Crusier Bike','City Bike','Others'),
  `img` longblob NOT NULL,
  PRIMARY KEY (`SKU`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

drop table bikes;

SELECT table_schema heroku_5dbfec48ecba66c, 
sum( data_length + index_length ) / 1024 / 
1024 size_in_mb
#sum( data_free )/ 1024 / 1024 free_space_in_mb 
FROM information_schema.TABLES 
GROUP BY table_schema ; 

select * from webapp_bikes;

GRANT USAGE ON *.* TO 'b02d8834ffb9be@<us-cdbr-iron-east-05.cleardb.net>' WITH MAX_QUERIES_PER_HOUR 100;

truncate table webapp_bikes;
describe webapp_bikes;

insert  into webapp_bikes (`SKU`,`name`,`description`,`rating`,`price`,`quantity`,`type`) values  
("DB-CTH","Diamondback Clutch Women's Mountain Bike","All-mountain riding is more popular than ever and that's thanks to bikes like the 2017 edition of the Diamondback Clutch women's dual-suspension mountain bike. With its slack women's-specific geometry, precision shifting courtesy of the 1x11-speed SRAM drivetrain, and burly Suntour and X-Fusion suspension, the Clutch takes trail hits in stride and delivers an incredible ride quality. The Clutch is meant to be ridden hard and fully enjoyed",4,1149,10,"Mountain Bike");

INSERT INTO webapp_bikes (`SKU`, `name`, `description`,`rating`,`price`,`quantity`,`type`) VALUES ("278002", "2017 Cannondale Adventure Women's 2","Find your own path on the Adventure Women's 2 from Cannondale. With a lightweight, easy-entry aluminum frame, you'll accelerate quickly and maintain excellent control. Shimano provides precise shifting and braking, and a suspension fork up front helps to smooth out any road turbulence you may encounter. Add in a Cannondale seat, seatpost, and adjustable stem, and you've got the perfect intrepid exploring companion.",0.000000,0.000000,14,"Multi-Speed");

INSERT INTO webapp_bikes (`SKU`, `name`, `description`,`rating`,`price`,`quantity`,`type`,`image`) VALUES 
("278002", "2017 Cannondale Adventure Women's 2","Find your own path on the Adventure Women's 2 from Cannondale. With a lightweight, easy-entry aluminum frame, you'll accelerate quickly and maintain excellent control. Shimano provides precise shifting and braking, and a suspension fork up front helps to smooth out any road turbulence you may encounter. Add in a Cannondale seat, seatpost, and adjustable stem, and you've got the perfect intrepid exploring companion.",0.000000,0.000000,14,"Multi-Speed","http://thebicyclechain.com/images/library/large/cannondale-adventure-2-278002-1.jpg");