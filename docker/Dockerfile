FROM debian:stable

LABEL maintainer "Diego Garrido Martín <diego.garrido@crg.eu>" \
      version "1.0" \
      description "Docker image for epigenomics course"

# Install basic tools
RUN apt-get update --fix-missing -qq && \
        apt-get install -y -q \
    bsdmainutils \
    bc \
    nano \ 
    wget \
    gawk \
    git-all \
    build-essential \
    python-is-python3 \
    r-base \
    bedtools \
    && apt-get clean \
    && apt-get purge \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

RUN mkdir software

## Install BEDtools
RUN apt-get update -qq && apt-get install -y bedtools && apt-get clean


## Install bigBedToBed
RUN cd software \
    && wget http://hgdownload.cse.ucsc.edu/admin/exe/linux.x86_64/bigBedToBed \
    && chmod +x bigBedToBed \
    && ln -s /software/bigBedToBed /usr/local/bin/bigBedToBed

## Install R packages
RUN R -e 'install.packages( c("optparse", "ggplot2", "VennDiagram"), repos="http://cloud.r-project.org/");' 

