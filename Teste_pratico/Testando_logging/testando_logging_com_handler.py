# usando handle e formatter
"""
O Handler é um componente do sistema de logging responsável por determinar onde as mensagens de log serão enviadas. Ele direciona os logs para diferentes destinos, como:

Console (tela): Para exibir as mensagens diretamente no terminal.
Arquivo (file): Para salvar os logs em um arquivo.
Servidor de log remoto: Para enviar os logs para um servidor específico.
EmailHandler: Para enviar logs por e-mail.
Você pode ter múltiplos handlers associados a um logger, e cada handler pode ser configurado com diferentes níveis de severidade e formatos.

----------------------------------------------------------------------------------------

O Formatter define o formato das mensagens de log. Ele controla como cada mensagem será apresentada, incluindo informações como:

Timestamp (data e hora) do evento de log.
Nome do logger.
Nível de severidade (DEBUG, INFO, WARNING, ERROR, CRITICAL).
Mensagem de log.
O Formatter é usado para definir um padrão de formato para as mensagens de log. O formato pode ser configurado usando placeholders, como %(asctime)s para o timestamp, %(name)s para o nome do logger, %(levelname)s para o nível de log, e %(message)s para a mensagem em si.
"""
import logging

# Criando um logger
logger = logging.getLogger('meu_logger_formatado')
logger.setLevel(logging.INFO) # Configura o logger para capturar mensagens de INFO e superiores

# Criando um handler para o console
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO) # Configura o handler para capturar mensagens de INFO e superiores

# Criando um handler para o arquivo
file_handler = logging.FileHandler(r"Teste_pratico\Testando_logging\app2.log")
file_handler.setLevel(logging.INFO)  # Configura o handler para capturar mensagens de INFO e superiores

# Criando um formatter e configurando-o no handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
console_handler.setFormatter(formatter) # console
file_handler.setFormatter(formatter) # arquivo

# Adicionando o handler ao logger
logger.addHandler(console_handler)
logger.addHandler(file_handler)

# Testando o logger
logger.debug('Esta mensagem de depuração não será exibida.')
logger.info('Mensagem de informação com formato customizado.')
logger.warning('Esta mensagem de aviso será capturada, pois é superior a INFO.')
logger.error('Mensagem de erro com formato customizado.')