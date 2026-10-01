



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNQAVBXA%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T181100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDklzc8hpaoTH%2Bignki%2FukpM1X3813x9JGVc1C3OFmg6AiEAr2EsimzSSE3eykH6KyDS96W9Y9Z2a0ODgRHiU3MXNucqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAhOwDsKtAqwT9BDNSrcA89KNnr4puAAdOUSDiMky7U04IcQc4BnBGJZwqIBH19R1m3Sjy7o%2FjVvSjzK5FG0hy7bWmf504PD4zWdY9aHSvPp5xnsR8b%2BvTzp2kDh8ar%2Be3keniwv7MNC%2F4FpXzwGa2evQMJrEYzh1P9lg4F90JGD5BQX0au2El8A7ab6MV3Cz8l0kWiUjHPu5aHPmKePXHf%2FqsG2R7qUcS4HTswPKh8uBc4mqMaZpcBXv2EeOPtSb3HSvSo0ArKc8rc5MMiXTp6H0BV4iXG1lDS3JdJLr9DWFsKpcn43QI3gR3GKSY61skvQr%2BpbcDZQD3vFPKfFaqwu4QT1WqV1%2FVpINlZkWowGopvcms4bj53j%2BI5hdLGEj%2FzDVPZ8WQJb3v69m8d3dHbbdSlIXR1mcP8GNWw%2BsoiPxKKRPpO0M%2BvqeaigaBy0WpWcFiNAZdOJem6eUA3kLhvjc9nAEAZKCUczG2qBiElz7tLMteAKW7%2BWkED%2BFpg%2BTpbLvt3BHXyyM00mnlZFKdQ4uw6YZniiN250D9fZAbQMYJX4CufUYGw3MsLUON4HVxErkAbHKe7vBmkjleyg%2Bqin2vuPFU6l%2FRrKBrL3UOQxxb5tXo5r4AMWrKLtas0l73FEZo%2BU2IbFfWM%2FMNnA%2BtUGOqUB%2BnqicyiPOWkYTuupqpi4tt30YhNJkJHpwPvrnM4euy31LMU7ckYm%2ByxPiUKEqKJroKhJ%2F8qGvrP6WofJjSQ2suE3JxwUf1%2BDYKg%2BUkSQUOtie%2F4LtA4zxPGVGzJFeaiPgOnGZQx%2BQKQHEfE1ylZgQL16Jk2Zc3ry95gz1e0H8Pcytlw169bJJGSckhEl81irBKTLZ1J5jOkst7ehnRtnyTyhPHJU&X-Amz-Signature=f32814329e39938464c653bee251b76b440055318a41eeabdd446c43132a63ab&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TNQAVBXA%2F20261001%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261001T181100Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjELr%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCIDklzc8hpaoTH%2Bignki%2FukpM1X3813x9JGVc1C3OFmg6AiEAr2EsimzSSE3eykH6KyDS96W9Y9Z2a0ODgRHiU3MXNucqiAQIgv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDAhOwDsKtAqwT9BDNSrcA89KNnr4puAAdOUSDiMky7U04IcQc4BnBGJZwqIBH19R1m3Sjy7o%2FjVvSjzK5FG0hy7bWmf504PD4zWdY9aHSvPp5xnsR8b%2BvTzp2kDh8ar%2Be3keniwv7MNC%2F4FpXzwGa2evQMJrEYzh1P9lg4F90JGD5BQX0au2El8A7ab6MV3Cz8l0kWiUjHPu5aHPmKePXHf%2FqsG2R7qUcS4HTswPKh8uBc4mqMaZpcBXv2EeOPtSb3HSvSo0ArKc8rc5MMiXTp6H0BV4iXG1lDS3JdJLr9DWFsKpcn43QI3gR3GKSY61skvQr%2BpbcDZQD3vFPKfFaqwu4QT1WqV1%2FVpINlZkWowGopvcms4bj53j%2BI5hdLGEj%2FzDVPZ8WQJb3v69m8d3dHbbdSlIXR1mcP8GNWw%2BsoiPxKKRPpO0M%2BvqeaigaBy0WpWcFiNAZdOJem6eUA3kLhvjc9nAEAZKCUczG2qBiElz7tLMteAKW7%2BWkED%2BFpg%2BTpbLvt3BHXyyM00mnlZFKdQ4uw6YZniiN250D9fZAbQMYJX4CufUYGw3MsLUON4HVxErkAbHKe7vBmkjleyg%2Bqin2vuPFU6l%2FRrKBrL3UOQxxb5tXo5r4AMWrKLtas0l73FEZo%2BU2IbFfWM%2FMNnA%2BtUGOqUB%2BnqicyiPOWkYTuupqpi4tt30YhNJkJHpwPvrnM4euy31LMU7ckYm%2ByxPiUKEqKJroKhJ%2F8qGvrP6WofJjSQ2suE3JxwUf1%2BDYKg%2BUkSQUOtie%2F4LtA4zxPGVGzJFeaiPgOnGZQx%2BQKQHEfE1ylZgQL16Jk2Zc3ry95gz1e0H8Pcytlw169bJJGSckhEl81irBKTLZ1J5jOkst7ehnRtnyTyhPHJU&X-Amz-Signature=4d1695e896b115a70beb39ee711b9cf48034d33effe31e159c99fc7e5c78f483&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







