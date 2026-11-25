#!/usr/bin/env python3
"""Decrypt the archived Steam pilot CSV using the separately saved PRIVATE key.

Usage:
  python scripts/decrypt_private_pilot.py \
    --input data_encrypted/steam_pilot_original_encrypted.json \
    --key /secure/location/steam_pilot_private_key.pem
"""
import argparse
import base64
import gzip
import hashlib
import json
import os
from pathlib import Path
from cryptography.hazmat.primitives import hashes, serialization
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives.ciphers.aead import AESGCM

p = argparse.ArgumentParser()
p.add_argument("--input", default="data_encrypted/steam_pilot_original_encrypted.json")
p.add_argument("--key", required=True, help="Path to private key. NEVER commit it.")
p.add_argument("--output", default="data_private/pilot_reviews_private.csv")
args = p.parse_args()
env = json.loads(Path(args.input).read_text(encoding="utf-8"))
assert env["format"] == "HCDE410_STEAM_PILOT_V1", "Unexpected envelope format"
key = serialization.load_pem_private_key(Path(args.key).read_bytes(), password=None)
def un64(s): return base64.b64decode(s, validate=True)
aeskey = key.decrypt(un64(env["encrypted_key_b64"]), padding.OAEP(
    mgf=padding.MGF1(algorithm=hashes.SHA256()), algorithm=hashes.SHA256(),
    label=None
))
raw = gzip.decompress(AESGCM(aeskey).decrypt(
    un64(env["nonce_b64"]), un64(env["encrypted_data_b64"]),
    b"HCDE410_STEAM_PILOT_V1"))
if hashlib.sha256(raw).hexdigest() != env["sha256_raw_csv"]:
    raise RuntimeError("Integrity check failed")
dst = Path(args.output)
dst.parent.mkdir(parents=True, exist_ok=True)
fd = os.open(dst, os.O_CREAT | os.O_WRONLY | os.O_TRUNC, 0o600)
with os.fdopen(fd, "wb") as f: f.write(raw)
os.chmod(dst, 0o600)
print("Decrypted and integrity-verified original CSV into", dst)
print("Bytes:", len(raw), "(raw content was not printed)")
