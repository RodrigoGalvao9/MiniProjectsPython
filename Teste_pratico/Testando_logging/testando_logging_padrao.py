import logging

# Configuração básica do logging
logging.basicConfig(filename=r"Teste_pratico\Testando_logging\app.log" ,level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

# Exemplos de logs em diferentes níveis
logging.debug('Mensagem de depuração')
logging.info('Informação útil')
logging.warning('Avis')
logging.error('Erro detectado')
logging.critical('Erro crítico')