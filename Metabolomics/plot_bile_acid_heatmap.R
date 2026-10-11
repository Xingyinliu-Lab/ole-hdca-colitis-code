library(pheatmap)
a <- commandArgs(trailingOnly=TRUE)
d <- read.delim(a[1],row.names=1,check.names=FALSE)
pheatmap(as.matrix(d),filename=a[2])
