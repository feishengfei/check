
# About

This project is inspired by [free](https://github.com/freefq/free) and [check](https://github.com/yeahwu/check) to filter free [v2](https://github.com/v2fly/v2ray-core) site periodically by [docker-v2](https://hub.docker.com/r/v2ray/official)

    

## Table valid
|    | id                   | addr                       | cn             | cc   | isp                                  | ip              | chatgpt          |
|---:|:---------------------|:---------------------------|:---------------|:-----|:-------------------------------------|:----------------|:-----------------|
|  0 | [3](config/3.json)   | 35.177.137.93              | United Kingdom | GB   | AMAZON-02                            | 13.40.181.177   | Yes (Region: GB) |
|  1 | [4](config/4.json)   | 51.104.230.134             | United Kingdom | GB   | MICROSOFT-CORP-MSN-AS-BLOCK          | 51.104.230.134  | Yes (Region: GB) |
|  2 | [9](config/9.json)   | series-a2-mec.samanehha.co | United Kingdom | GB   | AMAZON-02                            | 13.40.181.177   | Yes (Region: GB) |
|  3 | [11](config/11.json) | gz.daxun.cyou              | Taiwan         | TW   | Scloud Pte Ltd                       | 165.154.237.68  | Yes (Region: TW) |
|  4 | [12](config/12.json) | 104.18.202.250             | United Kingdom | GB   | AS-GLOBALTELEHOST                    | 185.221.219.83  | Yes (Region: GB) |
|  5 | [22](config/22.json) | data-us-v1.shwjfkw.cn      | United States  | US   | Brain PEACE Science Foundation, Inc. | 104.249.174.138 | Yes (Region: US) |

## Valid
```
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpJdlJEUTZiYzl5ckZyYWo0@18.171.124.19:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%201
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1MTdUM0J2cFlhYWl1VzJj@35.177.137.93:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BD%E5%8D%8E%E7%9B%9B%E9%A1%BF%E5%B7%9E%E8%A5%BF%E9%9B%85%E5%9B%BE%E5%B8%82%E4%BA%9A%E9%A9%AC%E9%80%8A%28Amazon%29%E5%85%AC%E5%8F%B8%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%203
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTpjV0txZ1oyWXJOV1RPTGhETXRKbjJS@51.104.230.134:60156#github.com/freefq%20-%20%E7%88%B1%E5%B0%94%E5%85%B0%20%204
ss://Y2hhY2hhMjAtaWV0Zi1wb2x5MTMwNTp1MTdUM0J2cFlhYWl1VzJj@series-a2-mec.samanehha.co:443#github.com/freefq%20-%20%E7%BE%8E%E5%9B%BDAmazon%E6%95%B0%E6%8D%AE%E4%B8%AD%E5%BF%83%209
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTUzMTdcdTRlYWNcdTVlMDJcdTc5ZmJcdTUyYTggMTEiLCAiYWRkIjogImd6LmRheHVuLmN5b3UiLCAicG9ydCI6ICIzODAxMSIsICJ0eXBlIjogIm5vbmUiLCAiaWQiOiAiYWM1ODUyZGYtOGNhZi00ZDg2LThjNzctOTNhNzA5MmY2NmYxIiwgImFpZCI6ICIwIiwgIm5ldCI6ICJ0Y3AiLCAicGF0aCI6ICIvIiwgImhvc3QiOiAiZ3ouZGF4dW4uY3lvdSIsICJ0bHMiOiAiIn0=
vmess://eyJhZGQiOiAiMTA0LjE4LjIwMi4yNTAiLCAidiI6ICIyIiwgInBzIjogImdpdGh1Yi5jb20vZnJlZWZxIC0gXHU3ZjhlXHU1NmZkQ2xvdWRGbGFyZVx1NTE2Y1x1NTNmOENETlx1ODI4Mlx1NzBiOSAxMiIsICJwb3J0IjogMjA4MiwgImlkIjogIjAzZmNjNjE4LWI5M2QtNjc5Ni02YWVkLThhMzhjOTc1ZDU4MSIsICJhaWQiOiAiMCIsICJuZXQiOiAid3MiLCAidHlwZSI6ICIiLCAiaG9zdCI6ICJlcmZhbm5ld2ZyZWVub2Rlcy52ZG1tc3d5em16aWdvbnZuams0NDMud29ya2Vycy5kZXYiLCAicGF0aCI6ICIvbmluYS5ib25kL2xpbmt2d3MiLCAidGxzIjogIiJ9
vmess://eyJ2IjogIjIiLCAicHMiOiAiZ2l0aHViLmNvbS9mcmVlZnEgLSBcdTVlN2ZcdTRlMWNcdTc3MDFcdTc5ZmJcdTUyYTggMjIiLCAiYWRkIjogImRhdGEtdXMtdjEuc2h3amZrdy5jbiIsICJwb3J0IjogIjIwNDAxIiwgImlkIjogImIxNDc4ZTI0LTQ5MTYtM2FiZS04ZjE3LTE1OTMxMDEyZWNiZSIsICJhaWQiOiAiMCIsICJzY3kiOiAiYXV0byIsICJuZXQiOiAid3MiLCAidHlwZSI6ICJub25lIiwgImhvc3QiOiAiZGF0YS11cy12MS5zaHdqZmt3LmNuIiwgInBhdGgiOiAiL2RlYmlhbiIsICJ0bHMiOiAiIiwgInNuaSI6ICIiLCAiYWxwbiI6ICIiLCAiZnAiOiAiIn0=
```

