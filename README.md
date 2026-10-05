



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUWG6WWK%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T002428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIG0TvKsC0wnA9BzwjatHSgmv8QcoKmGvbHOkSkHJlZN1AiEAnXoIr9Z8xOFsnAQillN9hS8kS52G%2F%2FyyseVD1Pq9RE4qiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVrjTQo8dHIrSGvPyrcA%2B7%2F%2BwPIAahNjZPcCOF2sE9m2PQavf4J8puxW2BIfF1jNstJ6%2Fkef8Vgiq6drnDRUXIHKs4Hzs1gcOf25JVgRTISdi%2BEI6tGUSOG9A9AjRnME9Mj%2F7nLc4N5LBQO4BPI4LqOBZIohsqbDuvNXbykNTra0YFhvetjbvVogxiIFJGpGKTx08KsJPe9biII68pf5zcbwrsWIEmZp7x3qMdRH49Q%2BwnoOCwdzfH5I%2FJQmBuq2%2FR%2BUvSCd%2BG%2F0x1IIgw0p1v1A0uDVt84EZnP%2BHCWDd0Oc0x%2BqLvPenRGAAr39Wq7wPgswlRAUUiARTJJzTMJRcZBmn5Nmg5jPkrbhkXBgU1NcWy1nTEv1AWmBEzulW%2FD%2FAiuUYFWW4UwaplxhkbjAlJL%2FQCDQgcwg6bHez9gzU6qoKRWdDayjzpiYvkXUT0kbGCSmdEbBXhnr3aNXnDgIlfaCvLPaJo2a%2B%2FCoL4fWSUY2NkXMHQm6b4TEbdtPCRlu9WmrlpTfNId3wfuR4nIRKeKhLRPKj0if5mjmHoRwr43x4pp%2F0%2FNEEEy4ud%2FGtLmW5eCa3%2BYH1uhXlfx6LM9%2Bgv%2BTZYItm3vi9zbYTbbD1Lhx2CU9xrwUWYqwO5UBSdtCxXieDQXUz98T8pcMI%2Bci9YGOqUBmDetCWlb5d68u79J7KuCycVDdVId10RgAAYA6MZHzQI8yyDM1bL4w3PZXU7M7dTqRLKCuIaxEXKUWP0VKp%2Fc2fSWh7sEYPRM1n7WAQOIyb5nh9icPDTvpIJcRUOiSP%2Fmf%2Ft5m2UKDUfNwY9NWRfkM%2BPQVS796jVnAQkYNm1QNoYaM%2Fgp%2BMyHdYIxNxgiuIo3vNi%2B1n9wBpX0ThlXtI6gHrwpkLYj&X-Amz-Signature=28ede038257f10708def3e22f6313c04e48a1c62ea062acdfa88d041617d3324&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466WUWG6WWK%2F20261005%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20261005T002428Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEAYaCXVzLXdlc3QtMiJHMEUCIG0TvKsC0wnA9BzwjatHSgmv8QcoKmGvbHOkSkHJlZN1AiEAnXoIr9Z8xOFsnAQillN9hS8kS52G%2F%2FyyseVD1Pq9RE4qiAQIzv%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FARAAGgw2Mzc0MjMxODM4MDUiDGVrjTQo8dHIrSGvPyrcA%2B7%2F%2BwPIAahNjZPcCOF2sE9m2PQavf4J8puxW2BIfF1jNstJ6%2Fkef8Vgiq6drnDRUXIHKs4Hzs1gcOf25JVgRTISdi%2BEI6tGUSOG9A9AjRnME9Mj%2F7nLc4N5LBQO4BPI4LqOBZIohsqbDuvNXbykNTra0YFhvetjbvVogxiIFJGpGKTx08KsJPe9biII68pf5zcbwrsWIEmZp7x3qMdRH49Q%2BwnoOCwdzfH5I%2FJQmBuq2%2FR%2BUvSCd%2BG%2F0x1IIgw0p1v1A0uDVt84EZnP%2BHCWDd0Oc0x%2BqLvPenRGAAr39Wq7wPgswlRAUUiARTJJzTMJRcZBmn5Nmg5jPkrbhkXBgU1NcWy1nTEv1AWmBEzulW%2FD%2FAiuUYFWW4UwaplxhkbjAlJL%2FQCDQgcwg6bHez9gzU6qoKRWdDayjzpiYvkXUT0kbGCSmdEbBXhnr3aNXnDgIlfaCvLPaJo2a%2B%2FCoL4fWSUY2NkXMHQm6b4TEbdtPCRlu9WmrlpTfNId3wfuR4nIRKeKhLRPKj0if5mjmHoRwr43x4pp%2F0%2FNEEEy4ud%2FGtLmW5eCa3%2BYH1uhXlfx6LM9%2Bgv%2BTZYItm3vi9zbYTbbD1Lhx2CU9xrwUWYqwO5UBSdtCxXieDQXUz98T8pcMI%2Bci9YGOqUBmDetCWlb5d68u79J7KuCycVDdVId10RgAAYA6MZHzQI8yyDM1bL4w3PZXU7M7dTqRLKCuIaxEXKUWP0VKp%2Fc2fSWh7sEYPRM1n7WAQOIyb5nh9icPDTvpIJcRUOiSP%2Fmf%2Ft5m2UKDUfNwY9NWRfkM%2BPQVS796jVnAQkYNm1QNoYaM%2Fgp%2BMyHdYIxNxgiuIo3vNi%2B1n9wBpX0ThlXtI6gHrwpkLYj&X-Amz-Signature=01547cbe966b7650cde968dd3175733f711b942abb8c4aa35226a03e368b334c&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







