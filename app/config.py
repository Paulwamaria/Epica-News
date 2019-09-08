class Config:
    '''
    General configuration parent class
    '''
    # https://newsapi.org/v2/sources?apiKey=cf19b9328d6c49fdb4bc3919cbd7f5a6
    NEWS_SOURCES_BASE_URL = 'https://newsapi.org/v2/sources?apiKey={}'
    ARTICLES_API_BASE_URL = 'https://newsapi.org/v2/everything?q={}&apiKey={}'
   


class ProdConfig(Config):
    '''
    Production  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''
    pass


class DevConfig(Config):
    '''
    Development  configuration child class

    Args:
        Config: The parent configuration class with General configuration settings
    '''

    DEBUG = True