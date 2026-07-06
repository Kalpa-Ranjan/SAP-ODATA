



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGHW2CSN%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T194850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJzww%2FgpN6kgkJzBeCgbc%2FaC0Pm5b2CwdLHw1DkSUnGgIhAOMrQsdII%2B3xG3cGbDoLhh17lYCy91Tf4Ft0zVZWbiv7Kv8DCFwQABoMNjM3NDIzMTgzODA1IgzejmJCVVkqlR9zjuwq3AOonMB6h3m4TxU8BFV%2BXsCQIKTQQRmCjC%2FuhISqHZ8NP9T3JOJTfHutixjaPOD%2FLR3ENxztJDa04TIqA4JvEvzKIxg2VeyQCS%2Fc9UFGJZUdcSoyQ4uTv82FbC5XErBIOa3loewf%2BhNYR1C3vJuj84xyKf1AG1l0SDc5%2BK4vydcHn%2B7ZApHmJlUnNpVT6SJK1RDbhYqMbQvamaXQuLxSnN2JXe5oCcEyVF2EFhCPYWc4nsPw77btK0%2B7Fh1HRXjG1yLtiLGR2oHwbC2fDf9bPXftSKgbZco0yQOFzq%2BRqYMz%2FM887SQNXB3aaohEM2wywfuZ8VIcEtov1z5x%2BruSs0TlrM%2BjOnWSMgQQy6cYEwqHRKcuxO3B10ToyK4fkuURjrMCkV5edQ93Pgd0h4r4gHPaiAIHDzd9BqkLOdcwtAlRZ1ZcSWCmfh6d6zHFLh2CNOUzzkkgnYO3zDdEfLuKtVpYqXIG%2B4OTsLGcgId7h0E1wbwbvB5Co5jrieh%2BlEIvThWIkKufuXVu8aJ1QiJc%2FmWq01HiB59XY2etv1DohA2GOxwkIVuibY17CvH0mzPFNzL%2B34SoETUu3U9rq8kTz2pnnWwj%2B1dPoRCpxRetkxRME9y1Ou2XgwA6uHvN1zDJ9a%2FSBjqkAaDUnFpqNPNFqLnx6P8Nxmc%2BjyXTV5Z1fcte9KqD30I9mhh766Up5dU4jPAbCtIhBGk8TwgcYhQzq%2FfGYs8dJq6rdFqDeucvHj6Ss4iYaZkhEVkgCP%2BZmq8VXeUglATqEBt9%2F98pFMDNmF%2FhoCADPfDJI3eWMeXVNWJB7FExnX1%2FZpFFQe5doJwXfXn00dmbM10dQT1ga1R5xBqrwpaBJsBUZuBS&X-Amz-Signature=fcee3b900a559d294bc32c9e103431c8f86c59dfc3c783f6ef84f4720058466a&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466TGHW2CSN%2F20260706%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260706T194850Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEJP%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJIMEYCIQDJzww%2FgpN6kgkJzBeCgbc%2FaC0Pm5b2CwdLHw1DkSUnGgIhAOMrQsdII%2B3xG3cGbDoLhh17lYCy91Tf4Ft0zVZWbiv7Kv8DCFwQABoMNjM3NDIzMTgzODA1IgzejmJCVVkqlR9zjuwq3AOonMB6h3m4TxU8BFV%2BXsCQIKTQQRmCjC%2FuhISqHZ8NP9T3JOJTfHutixjaPOD%2FLR3ENxztJDa04TIqA4JvEvzKIxg2VeyQCS%2Fc9UFGJZUdcSoyQ4uTv82FbC5XErBIOa3loewf%2BhNYR1C3vJuj84xyKf1AG1l0SDc5%2BK4vydcHn%2B7ZApHmJlUnNpVT6SJK1RDbhYqMbQvamaXQuLxSnN2JXe5oCcEyVF2EFhCPYWc4nsPw77btK0%2B7Fh1HRXjG1yLtiLGR2oHwbC2fDf9bPXftSKgbZco0yQOFzq%2BRqYMz%2FM887SQNXB3aaohEM2wywfuZ8VIcEtov1z5x%2BruSs0TlrM%2BjOnWSMgQQy6cYEwqHRKcuxO3B10ToyK4fkuURjrMCkV5edQ93Pgd0h4r4gHPaiAIHDzd9BqkLOdcwtAlRZ1ZcSWCmfh6d6zHFLh2CNOUzzkkgnYO3zDdEfLuKtVpYqXIG%2B4OTsLGcgId7h0E1wbwbvB5Co5jrieh%2BlEIvThWIkKufuXVu8aJ1QiJc%2FmWq01HiB59XY2etv1DohA2GOxwkIVuibY17CvH0mzPFNzL%2B34SoETUu3U9rq8kTz2pnnWwj%2B1dPoRCpxRetkxRME9y1Ou2XgwA6uHvN1zDJ9a%2FSBjqkAaDUnFpqNPNFqLnx6P8Nxmc%2BjyXTV5Z1fcte9KqD30I9mhh766Up5dU4jPAbCtIhBGk8TwgcYhQzq%2FfGYs8dJq6rdFqDeucvHj6Ss4iYaZkhEVkgCP%2BZmq8VXeUglATqEBt9%2F98pFMDNmF%2FhoCADPfDJI3eWMeXVNWJB7FExnX1%2FZpFFQe5doJwXfXn00dmbM10dQT1ga1R5xBqrwpaBJsBUZuBS&X-Amz-Signature=0aea1741d60cb3cfdd2dd4aedd24cb10a47206376e612591f413b754e3f684e5&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







