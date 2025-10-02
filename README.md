# Проект с кеширующем слоем

Хосты настраивал с помощью ansible\
-**firewall-setup.yml**\
-**firewall-setup.j2**

[Отчёт со скринами](https://disk.yandex.ru/d/z7EsvTVYxn97XA)
___
[redis]\
redis-server ansible_host=192.168.1.138

[postgresql]\
postgresql-server ansible_host=192.168.1.193

[backendapi]\
backend-api ansible_host=192.168.1.216

[proxy]\
proxy-server ansible_host=192.168.1.238
___
