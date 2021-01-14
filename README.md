# Spec spider

[![Build Status](https://travis-ci.org/orange2348/spec-spider.svg?branch=master)](https://travis-ci.org/orange2348/spec-spider)

#### Introduction
spec spider, use scrapy framework to get some spec. Now it can spide the Autosar 4.4、R19-11、R20-11 and Eth specs. You can specify the Autosar spec version you want to download in settings.py.


#### Install

1. Install scrapy:  
   pip install scrapy

#### Usage

1. scrapy crawl Autosar --nolog
1. scrapy crawl EthSpec --nolog
