



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637SVSGQQ%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T182026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVGJwAybJZBANFRqDey3KbCA16uZwV9pMN9Wg1kPMywAiB9UuM2aS7gtOgnTXZ%2Ftx2TFTQtQveoXbtPCLaS0caaMCqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSPux5Vy%2Bn%2FCajSLOKtwDJ3mDBtHe%2BqKSLq58NALQ0cD0dtDune7GXw%2BETtimwBGoyk%2FOcBzknfrsOBNF03oJEj2cd5v8kp4HR4DYTlc01TQ5uv3r0qm3T4ZZkyohjtpdF%2B6Ze8EEiDqyWFcEJyQPvlYysmICGhRCXEN3XulNZx0fCIrFcP3PqaaUYIYPDJM5RINAguc4I%2BDbR3WM7DEvQsi4fdwYfapZA%2Fj3rhF1nybrXkRUZerno7CHhOYr2ZDIkBM7f%2Fa8%2F165HtucmoE7dWXWyOz%2BHpubXUQvb%2FebKJozkxLgSOosoyJ5gneWwWWTeZFcPp1xXJ%2FYQeyQj%2FXaawBzrLaCvxF9vqyUcmp1Hol40Ou5kjde7g8e8BjL9iYmZlCVsfHc%2B%2Btxm7vFSxKukbqYZQt%2F4OexP9X33WsClbYZunZJ0d6ZkS4H16WHHFGE2z9BrkXMpU34YgjoT7X0t3oTlIelqPZVM6VTIvrQmivNG2fsRl7k1Am49pYZkwt6ntLLER4ip2s7cm2AK8U3faQVKkKsFXCXbFtDgTW14%2BOfrFRbjmxBL1oqy4VFH8n4DTZkbziT6P6ih4IjaV75natUxN59daLI2w8kzVPIci3pV4RMdweU9iAKIsAZJn1Ww5zhmFYWUz%2FVflYwyrSn1AY6pgH5A06%2F0T2NyeepqE%2FpS5w5Soq462GDJW6QYznvQUujGEDjyGUP2wqBLuxTi6Gyas5h3U4ptOMmAyHHdBqcSqt%2B61d0gbDIucwRm%2FCrw11YQ7XH78v6ihIRDqulDFofMKdkarOK%2BftK230iXpARyRO%2BZ9ycFHLTgHwk%2FdPfeSwwsAQ0MJTZMc46c3zllMacqV4pJIZLwhE8fd3E1R3MGa98vIq1FDYJ&X-Amz-Signature=8166e6eced0294f6bcf4e49eb1377473d40e1b6e2cb696fb7adf1f81218e8d9e&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB46637SVSGQQ%2F20260822%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260822T182026Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEPr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFVGJwAybJZBANFRqDey3KbCA16uZwV9pMN9Wg1kPMywAiB9UuM2aS7gtOgnTXZ%2Ftx2TFTQtQveoXbtPCLaS0caaMCqIBAjC%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSPux5Vy%2Bn%2FCajSLOKtwDJ3mDBtHe%2BqKSLq58NALQ0cD0dtDune7GXw%2BETtimwBGoyk%2FOcBzknfrsOBNF03oJEj2cd5v8kp4HR4DYTlc01TQ5uv3r0qm3T4ZZkyohjtpdF%2B6Ze8EEiDqyWFcEJyQPvlYysmICGhRCXEN3XulNZx0fCIrFcP3PqaaUYIYPDJM5RINAguc4I%2BDbR3WM7DEvQsi4fdwYfapZA%2Fj3rhF1nybrXkRUZerno7CHhOYr2ZDIkBM7f%2Fa8%2F165HtucmoE7dWXWyOz%2BHpubXUQvb%2FebKJozkxLgSOosoyJ5gneWwWWTeZFcPp1xXJ%2FYQeyQj%2FXaawBzrLaCvxF9vqyUcmp1Hol40Ou5kjde7g8e8BjL9iYmZlCVsfHc%2B%2Btxm7vFSxKukbqYZQt%2F4OexP9X33WsClbYZunZJ0d6ZkS4H16WHHFGE2z9BrkXMpU34YgjoT7X0t3oTlIelqPZVM6VTIvrQmivNG2fsRl7k1Am49pYZkwt6ntLLER4ip2s7cm2AK8U3faQVKkKsFXCXbFtDgTW14%2BOfrFRbjmxBL1oqy4VFH8n4DTZkbziT6P6ih4IjaV75natUxN59daLI2w8kzVPIci3pV4RMdweU9iAKIsAZJn1Ww5zhmFYWUz%2FVflYwyrSn1AY6pgH5A06%2F0T2NyeepqE%2FpS5w5Soq462GDJW6QYznvQUujGEDjyGUP2wqBLuxTi6Gyas5h3U4ptOMmAyHHdBqcSqt%2B61d0gbDIucwRm%2FCrw11YQ7XH78v6ihIRDqulDFofMKdkarOK%2BftK230iXpARyRO%2BZ9ycFHLTgHwk%2FdPfeSwwsAQ0MJTZMc46c3zllMacqV4pJIZLwhE8fd3E1R3MGa98vIq1FDYJ&X-Amz-Signature=9ec55efc92c2010bfe6af9a74c6481bedb874e003844d5894fbad984638c36a5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







