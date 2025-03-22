import logging

logformat = '%(asctime)s - %(levelname)s - %(message)s'

def setup_logging():
    # Set up basic configuration for logging
    logging.basicConfig(level=logging.DEBUG, format=logformat)
    
    # Extract logger
    extract_logger = logging.getLogger('extract')
    extract_logger.setLevel(logging.DEBUG)
    extract_handler = logging.FileHandler('extract/extract.log')
    extract_handler.setFormatter(logging.Formatter(logformat))
    extract_logger.addHandler(extract_handler)

    # Transform logger
    transform_logger = logging.getLogger('transform')  # Corrected typo here
    transform_logger.setLevel(logging.DEBUG)
    transform_handler = logging.FileHandler('transform/transform.log')
    transform_handler.setFormatter(logging.Formatter(logformat))
    transform_logger.addHandler(transform_handler)

    # Load logger
    load_logger = logging.getLogger('load')
    load_logger.setLevel(logging.DEBUG)
    load_handler = logging.FileHandler('load/load.log')
    load_handler.setFormatter(logging.Formatter(logformat))
    load_logger.addHandler(load_handler)

    # ETL pipeline logger
    etl_logger = logging.getLogger('etl_pipeline')
    etl_logger.setLevel(logging.DEBUG)
    etl_handler = logging.FileHandler('etl_pipeline/etl_pipeline.log')
    etl_handler.setFormatter(logging.Formatter(logformat))
    etl_logger.addHandler(etl_handler)

    # Return the ETL pipeline logger to be used elsewhere
    return etl_logger
