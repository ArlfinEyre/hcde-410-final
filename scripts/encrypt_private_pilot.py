#!/usr/bin/env python3
"""Encrypt raw original Steam review CSV with a public RSA key before persistence.

Private key MUST NOT be placed on the runner, repository, or Action logs.
Cipher: gzip + AES-256-GCM; AES key is wrapped using RSA-OAEP-SHA256.
"""
import base64
import gzip
import hashlib
import json
import os
from datetime import datetime, timezone
from pathlib import Path

from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

plain_file = Path("data_private/pilot_reviews_private.csv")
if not plain_file.exists() or plain_file.stat().st_size == 0:
    raise RuntimeError("Missing original Steam API CSV; refusing to create placeholder")
raw = plain_file.read_bytes()
pubkey = serialization.load_pem_public_key(Path("scripts/steam_pilot_public_key.pem").read_bytes())
aeskey = os.urandom(32)
nonce = os.urandom(12)
context = b"HCDE410_STEAM_PILOT_V1"
encrypted_data = AESGCM(aeskey).encrypt(nonce, gzip.compress(raw, compresslevel=9), context)
encrypted_key = pubkey.encrypt(
    aeskey, padding.OAEP(mgf=padding.MGF1(algorithm=hashes.SHA256()),
    algorithm=hashes.SHA256(), label=None)
)
def b64(v): return base64.b64encode(v).decode("ascii")
out = Path("data_encrypted")
out.mkdir(parents=True, exist_ok=True)
envelope = {
    "format": "HCDE410_STEAM_PILOT_V1",
    "created_utc": datetime.now(timezone.utc).isoformat(),
    "algorithm": "gzip + AES-256-GCM + RSA-OAEP-SHA256",
    "public_key_file": "scripts/steam_pilot_public_key.pem",
    "encrypted_key_b64": b64(encrypted_key),
    "nonce_b64": b64(nonce),
    "encrypted_data_b64": b64(encrypted_data),
    "sha256_raw_csv": hashlib.sha256(raw).hexdigest(),
}
path = out / "steam_pilot_original_encrypted.json"
path.write_text(json.dumps(envelope, indent=2) + "\n", encoding="utf-8")
print("Encrypted genuine original review CSV to:", path)
print("Plaintext SHA256:", envelope["sha256_raw_csv"])
print("Raw review text is NOT printed and NOT committed.")
