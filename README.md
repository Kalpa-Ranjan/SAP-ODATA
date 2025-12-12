



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAQTCYXZ%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T011643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFyBC1R7QXlHPMsLy7TAmRW51TxgroNytbCZxSjqzDaTAiBAAtBMKAEH4y%2FrrNz%2Bamxy0%2FfCyndqnp83iqw3qfUzMiqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSRqM49avALertDFMKtwDW1fhPZ9%2FbdqftV3cMhmKVpYQvdkhcO%2BRTbrL8CGwjInw%2B2hMygZdh9kTtewlbczISux26%2Fd4FGJQfbiut05XMTN%2FoltFGOB4POVMHax2N759ZgOJDSeorlgt1ak4H3G1jHyyj85eB7Kz9ndZrKAEDSHMaQFm2FyWt6sMSwkJdn8mig%2B507GYYzysMWKqq7GHd1D%2B7Skt5J%2FrtZH2oDf%2BzAzDYzuUCIsd8PK%2BcBdXEfxIVKcoBl7%2FFQWYsUWgIHv5yehsj5Q21s4N2%2BS%2FUdnE%2BAgdfd3Lo1agE2gwJZPluAKT1vFYIWfmY2VbGgl6eFZ%2Bq4E92YUnRW7kWEUcWQIVq6mcK9Wkhktq9q6w5TaNLW7kg4xGrLw5FWIAwAFo7xoVW6svp3IX9SHv5L4EwsKkRh2vAFbllk1LeZqXCMVZ8gIy9BnPq174GtpWTn%2F5AZLfZnTtWjgy8xbLF400TMuTlluqntf5V0olVgFlF6Rz128HU7ZgFzmiiRO3BSjLkuS%2B0cB99chvNPntWAYwyRHx2fOghTTpAkcyzJdOfYKD%2FmHl%2BIvSxuG4CF4zF%2F5dMjkErNr04lilkP9hCeiCn3IwgRsN5Alf5SuZWptkulDwFPj3pEpTEEpvEoNPRjcwjtXtyQY6pgGMmzhHf56fdKg7vt3LRnAY3esppT0F6jykBfBQYsbFOwv002WhfEz6sjRgkfdqz8UhKBitnjvhaJQrSC%2B00uZMAfNS23UzGl7dpt3NR4CYJBfm2oHognnT9h5IWrLkbSNWdtmq6hcknsoeya7s%2Bf2lshtW0olmbxx97oc6tMyyjNpPWF872SE71u4wgrZ4zceBo%2B1szxoBcVrhPrpE2G9ozSrptWcl&X-Amz-Signature=2f3a70cb228520285b330eb05c783cd569d02e7205415dd1626dff231bfafe94&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XAQTCYXZ%2F20251212%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20251212T011643Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEDEaCXVzLXdlc3QtMiJGMEQCIFyBC1R7QXlHPMsLy7TAmRW51TxgroNytbCZxSjqzDaTAiBAAtBMKAEH4y%2FrrNz%2Bamxy0%2FfCyndqnp83iqw3qfUzMiqIBAj6%2F%2F%2F%2F%2F%2F%2F%2F%2F%2F8BEAAaDDYzNzQyMzE4MzgwNSIMSRqM49avALertDFMKtwDW1fhPZ9%2FbdqftV3cMhmKVpYQvdkhcO%2BRTbrL8CGwjInw%2B2hMygZdh9kTtewlbczISux26%2Fd4FGJQfbiut05XMTN%2FoltFGOB4POVMHax2N759ZgOJDSeorlgt1ak4H3G1jHyyj85eB7Kz9ndZrKAEDSHMaQFm2FyWt6sMSwkJdn8mig%2B507GYYzysMWKqq7GHd1D%2B7Skt5J%2FrtZH2oDf%2BzAzDYzuUCIsd8PK%2BcBdXEfxIVKcoBl7%2FFQWYsUWgIHv5yehsj5Q21s4N2%2BS%2FUdnE%2BAgdfd3Lo1agE2gwJZPluAKT1vFYIWfmY2VbGgl6eFZ%2Bq4E92YUnRW7kWEUcWQIVq6mcK9Wkhktq9q6w5TaNLW7kg4xGrLw5FWIAwAFo7xoVW6svp3IX9SHv5L4EwsKkRh2vAFbllk1LeZqXCMVZ8gIy9BnPq174GtpWTn%2F5AZLfZnTtWjgy8xbLF400TMuTlluqntf5V0olVgFlF6Rz128HU7ZgFzmiiRO3BSjLkuS%2B0cB99chvNPntWAYwyRHx2fOghTTpAkcyzJdOfYKD%2FmHl%2BIvSxuG4CF4zF%2F5dMjkErNr04lilkP9hCeiCn3IwgRsN5Alf5SuZWptkulDwFPj3pEpTEEpvEoNPRjcwjtXtyQY6pgGMmzhHf56fdKg7vt3LRnAY3esppT0F6jykBfBQYsbFOwv002WhfEz6sjRgkfdqz8UhKBitnjvhaJQrSC%2B00uZMAfNS23UzGl7dpt3NR4CYJBfm2oHognnT9h5IWrLkbSNWdtmq6hcknsoeya7s%2Bf2lshtW0olmbxx97oc6tMyyjNpPWF872SE71u4wgrZ4zceBo%2B1szxoBcVrhPrpE2G9ozSrptWcl&X-Amz-Signature=f3a77c33e7a62e9467259e7baf24f9d68f59cc044761077dcaad1e22c27156fc&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







