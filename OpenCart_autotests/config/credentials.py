from OpenCart_autotests.utils.docker_setup import get_local_ip


class Credentials:
    HOST = get_local_ip()
    ADMIN_LOGIN = {
        "username": "user",
        "password": "bitnami"
    }
    DB_CREDS = {
        # "host": "192.168.2.33",
        "port": "3306",
        "db_name": "bitnami_opencart",
        "user": "bn_opencart",
        "password": ""
    }
    API_CREDS = {
        "username": "Default",
        "key": "946fbf10c9364946e5dffa67d5240ad13a8b69b3bed1c358acdf65e6685be67c81e40254fca9839638337eb77851c000a8d5154433b87a181d15407705eb583e2330c95c37b34df1dd8b8011353a363e53f2045b52bc0d2d00b78a6ab683f5cfc8397f91f8d4f2d0fc13c185f5a62a17cd12fdb8f0cd30a00c103adb88f742b5"
    }
