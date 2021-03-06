###############################################################################
# Project-specific settings
###############################################################################

# Shows debug messages while Silence is running
DEBUG_ENABLED = False

# Database connection details
DB_CONN = {
    "host": "127.0.0.1",
    "port": 3306,
    "username": "iissi$user",
    "password": "iissi$user",
    "database": "entrega4",
}

# The sequence of SQL scripts located in the sql/ folder that must
# be ran when the 'silence createdb' command is issued
SQL_SCRIPTS = [
    "1-CreateTablesAndPopulate.sql",
    "2-CreateTriggersandProcedures.sql"
]

# The port in which the API and the web server will be deployed
HTTP_PORT = 8080

# The URL prefix for all API endpoints
API_PREFIX = "/api/v1"

# Table and fields that are used for both login and register
USER_AUTH_DATA = {
    "table": "Professors",
    "identifier": "email",
    "password": "dni",
}

# A random string that is used for security purposes
# (this has been generated automatically upon project creation)
SECRET_KEY = "RpgH_pBZwUTC_OMt24SdkaWWhGPypwh6hybST7EPmn4"
