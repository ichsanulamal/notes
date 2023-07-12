```
javac WordCount.java
jar cf wc.jar WordCount*.class
hadoop jar wc.jar WordCount /Data/ebook /Output/wc

hadoop fs -mkdir /Data
hadoop fs -mkdir Data/ebook
hadoop fs -copyFromLocal The-Night- Before.txt Data/ebook
hadoop fs -copyFromLocal free-at-last-US_civil_rights-PD-FKB.txt
hadoop fs -copyFromLocal pg2701.txt
```