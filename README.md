



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHXSSX7P%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T002433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDuR7UQTLtCRPrstF3e8Y0eB18WA7hZHrWspT25dm%2FPaAiEA%2FsH%2BWrExjeH1ouQwJA3AtHtyU6SiiEG93Y%2FM8i%2FCzeUq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDDVpZpMIviFrxkcLwyrcAzzVv4XYqKZ6ep7zy0JLogcT2fWn55YYGWpg5GMR2%2BidM9rIpOaJ2kq43aeS4FyVUxFdb9PRxEB%2FaVHRztgL5DhNZkEywMfvEMqGtak1Lobvyu6cmGaOhrTIdtud2SW5qjJ2vgtL4C5cVp86F8Iyu3kgtOKx8rM6MdXbWJyQKuix5u5NJ%2FV8cGLnjSwv7xFZbcfI48Gbi8y12OrnPwQDPtAioqYYhI3DyLrJ4pSd4FKFv3qPH5r2g8uPGK5OmcsxX9mvqO3O5hxCZ%2BxBPTMGoxBf%2FenDvfLOCSYCXiuLdB0QcRDM3U1vWwBct12t0ZHORgnM4CFff7tSxfc2Ihdos21Q4pSNYyIiVg9uvvNdeGS3ZOB90uEEVmNp1uJ4BRX4Ef%2FLKSr%2FGt1FuC4MKHSLGpmtUGdZbHk8GsGP49PUC%2FjglKVTuPy%2BMKqoT%2Flto785imNHb%2B5W7hW%2FDDvjXOAEMaOpjcHFYALbVFBn0MQIUMaK20O%2FtDPhYgw3Ets%2BEJ3%2Fv4DEuu4%2F0ebCmPtwdURmIm5aOsuNmg2GVQ40L67mw3Mc4jEJujTfcHJrQQCtodMsY8rPkOWD%2FEpwCr4Fv8wcPBJjUpALLSP7k9UZYlQuUrslkI9TXH0R9PXsV0JtMI%2FA5tUGOqUBDWGJ%2B2Qv%2BWK2%2BgYjhzNQF4I03Nmq94HKA2bSa%2FrxTghRSJDw1YL%2F3KjvlBXQqzWVcgrZipo2hasi8rD4UPx7aGFTYL6pUQUpJ7Px6ynhS6wNjnG9A9uBOSZmeclDLxpHsJRovaY307xigWvda0H2LECL9A%2Bt8N78VFYOiANk5OYbJVuDYekW6ZxVw5j702nwp142eqb%2BiOXJA3Ly953W0NyZRfKs&X-Amz-Signature=9538a73800f44698395ffbab622e8e8a811ce1745503fb39255591da03336aed&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466QHXSSX7P%2F20260928%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260928T002433Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEF8aCXVzLXdlc3QtMiJHMEUCIDuR7UQTLtCRPrstF3e8Y0eB18WA7hZHrWspT25dm%2FPaAiEA%2FsH%2BWrExjeH1ouQwJA3AtHtyU6SiiEG93Y%2FM8i%2FCzeUq%2FwMIKBAAGgw2Mzc0MjMxODM4MDUiDDVpZpMIviFrxkcLwyrcAzzVv4XYqKZ6ep7zy0JLogcT2fWn55YYGWpg5GMR2%2BidM9rIpOaJ2kq43aeS4FyVUxFdb9PRxEB%2FaVHRztgL5DhNZkEywMfvEMqGtak1Lobvyu6cmGaOhrTIdtud2SW5qjJ2vgtL4C5cVp86F8Iyu3kgtOKx8rM6MdXbWJyQKuix5u5NJ%2FV8cGLnjSwv7xFZbcfI48Gbi8y12OrnPwQDPtAioqYYhI3DyLrJ4pSd4FKFv3qPH5r2g8uPGK5OmcsxX9mvqO3O5hxCZ%2BxBPTMGoxBf%2FenDvfLOCSYCXiuLdB0QcRDM3U1vWwBct12t0ZHORgnM4CFff7tSxfc2Ihdos21Q4pSNYyIiVg9uvvNdeGS3ZOB90uEEVmNp1uJ4BRX4Ef%2FLKSr%2FGt1FuC4MKHSLGpmtUGdZbHk8GsGP49PUC%2FjglKVTuPy%2BMKqoT%2Flto785imNHb%2B5W7hW%2FDDvjXOAEMaOpjcHFYALbVFBn0MQIUMaK20O%2FtDPhYgw3Ets%2BEJ3%2Fv4DEuu4%2F0ebCmPtwdURmIm5aOsuNmg2GVQ40L67mw3Mc4jEJujTfcHJrQQCtodMsY8rPkOWD%2FEpwCr4Fv8wcPBJjUpALLSP7k9UZYlQuUrslkI9TXH0R9PXsV0JtMI%2FA5tUGOqUBDWGJ%2B2Qv%2BWK2%2BgYjhzNQF4I03Nmq94HKA2bSa%2FrxTghRSJDw1YL%2F3KjvlBXQqzWVcgrZipo2hasi8rD4UPx7aGFTYL6pUQUpJ7Px6ynhS6wNjnG9A9uBOSZmeclDLxpHsJRovaY307xigWvda0H2LECL9A%2Bt8N78VFYOiANk5OYbJVuDYekW6ZxVw5j702nwp142eqb%2BiOXJA3Ly953W0NyZRfKs&X-Amz-Signature=9e386fb85478d06e9da50882fe92ef5d8ce4cefb09be5d6dedb99ff0d7228758&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







