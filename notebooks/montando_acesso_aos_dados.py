# Databricks notebook source
dbutils.fs.mkdirs('/mnt/dados')

# COMMAND ----------

# MAGIC %python
# MAGIC dbutils.fs.ls('/mnt')

# COMMAND ----------

# MAGIC %scala
# MAGIC val configs = Map(
# MAGIC   "fs.azure.account.auth.type" -> "OAuth",
# MAGIC   "fs.azure.account.oauth.provider.type" -> "org.apache.hadoop.fs.azurebfs.oauth2.ClientCredsTokenProvider",
# MAGIC   "fs.azure.account.oauth2.client.id" -> "5e4e8a69-0d37-47b4-881f-57ad4aa1ea1b",
# MAGIC   "fs.azure.account.oauth2.client.secret" -> "NbR8Q~xwNEWIyPxvc9ib9hOEV87b786o4yV86bcr",
# MAGIC   "fs.azure.account.oauth2.client.endpoint" -> "https://login.microsoftonline.com/98a8cfda-dc18-4b82-be95-f39a78e77a7f/oauth2/token")
# MAGIC // Optionally, you can add <directory-name> to the source URI of your mount point.
# MAGIC dbutils.fs.mount(
# MAGIC   source = "abfss://imoveis@datalakemillena.dfs.core.windows.net/",
# MAGIC   mountPoint = "/mnt/dados",
# MAGIC   extraConfigs = configs)
# MAGIC

# COMMAND ----------

# MAGIC %python
# MAGIC dbutils.fs.ls('/mnt/dados')

# COMMAND ----------


