import logging

# Configuração básica do logging
logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplos de logs em diferentes níveis
logging.debug('Mensagem de depuração (debug)')
logging.info('Informação útil (info)')
logging.warning('Aviso (warning)')
logging.error('Erro detectado (error)')
logging.critical('Erro crítico (critical)')