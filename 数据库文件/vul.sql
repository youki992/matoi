-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: vul
-- ------------------------------------------------------
-- Server version	8.0.23

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `vul`
--

DROP TABLE IF EXISTS `vul`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `vul` (
  `id` varchar(500) DEFAULT NULL,
  `time` varchar(100) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `ip` varchar(500) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `vul`
--

LOCK TABLES `vul` WRITE;
/*!40000 ALTER TABLE `vul` DISABLE KEYS */;
INSERT INTO `vul` VALUES ('1647588774.1234548','Fri Mar 18 15:32:54 2022','xray','http://121.4.255.248:8000/_book/','expired'),('1647588963.6013496','Fri Mar 18 15:36:03 2022','xray','127.0.0.1','expired'),('1647590388.574706','Fri Mar 18 15:59:48 2022','xray','http://121.4.255.248','expired'),('1647590388.5896652','Fri Mar 18 15:59:48 2022','xray','http://121.4.255.248','expired'),('1647590538.1175146','Fri Mar 18 16:02:18 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public/','vul'),('1647590538.118507','Fri Mar 18 16:02:18 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public/','vul'),('1647590599.1955538','Fri Mar 18 16:03:19 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public/','vul'),('1647590599.2015426','Fri Mar 18 16:03:19 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public/','vul'),('1647590889.3353019','Fri Mar 18 16:08:09 2022','Thinkphp 5.0.x 远程代码执行漏洞','127.0.0.1','not vul'),('1647590889.336296','Fri Mar 18 16:08:09 2022','Thinkphp 5.0.x 远程代码执行漏洞','127.0.0.1','not vul'),('1647590938.364141','Fri Mar 18 16:08:58 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647590938.3661356','Fri Mar 18 16:08:58 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647592064.320927','Fri Mar 18 16:27:44 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647592064.3269143','Fri Mar 18 16:27:44 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647592674.0946894','Fri Mar 18 16:37:54 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647592674.105661','Fri Mar 18 16:37:54 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647592740.8032336','Fri Mar 18 16:39:00 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647592741.5689778','Fri Mar 18 16:39:01 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647593447.613087','Fri Mar 18 16:50:47 2022','Thinkphp 5.0.x 远程代码执行漏洞','1.2.3.4','not vul'),('1647593447.651983','Fri Mar 18 16:50:47 2022','Thinkphp 5.0.x 远程代码执行漏洞','1.2.3.4','not vul'),('1647593493.2207572','Fri Mar 18 16:51:33 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647593493.2257428','Fri Mar 18 16:51:33 2022','Thinkphp 5.0.x 远程代码执行漏洞','http://121.4.255.248:8000/tp/public','vul'),('1647593590.4619503','Fri Mar 18 16:53:10 2022','xray','http://121.4.255.248:8000/tp/public','expired'),('1647593590.4777627','Fri Mar 18 16:53:10 2022','xray','http://121.4.255.248:8000/tp/public','expired');
/*!40000 ALTER TABLE `vul` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-09 16:59:47
