import bcrypt


def hash_passwd(passwd: str):
    return bcrypt.hashpw(passwd.encode("utf-8"), bcrypt.gensalt()).decode()


def check_passwd(passwd: str, hash_passwd: str):
    return bcrypt.checkpw(passwd.encode("utf-8"), hash_passwd.encode("utf-8"))
