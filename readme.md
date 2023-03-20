<h1>Python Web Scraping using selenium</h1>
<p>This is project created using python and selenium to scrap some data from <a href="https://www.1mg.com/drugs-all-medicines">1mg</a> about the medicine and its details this is a practice project for learning browser automation </p>

<h1>the following SQL table was used to save the data</h1>
<p>
CREATE TABLE `data` (<br>
  `id` int NOT NULL AUTO_INCREMENT,<br>
  `name` text,<br>
  `composition` text,<br>
  `company` text,<br>
  `use_med` text,<br>
  `side_effect` text,<br>
  `packing` text,<br>
  `mrp` varchar(100) DEFAULT NULL,<br>
  `onemglink` varchar(1000) DEFAULT NULL,<br>
  PRIMARY KEY (`id`)<br>
)
</p>
