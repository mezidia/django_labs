-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='ONLY_FULL_GROUP_BY,STRICT_TRANS_TABLES,NO_ZERO_IN_DATE,NO_ZERO_DATE,ERROR_FOR_DIVISION_BY_ZERO,NO_ENGINE_SUBSTITUTION';

-- -----------------------------------------------------
-- Schema DJango
-- -----------------------------------------------------

-- -----------------------------------------------------
-- Schema DJango
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `DJango` DEFAULT CHARACTER SET utf8 ;
USE `DJango` ;

-- -----------------------------------------------------
-- Table `DJango`.`CAR`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJango`.`CAR` (
  `ID` INT NOT NULL,
  `NAME` VARCHAR(45) NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE)
ENGINE = InnoDB;


-- -----------------------------------------------------
-- Table `DJango`.`ROUTES`
-- -----------------------------------------------------
CREATE TABLE IF NOT EXISTS `DJango`.`ROUTES` (
  `ID` INT UNSIGNED NOT NULL AUTO_INCREMENT,
  `NAME` VARCHAR(45) NOT NULL,
  `PLACE_FROM` VARCHAR(45) NOT NULL,
  `PLACE_TO` VARCHAR(45) NOT NULL,
  `PRICE` DOUBLE NOT NULL,
  `TIME` DATETIME NOT NULL,
  `CAR` INT NOT NULL,
  PRIMARY KEY (`ID`),
  UNIQUE INDEX `ID_UNIQUE` (`ID` ASC) VISIBLE,
  INDEX `CAR_idx` (`CAR` ASC) VISIBLE,
  CONSTRAINT `CAR`
    FOREIGN KEY (`CAR`)
    REFERENCES `DJango`.`CAR` (`ID`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION)
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;
