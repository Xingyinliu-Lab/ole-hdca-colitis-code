# Oleuropein–HDCA Colitis Code

Code for analyses and visualizations in a mouse DSS-induced colitis study of oleuropein, gut microbiota, bile acid metabolism, histone methylation, and NLRP3 regulation.

## Contents

- `16S/`: microbial diversity, taxonomic, functional, and network visualizations
- `Metabolomics/`: metabolomics PCA, differential metabolites, enrichment, and bile acid visualizations
- `RNA-seq/`: transcriptomic PCA, pathway, expression, heatmap, and correlation visualizations
- `Molecular/`: SPR, CUT&Tag, docking, and molecular visualization scripts

## Usage

R scripts accept tab-delimited input data and an output figure path as command-line arguments. The docking script accepts receptor, ligand, and output paths. Input data are not included in this repository.

## Requirements

R, Python, ggplot2, pheatmap, igraph, DESeq2, ggrepel, and PyMOL.
