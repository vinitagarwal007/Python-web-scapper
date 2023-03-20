<h1>Python Web Scraping using selenium</h1>
<p>This is project created using python and selenium to scrap some data from <a href="http://www.1mg.com">1mg</a> about the medicine and its details this is a practice project for learning browser automation </p>

<h1>the following SQL table was used to save the data</h1>
<p>
CREATE TABLE `data` (
  `id` int NOT NULL AUTO_INCREMENT,
  `name` text,
  `composition` text,
  `company` text,
  `use_med` text,
  `side_effect` text,
  `packing` text,
  `mrp` varchar(100) DEFAULT NULL,
  `onemglink` varchar(1000) DEFAULT NULL,
  PRIMARY KEY (`id`)
)
</p>
