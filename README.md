## Our buildserver is currently running on: ##

> Ubuntu 12.04.5 LTS (GNU/Linux 3.2.13-grsec-xxxx-grs-ipv6-64 x86_64)

## OpenSPA is build using oe-alliance build-environment and several git repositories: ##

> [https://github.com/oe-alliance/oe-alliance-core](https://github.com/oe-alliance/oe-alliance-core "OE-Alliance")
> 
> [https://github.com/OpenSPA/dvbapp](https://github.com/OpenSPA/dvbapp "OpenSPA E2")
> 
> [https://github.com/OpenSPA/enigma2-plugin-skins-blackmodernhd](https://github.com/OpenSPA/enigma2-plugin-skins-blackmodernhd "OpenSPA Skin")

> and a lot more...


----------

# Building Instructions #

1 - Install packages on your buildserver

    sudo apt-get install -y autoconf automake bison bzip2 chrpath cvs diffstat flex g++ gawk gcc gettext git-core gzip help2man htop libc6-dev libglib2.0-dev libproc-processtable-perl libtool libxml2-utils make ncdu ncurses-bin ncurses-dev patch perl pkg-config po4a pseudo python-setuptools quilt sgmltools-lite sshpass subversion swig tar texi2html texinfo wget xsltproc zip zlib1g-dev

----------
2 - Set your shell to /bin/bash

    sudo dpkg-reconfigure dash
    When asked: Install dash as /bin/sh?
    select "NO"

----------
3 - Add user openspabuilder

    sudo adduser openspabuilder

----------
4 - Switch to user openspabuilder

    su openspabuilder

----------
5 - Switch to home of openspabuilder

    cd ~

----------
6 - Create folder openspa

    mkdir -p ~/openspa

----------
7 - Switch to folder openspa

    cd openspa

----------
8 - Clone oe-alliance git

    git clone git://github.com/oe-alliance/build-enviroment.git

----------
9 - Switch to folder build-enviroment

    cd build-enviroment

----------
10 - Update build-enviroment

    make update

----------
11 - Finally you can start building a image

    make MACHINE=vusolo2 DISTRO=openspa image
