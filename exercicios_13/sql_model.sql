-- MySQL Script generated by MySQL Workbench
-- Fri 16 Aug 2019 08:51:03 PM -03
-- Model: New Model    Version: 1.0
-- MySQL Workbench Forward Engineering

SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0;
SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0;
SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='TRADITIONAL,ALLOW_INVALID_DATES';

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
DROP SCHEMA IF EXISTS `mydb` ;

-- -----------------------------------------------------
-- Schema mydb
-- -----------------------------------------------------
CREATE SCHEMA IF NOT EXISTS `mydb` DEFAULT CHARACTER SET utf8 ;
USE `mydb` ;

-- -----------------------------------------------------
-- Table `mydb`.`saldos`
-- -----------------------------------------------------
DROP TABLE IF EXISTS `mydb`.`saldos` ;

CREATE TABLE IF NOT EXISTS `mydb`.`saldos` (
  `ds_login` VARCHAR(55) NOT NULL,
  `ds_senha` VARCHAR(55) NULL,
  `qt_saldo` VARCHAR(55) NULL,
  PRIMARY KEY (`ds_login`))
ENGINE = InnoDB;


SET SQL_MODE=@OLD_SQL_MODE;
SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS;
SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS;

-- -----------------------------------------------------
-- Data for table `mydb`.`saldos`
-- -----------------------------------------------------
START TRANSACTION;
USE `mydb`;
INSERT INTO `mydb`.`saldos` (`ds_login`, `ds_senha`, `qt_saldo`) VALUES ('Rovigo', 'b667ba7559e55f03a23e882874c3b45d', 'Muito pouco');
INSERT INTO `mydb`.`saldos` (`ds_login`, `ds_senha`, `qt_saldo`) VALUES ('Gustavo', 'b6e3aa27420159f15dbd3814467df3eb', 'Menos ainda');

COMMIT;

