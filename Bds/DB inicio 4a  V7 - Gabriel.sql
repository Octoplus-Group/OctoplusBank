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
  `ID_BANCO` int DEFAULT '1',
  `ID_AGENCIA` int NOT NULL AUTO_INCREMENT,
  `GERENTE` varchar(45) DEFAULT NULL,
  `NOME_DA_AGENCIA` varchar(100) DEFAULT NULL,
  `N_CONTAS` int DEFAULT '0',
  PRIMARY KEY (`ID_AGENCIA`),
  KEY `ID_BANCO` (`ID_BANCO`)
) ENGINE=MyISAM AUTO_INCREMENT=4 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agencia`
--

LOCK TABLES `agencia` WRITE;
/*!40000 ALTER TABLE `agencia` DISABLE KEYS */;
INSERT INTO `agencia` VALUES (1,1,'JEAN MACEDO','alpha',2),(1,2,'GABRIEL','Omega',1),(1,3,'MARCELO','Teste',1);
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
  `CAPITAL_TOTAL` float(100,2) DEFAULT NULL,
  `JUROS_POUPANCA` float DEFAULT NULL,
  `JUROS_CQ` float DEFAULT NULL,
  `DATA_IS` datetime DEFAULT NULL,
  `DATA_ATUAL` datetime DEFAULT NULL,
  PRIMARY KEY (`ID_BANCO`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banco`
--

LOCK TABLES `banco` WRITE;
/*!40000 ALTER TABLE `banco` DISABLE KEYS */;
INSERT INTO `banco` VALUES (1,'OCTOPLUS_BANK',9101.01,1,1,'2022-11-24 13:06:22','2022-12-25 13:06:22');
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
  `CEP` varchar(9) NOT NULL,
  `ENDERECO` varchar(255) NOT NULL,
  `CIDADE` varchar(255) NOT NULL,
  `BAIRRO` varchar(255) NOT NULL,
  `NUMERO` varchar(10) NOT NULL,
  `SENHA` char(6) NOT NULL,
  `STATUS` varchar(10) NOT NULL DEFAULT 'ANALISE',
  `FUNCAO` varchar(10) NOT NULL DEFAULT 'CL',
  `ID_AGENCIA` int NOT NULL DEFAULT '1',
  `REQUISICAO` varchar(10) NOT NULL DEFAULT 'NENHUMA',
  PRIMARY KEY (`ID_CLIENTE`),
  KEY `ID_CONTA` (`ID_CONTA`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (4,1,'GABRIEL BROSIG BRISCESE','351.487.988-58','1986-09-12','Masculino','(12) 99162-9611','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','APROVADO','CL',2,'NENHUMA'),(7,7,'KENZO','666.666.666-66','2000-05-05','Masculino','(12) 33333-3333','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','APROVADO','CL',1,'NENHUMA'),(5,5,'THIAGO SILVIA','777.777.777-77','1986-09-12','Feminino','(22) 22222-2222','12235-450','Rua Madagascar','São José dos Campos','Jardim Paraíso','209','1234','APROVADO','CL',1,'NENHUMA'),(6,6,'JEAN MARCELO','777.777.777-77','1989-06-12','Masculino','(11) 11111-1111','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','APROVADO','CL',1,'NENHUMA'),(8,8,'GABI','999.999.999-99','2000-05-05','Feminino','(22) 22222-2222','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','ANALISE','CL',1,'NENHUMA'),(9,9,'PEDRO','999.999.999-99','2000-08-06','Feminino','(12) 55555-5555','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','ANALISE','CL',1,'NENHUMA'),(10,10,'LARA','888.888.888-88','2000-01-01','Masculino','(11) 11111-1111','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','ANALISE','CL',1,'NENHUMA'),(11,11,'BERNARDO','444.444.444-44','2000-05-02','Masculino','(55) 55555-5555','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','ANALISE','CL',2,'NENHUMA'),(12,12,'HUAHUA','777.777.777-77','1956-01-01','Masculino','(22) 22222-2222','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','ANALISE','CL',3,'NENHUMA'),(13,13,'TESTE 3','555.555.555-55','1986-09-12','Feminino','(11) 11111-1111','12235-400','Rua Merida','São José dos Campos','Jardim América','209','1234','APROVADO','CL',1,'NENHUMA');
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
  `ID_CONTA` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `DATA_ABERTURA` datetime NOT NULL,
  `TIPO_CONTA` varchar(15) NOT NULL DEFAULT 'CORRENTE',
  `SALDO` float(100,2) DEFAULT '0.00',
  `STATUS` varchar(10) NOT NULL DEFAULT 'ANALISE',
  `ANIVERSARIO` int NOT NULL DEFAULT '0',
  PRIMARY KEY (`ID_CONTA`),
  KEY `ID_AGENCIA` (`ID_AGENCIA`)
) ENGINE=MyISAM AUTO_INCREMENT=14 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conta`
--

LOCK TABLES `conta` WRITE;
/*!40000 ALTER TABLE `conta` DISABLE KEYS */;
INSERT INTO `conta` VALUES (2,0000000001,'2022-11-24 13:17:51','POUPANCA',0.00,'APROVADO',1),(2,0000000002,'2022-11-24 17:56:32','CORRENTE',0.00,'APROVADO',1),(2,0000000003,'2022-11-24 18:46:53','POUPANCA',3131.00,'APROVADO',1),(2,0000000004,'2022-11-24 18:38:37','CORRENTE',0.00,'APROVADO',1),(1,0000000005,'2022-11-25 10:03:17','POUPANCA',0.00,'APROVADO',1),(NULL,0000000006,'2022-11-25 10:10:13','POUPANCA',0.00,'APROVADO',0),(NULL,0000000007,'2022-11-25 10:13:36','POUPANCA',0.00,'APROVADO',0),(NULL,0000000008,'2022-11-25 10:20:40','CORRENTE',0.00,'ANALISE',0),(NULL,0000000009,'2022-11-25 10:27:25','POUPANCA',0.00,'ANALISE',0),(NULL,0000000010,'2022-11-25 10:30:18','CORRENTE',0.00,'ANALISE',0),(2,0000000011,'2022-11-25 10:36:18','POUPANCA',0.00,'ANALISE',1),(3,0000000012,'2022-11-25 10:36:53','POUPANCA',0.00,'ANALISE',1),(1,0000000013,'2022-11-25 19:36:59','POUPANCA',5000.00,'APROVADO',1);
/*!40000 ALTER TABLE `conta` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `funcionarios`
--

DROP TABLE IF EXISTS `funcionarios`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `funcionarios` (
  `ID_FUNC` int NOT NULL AUTO_INCREMENT,
  `NOME` varchar(50) NOT NULL,
  `FUNCAO` varchar(45) NOT NULL,
  `SENHA` char(6) NOT NULL,
  `DATA_NASCIMENTO` date DEFAULT NULL,
  `TELEFONE` varchar(45) DEFAULT NULL,
  `GENERO` enum('Masculino','Feminino','Outro') DEFAULT NULL,
  `CPF` varchar(14) DEFAULT NULL,
  `CEP` varchar(9) DEFAULT NULL,
  `NUMERO_CASA` varchar(10) DEFAULT NULL,
  `ENDERECO` varchar(45) DEFAULT NULL,
  `BAIRRO` varchar(45) DEFAULT NULL,
  `CIDADE` varchar(45) DEFAULT NULL,
  `AGENCIA` int DEFAULT NULL,
  PRIMARY KEY (`ID_FUNC`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `funcionarios`
--

LOCK TABLES `funcionarios` WRITE;
/*!40000 ALTER TABLE `funcionarios` DISABLE KEYS */;
INSERT INTO `funcionarios` VALUES (1,'mezenga','GG','1234',NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL,NULL),(2,'JEAN MACEDO','GA','1234','2000-06-12','(22) 22222-2222','Masculino','333.333.333-33','12235-400','209','Rua Merida','Jardim América','São José dos Campos',1),(3,'GABRIEL','GA','1234','1986-09-12','(12) 99162-9611','Feminino','351.487.988-58','12235-400','209','Rua Merida','Jardim América','São José dos Campos',2),(4,'MARCELO','GA','1234','2000-06-06','(11) 11111-1111','Masculino','888.888.888-88','12235-400','209','Rua Merida','Jardim América','São José dos Campos',3);
/*!40000 ALTER TABLE `funcionarios` ENABLE KEYS */;
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
  `DATA` datetime DEFAULT NULL,
  `VALOR` float DEFAULT NULL,
  `STATUS` varchar(10) NOT NULL DEFAULT 'ANALISE',
  `DE` varchar(255) DEFAULT NULL,
  `PARA` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`ID_TRANSACAO`),
  KEY `ID_CONTA` (`ID_CONTA`),
  KEY `DE` (`DE`),
  KEY `PARA` (`PARA`)
) ENGINE=MyISAM AUTO_INCREMENT=10 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transacoes`
--

LOCK TABLES `transacoes` WRITE;
/*!40000 ALTER TABLE `transacoes` DISABLE KEYS */;
INSERT INTO `transacoes` VALUES (3,1,'DEPOSITO','2022-11-24 18:46:53',1000,'APROVADO',NULL,NULL),(3,2,'DEPOSITO','2022-11-24 18:51:09',2000,'APROVADO',NULL,NULL),(3,3,'DEPOSITO','2022-11-24 18:52:40',100,'APROVADO',NULL,NULL),(3,4,'DEPOSITO','2022-11-24 18:54:38',200,'NEGADO',NULL,NULL),(13,5,'DEPOSITO','2022-11-25 19:36:59',1000,'APROVADO',NULL,NULL),(13,6,'DEPOSITO','2022-11-25 19:37:57',1000,'APROVADO',NULL,NULL),(13,7,'DEPOSITO','2022-11-25 19:41:21',1000,'APROVADO',NULL,NULL),(13,8,'DEPOSITO','2022-11-25 19:46:46',1000,'APROVADO',NULL,NULL),(13,9,'DEPOSITO','2022-11-25 19:54:20',1000,'APROVADO',NULL,NULL);
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

-- Dump completed on 2022-11-25 19:56:54
