



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJEXOPGD%2F20251103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251103T182141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF4xpN5C3GA%2BJGfrmK4ndwVozbXI4PmHzB906cyKLTZVAiEAxJm3vbguIq9xn58Hgw1Tv8wFa3Du1f272hIXxmWhqa8q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDEqeztMicXR0eQlLmircA5MKKoEzzjG9YV%2Bo3hIYNnw2VARhNGTHc%2FVYmyhTthm3V7bC8tbwkEBL8KG8xjOPcDNvVr9urIslUNZVhFI7UpY6U%2BMC6pdR25a6s6WBhZ4ektPoce3jfnOfHIWezVOMAKgeE%2BcgWrneUkzKv5XUsM3lEx7kZPhBWwET1KMLJwcqPx70UUqWL9ouRrlfr8iv7T4jC0Shrzh1lIpCYTKoImWrZ20n9%2BMwD%2BHuvqDhPI%2FNaFGYuxplNUNSFHXeR52vQbirIZ3KtMyv4kKYc6svetNpch4rv929oYoTnTp1u9kvJ2IQbbVJBuxDZ7tcbeUiT5wfHbcsXf3uLpn0Yxd2J8Fp2R6lX7b1FKlhYLe42%2FCkr5AAQoseDKrhNQ2S4zZcWZ9l26cF20gU%2FFQaWNhTzdKLGkccF0a4K9ewvfsOexhymWNa5%2Br%2Be97HjG1Pq0M0XNRcHx%2FMRq9o12E1XOOU9W5jco7Ry4nDcEqkPmBhEg7lyqekKmfRIkIUPEnkPCFqEPpNYH4l0PnBvy%2B8bwvz7DIkNALb%2FsqHMIgZQQJzpsS9RT5OSz9W3ooKXFZDc8P8hj6%2FV0H3KWzH8asaTxoNBYAkuSQr9AgHGok2mHiqG5rI2DwNrTZhpGiz8eOzMLjIo8gGOqUBumugXdbQt4rGIls%2F00nC9i1XPYFFcq6VBahjFJac46vQH44QgC0zy7dtVAvX90egCzTmG2y4zeHMjl7%2FGQzihYp0%2F4yNcEvFMf1BMaSYyZ5vksTL8Ix%2FbPcomuvrLlsMSghHzMuz7mSmPIKWJbo1zMjy6llyGA%2FUMwEFlgbo4cuXEvMe%2B%2FRegpQkI7ELqCdTAMgnOb137Ey1DQPt0zhkjJ1YAe%2Br&X-Amz-Signature=966f694d2c453e0cc360a1c060064983809441f6f454ef0efec1deb79d8e5eb6&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466YJEXOPGD%2F20251103%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251103T182141Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIF4xpN5C3GA%2BJGfrmK4ndwVozbXI4PmHzB906cyKLTZVAiEAxJm3vbguIq9xn58Hgw1Tv8wFa3Du1f272hIXxmWhqa8q%2FwMIYhAAGgw2Mzc0MjMxODM4MDUiDEqeztMicXR0eQlLmircA5MKKoEzzjG9YV%2Bo3hIYNnw2VARhNGTHc%2FVYmyhTthm3V7bC8tbwkEBL8KG8xjOPcDNvVr9urIslUNZVhFI7UpY6U%2BMC6pdR25a6s6WBhZ4ektPoce3jfnOfHIWezVOMAKgeE%2BcgWrneUkzKv5XUsM3lEx7kZPhBWwET1KMLJwcqPx70UUqWL9ouRrlfr8iv7T4jC0Shrzh1lIpCYTKoImWrZ20n9%2BMwD%2BHuvqDhPI%2FNaFGYuxplNUNSFHXeR52vQbirIZ3KtMyv4kKYc6svetNpch4rv929oYoTnTp1u9kvJ2IQbbVJBuxDZ7tcbeUiT5wfHbcsXf3uLpn0Yxd2J8Fp2R6lX7b1FKlhYLe42%2FCkr5AAQoseDKrhNQ2S4zZcWZ9l26cF20gU%2FFQaWNhTzdKLGkccF0a4K9ewvfsOexhymWNa5%2Br%2Be97HjG1Pq0M0XNRcHx%2FMRq9o12E1XOOU9W5jco7Ry4nDcEqkPmBhEg7lyqekKmfRIkIUPEnkPCFqEPpNYH4l0PnBvy%2B8bwvz7DIkNALb%2FsqHMIgZQQJzpsS9RT5OSz9W3ooKXFZDc8P8hj6%2FV0H3KWzH8asaTxoNBYAkuSQr9AgHGok2mHiqG5rI2DwNrTZhpGiz8eOzMLjIo8gGOqUBumugXdbQt4rGIls%2F00nC9i1XPYFFcq6VBahjFJac46vQH44QgC0zy7dtVAvX90egCzTmG2y4zeHMjl7%2FGQzihYp0%2F4yNcEvFMf1BMaSYyZ5vksTL8Ix%2FbPcomuvrLlsMSghHzMuz7mSmPIKWJbo1zMjy6llyGA%2FUMwEFlgbo4cuXEvMe%2B%2FRegpQkI7ELqCdTAMgnOb137Ey1DQPt0zhkjJ1YAe%2Br&X-Amz-Signature=a1da30c56cfe924cb3ba897296f60a89fbf52e41d348281e4af9ecb853f2009d&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







