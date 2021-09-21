CREATE TABLE `routes` (
  `ID` int unsigned NOT NULL AUTO_INCREMENT,
  `NAME` varchar(45) NOT NULL,
  `PLACE_FROM` varchar(45) NOT NULL,
  `PLACE_TO` varchar(45) NOT NULL,
  `PRICE` double NOT NULL,
  `TIME` datetime NOT NULL,
  `CAR` int NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE KEY `ID_UNIQUE` (`ID`),
  KEY `CAR_idx` (`CAR`),
  CONSTRAINT `CAR` FOREIGN KEY (`CAR`) REFERENCES `car` (`ID`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb3;
