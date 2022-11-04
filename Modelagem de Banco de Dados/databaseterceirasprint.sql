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
  `NOME_AGENCIA` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`ID_AGENCIA`),
  KEY `ID_BANCO` (`ID_BANCO`)
) ENGINE=MyISAM AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `agencia`
--

LOCK TABLES `agencia` WRITE;
/*!40000 ALTER TABLE `agencia` DISABLE KEYS */;
INSERT INTO `agencia` VALUES (1,1,'GABRIEL BROSIG BRISCESE','AGENCIA FATEC'),(1,2,'THIAGO SILVA','AGENCIA UNESP'),(1,3,'IGOR KENZO','AGENCIA TOKYO'),(1,4,'JEAN BILOLA','AGENCIA TESTE');
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
  PRIMARY KEY (`ID_BANCO`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `banco`
--

LOCK TABLES `banco` WRITE;
/*!40000 ALTER TABLE `banco` DISABLE KEYS */;
INSERT INTO `banco` VALUES (1,'OCTOPLUS_BANK',2003001.00,0.07,3);
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
) ENGINE=MyISAM AUTO_INCREMENT=37 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `cliente`
--

LOCK TABLES `cliente` WRITE;
/*!40000 ALTER TABLE `cliente` DISABLE KEYS */;
INSERT INTO `cliente` VALUES (1,1,'GABRIEL BROSIG BRISCESE','35148798858','1986-09-12','Masculino','012991629611','12235400','Rua Merida','Sao Jose dos Campos','Jardim America','209','1234','APROVADO','GA',1,'NENHUMA'),(11,13,'Kenzo Kid Bengala','111.222.555-99','1955-09-12','Feminino','12991629611','12235400','Rua Merida','Sjc','Jardim America','69','1234','APROVADO','GA',1,'NENHUMA'),(10,12,'Felicia mimosa','888.999.222-45','1969-09-09','Feminino','991264589','12235465','Ali do Lado','Vermelha','Quente','69','1234','APROVADO','CL',1,'NENHUMA'),(9,11,'Kenzo','111.222.444-99','1955-09-12','Outro','12991629611','12235400','Rua Merida','Sjc','Jardim America','69','1234','APROVADO','CL',1,'NENHUMA'),(8,10,'Lucas','555.444.111-25','1986-09-12','Feminino','12991629621','12235400','Rua Merida','Jacarei','Campos','69','1234','APROVADO','CL',1,'NENHUMA'),(12,14,'Jean Manjador','888.777.444-23','1996-05-06','Masculino','12991629611','12235400','Rua dos Manjadores','Caçapava','Zoio','69','1234','APROVADO','CL',1,'NENHUMA'),(13,15,'Joao Pedrao','233.566.988-20','1959-06-12','Masculino','12991629611','12235400','Rua Merida ','SJC','Jardim America','12','1234','ANALISE','CL',1,'NENHUMA'),(14,16,'Joao Pedrao','233.566.988-20','1959-06-12','Masculino','12991629611','12235400','Rua Merida ','SJC','Jardim America','12','1234','ANALISE','CL',1,'NENHUMA'),(15,17,'Pedrisco Louco','444.555.999-20','1986-06-25','Masculino','12991629611','12235400','RUa Mercori','Jacarei','Agosto','63','1234','ANALISE','CL',1,'NENHUMA'),(16,18,'Gabriela Silvia','888.999.559-56','2001-04-05','Feminino','23991629611','12235400','Rua Ali','Jacarei','Lá','89','1234','APROVADO','CL',1,'NENHUMA'),(28,30,'Gerente Geral - Master','351.487.988.58','1986-09-12','Masculino','(12)99162-9611','12235400','Rua Merida','São José dos Campos','Jardim América','06','1234','APROVADO','GG',1,'NENHUMA'),(27,29,'TIFA BALAO GRANDE','444.555.888-79','1986-09-12','Masculino','(12) 44444-7777','12233310','Rua Merida','São José dos Campos','Jardim América','209','1234','APROVADO','CL',1,'NENHUMA'),(19,21,'Teste3','111.222.828-78','2000-03-03','Masculino','12991629611','12235400','Rua a','Sjc','B','323','1234','APROVADO','CL',1,'NENHUMA'),(20,22,'teste final sera','555.555.888-29','2022-12-31','Masculino','12991629611','12345123','Trinta','Vinte','Jubi','1234','1234','APROVADO','CL',1,'NENHUMA'),(21,23,'teste final sera','555.555.888-29','2022-12-31','Masculino','12991629611','12345123','Trinta','Vinte','Jubi','1234','1234','APROVADO','CL',1,'NENHUMA'),(22,24,'Teste Mais uma vez','444.444.444-45','2022-12-31','Feminino','5699162695','12345321','A','Sjc','A','56','1234','APROVADO','CL',1,'NENHUMA'),(23,25,'Agora vai','555.555.555-96','2019-12-31','Masculino','56991629611','12345654','B','A','C','85','1234','APROVADO','CL',1,'NENHUMA'),(26,27,'Tadeo 2','351.487.988-58','1986-12-12','Masculino','(12) 23548-9878','12235400','Rua Merida','São José dos Campos','Jardim América','06','1234','APROVADO','CL',1,'NENHUMA'),(29,35,'JEAN BILOLA','777.777.777-77','2000-07-07','Feminino','(77) 77777-7777','12235-400','Rua Merida','São José dos Campos','Jardim América','69','1234','APROVADO','GA',1,'NENHUMA'),(30,36,'THIAGO ZANI','226.746.058-04','1984-02-25','Masculino','(12) 99620-2320','12233-000','Avenida Andrômeda','São José dos Campos','Bosque dos Eucaliptos','1000','1234','APROVADO','CL',1,'NENHUMA');
/*!40000 ALTER TABLE `cliente` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `conta`
--

DROP TABLE IF EXISTS `conta`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `conta` (
  `ID_AGENCIA` int DEFAULT '1',
  `ID_CONTA` int(10) unsigned zerofill NOT NULL AUTO_INCREMENT,
  `DATA_ABERTURA` datetime NOT NULL,
  `TIPO_CONTA` varchar(15) NOT NULL DEFAULT 'CORRENTE',
  `SALDO` float(100,2) DEFAULT '0.00',
  `STATUS` varchar(10) NOT NULL DEFAULT 'APROVADO',
  PRIMARY KEY (`ID_CONTA`),
  KEY `ID_AGENCIA` (`ID_AGENCIA`)
) ENGINE=MyISAM AUTO_INCREMENT=31 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `conta`
--

LOCK TABLES `conta` WRITE;
/*!40000 ALTER TABLE `conta` DISABLE KEYS */;
INSERT INTO `conta` VALUES (1,0000000001,'2022-10-03 00:00:00','CORRENTE',12259.38,'ATIVO'),(1,0000000004,'2022-10-04 00:00:00','CORRENTE',1000.50,'ANALISE'),(1,0000000005,'2022-10-04 00:00:00','POUPANCA',0.00,'ANALISE'),(1,0000000006,'2022-10-04 00:00:00','POUPANCA',0.00,'ANALISE'),(1,0000000007,'2022-10-04 00:00:00','POUPANCA',0.00,'ANALISE'),(1,0000000008,'2022-10-04 00:00:00','POUPANCA',0.00,'ANALISE'),(1,0000000009,'2022-10-04 00:00:00','CORRENTE',5000.00,'APROVADO'),(1,0000000010,'2022-10-04 00:00:00','POUPANCA',0.00,'APROVADO'),(1,0000000011,'2022-10-05 00:00:00','CORRENTE',0.00,'APROVADO'),(1,0000000012,'2022-10-06 00:00:00','CORRENTE',0.00,'APROVADO'),(1,0000000013,'2022-10-08 16:44:18','CORRENTE',0.00,'APROVADO'),(1,0000000014,'2022-10-08 16:46:30','CORRENTE',0.00,'APROVADO'),(1,0000000015,'2022-10-08 16:49:30','POUPANCA',0.00,'APROVADO'),(1,0000000016,'2022-10-08 19:58:21','CORRENTE',0.00,'APROVADO'),(1,0000000017,'2022-10-08 20:40:43','CORRENTE',0.00,'APROVADO'),(1,0000000018,'2022-10-08 20:53:32','CORRENTE',0.00,'APROVADO'),(1,0000000019,'2022-10-08 20:54:44','CORRENTE',0.00,'APROVADO'),(1,0000000020,'2022-10-08 21:26:12','CORRENTE',0.00,'APROVADO'),(1,0000000021,'2022-10-08 21:27:03','CORRENTE',0.00,'APROVADO'),(1,0000000022,'2022-10-08 21:33:25','CORRENTE',0.00,'APROVADO'),(1,0000000023,'2022-10-08 21:42:18','POUPANCA',0.00,'APROVADO'),(1,0000000024,'2022-10-08 21:45:13','CORRENTE',0.00,'APROVADO'),(1,0000000025,'2022-10-09 12:30:09','POUPANCA',0.00,'APROVADO'),(1,0000000026,'2022-10-26 07:33:56','POUPANCA',0.00,'APROVADO'),(1,0000000027,'2022-10-26 07:41:13','POUPANCA',0.00,'APROVADO'),(1,0000000028,'2022-10-26 07:41:50','CORRENTE',0.00,'APROVADO'),(1,0000000029,'2022-11-02 10:18:29','CORRENTE',0.00,'APROVADO'),(1,0000000030,'2022-11-03 07:29:06','CORRENTE',-1000000.00,'APROVADO');
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
  `DATA` datetime DEFAULT NULL,
  `VALOR` float DEFAULT NULL,
  `STATUS` varchar(10) NOT NULL DEFAULT 'ANALISE',
  PRIMARY KEY (`ID_TRANSACAO`),
  KEY `ID_CONTA` (`ID_CONTA`)
) ENGINE=MyISAM AUTO_INCREMENT=42 DEFAULT CHARSET=utf8mb3;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `transacoes`
--

LOCK TABLES `transacoes` WRITE;
/*!40000 ALTER TABLE `transacoes` DISABLE KEYS */;
INSERT INTO `transacoes` VALUES (1,1,'DEPOSITO','2022-10-04 00:00:00',300.25,'APROVADO'),(1,2,'DEPOSITO','2022-10-04 00:00:00',100,'APROVADO'),(1,3,'DEPOSITO','2022-10-04 00:00:00',200.5,'APROVADO'),(1,4,'DEPOSITO','2022-10-04 00:00:00',500,'APROVADO'),(1,5,'DEPOSITO','2022-10-04 00:00:00',300,'APROVADO'),(1,6,'DEPOSITO','2022-10-04 00:00:00',900,'APROVADO'),(1,7,'DEPOSITO','2022-10-04 00:00:00',100,'APROVADO'),(1,8,'DEPOSITO','2022-10-04 00:00:00',300,'APROVADO'),(1,9,'DEPOSITO','2022-10-05 00:00:00',200.59,'APROVADO'),(1,10,'DEPOSITO','2022-10-05 00:00:00',200,'APROVADO'),(1,11,'SAQUE','2022-10-05 00:00:00',-100,'APROVADO'),(1,12,'SAQUE','2022-10-05 00:00:00',-500,'APROVADO'),(1,13,'SAQUE','2022-10-05 00:00:00',-1000,'APROVADO'),(9,14,'SAQUE','2022-10-05 00:00:00',-1000,'APROVADO'),(11,15,'SAQUE','2022-10-05 00:00:00',-1000,'APROVADO'),(9,16,'DEPOSITO','2022-10-05 00:00:00',1000,'APROVADO'),(9,17,'DEPOSITO','2022-10-05 00:00:00',1000,'APROVADO'),(9,18,'DEPOSITO','2022-10-05 00:00:00',1000,'APROVADO'),(9,19,'DEPOSITO','2022-10-05 00:00:00',1000,'APROVADO'),(9,20,'DEPOSITO','2022-10-05 00:00:00',1000,'APROVADO'),(11,21,'DEPOSITO','2022-10-05 00:00:00',1000,'APROVADO'),(11,22,'SAQUE','2022-10-05 00:00:00',-1000,'APROVADO'),(11,23,'DEPOSITO','2022-10-06 00:00:00',1000,'APROVADO'),(11,24,'DEPOSITO','2022-10-06 00:00:00',1000,'APROVADO'),(11,25,'DEPOSITO','2022-10-06 00:00:00',1000,'APROVADO'),(11,26,'DEPOSITO','2022-10-06 00:00:00',1000,'APROVADO'),(11,27,'SAQUE','2022-10-06 00:00:00',-100,'APROVADO'),(11,28,'SAQUE','2022-10-06 00:00:00',-100,'APROVADO'),(11,29,'SAQUE','2022-10-06 00:00:00',-100,'APROVADO'),(11,30,'SAQUE','2022-10-06 00:00:00',-1000,'APROVADO'),(11,31,'SAQUE','2022-10-06 00:00:00',-100.5,'APROVADO'),(1,32,'SAQUE','2022-10-06 00:00:00',-1000,'APROVADO'),(1,33,'DEPOSITO','2022-10-06 00:00:00',1000,'APROVADO'),(12,34,'SAQUE','2022-10-06 00:00:00',-100.25,'APROVADO'),(12,35,'DEPOSITO','2022-10-06 00:00:00',100.25,'APROVADO'),(1,36,'DEPOSITO','2022-10-07 00:00:00',10000,'APROVADO'),(1,37,'DEPOSITO','2022-10-08 00:00:00',500,'APROVADO'),(1,38,'DEPOSITO','2022-10-08 15:55:03',200,'APROVADO'),(1,39,'DEPOSITO','2022-10-08 15:57:32',256.52,'APROVADO'),(11,40,'SAQUE','2022-10-17 09:10:36',-1599.5,'APROVADO'),(30,41,'SAQUE','2022-11-03 11:04:05',-1000000,'APROVADO');
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

-- Dump completed on 2022-11-03 21:45:45
