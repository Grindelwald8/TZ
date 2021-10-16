FROM ubuntu:20.04
RUN apt-get -y update
ENV TZ=Europe/Moscow
WORKDIR /usr/src/myapp
COPY . /usr/src/myapp
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone
RUN  apt-get install -y build-essential libtool autotools-dev automake pkg-config libssl-dev libevent-dev bsdmainutils
RUN apt-get install -y libboost-system-dev libboost-filesystem-dev libboost-chrono-dev libboost-program-options-dev libboost-test-dev libboost-thread-dev
RUN apt install -y libdb5.3++-dev libdb5.3++ libdb5.3-dev
EXPOSE 22556:22556
RUN ./autogen.sh
RUN ./configure --with-incompatible-bdb
CMD ["make"]