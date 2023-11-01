#!/usr/bin/env bash


brew install jpeg-xl

#/opt/homebrew/bin/pip3.10 install --config-settings="--build-option=-I/opt/homebrew/include/" git+https://github.com/foosoftsrl/jxlpy@0.9.5

LDFLAGS="-L/opt/homebrew/lib/" CPPFLAGS="-I/opt/homebrew/include/" /opt/homebrew/bin/pip3.10 install git+https://github.com/olokelo/jxlpy
