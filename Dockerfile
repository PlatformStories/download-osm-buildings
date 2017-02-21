FROM debian:latest
MAINTAINER Kostas Stamatiou <kostas.stamatiou@digitalglobe.com>

RUN apt-get update && \
    apt-get install -y wget bzip2 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

ENV CONDA_DIR /opt/conda
ENV PATH $CONDA_DIR/bin:$PATH

# install conda
RUN wget --quiet https://repo.continuum.io/miniconda/Miniconda2-4.2.12-Linux-x86_64.sh && \
    /bin/bash Miniconda2-4.2.12-Linux-x86_64.sh -f -b -p $CONDA_DIR && \
    rm Miniconda2-4.2.12-Linux-x86_64.sh && \
    $CONDA_DIR/bin/conda config --system --add channels conda-forge

# install gdal
RUN conda install --quiet --yes -c conda-forge gdal=2.1.3 requests && \
    conda clean -tipsy

ADD download-osm-buildings.py /
