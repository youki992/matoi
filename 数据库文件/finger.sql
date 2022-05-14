-- MySQL dump 10.13  Distrib 8.0.23, for Win64 (x86_64)
--
-- Host: localhost    Database: finger
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
-- Table structure for table `finger`
--

DROP TABLE IF EXISTS `finger`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `finger` (
  `id` varchar(100) NOT NULL,
  `url` varchar(400) DEFAULT NULL,
  `result1` varchar(200) DEFAULT NULL,
  `result2` varchar(200) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `finger`
--

LOCK TABLES `finger` WRITE;
/*!40000 ALTER TABLE `finger` DISABLE KEYS */;
INSERT INTO `finger` VALUES ('Fri Mar 18 10:58:28 2022','http://www.baidu.com','jquery  Embed JSON  Cookies  ','没有结果'),('Fri Mar 18 11:03:09 2022','http://www.bilibili.com','Cookies  baidu站长平台  ',' Vue.js | Microsoft(ISA Server)'),('Fri Nov 19 10:48:07 2021','http://www.baidu.com','jquery  Embed JSON  Cookies  ','没有结果'),('Fri Nov 19 10:48:53 2021','http://www.bilibili.com','Cookies  baidu站长平台  ',' Microsoft(ISA Server) | Vue.js'),('Fri Nov 19 10:51:03 2021','http://www.7k7k.com','jquery  ',' Cdn Cache | jquery | 网宿CDN | CDN-Cache-Server'),('Mon Feb 21 21:40:04 2022','http://www.baidu.com','jquery  Embed JSON  Cookies  ','没有结果'),('Mon Feb 21 21:40:29 2022','http://www.baidu.com','jquery  Embed JSON  Cookies  ','没有结果'),('Mon Nov 22 10:22:45 2021','http://www.sina.com.cn/','jquery  中网可信网站权威数据库  iframe  ',' Apache-Traffic-Server | iframe | jquery | Microsoft(ISA Server) | Tengine | 中网可信网站权威数据库'),('Mon Nov 22 10:53:07 2021','http://www.baidu.com','jquery  Embed JSON  P3p  Cookies  ','没有结果');
/*!40000 ALTER TABLE `finger` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2022-05-09 16:58:46
