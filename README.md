



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYCNTD4O%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T123400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIDJjutrmoX8%2BtyfiFLt46srXKOmX1FDORTT8xZObVS%2BYAiBo7O8DJoBOapxo78kz6D6Xs7%2FgSx%2FQ9USBVxe20Eew7iqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmAicRdO7WzAJXQCPKtwDLUHRoKSFyPnuqt2JXZzujht8KDwHNR%2BEupajsrbbCEiPNm8HeQF%2FgYiJU6caePzhRzgk6P2baZ3%2FgcrPbr%2BfgeIdGkm4kGEMjVeJXWTj831aUQ%2BtSGkB%2Fp5Z5eSzxbVvEDpax2UoI0BFbUlYKINEMbUum2of1CotQzi2dOM1FO2Fqly4L12%2FBLNQWWTaQWqaGCX0TxNwNOBfAqOfqtt5s%2FC7HwUCw4mJ0lon8BwQttxdNO1pqu%2FslL7GKtOyv%2FoabRup15fg4ZOlk6UBgNWzRfsHpnVOaHIBzKALQSSBRcQqttSHKEna2u6MaL4TYjmL9nVdg3ElCMZ8xFnpCsqyX0VafHKdYTR2weBPXx2QIRhVsNvQcwMZ7SKCnouVlhxGj5I93Gn0TQLy2KfIbryObTpJ0nX2pv1krkFKYq%2B9QL24dcq0hDrpVhc904mEP7aZ4VFIYMbEF6vPaWxSBiuleFoCM0yHOzwPGWbAI%2BVhuPXW2SJDg%2BlSMzq1hqC221PvuHP37PBFp0Es0rTox4L92aW1ROnx%2FNzuvf4ef4GW2NdMj6foijN2%2Bi8%2BmGD5bbBjOkO0Pkgf3hqfmW1beqPueXFXxGV87eVg3O8TeksKg2dInYVPITpf7w%2Bs4Asw%2Fu6kygY6pgHiFzpKmaL%2BImBuR2MAuTvTEld4M8A5nEDv5i2Q70DRUaiQYILWXqkHwPILbxtNl%2Bih0O20O%2FqW3mMXWI4AZOXjVLV6usHOFb4SWQGPRo2rakeuoEhVEbYLwc6cvexYqb5qa9Zp8JHMK4GDIR9lgW%2FmgCOtATjZQzmuY%2BLAN%2F7mpqX%2BMQOgq3qnPRI5hoBioOSFw%2BRy%2B2adxG8FqL7CNS%2BOFY16ATCo&X-Amz-Signature=a737d2d3f570307f3ad7ef260b17a14d5606f292b6aa57a53941e692bab284af&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466ZYCNTD4O%2F20251222%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251222T123400Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEC0aCXVzLXdlc3QtMiJGMEQCIDJjutrmoX8%2BtyfiFLt46srXKOmX1FDORTT8xZObVS%2BYAiBo7O8DJoBOapxo78kz6D6Xs7%2FgSx%2FQ9USBVxe20Eew7iqIBAj1%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMmAicRdO7WzAJXQCPKtwDLUHRoKSFyPnuqt2JXZzujht8KDwHNR%2BEupajsrbbCEiPNm8HeQF%2FgYiJU6caePzhRzgk6P2baZ3%2FgcrPbr%2BfgeIdGkm4kGEMjVeJXWTj831aUQ%2BtSGkB%2Fp5Z5eSzxbVvEDpax2UoI0BFbUlYKINEMbUum2of1CotQzi2dOM1FO2Fqly4L12%2FBLNQWWTaQWqaGCX0TxNwNOBfAqOfqtt5s%2FC7HwUCw4mJ0lon8BwQttxdNO1pqu%2FslL7GKtOyv%2FoabRup15fg4ZOlk6UBgNWzRfsHpnVOaHIBzKALQSSBRcQqttSHKEna2u6MaL4TYjmL9nVdg3ElCMZ8xFnpCsqyX0VafHKdYTR2weBPXx2QIRhVsNvQcwMZ7SKCnouVlhxGj5I93Gn0TQLy2KfIbryObTpJ0nX2pv1krkFKYq%2B9QL24dcq0hDrpVhc904mEP7aZ4VFIYMbEF6vPaWxSBiuleFoCM0yHOzwPGWbAI%2BVhuPXW2SJDg%2BlSMzq1hqC221PvuHP37PBFp0Es0rTox4L92aW1ROnx%2FNzuvf4ef4GW2NdMj6foijN2%2Bi8%2BmGD5bbBjOkO0Pkgf3hqfmW1beqPueXFXxGV87eVg3O8TeksKg2dInYVPITpf7w%2Bs4Asw%2Fu6kygY6pgHiFzpKmaL%2BImBuR2MAuTvTEld4M8A5nEDv5i2Q70DRUaiQYILWXqkHwPILbxtNl%2Bih0O20O%2FqW3mMXWI4AZOXjVLV6usHOFb4SWQGPRo2rakeuoEhVEbYLwc6cvexYqb5qa9Zp8JHMK4GDIR9lgW%2FmgCOtATjZQzmuY%2BLAN%2F7mpqX%2BMQOgq3qnPRI5hoBioOSFw%2BRy%2B2adxG8FqL7CNS%2BOFY16ATCo&X-Amz-Signature=627dee30dda652077f081ea1aca872a8f5020d92e79824ae3f97bbbcbad1377b&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







