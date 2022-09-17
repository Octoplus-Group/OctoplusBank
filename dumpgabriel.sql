CREATE DATABASE  IF NOT EXISTS `banco` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `banco`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: banco
-- ------------------------------------------------------
-- Server version	8.0.30

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `clientes`
--

DROP TABLE IF EXISTS `clientes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `clientes` (
  `id` int(5) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `nome` char(50) NOT NULL,
  `CPF` varchar(11) DEFAULT NULL,
  `dataNascimento` date DEFAULT NULL,
  `genero` varchar(10) DEFAULT NULL,
  `telefone` varchar(11) DEFAULT NULL,
  `cep` varchar(8) DEFAULT NULL,
  `cidade` varchar(30) DEFAULT NULL,
  `endereco` char(100) DEFAULT NULL,
  `bairro` char(50) DEFAULT NULL,
  `numeroCasa` int DEFAULT NULL,
  `tipoConta` varchar(20) DEFAULT NULL,
  `senha` varchar(20) DEFAULT NULL,
  `saldo` float(20,2) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `clientes`
--

LOCK TABLES `clientes` WRITE;
/*!40000 ALTER TABLE `clientes` DISABLE KEYS */;
INSERT INTO `clientes` VALUES (00003,'Kenz4','11122233359','2022-09-15','Masculino','129996584','1256325','Sjc','Rua Beta','Luz Vermelha',59,'ContaCorrente','1234',0.00),(00005,'Gabriel Brosig Briscese','35148798858','1986-09-12','Masculino','12991629611','12235400','Sao Jose dos Campos','Rua Merida','Jardim America',209,'ContaCorrente','4321',7052.00),(00006,'Lira Pria','11122233344','1990-05-05','Masculino','21991629568','12235400','Sao Jose dos Campos','Rua Marcos','200',59,'ContaCorrente','1234',0.00),(00007,'Lucas o Pegador','33344455599','1986-06-06','Masculino','12991629611','2356985','Sjc','Rua dos Ouvidos','Morumbi',69,'ContaPoupanca','1234',-100.00);
/*!40000 ALTER TABLE `clientes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-09-17 17:09:12
