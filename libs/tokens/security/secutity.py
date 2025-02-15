from dataclasses import dataclass

@dataclass
class Security():
    SECURITY_KEY = "e859fa584aeb78113af2ac7846cd0a5b28d96a56ecc60ec247e6eb4f4d503cec6fc2618687e92432363ddd602f4a80f6bd3d48fead411a229dd8665a7e11c699" # openssl rand -hex 64
    ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 1
    ALGORYTM = "HS512"