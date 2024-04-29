import sys
from mbedtls.pk import get_supported_curves
from mbedtls import pk


# expencted inputs "data, signature" are bytes
def autenticate_message(data, signature, certpath):
    # get certificate name
    pem_file = "ecdsa-secp192r1-pub-key.pem"

    # load public key
    key = load_public_key_from_pem(certpath)

    # verify message autenticity
    verification_result = key.verify(data, signature, "sha256")

    return verification_result


def load_public_key_from_pem(pem_file):
    # Read the PEM file
    with open(pem_file, "rb") as file:
        pem_data = file.read()

    ecdsa = pk.ECC(curve=get_supported_curves()[9]).from_PEM(pem_data.decode())
    print("Public key")
    print(ecdsa.export_public_key(format("PEM")))
    return ecdsa



if __name__ == '__main__':

    arguments = sys.argv
    print(arguments)

    #ukazak vstupov, funguje aj v takom aj v takom formate
    received_data1 = b'\x76\x73\x74\x75\x70'
    received_data = b'vstup'
    received_signature = b'\x30\x34\x02\x18\x49\xC8\x2A\x89\x14\x44\xB1\xF0\x25\x1C\x81\x08\x60\xBB\x29\x27\x9E\x08\x15\xA1\x94\xFA\xD1\x08\x02\x18\x00\xF4\x58\x9D\x88\xC9\x1D\xCA\xBD\x54\xEB\xD7\x69\xF3\xB8\xFA\xC4\x75\xC0\xC3\x54\x62\xB4\x65'

    # toto sa bude volat na overenie, vysledok vrati (true/false)
    #vysledok = autenticate_message(received_data, received_signature)
    
    vysledok = autenticate_message(arguments[1], bytes(arguments[2]), arguments[3])
    print(vysledok)



