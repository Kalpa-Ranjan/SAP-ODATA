



ODATA —> Open Data Protocol 

                  (ISO International Organization for Standardization/

               IEC International Electrotechnical Commission approved)

    

    OASIS (Organization for the Advancement of Structured Information Standards) standard that defines a set of best practices for building and consuming RESTful APIs

     

## What is API?

    API (Application Programming Interface) is a set of rules, protocols, and tools that allows different software applications to communicate with each other.

## Four different ways API can work

    1. SOAP APIs:- XML, Used in past
    2. RPC APIs:- Remote Procedure Calls
    3. WebSocket APIs:- Used JSON objects, two way communication
    4. REST API: - Most Popular
    

# REST Principles/ 
architectural constraints

    

```mermaid

flowchart LR
  A[REST]
  A --> B[Uniform Interface]
  A --> C[Statelessness]
  A --> D[Client-Server]
  A --> E[Cacheabilit]
  A --> F[Layered System]
  A --> G[Code on Demand]
  
  style A fill:#64bef9, stroke:#000, stroke-width:2px,color:#000
  style B fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style A fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style C fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style D fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style E fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style F fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000
  style G fill:#bce2fb, stroke:#000, stroke-width:2px,color:#000

```

## Uniform Interface

    It indicates Server transfers information in a standard format.

    5. The formatted resource is called a Representation in REST.
    6. Request should identify recourses by using URI
    7. Clients have enough information in the resource representation to modify, delete the resource. The server meets this condition by sending metadata that describes the resource further. 
    8. Client receive information about how to process the representation further. The server achieves this by sending self descriptive messages that contain metadata about how the client can best use them.
    9. For other related resourses server sends hyperlink in the represenation. So client can dynamically discover more resources.
    

## Statelessness

    

    10. Communication method in which the server completes every client request independently of all previous request.
## Layered System

    

    The client can connect to other authorized intermediaries between client and server.

## Catchability

    It stores some responses on the client or an intermediary to improve server response time.

## Code on Demand

    Server can temporarily extend or customize client functionality by transferring softare programming code to client

    Example:

    When you fill registration form on any websites, your browser heighlights mistake. Such as incorrect phone number. It can do this by the code sent by server. 

    

    

    



```mermaid
graph LR
  A[ODATA]--as --> B[Web SQL]
  style A fill:#0287de
  style B fill:#0287de
```





## Remote API vs Web API

Remote API: designed to interact with communication network. By remote, we mean that resources being manipulated by the API are somewhere outside computer making the request.



Web API: Communication Network(WWW)

ALL Web services are APIs, but not all APIs are web services.

## What does the RESTful API Client Request contain?

1. Unique recourse identifier:- URI ⇒ (URL- Location + URN-Name)
1. HTTP Method: GET, POST, DELETE, PUT, PATCH
1. HTTP Headers: Extra information


## What does the RESTful API server response contain?



- Status  line 
  1XX :- Informational → Processing 102

  2XX :- Success →Ok 200, Ok Created 201

  3XX :- Redirection → moved to new URL 301

  4XX :- Client Side Error → Bad request 400

  5XX:- Server Side Error → Not implemented 501



- Message body
  Contains recourse representation

-  Header


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAH3EUXN%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T182450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuX3fIDDCSQiS1vZ3%2FABku2kKV%2F9niwBiHyvzzgzzooAiBBj8oZe93kBipZ1DRTCzmweQa0E4dw8m5WAp2Bb%2Fkk8SqIBAi3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeLBRwKQZ3FLrs8%2FSKtwDVDM3pkbJWolsdlSTme4w73wGmyXCIykcNGEUNIHkE9nhS1%2FPSFIjZSsBZLfY6u2kCP1kQlnL85R4xe%2ByfPbwNIHl7N2%2Fd1RO%2Ff%2BolUirPULqmEzVVsst2fsRO%2BcH1uhuyFd8cCpd6whxE4jEFxR8aY1xNHhm1JwkQ1byfsubaozmIe%2Fl9vudbIm5osrC1wECPxFx4nbl%2FqJXTZdUxzNV%2FGYVwdTn5qVPJhReNeQhDmALov8RgysMtW2O5onKF0W9%2FwoE2%2FRNt9EZIhj9erT7YIqsBfGEkyuTK9d9gLQnvb2dvc8BoGFzTHDF9UW7ZL92icz0zyJqA35fTfd6Z0POasnJb1AGV%2FDpBldf6So3%2FtzFlYb6w6yaC74iqSw3%2FAywJslZGi50UWIs3AodNMEGFbFrzs6mp9JH%2Fjt5rDGdQp1f8fxQnsTqQSO5NhtmlfMfRxfTGMq6w3UHqBgGVVIr9SXzPhAL6FULuPLYmLIQ8Paymfs%2FUEvVs7G1Rssc%2BZd%2F2M8eV3fonlpvh0v3KwQ8RbeInOPypSGMK9RQ%2FPT4cXRI6X6B7Tx4nhwR8b%2FDl%2BjP4rE8Un57JplR0OsH%2BiTzFTiEGl4gMQMBGaQ93R5Lt4zxxYBGUsIJfPrXRHQw17PPygY6pgHQYlZgbYamrZoe%2BMIbfxNWgKkKzTtav6%2BdbFjEgDMIzHmez%2Baf8C0Fh4ta%2Fd83Ij4bVqiub42EhfTGhDbh2edHNzKTclGnLhXPKxpk6XqKrDkxNFqUlMqtz22WgGWdyX5tHVLXa3YIHhwza3EN%2BI%2BuGmv%2BKWynIZzp1hQYulsC3cE3QoixUjMvp8cEY0baWtmiJGLY%2BhjZAM%2BOneyEqhv%2F8PlN7X1w&X-Amz-Signature=02529165f9174291beead303a0cc3e3e4e8ba8445d9620e1311476edf78feb6b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QAH3EUXN%2F20251230%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251230T182450Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEO7%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIBuX3fIDDCSQiS1vZ3%2FABku2kKV%2F9niwBiHyvzzgzzooAiBBj8oZe93kBipZ1DRTCzmweQa0E4dw8m5WAp2Bb%2Fkk8SqIBAi3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMeLBRwKQZ3FLrs8%2FSKtwDVDM3pkbJWolsdlSTme4w73wGmyXCIykcNGEUNIHkE9nhS1%2FPSFIjZSsBZLfY6u2kCP1kQlnL85R4xe%2ByfPbwNIHl7N2%2Fd1RO%2Ff%2BolUirPULqmEzVVsst2fsRO%2BcH1uhuyFd8cCpd6whxE4jEFxR8aY1xNHhm1JwkQ1byfsubaozmIe%2Fl9vudbIm5osrC1wECPxFx4nbl%2FqJXTZdUxzNV%2FGYVwdTn5qVPJhReNeQhDmALov8RgysMtW2O5onKF0W9%2FwoE2%2FRNt9EZIhj9erT7YIqsBfGEkyuTK9d9gLQnvb2dvc8BoGFzTHDF9UW7ZL92icz0zyJqA35fTfd6Z0POasnJb1AGV%2FDpBldf6So3%2FtzFlYb6w6yaC74iqSw3%2FAywJslZGi50UWIs3AodNMEGFbFrzs6mp9JH%2Fjt5rDGdQp1f8fxQnsTqQSO5NhtmlfMfRxfTGMq6w3UHqBgGVVIr9SXzPhAL6FULuPLYmLIQ8Paymfs%2FUEvVs7G1Rssc%2BZd%2F2M8eV3fonlpvh0v3KwQ8RbeInOPypSGMK9RQ%2FPT4cXRI6X6B7Tx4nhwR8b%2FDl%2BjP4rE8Un57JplR0OsH%2BiTzFTiEGl4gMQMBGaQ93R5Lt4zxxYBGUsIJfPrXRHQw17PPygY6pgHQYlZgbYamrZoe%2BMIbfxNWgKkKzTtav6%2BdbFjEgDMIzHmez%2Baf8C0Fh4ta%2Fd83Ij4bVqiub42EhfTGhDbh2edHNzKTclGnLhXPKxpk6XqKrDkxNFqUlMqtz22WgGWdyX5tHVLXa3YIHhwza3EN%2BI%2BuGmv%2BKWynIZzp1hQYulsC3cE3QoixUjMvp8cEY0baWtmiJGLY%2BhjZAM%2BOneyEqhv%2F8PlN7X1w&X-Amz-Signature=751703c001218bd7090f3ae141c4fd7d845594dc8f6d27308913368e5fe8bf76&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





For HTTP PORT is 80



What is ODATA?

  ODATA is a Web protocol based om REST, for querying and updating Data.

Applying and building on Web technologies such as

  1. HTTP
  2. Atom publishing Protocol
  3. RSS ( Really Simple Syndication) 


Provide access information from Variety of applications.



## 

```mermaid
graph LR
  A[ODATA]
  A --> B[Format]
  A --> C[Protocol]
```

Format:- How data is described and how it is serialized.

Protocol:- How that Data is manipulated.



Origin of ODATA format





Final Test







