import hmac
import hashlib

def calcular_assinatura(payload: bytes, secret: bytes) -> str:
    """
    Calcula a assinatura para um payload específico.
    
    Args:
        payload (bytes): O payload a ser assinado.
        secret (bytes): A chave secreta usada para calcular a assinatura.
        
    Returns:
        str: A assinatura calculada no formato hexadecimal.
    """
    return hmac.new(
        secret,
        payload,
        hashlib.sha256
    ).hexdigest()

def verificar_assinatura(payload: bytes, assinatura_recebida: str, secret: bytes) -> bool:
    """
    Verifica a assinatura recebida para um payload específico.
    
    Args:
        payload (bytes): O payload a ser verificado.
        assinatura_recebida (str): A assinatura recebida.
        secret (bytes): A chave secreta usada para calcular a assinatura.
        
    Returns:
        bool: True se a assinatura for válida, False caso contrário.
    """
    return calcular_assinatura(payload, secret) == assinatura_recebida

def simular_situacao_valida():
    secret = b"minha_chave_super_secreta"
    payload = b'{"evento":"push","usuario":"ana"}'
    assinatura_recebida = calcular_assinatura(payload, secret)
    
    if verificar_assinatura(payload, assinatura_recebida, secret):
        print("Situacao valida")
    else:
        print("Situacao invalida")

def simular_situacao_invalida():
    secret = b"minha_chave_super_secreta"
    payload = b'{"evento":"push","usuario":"ana"}'
    assinatura_recebida = "assinatura_invalida"
    
    if verificar_assinatura(payload, assinatura_recebida, secret):
        print("Situacao valida")
    else:
        print("Situacao invalida")

def simular_situacao_payload_invalido():
    secret = b"minha_chave_super_secreta"
    payload = b'{"evento":"push","usuario":"invalido"}'
    assinatura_recebida = calcular_assinatura(payload, secret)
    
    if verificar_assinatura(payload, assinatura_recebida, secret):
        print("Situacao valida")
    else:
        print("Situacao invalida")

def main():
    simular_situacao_valida()
    simular_situacao_invalida()
    simular_situacao_payload_invalido()

if __name__ == "__main__":
    main()
    