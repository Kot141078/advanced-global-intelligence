from __future__ import annotations

import base64
import hashlib
import json
import os
from pathlib import Path
from typing import Any

from cryptography.hazmat.primitives.asymmetric.ed25519 import Ed25519PrivateKey, Ed25519PublicKey
from cryptography.hazmat.primitives.serialization import Encoding, NoEncryption, PrivateFormat, PublicFormat

from .common import canonical_bytes


def _b64(value: bytes) -> str:
    return base64.b64encode(value).decode("ascii")


def _unb64(value: str) -> bytes:
    return base64.b64decode(value.encode("ascii"), validate=True)


class TestKeyStore:
    """Ephemeral task-local key store. Private bytes never enter evidence output."""

    def __init__(self, root: Path):
        self.root = root
        self.root.mkdir(parents=True, exist_ok=True)

    def ensure(self, key_id: str) -> Ed25519PrivateKey:
        path = self.root / f"{key_id}.key"
        if path.exists():
            return Ed25519PrivateKey.from_private_bytes(path.read_bytes())
        key = Ed25519PrivateKey.generate()
        raw = key.private_bytes(Encoding.Raw, PrivateFormat.Raw, NoEncryption())
        fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_EXCL, 0o600)
        with os.fdopen(fd, "wb") as stream:
            stream.write(raw)
        return key

    def public_map(self, bindings: dict[str, str]) -> dict[str, Any]:
        keys: dict[str, Any] = {}
        for key_id, root_id in bindings.items():
            raw = self.ensure(key_id).public_key().public_bytes(Encoding.Raw, PublicFormat.Raw)
            keys[key_id] = {
                "algorithm": "Ed25519",
                "principal_root": root_id,
                "public_key_b64": _b64(raw),
                "fingerprint_sha256": hashlib.sha256(raw).hexdigest(),
            }
        return {"canonicalization": "RFC8785-JCS", "keys": keys}


def sign(payload: dict[str, Any], key_id: str, key: Ed25519PrivateKey, principal_root: str) -> dict[str, Any]:
    protected = {"algorithm": "Ed25519", "canonicalization": "RFC8785-JCS", "key_id": key_id, "principal_root": principal_root}
    signed = {"protected": protected, "payload": payload}
    return {**signed, "signature_b64": _b64(key.sign(canonical_bytes(signed)))}


def verify(envelope: dict[str, Any], public_map: dict[str, Any]) -> tuple[bool, str]:
    try:
        protected = envelope["protected"]
        key_id = protected["key_id"]
        entry = public_map["keys"][key_id]
        if protected["algorithm"] != "Ed25519" or protected["canonicalization"] != "RFC8785-JCS":
            return False, "UNSUPPORTED_ENVELOPE"
        if protected["principal_root"] != entry["principal_root"]:
            return False, "ISSUER_ROOT_MISMATCH"
        signed = {"protected": protected, "payload": envelope["payload"]}
        Ed25519PublicKey.from_public_bytes(_unb64(entry["public_key_b64"])).verify(
            _unb64(envelope["signature_b64"]), canonical_bytes(signed)
        )
        return True, "VALID"
    except (KeyError, ValueError, TypeError, Exception) as exc:
        return False, f"INVALID_SIGNATURE:{type(exc).__name__}"


def distinct_roots(envelopes: list[dict[str, Any]], public_map: dict[str, Any]) -> tuple[int, list[str]]:
    roots: set[str] = set()
    errors: list[str] = []
    for envelope in envelopes:
        valid, reason = verify(envelope, public_map)
        if valid:
            roots.add(public_map["keys"][envelope["protected"]["key_id"]]["principal_root"])
        else:
            errors.append(reason)
    return len(roots), errors

