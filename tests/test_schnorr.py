from crypto.parameters import PedersenParameters
from crypto.pedersen import create_commitment
from crypto.schnorr import (
    compute_public_statement,
    generate_nonce,
    compute_schnorr_commitment,
    generate_challenge,
    compute_response,
    verify_schnorr_proof
)

p = 23
q = 11
g = 2
h = 4
params = PedersenParameters(p, q, g, h)

def test_valid_schnorr_proof():
    value = 5
    randomness = 3

    commitment = create_commitment(value, randomness, params)
    public_statement = compute_public_statement(commitment, value, params)

    nonce = generate_nonce(q)
    proof_commitment = compute_schnorr_commitment(nonce, params)

    challenge = generate_challenge(q)
    response = compute_response(nonce, challenge, randomness, q)

    assert verify_schnorr_proof(
        public_statement,
        proof_commitment,
        challenge,
        response,
        params
    )

def test_invalid_response():
    value = 5
    randomness = 3

    commitment = create_commitment(value, randomness, params)
    public_statement = compute_public_statement(commitment, value, params)

    nonce = generate_nonce(q)
    proof_commitment = compute_schnorr_commitment(nonce, params)

    challenge = generate_challenge(q)
    response = compute_response(nonce, challenge, randomness, q)

    wrong_response = (response + 1) % q

    assert not verify_schnorr_proof(
        public_statement,
        proof_commitment,
        challenge,
        wrong_response,
        params
    )
    

"""
1- Test d'une preuve valide
Objectif : vérifier qu'une preuve Schnorr correctement construite est acceptée.

Déroulement :
1. Choisir un secret \(r\).
2. Construire un engagement de Pedersen \(C\) pour une valeur connue \(m\).
3. Calculer le statement public \(Y\).
4. Générer un nonce \(w\).
5. Calculer l'engagement Schnorr \(A\).
6. Générer un défi \(e\).
7. Calculer la réponse \(z\).
8. Vérifier la preuve.

------------------------------------------------------------------------------

2- Test avec une mauvaise réponse
Objectif : vérifier que Bob rejette une preuve dont la réponse a été modifiée.

Déroulement :
1. Construire une preuve valide comme dans le premier test.
2. Modifier volontairement la réponse \(z\), par exemple en lui ajoutant 1 modulo \(q\).
3. Soumettre cette réponse modifiée à la fonction de vérification.

--------------------------------------------------------------------------------

3- Test avec un mauvais défi
Objectif : vérifier qu'une preuve construite pour un défi donné ne fonctionne pas avec un autre défi.

Déroulement :
1. Construire une preuve valide avec un défi \(e\).
2. Générer un autre défi \(e'\), différent de \(e\).
3. Conserver les mêmes \(Y\), \(A\) et \(z\).
4. Vérifier la preuve avec \(e'\) au lieu de \(e\).
"""
