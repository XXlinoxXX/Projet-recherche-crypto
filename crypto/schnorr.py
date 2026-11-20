import math
import random
import secrets

def compute_public_statement(commitment, value, params):
    C = commitment % params.p
    return (C * pow(params.g, -value, params.p)) % params.p


def generate_nonce(q):
    return secrets.randbelow(q)


def compute_schnorr_commitment(nonce, params):
    return pow(params.h, nonce, params.p)


def generate_challenge(q):
    return secrets.randbelow(q)

def compute_response(nonce, challenge, randomness, q):
    return (nonce + challenge * randomness) % q
    

def verify_schnorr_proof(public_statement, proof_commitment, challenge, response, params):
    valueSchnorr = proof_commitment % params.p * pow(public_statement, challenge, params.p)
    return pow(params.h, response, params.p) == valueSchnorr % params.p

