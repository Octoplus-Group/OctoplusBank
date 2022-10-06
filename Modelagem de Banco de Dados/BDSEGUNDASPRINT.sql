CREATE DATABASE  IF NOT EXISTS `octoplus_bank` /*!40100 DEFAULT CHARACTER SET latin1 */ /*!80016 DEFAULT ENCRYPTION='N' */;
USE `octoplus_bank`;
-- MySQL dump 10.13  Distrib 8.0.30, for Win64 (x86_64)
--
-- Host: localhost    Database: octoplus_bank
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
-- Table structure for table `agencia`
--

DROP TABLE IF EXISTS `agencia`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `agencia` (
  `ID_BANCO` int DEFAULT NULL,
  `ID_AGENCIA` int NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`ID_AGENCIA`),
  KEY `ID_BANCO` (`ID_BANCO`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agencia`
--

LOCK TABLES `agencia` WRITE;
/*!40000 ALTER TABLE `agencia` DISABLE KEYS */;
INSERT INTO `agencia` VALUES (1,1);
/*!40000 ALTER TABLE `agencia` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `banco`
--

DROP TABLE IF EXISTS `banco`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `banco` (
  `ID_BANCO` int NOT NULL AUTO_INCREMENT,
  `NOME_BANCO` varchar(20) DEFAULT NULL,
  `CAPITAL_TOTAL` float DEFAULT NULL,
  PRIMARY KEY (`ID_BANCO`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banco`
--

LOCK TABLES `banco` WRITE;
/*!40000 ALTER TABLE `banco` DISABLE KEYS */;
INSERT INTO `banco` VALUES (1,'OCTOPLUS_BANK',1000000);
/*!40000 ALTER TABLE `banco` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `cliente`
--

DROP TABLE IF EXISTS `cliente`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `cliente` (
  `ID_CONTA` int DEFAULT NULL,
  `ID_CLIENTE` int NOT NULL AUTO_INCREMENT,
  `NOME` varchar(255) NOT NULL,
  `CPF` varchar(14) NOT NULL,
  `DATA_NASCIMENTO` date NOT NULL,
  `GENERO` enum('Masculino','Feminino','Outro') NOT NULL,
  `TELEFONE` varchar(15) NOT NULL,
  `CEP` varchar(8) NOT NULL,
  `ENDERECO` varchar(255) NOT NULL,
  `CIDADE` varchar(255) NOT NULL,
  `BAIRRO` varchar(255) NOT NULL,
  `NUMERO` varchar(10) NOT NULL,
  `SENHA` char(6) NOT NULL,
  `STATUS` varchar(10) NOT NULL DEFAULT 'ANALISE',
  `FUNCAO` varchar(10) NOT NULL DEFAULT 'CL',
  `ID_AGENCIA` int NOT NULL DEFAULT '1',
  PRIMARY KEY (`ID_CLIENTE`),
  KEY `ID_CONTA` (`ID_CONTA`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,1,'GABRIEL BROSIG BRISCESE','35148798858','1986-09-12','Masculino','012991629611','12235400','Rua Merida','Sao Jose dos Campos','Jardim America','209','1234','APROVADO','GA',1),(11,13,'Kenzo','111.222.333-99','1955-09-12','Masculino','12991629611','12235400','Rua Merida','Sjc','Jardim America','69','1234','APROVADO','CL',1),(10,12,'Felicia mimosa','888.999.222-45','1969-09-09','Feminino','991264589','12235465','Ali do Lado','Vermelha','Quente','69','1234','APROVADO','CL',1),(9,11,'Thiago Cunha','555.444.777-89','1989-08-15','Masculino','12991629611','12235400','Rua cinco','Jacarei','Jardim','89','4321','APROVADO','CL',1),(8,10,'Lucas','555.444.111-25','1986-09-12','Feminino','12991629621','12235400','Rua Merida','Jacarei','Campos','69','1234','APROVADO','CL',1);
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conta`
--

DROP TABLE IF EXISTS `conta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conta` (
  `ID_AGENCIA` int DEFAULT NULL,
  `ID_CONTA` int NOT NULL AUTO_INCREMENT,
  `DATA_ABERTURA` datetime NOT NULL,
  `TIPO_CONTA` varchar(15) NOT NULL,
  `SALDO` float DEFAULT '0',
  `STATUS` varchar(10) NOT NULL DEFAULT 'APROVADO',
  PRIMARY KEY (`ID_CONTA`),
  KEY `ID_AGENCIA` (`ID_AGENCIA`)
) ENGINE=MyISAM AUTO_INCREMENT=12 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conta`
--

LOCK TABLES `conta` WRITE;
/*!40000 ALTER TABLE `conta` DISABLE KEYS */;
INSERT INTO `conta` VALUES (1,1,'2022-10-03 00:00:00','CORRETE',1302.86,'ATIVO'),(1,4,'2022-10-04 00:00:00','CORRENTE',1000.5,'ANALISE'),(1,5,'2022-10-04 00:00:00','POUPANCA',0,'ANALISE'),(1,6,'2022-10-04 00:00:00','POUPANCA',0,'ANALISE'),(1,7,'2022-10-04 00:00:00','POUPANCA',0,'ANALISE'),(1,8,'2022-10-04 00:00:00','POUPANCA',0,'ANALISE'),(1,9,'2022-10-04 00:00:00','CORRENTE',5000,'APROVADO'),(1,10,'2022-10-04 00:00:00','POUPANCA',0,'APROVADO'),(1,11,'2022-10-05 00:00:00','POUPANCA',-1000,'APROVADO');
/*!40000 ALTER TABLE `conta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `transacoes`
--

DROP TABLE IF EXISTS `transacoes`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `transacoes` (
  `ID_CONTA` int DEFAULT NULL,
  `ID_TRANSACAO` int NOT NULL AUTO_INCREMENT,
  `TIPO` varchar(10) DEFAULT NULL,
  `DATA` date DEFAULT NULL,
  `VALOR` float DEFAULT NULL,
  `STATUS` varchar(10) NOT NULL DEFAULT 'ANALISE',
  PRIMARY KEY (`ID_TRANSACAO`),
  KEY `ID_CONTA` (`ID_CONTA`)
) ENGINE=MyISAM AUTO_INCREMENT=23 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transacoes`
--

LOCK TABLES `transacoes` WRITE;
/*!40000 ALTER TABLE `transacoes` DISABLE KEYS */;
INSERT INTO `transacoes` VALUES (1,1,'DEPOSITO','2022-10-04',300.25,'APROVADO'),(1,2,'DEPOSITO','2022-10-04',100,'APROVADO'),(1,3,'DEPOSITO','2022-10-04',200.5,'APROVADO'),(1,4,'DEPOSITO','2022-10-04',500,'APROVADO'),(1,5,'DEPOSITO','2022-10-04',300,'APROVADO'),(1,6,'DEPOSITO','2022-10-04',900,'APROVADO'),(1,7,'DEPOSITO','2022-10-04',100,'APROVADO'),(1,8,'DEPOSITO','2022-10-04',300,'APROVADO'),(1,9,'DEPOSITO','2022-10-05',200.59,'APROVADO'),(1,10,'DEPOSITO','2022-10-05',200,'APROVADO'),(1,11,'SAQUE','2022-10-05',-100,'APROVADO'),(1,12,'SAQUE','2022-10-05',-500,'APROVADO'),(1,13,'SAQUE','2022-10-05',-1000,'APROVADO'),(9,14,'SAQUE','2022-10-05',-1000,'APROVADO'),(11,15,'SAQUE','2022-10-05',-1000,'APROVADO'),(9,16,'DEPOSITO','2022-10-05',1000,'APROVADO'),(9,17,'DEPOSITO','2022-10-05',1000,'APROVADO'),(9,18,'DEPOSITO','2022-10-05',1000,'APROVADO'),(9,19,'DEPOSITO','2022-10-05',1000,'APROVADO'),(9,20,'DEPOSITO','2022-10-05',1000,'APROVADO'),(11,21,'DEPOSITO','2022-10-05',1000,'APROVADO'),(11,22,'SAQUE','2022-10-05',-1000,'APROVADO');
/*!40000 ALTER TABLE `transacoes` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-10-06  8:45:29
