FROM theteamultroid/ultroid:main

COPY installer.sh .

RUN bash installer.sh

# changing workdir
WORKDIR "/root/ArmanGG01"

# start the bot.
CMD ["bash", "start"]
