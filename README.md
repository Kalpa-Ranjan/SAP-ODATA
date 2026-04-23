



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GCNSVVR%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T190109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbDXgi6ki73GMxZDyc3%2FBoO90GnHr5q3yi2odPrufVjwIhAJlDa%2F6UOuPkWsgOhDGJcXBFEXZZdcyt47ws8y8j9ZkSKv8DCGsQABoMNjM3NDIzMTgzODA1IgyNikg7Klkzfe%2F8Atoq3APDSQV0zWaEw6i53CofBOvbKyg7mRL08ZlfO0ZE4mdYtmpYxbL5e3k0KWa62PwlxKoXHMgtgMuYJ69%2FuKJq9eS8OXvdbZoHeXmp5TT26VinG6%2FFuowNumIyz6RlbqAHKG7APQ5Lmhb%2B1sqLraR%2BvcwSf46rM5Pk4q5Zi1EHX1IW0srwyPe%2BTn5bVHwdFb%2FUcnFWOhXPcv%2FkXH%2FS7C2oMeKCpZyJepoQYXFZvf7GpANTYIhf3ImNWKAtzEBqOhJRVlLfPewQE3YDTyuS7NzV6AEco3ooGgreWkJzQBJ2ljL5UeIG6MIXUMcOXv7NBWHd7Lt8KR7rKWWkHXvoXp2NFukkpxMrRX25YAsqaJRv4UGJocFPEqkdEPdXFcpwSuBE9bk%2F5KBizxDDnbevNSnF6fbXLEFxm3uEQ2uLqLnusE5H7nwAXHAolKxbgaswaK88VRw66YN2H5epGQ297XSSJ5qcGvOfFwl1Vk3U5%2BIjlpYmJRpejDJtz%2FMVAx0ALdB3OEs%2FryUvixyDC8s7iVMys4nB9vhJnYsgM14cPu0VVfTnoBwwzfNtPPCn83whoXRzowwgytd%2Ftk1%2BlZXjdTXMvDPN2RlYHOxmklHxpbguOWmvcjwGZHmwBRUNNZSIuzCiuanPBjqkAW7LYtewI05fLjYtgTc%2BkIL4q4xT04RHWZm8sEzb%2BqpdxwCIFoFx%2FgIEgbv0arcNmMwFpFqBph0sg%2BPEN0bkMUg2W30Wc%2FFruhqt0908yyDwwR4%2FB4ZWpuRlvfHRA4jqDaTNY7AkL%2BSXQXhZjsFsczaPUACBk4PM%2B5EvkaBa7JfWvzPL9%2BdEWfPneAW456uHjhHqVvl1GEUQSgBqqtCxHetYzLg2&X-Amz-Signature=c68d41ea8bfdb90a260d955381499ad6d792bf15c28483903960086512eb0505&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB4667GCNSVVR%2F20260423%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260423T190109Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEKL%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDbDXgi6ki73GMxZDyc3%2FBoO90GnHr5q3yi2odPrufVjwIhAJlDa%2F6UOuPkWsgOhDGJcXBFEXZZdcyt47ws8y8j9ZkSKv8DCGsQABoMNjM3NDIzMTgzODA1IgyNikg7Klkzfe%2F8Atoq3APDSQV0zWaEw6i53CofBOvbKyg7mRL08ZlfO0ZE4mdYtmpYxbL5e3k0KWa62PwlxKoXHMgtgMuYJ69%2FuKJq9eS8OXvdbZoHeXmp5TT26VinG6%2FFuowNumIyz6RlbqAHKG7APQ5Lmhb%2B1sqLraR%2BvcwSf46rM5Pk4q5Zi1EHX1IW0srwyPe%2BTn5bVHwdFb%2FUcnFWOhXPcv%2FkXH%2FS7C2oMeKCpZyJepoQYXFZvf7GpANTYIhf3ImNWKAtzEBqOhJRVlLfPewQE3YDTyuS7NzV6AEco3ooGgreWkJzQBJ2ljL5UeIG6MIXUMcOXv7NBWHd7Lt8KR7rKWWkHXvoXp2NFukkpxMrRX25YAsqaJRv4UGJocFPEqkdEPdXFcpwSuBE9bk%2F5KBizxDDnbevNSnF6fbXLEFxm3uEQ2uLqLnusE5H7nwAXHAolKxbgaswaK88VRw66YN2H5epGQ297XSSJ5qcGvOfFwl1Vk3U5%2BIjlpYmJRpejDJtz%2FMVAx0ALdB3OEs%2FryUvixyDC8s7iVMys4nB9vhJnYsgM14cPu0VVfTnoBwwzfNtPPCn83whoXRzowwgytd%2Ftk1%2BlZXjdTXMvDPN2RlYHOxmklHxpbguOWmvcjwGZHmwBRUNNZSIuzCiuanPBjqkAW7LYtewI05fLjYtgTc%2BkIL4q4xT04RHWZm8sEzb%2BqpdxwCIFoFx%2FgIEgbv0arcNmMwFpFqBph0sg%2BPEN0bkMUg2W30Wc%2FFruhqt0908yyDwwR4%2FB4ZWpuRlvfHRA4jqDaTNY7AkL%2BSXQXhZjsFsczaPUACBk4PM%2B5EvkaBa7JfWvzPL9%2BdEWfPneAW456uHjhHqVvl1GEUQSgBqqtCxHetYzLg2&X-Amz-Signature=4b21337ced62eef78c0cd7f02892478b40731bb958ad07dd00c2a8d001a624ea&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







