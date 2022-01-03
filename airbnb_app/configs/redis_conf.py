import redis
from redis.sentinel import Sentinel

from django.conf import settings


redis_instance = redis.Redis(
    host=settings.REDIS_HOST,
    port=settings.REDIS_PORT,
    db=settings.REDIS_DB,
    charset=settings.DEFAULT_CHARSET,
    decode_responses=settings.REDIS_DECODE_RESPONSES,
)
if settings.PROJECT_ENVIRONMENT == settings.EnvironmentType.PROD.value:
    hosts = settings.REDIS_SENTINEL_HOSTS
    sentinel = Sentinel(
        sentinels=[(host, 26379) for host in hosts],
        socket_timeout=0.1,
        ssl=True,
        ssl_ca_certs=settings.REDIS_SSL_CERT_DOCKER_PATH,
    )
    redis_instance: redis.Redis = sentinel.master_for(
        service_name=settings.REDIS_CLUSTER_NAME,
        password=settings.REDIS_CLUSTER_PASSWORD,
        decode_responses=settings.REDIS_DECODE_RESPONSES,
    )
