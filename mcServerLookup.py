from mcstatus import MinecraftServer

print("\n==========Checking Status Of Conspirator.dev==========\n")

server = MinecraftServer.lookup("conspirator.dev:25565")

status = server.status()
serverName = status.description
print("Server Name: {0}".format(serverName["text"]))
print("The server has {0} players and replied in {1} ms".format(status.players.online, status.latency))


query = server.query()
print("The server has the following players online: {0}".format(", ".join(query.players.names)))

print("\n======================================================")
