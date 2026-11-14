



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3BBS7ZH%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T060708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrpoWaAJz%2B2O%2BduZu9L%2FoRP4ne%2BknyoIPcuTpKbOSQhAiA5SZJNeTny3dJfRMXdtZRIwuLwfCK%2F%2Fs2lgJslLNmUKSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUKMb6xq3kV7py2pzKtwDUGY0oIidvfDW0wfCBAuMKp9Sx9aE5H7GBIwkchwWeKrFFbDBmIv53ttpg5%2FVseKkxjsvDi2PUHXxjerbUebp41EUbd5%2B4hmbk7l39b8AEO9663QJjYAinfga9VlZhS%2BWmP3tPHiNRylisUpF64Q6dvRUxcrOMu2e53LZozFSAC77jE9vRn4hueDuYs%2Bvwk35pf11FJkP0UQG%2BoilArtBb0eYPlehCgJen1%2BqY7FOU3GGTgbdv0%2Bry%2BnyP7FpoWnmCF6aWrU34mGz%2FoiGBaO1yh9WjY7O2Enr5DtfHuILTm%2FOzp7YzQN4EfaDQMPYgyyRKlk6HslQTzr9I2lISM6NDPdGGpABrADNiPnTnQKoNg1vz2LC96IjPp7TN9a5KjgIl6hs7m0m4a0kmQRd9SxrzKFFmHzsBsOOw2Wrfbos%2B46L9jv2ccDMXsUVSirfbcbciPty%2B9%2B7%2BlumFiHkulp28lDvq9cZUBwGdklxtMT73ZqGufd8kSN3G%2B%2FjuvAfYkqrGjCUGIQirE3NSqOjCTI%2FclWsCdIXyk%2BlDA63fM%2BmPRoR6Z%2B4l5n%2B0X8TeIdQUXptDHzZzzH2%2Fm29JNYhaFPOvRS0HAZDN2E5w9vaap0BDfeigY0yUEVtXrnTdtEwz%2Fbe1wY6pgEOLju%2BOLwL%2Bod42Nx5w4wykCGGUWvJBLvM1Ipi1rwoqQ4eUuz5NClvMILOO6zddwIKqwspl%2BPPb%2BerPCuxjz0mOHL0oMFD6AWUTY%2B9ccxKQ7gpGXe5yRwvTL5%2Bv9bTruvfZKngn7yawKb2eWJ0RYGvZf2XH4fzcEdEMBZU1W8HBL1SIdqxCcOIaigaD8vuIHaFJWPG3R3YoMvE%2FmVk8aTMNwO7LdOW&X-Amz-Signature=3d2357f924f844eac3031a4dd6981c0775f86f2ca1b96e68639f4b82009f9cdc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466R3BBS7ZH%2F20261114%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261114T060708Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEMr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJGMEQCIFrpoWaAJz%2B2O%2BduZu9L%2FoRP4ne%2BknyoIPcuTpKbOSQhAiA5SZJNeTny3dJfRMXdtZRIwuLwfCK%2F%2Fs2lgJslLNmUKSqIBAiS%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMUKMb6xq3kV7py2pzKtwDUGY0oIidvfDW0wfCBAuMKp9Sx9aE5H7GBIwkchwWeKrFFbDBmIv53ttpg5%2FVseKkxjsvDi2PUHXxjerbUebp41EUbd5%2B4hmbk7l39b8AEO9663QJjYAinfga9VlZhS%2BWmP3tPHiNRylisUpF64Q6dvRUxcrOMu2e53LZozFSAC77jE9vRn4hueDuYs%2Bvwk35pf11FJkP0UQG%2BoilArtBb0eYPlehCgJen1%2BqY7FOU3GGTgbdv0%2Bry%2BnyP7FpoWnmCF6aWrU34mGz%2FoiGBaO1yh9WjY7O2Enr5DtfHuILTm%2FOzp7YzQN4EfaDQMPYgyyRKlk6HslQTzr9I2lISM6NDPdGGpABrADNiPnTnQKoNg1vz2LC96IjPp7TN9a5KjgIl6hs7m0m4a0kmQRd9SxrzKFFmHzsBsOOw2Wrfbos%2B46L9jv2ccDMXsUVSirfbcbciPty%2B9%2B7%2BlumFiHkulp28lDvq9cZUBwGdklxtMT73ZqGufd8kSN3G%2B%2FjuvAfYkqrGjCUGIQirE3NSqOjCTI%2FclWsCdIXyk%2BlDA63fM%2BmPRoR6Z%2B4l5n%2B0X8TeIdQUXptDHzZzzH2%2Fm29JNYhaFPOvRS0HAZDN2E5w9vaap0BDfeigY0yUEVtXrnTdtEwz%2Fbe1wY6pgEOLju%2BOLwL%2Bod42Nx5w4wykCGGUWvJBLvM1Ipi1rwoqQ4eUuz5NClvMILOO6zddwIKqwspl%2BPPb%2BerPCuxjz0mOHL0oMFD6AWUTY%2B9ccxKQ7gpGXe5yRwvTL5%2Bv9bTruvfZKngn7yawKb2eWJ0RYGvZf2XH4fzcEdEMBZU1W8HBL1SIdqxCcOIaigaD8vuIHaFJWPG3R3YoMvE%2FmVk8aTMNwO7LdOW&X-Amz-Signature=b37b2b1bb84ec252f86a9ad136f9b6e920d37aebf478baf60da759ffa17acb0b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







