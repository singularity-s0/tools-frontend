FROM apache/apisix:latest
USER root
RUN apt-get update
RUN apt-get install -y git python3 python3-pip make python3-setuptools python3-dev
RUN apt-get clean
RUN git clone https://github.com/apache/apisix-python-plugin-runner.git
RUN cd apisix-python-plugin-runner && make setup && make install

USER apisix
COPY --chown=apisix:apisix /apisix.yaml /usr/local/apisix/conf/apisix.yaml
COPY --chown=apisix:apisix /config.yaml /usr/local/apisix/conf/config.yaml
COPY --chown=apisix:apisix /plugins /usr/local/apisix/apisix-python-plugin-runner/apisix/plugins
COPY --chown=apisix:apisix /docker-entrypoint.sh /docker-entrypoint.sh
RUN chmod +x /docker-entrypoint.sh

ENTRYPOINT ["/docker-entrypoint.sh"]
CMD ["docker-start"]