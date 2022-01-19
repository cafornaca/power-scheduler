from urllib.parse import quote_plus

class MicrosoftSQLServer(object):
    """
    This is a class to store and create the appropriate connection string. It
    takes in the various parameters required by connection string.

    Args:
        server
    """

    def __init__(self, server, database, username, password, driver='FreeTDS',
                 port=1433, driver_version=8.0):

        # Going through the parameters and checking if they exist then
        # assembling the connection string
        try:
            if driver:
                temp_string = 'DRIVER={};'.format(driver)
            if server:
                temp_string = temp_string + 'SERVER={};'.format(server)
            if port:
                temp_string = temp_string + 'PORT={};'.format(port)
            if database:
                temp_string = temp_string + 'DATABASE={};'.format(database)
            if username:
                temp_string = temp_string + 'UID={};'.format(username)
            if username:
                temp_string = temp_string + 'PWD={};'.format(password)


            temp_string = temp_string + 'CHARSER=UTF-8;'

            if driver == 'FreeTDS':
                temp_string = temp_string + \
                    'TDS_VERSION={}'.format(driver_version)
        except Exception:
            raise ProcessLookupError

        self.connection_string = temp_string

    @property
    def connection_string(self):
        """

        """
        return self._connection_string

    @connection_string.setter
    def connection_string(self, connection_string):
        parsed = quote_plus(connection_string)
        parsed = 'mssql+pyodbc:///?odbc_connect={}'.format(parsed)
        self._connection_string = parsed

def get_db_session(config):
    if config.db['flavor'] == 'microsoft':
        config.process_server()
        connection = MicrosoftSQLServer(
            server=config.db['server'],
            database=config.db['database'],
            username=config.db['username'],
            password=config.db['password'])
        connection = connection.connection_string