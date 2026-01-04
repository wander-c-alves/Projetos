velocidade = 65  # velocidade atual do carro
localizacao_carro = 100  # local em que o carro está na estrada

VM_RADAR_1 = 60  # velocidade máxima do radar 1
LOCAL_RADAR_1 = 100  # local onde o radar 1 está
RADAR_RANGE = 1  # A distância onde o radar pega

# 1. Verificar se o carro está no alcance do radar
alcance_min = localizacao_carro - RADAR_RANGE
alcance_max = localizacao_carro + RADAR_RANGE
alcance_carro = (localizacao_carro >= alcance_min) and (localizacao_carro <= alcance_max)

# 2. Verificar se o carro excedeu a velocidade máxima
velocidade_excedida = velocidade > VM_RADAR_1

# 3. Determinar se o carro foi multado
multado = velocidade_excedida and alcance_carro

# 4. Exibir o resultado
if multado:
    print('Multado')
else:
    print('Não foi multado')
