from chor import (
    Compressor, 
    Logger, 
    Authenticator, 
    WebServer,
    HttpRequest,
)

def main():
    '''
        We want to have a chain like this:
        authenticator -> logger -> compressor 
    '''
    compressor = Compressor(None)
    logger = Logger(compressor)
    authenticator = Authenticator(logger)

    server = WebServer(authenticator)
    server.handle(HttpRequest("admin", "1234"))
    # server.handle(HttpRequest("admin", "124"))


if __name__ == '__main__':
    main()