



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


![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/de3257b0-99da-4a97-9108-71d731170890/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNC7FCYD%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T012843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1hzmoOIK0vOdfgMslwU46Nzoa9LXsf3hnJOLjk%2FsFSAiEAus1lqZHim3N1hThd%2FOsPv60tedF98Bt48wzkPtCG0YMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDCRmbIexQ6tVPkr9YSrcAyKvnADpjq%2FqKLI7cxJTmBR8UYJG%2F9YDK6AcBbqU4IWOt3iBcRY7Bsp6s1BZKP%2BuIgC6%2B2Os%2BGD89j0zdAXNTC%2FEP%2B4Pwq5%2BCWDCSioaLUrZL0nGZzQaMe%2FoffnhanWUPMYCYfyK0k9TsN86NHY4pwfZeR6rsNurZp8b59%2BShDCUAPxinBReQSTqtfZhGdUfKv0tjkyIaoH51y8XsuBJV2mvUN7nb9VwDU8XnG7waWsXecovTF4KcDE4XdEx2Zbacj9NGap7a7qwArtKCf%2BWDCaN2SRN4wn8myyZbgORUqDKAVjE9s53IX4mPckKPvvj5mwEmBlb5MPSRCUKE%2FUN%2FaTIUMIy0jv%2Bq1LbSbzVHUjdKW6pcWuS8c9XVfgdDYo64q4JmJPAn5xDlcc1O5q%2B9rfp%2B1sZYjPBYU%2Bhy4VYNI2Z1hTCAVFnRI0EoHYEZ0leMQ0YVkPzMGr7ZBKPIUYq4KtUMX13aMztF6DtkNrKEFYsZ%2FbgfPmOv1ezPcSi847dcbIrv%2F23yEVG0vngCU4ezrhjgDvBDRSpHT6xVRrVdsHrcw1eKuwPFcJ1D1SufqiWNxrmIgcTjXsQelKOjsenKNANegkM2hHqdCAxbRwnC%2BYJbyH8%2FqHENitXEwGTMNbzws0GOqUBKGj4jLK71rcQlxoXb1GV7pBgFXmU4tdaagNWYC%2FfCE%2FTnG8zApzooxBRdu4kuXKe%2B73ZpBBHlQQTucGT7uwi4p5RlfilsGnOY6Op9x%2BHfy3O1z%2Fh7gWBdL9eJtUHVJJDwNVOZsIbVIsoBIh%2BRrL%2F5uDi4P%2FbvOhDz1edwFdAd4dhvpV4OreHyenAV23m7I8BzKwZuYNIx6fG6uxwBNFFx9xoKuoY&X-Amz-Signature=8044a4076e5b91ce369ef9d56b3fb8535d2dd29441f7ca176fee1157303a7ab7&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)



Port 443: HTTPS

HTTP method: GET



![Image](https://prod-files-secure.s3.us-west-2.amazonaws.com/957548da-634d-4c7f-b0aa-dd4d7a9da4c5/dc56f68d-8daf-4b31-bc04-5bd2547ffac9/image.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=ASIAZI2LB466XNC7FCYD%2F20260311%2Fus-west-2%2Fs3%2Faws4_request&X-Amz-Date=20260311T012843Z&X-Amz-Expires=3600&X-Amz-Security-Token=IQoJb3JpZ2luX2VjEIn%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLXdlc3QtMiJHMEUCID1hzmoOIK0vOdfgMslwU46Nzoa9LXsf3hnJOLjk%2FsFSAiEAus1lqZHim3N1hThd%2FOsPv60tedF98Bt48wzkPtCG0YMq%2FwMIUhAAGgw2Mzc0MjMxODM4MDUiDCRmbIexQ6tVPkr9YSrcAyKvnADpjq%2FqKLI7cxJTmBR8UYJG%2F9YDK6AcBbqU4IWOt3iBcRY7Bsp6s1BZKP%2BuIgC6%2B2Os%2BGD89j0zdAXNTC%2FEP%2B4Pwq5%2BCWDCSioaLUrZL0nGZzQaMe%2FoffnhanWUPMYCYfyK0k9TsN86NHY4pwfZeR6rsNurZp8b59%2BShDCUAPxinBReQSTqtfZhGdUfKv0tjkyIaoH51y8XsuBJV2mvUN7nb9VwDU8XnG7waWsXecovTF4KcDE4XdEx2Zbacj9NGap7a7qwArtKCf%2BWDCaN2SRN4wn8myyZbgORUqDKAVjE9s53IX4mPckKPvvj5mwEmBlb5MPSRCUKE%2FUN%2FaTIUMIy0jv%2Bq1LbSbzVHUjdKW6pcWuS8c9XVfgdDYo64q4JmJPAn5xDlcc1O5q%2B9rfp%2B1sZYjPBYU%2Bhy4VYNI2Z1hTCAVFnRI0EoHYEZ0leMQ0YVkPzMGr7ZBKPIUYq4KtUMX13aMztF6DtkNrKEFYsZ%2FbgfPmOv1ezPcSi847dcbIrv%2F23yEVG0vngCU4ezrhjgDvBDRSpHT6xVRrVdsHrcw1eKuwPFcJ1D1SufqiWNxrmIgcTjXsQelKOjsenKNANegkM2hHqdCAxbRwnC%2BYJbyH8%2FqHENitXEwGTMNbzws0GOqUBKGj4jLK71rcQlxoXb1GV7pBgFXmU4tdaagNWYC%2FfCE%2FTnG8zApzooxBRdu4kuXKe%2B73ZpBBHlQQTucGT7uwi4p5RlfilsGnOY6Op9x%2BHfy3O1z%2Fh7gWBdL9eJtUHVJJDwNVOZsIbVIsoBIh%2BRrL%2F5uDi4P%2FbvOhDz1edwFdAd4dhvpV4OreHyenAV23m7I8BzKwZuYNIx6fG6uxwBNFFx9xoKuoY&X-Amz-Signature=ef46d6a2b470f7dce5cd5740a71e7996a912c1462b85116b50f593acc6f9c09f&X-Amz-SignedHeaders=host&x-amz-checksum-mode=ENABLED&x-id=GetObject)





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







